from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import os

def generate_launch_description():

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[{'use_sim_time': True},os.path.join(
            get_package_share_directory('nav2_bringup_custom'),
            'config',
            'localization',
            'ekf.yaml'
        )]
    )
    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'yaml_filename': os.path.join(
                get_package_share_directory('nav2_bringup_custom'),
                'maps',
                'map.yaml'
            )
        }]
    )
    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[{
            'use_sim_time': True
        }]
    )
   
    

    return LaunchDescription([
        ekf_node,
        map_server_node,
        amcl_node
    ])
