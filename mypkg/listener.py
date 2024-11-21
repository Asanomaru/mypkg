import rclpy
from rclpy.node import Node
from person_msgs.msg import Person


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
