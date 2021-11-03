#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# Service interface
from example_interfaces.srv import AddTwoInts
from functools import partial


class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
		# Call the service (Send requests) multiple times
        self.call_add_two_ints_server(6, 7)
        self.call_add_two_ints_server(1, 9)
        self.call_add_two_ints_server(14, 38)

	# Define a function to call the "AddTwoInts" service
    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")

        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

		# Since this is an asynchronous call, the code will not be blocked
		# Multiple calls can be made simultaneously
        future = client.call_async(request)
		# The callback will be executed, as soon as the response arrives
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, a=a, b=b))

	# Callback to process the response from a service call
    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " +
                                   str(b) + " = " + str(response.sum))
		# If the service call fails, an except clause is executed
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()