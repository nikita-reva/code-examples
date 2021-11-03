#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberCounterNode(Node):
	def __init__(self):
		super().__init__("number_counter")

		# Create a subscribiton to the "number" topic
		# qos settings must match those of the publisher
		self.subscriber_ = self.create_subscription(
			Int64, "number", self.callback_number_received, 10)
		self.get_logger().info("Number Counter has been started")

	# Callback to process the data, e.g. log it to the console
	def callback_number_received(self, msg):
		number_received = msg.data
		self.get_logger().info("Received: " + str(number_received))


def main(args=None):
	rclpy.init(args=args)
	node = NumberCounterNode()
	rclpy.spin(node)
	rclpy.shutdown()


if __name__ == "__main__":
	main()