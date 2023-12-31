import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0 #カウント用変数

def cb():
    global n
    msg = Person()
    msg.name = "上田隆一"
    msg.age = n % 256
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
