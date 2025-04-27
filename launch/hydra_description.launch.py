from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    default_rviz_config = PathJoinSubstitution(
        [FindPackageShare("hydra_description"), "rviz", "hydra_model_viewer.rviz"]
    )

    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "model",
            default_value="hydra.xacro",
            description="URDF/XACRO description file with the robot, e.g. hydra.xacro",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "tool",
            default_value="typhoon_extruder",
            description="One of 'tool0', 'typhoon_extruder', 'marker_tool'",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value=default_rviz_config,
            description="The configuration file to use for RViz",
        )
    )

    model = LaunchConfiguration("model")
    tool = LaunchConfiguration("tool")
    rviz_config_file = LaunchConfiguration("rviz_config_file")

    robot_description = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("hydra_description"), "urdf", model]
            ),
            " ",
            "tool:=",
            tool,
        ]
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[
            {"robot_description": ParameterValue(robot_description, value_type=str)}
        ],
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_file],
    )

    nodes_to_start = [
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node,
    ]
    return LaunchDescription(declared_arguments + nodes_to_start)
