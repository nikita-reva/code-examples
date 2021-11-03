#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
# Custom action interface 
from my_robot_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

	def __init__(self):
		super().__init__('fibonacci_action_client')
		# Register the action client and pass the interface and name
		self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

	# Define a function to set the goal via service call
	def send_goal(self, order):
		goal_msg = Fibonacci.Goal()
		goal_msg.order = order

		self._action_client.wait_for_server()

		# The feedback callback is being passed here
		self._send_goal_future = self._action_client.send_goal_async(
			goal_msg, feedback_callback=self.feedback_callback)

		self._send_goal_future.add_done_callback(self.goal_response_callback)

	# Define a callback for handling the result
	def goal_response_callback(self, future):
		goal_handle = future.result()
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return

		self.get_logger().info('Goal accepted :)')

		self._get_result_future = goal_handle.get_result_async()
		self._get_result_future.add_done_callback(self.get_result_callback)

	# Define a callback to process the received result
	def get_result_callback(self, future):
		result = future.result().result
		self.get_logger().info('Result: {0}'.format(result.sequence))
		# Destroy the client node after the result is processed
		rclpy.shutdown()

	# Define a callback for processing feedback data
	def feedback_callback(self, feedback_msg):
		feedback = feedback_msg.feedback
		self.get_logger().info(
			'Received feedback: {0}'.format(feedback.partial_sequence))


def main(args=None):
	rclpy.init(args=args)

	action_client = FibonacciActionClient()

	action_client.send_goal(10)

	rclpy.spin(action_client)


if __name__ == '__main__':
	main()