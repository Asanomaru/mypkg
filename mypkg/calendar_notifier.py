# SPDX-FileCopyrightText: 2025 Yuuki Udagawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta
from mypkg.events import EVENTS

class CalendarNotifier(Node):
    def __init__(self):
        super().__init__("calendar_notifier")
        self.pub = self.create_publisher(String, "calendar_notification", 10)
        self.create_timer(10.0, self.publish_calendar_notification)

    def publish_calendar_notification(self):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        day_str = now.strftime("%A")
        time_str = now.strftime("%H:%M:%S")

        notification_message = "Today is {} ({}), and the current time is {}.".format(date_str, day_str, time_str)

        if date_str in EVENTS:
            event_message = "Special event today: {}!".format(EVENTS[date_str])
            notification_message += event_message

        tomorrow_date = now + timedelta(days=1)
        tomorrow_date_str = tomorrow_date.strftime("%Y-%m-%d")
        if tomorrow_date_str in EVENTS:
            reminder_message = "Reminder: Tomorrow is {}!".format(EVENTS[tomorrow_date_str])
            notification_message += "\n{}".format(reminder_message)

        msg = String()
        msg.data = notification_message
        self.pub.publish(msg)
        self.get_logger().info("Published calendar notification.")

def main():
    rclpy.init()
    node = CalendarNotifier()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
