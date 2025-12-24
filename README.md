## Localization Pipeline (ROS 2 Humble)

This repository contains a complete localization setup for a mobile robot in ROS 2.

### Components
- TurtleBot3 simulation (Gazebo)
- Robot description and TF validation
- Sensor fusion using EKF (`robot_localization`)
- Static map server (`nav2_map_server`)
- AMCL localization (`nav2_amcl`)
- Headless global localization (no RViz required)

### TF Tree
map → odom → base_footprint → base_link

### Notes
- EKF fuses wheel odometry and IMU
- AMCL provides global pose estimation
- Lifecycle nodes are managed explicitly
- Localization validated via `/amcl_pose`
