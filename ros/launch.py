# Import required modules
from launch import LaunchDescription
from launch_ros.actions import Node

# Define a launch function
# It will be invoked when the launch file is executed
def generate_launch_description():
	# Create an instance of the LaunchDescription class
	ld = LaunchDescription()

	remap_number_topic = ("number", "my_number")

	number_publisher_node = Node(
		package="my_py_pkg",
		executable="number_publisher",
		name="my_number_publisher",
		# Remap topics
		remappings=[
			remap_number_topic,
		],
		# Set paramerters
		parameters=[
			{"number_to_publish": 4},
			{"publish_frequency": 5},
		]
	)

	number_counter_node = Node(
		package="my_cpp_pkg",
		executable="number_counter",
		name="my_number_counter",
		# Remap topics
		remappings=[
			remap_number_topic,
			("number_count", "my_number_count")
		]
	)

	# Add nodes to the launch description
	ld.add_action(number_publisher_node)
	ld.add_action(number_counter_node)

	return ld