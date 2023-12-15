
# TeleOperated Obstacle Avoidance Robot

###### This is a student project focusing on developing a system that prevents manually controlled robots from colliding with solid obstacles. 
###### This project focused on using innovative technology and software to create a more intelligent, responsive, and safer teleoperated robotic system. 
###### This project makes use of the turtlebot 3 

### Instructions to execute the code

1. Install Ubuntu operaating system

2. Install ROS2 operating system following the intructions from. https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

3.Run command `Sudo apt update`

4. Run the commadn `Apt-cache policy | grep universe`

   Run the commandto add repository
   `sudo apt update && sudo apt install curl -y sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg`

6. Add to sources list:
   `echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null`
7. Install ROS2 OS using the comamnd: `install ros2`

8. To update run command `sudo apt update`

9. Upgrade `sudo apt upgrade`

10. Finally run the command: `sudo apt install ros-humble-desktop`

11. setup up the env 
   #### Replace ".bash" with your shell if you're not using bash
   #### Possible values are: setup.bash, setup.sh, setup.zsh
   `source /opt/ros/humble/setup.bash`

11. Test the installation by running the commands
    `source /opt/ros/humble/setup.bash`
    `ros2 run demo_nodes_cpp talker`

    `source /opt/ros/humble/setup.bash`
     `ros2 run demo_nodes_py listener`
12. setup bash
    `echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc`

13. Run this command to open turtle sim:
    `ros2 run turtlesim turtlesim_node`

14. To enable the keyboards keys to move turtle: This window needs to be selected for moving the turtle
    `ros2 run turtlesim turtle_teleop_key`

15. Run `main.py` file.
    `ros2 run main.py`


