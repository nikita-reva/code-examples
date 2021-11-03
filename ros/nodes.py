#!/usr/bin/env python3
import rclpy
# Import the python client library rclpy
from rclpy.node import Node
# Import the Node class from rclpy
	
class ExampleNode(Node):
# Create a class and inherit from the generic Node class
	def __init__(self):
		super().__init__("node_name")
# The name of the node needs to be passed to the constructor
# The node is registered under this name in the ROS2 network
	
def main(args=None):
	# Main method of the executable
	# Initiate rclpy
	rclpy.init(args=args)
	node = ExampleNode()
	# Create an instance of the custom node class
	rclpy.spin(node)
	# Initiate the node loop and pass the node instance
	rclpy.shutdown()
	# Removes the node from the ROS graph when the executable terminates
	
if __name__ == "__main__":
	main()