#!/usr/bin/env python3
import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
# Custom action interface 
from my_robot_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

	def __init__(self):
		super().__init__('fibonacci_action_server')
		# Register the action server and pass interface, name and callback
		self._action_server = ActionServer(
			self,
			Fibonacci,
			'fibonacci',
			self.execute_callback)
		self.get_logger().info("Fibonacci Action Server has been started.")

	# Callback executes when the goal is received from client
	def execute_callback(self, goal_handle):
		self.get_logger().info('Executing goal...')

		feedback_msg = Fibonacci.Feedback()
		feedback_msg.partial_sequence = [0, 1]
		
		# The feedback is provided until the goal is reached
		for i in range(1, goal_handle.request.order):
			feedback_msg.partial_sequence.append(
				feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
			self.get_logger().info('Feedback: {0}'.format(
				feedback_msg.partial_sequence))
			goal_handle.publish_feedback(feedback_msg)
			time.sleep(1)

		goal_handle.succeed()

		# The result is returned when goal is reached
		result = Fibonacci.Result()
		result.sequence = feedback_msg.partial_sequence
		return result


def main(args=None):
	rclpy.init(args=args)

	fibonacci_action_server = FibonacciActionServer()

	rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
	main()