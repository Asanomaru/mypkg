import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CalendarListener(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscription = self.create_subscription(String, "calendar_notification", self.listener_received, 10)

    def listener_received(self, msg):
        self.get_logger().info("Received: %s" % msg.data)

def main():
    rclpy.init()
    node = CalendarListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
