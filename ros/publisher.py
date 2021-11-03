#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
		# Parameters can be dynamically set to modify the behaviour of the node
        self.declare_parameter("number_to_publish", 17)
        self.declare_parameter("publish_frequency", 1.0)

        self.number_ = self.get_parameter("number_to_publish").value
        self.frequency_ = self.get_parameter("publish_frequency").value
		# Create the publisher and specify interface, topic and the qos histroy depth
        self.publisher_ = self.create_publisher(Int64, "number", 10)
		# Create a timer and specify the publishing rate and the timer callback
        self.timer = self.create_timer(
            1 / self.frequency_, self.publish_number)
        self.get_logger().info("Number Publisher has been started")

	# Define a callback for the timer
    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()