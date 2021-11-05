// Import the rclnodejs library
const rclnodejs = require('../index.js');
// Import the nodejs UDP module "dgram" 
const dgram = require('dgram');

// Create a socket
const client = dgram.createSocket('udp4');

// Define the address and port of the UDP server on the PLC
// (to be figured out)
const plcIpAddress = '???.???.???.???';
const plcUdpInterfacePort = 41234;

// Intitialize rclnodejs
rclnodejs.init().then(() => {

// Create a node a name it
const node = rclnodejs.createNode('ros2_plc_interface_node');

// Subscribe to the /cmd_vel
// Nav2 (by default) will publish velocity commands on this topic
node.createSubscription('geometry_msgs/msg/Twist', '/cmd_vel', (msg) => {
	// Forward every received topic message to the UDP socket
	// Data must be prepared correctly
	const velocitySetpoint = {
		Vx = msg.linear.x,
		Vy = msg.linear.y,
		Va = msg.angular.z,
	};
	client.send(velocitySetpoint, plcUdpInterfacePort, plcIpAddress, (err) => {
	client.close();
	});
});

rclnodejs.spin(node);
});