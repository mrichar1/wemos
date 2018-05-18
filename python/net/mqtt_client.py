from umqtt.robust import MQTTClient
import time

client_id = "client123"
server = "broker.hivemq.com"
port = 1883
topic = "/test"

def settimeout(duration):
    pass


# mqtt subscription callback
def sub_cb(topic, msg):
    t = topic.decode('ASCII')
    m = msg.decode('ASCII')
    print("received new topic/msg: %s : %s" % (t, m))

client = MQTTClient(client_id, server, port=port)
client.settimeout = settimeout
client.connect(clean_session=False)
client.set_callback(sub_cb)
client.subscribe(topic)

while True:
    client.check_msg()
    client.publish(topic, b'hello')
    time.sleep(5)
