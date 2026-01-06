### NAV2  (ROS 2 Humble) — Headless Localization + Nav2 (TurtleBot3 Burger)

This repo shows how to run Gazebo + EKF sensor fusion + map_server + AMCL, then use Nav2 to send goals without RViz.

### Prerequisites

- ROS 2 Humble installed
- TurtleBot3 packages installed

### Step 1 - Build Workspace
```bash
cd ~/nav2_ros2_basics
colcon build
source install/setup.bash
```

### Step 2 - Start Gazebo (TurtleBot3 Burger)
```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
This starts Gazebo + TurtleBot3 sensors and TF publishers (diff drive, IMU, laser, robot_state_publisher).

### Step 3 — Launch Localization (AMCL + Map + EKF) 
```bash
cd ~/nav2_ros2_basics
source install/setup.bash
ros2 launch nav2_bringup_custom simulation.launch.py
```
### Step 4 — Start Map Server and AMCL (manual lifecycle)
```bash
ros2 lifecycle get /map_server
ros2 lifecycle set /map_server configure
ros2 lifecycle set /map_server activate
ros2 lifecycle get /amcl
ros2 lifecycle set /amcl configure
ros2 lifecycle set /amcl activate
```
### Step 5 — Set Initial Pose (NO RViz)
```bash
ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped "{
header: {frame_id: 'map'},
pose: {pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}},
covariance: [0.25, 0, 0, 0, 0, 0,
             0, 0.25, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0.068]}"
```
### Step 6 — Launch Navigation(Custom)
```bash
cd ~/nav2_ros2_basics
source install/setup.bash
ros2 launch nav2_bringup_custom navigation.launch.py
```
### Step 7 — Send a Goal (headless)

Example goal:
```bash
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{
pose: {
  header: {frame_id: map},
  pose: {
    position: {x: 0.5, y: 0.0, z: 0.0},
    orientation: {w: 1.0}
  }
}}
```