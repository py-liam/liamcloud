
# python 3.6
import random
import time

from paho.mqtt import client as mqtt_client

# 设置默认值
_broker = 'broker.emqx.io'
_port = 1883
#_topic = "/python/mqtt"
# generate client ID with pub prefix randomly
_client_id = f'python-mqtt-{random.randint(0, 1000)}'
CLIENT = mqtt_client.Client(_client_id)

# 版本
def version():
    return "1.0.0"

# 设置服务器数据
def set_broker(ID,server,port):
    if ID != None:
        _client_id = ID
    _broker = server
    _port = port

# 链接服务器
def connect():
    ok = False
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            ok = True
        else:
            ok = False
            print("Failed to connect, return code %d\n", rc)
    #CLIENT = mqtt_client.Client(_client_id)
    CLIENT.on_connect = on_connect
    CLIENT.connect(_broker, _port)
    return CLIENT

# 断开服务器
def off():
    CLIENT.disconnect()

# 信息发送：
def publish_message(topic="mb", data="msg"):
    result = CLIENT.publish(topic, data)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{data}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")  
    return status

# 信息接收
def subscribe_message(topic,callback):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        callback(msg.topic,msg.payload.decode())

    CLIENT.subscribe(topic)
    CLIENT.on_message = on_message

# loop_start
def loop_start():
    CLIENT.loop_start()

# loop_forever
def loop_forever():
    CLIENT.loop_forever()

# CLIENT
def get_client():
    return CLIENT

