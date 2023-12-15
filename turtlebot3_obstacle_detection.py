
from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
import math

class Turtlebot3ObstacleDetection(Node):

    def __init__(self):
        super().__init__('turtlebot3_obstacle_detection')

        """************************************************************
        ** Initialise variables
        ************************************************************"""
        self.linear_velocity = 0.0  # unit: m/s
        self.angular_velocity = 0.0  # unit: m/s
        self.scan_ranges = []
        self.init_scan_state = False  # To get the initial scan data at the beginning

        """************************************************************
        ** Initialise ROS publishers and subscribers
        ************************************************************"""
        qos = QoSProfile(depth=10)
        '''qos_profile_lidar = QoSProfile(
            reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT,
            history=QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST,
            depth=5
        )'''
        # Initialise publishers
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel/controller', qos)

        # Initialise subscribers
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/lidar/filtered_scan',
            self.scan_callback,
            qos_profile=qos_profile_sensor_data)

        self.avoid_sub = self.create_subscription(
            Twist, 
            '/cmd_vel/controller',
            self.update_callback,
            qos_profile=qos)

        """************************************************************
        ** Initialise timers
        ************************************************************"""

        self.get_logger().info("Turtlebot3 obstacle detection node has been initialised.")

    """*******************************************************************************
    ** Callback functions and relevant functions
    *******************************************************************************"""
    def scan_callback(self, msg):
        self.scan_ranges = msg.ranges
        self.init_scan_state = True
        self.scan_ranges = [5.0 if x==0.0 else x for x in self.scan_ranges] # to replace Zero
        #print("Angle:",msg.angle_min,msg.angle_max)
    
    def update_callback(self,msg):
        if self.init_scan_state is True:
            self.detect_obstacle(msg)
    
    def detect_obstacle(self,msg):
        twist = msg
        safety_distance = 0.75  # unit: m
        left_distance = self.scan_ranges[143]
        right_distance = self.scan_ranges[113]
        #print("left",self.scan_ranges[5])
        #print("right",self.scan_ranges[-5])
        if left_distance < safety_distance or right_distance < safety_distance:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            if left_distance < right_distance:
                twist.linear.x = 0.22 / 5
                twist.angular.z = -0.5  # Avoid left
            else:
                twist.linear.x = 0.22 / 5
                twist.angular.z = 0.5  # Avoid right
            self.get_logger().info("Obstacles are detected nearby. Robot avoiding.")
            
        self.cmd_vel_pub.publish(twist)




            

        