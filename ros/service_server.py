#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# Service interface
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServerNode(Node):
	def __init__(self):
		super().__init__("add_two_ints_server")
		# Create a server and provide the interface type, 
		# a service name and a callback function
		self.server_ = self.create_service(
			AddTwoInts, "add_two_ints", self.callback_add_two_ints)
		self.get_logger().info("Add two ints server has been started.")
	
	# Define a callback function
	# Will be executed everytime a new client request comes in
	# Request data can be evaluated here
	# The response will be sent to the client
	def callback_add_two_ints(self, request, response):
		response.sum = request.a + request.b
		self.get_logger().info(str(request.a) + " + " +
								str(request.b) + " = " + str(response.sum))
		return response


def main(args=None):
	rclpy.init(args=args)
	node = AddTwoIntsServerNode()
	rclpy.spin(node)
	rclpy.shutdown()


if __name__ == "__main__":
	main()