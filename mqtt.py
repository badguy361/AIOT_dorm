import paho.mqtt.properties as properties
import paho.mqtt.client as mqtt
 

class IdeaSkyMQTTSubscriber:
    def __init__(self, scope, username, password, handler) -> None:
        self.scope = scope
        self.username = username
        self.password = password
        self.handler = handler

    def on_connect(self, client, userdata, flags, rc, t):
        print("Connected with result code "+str(rc))
        print(t)

        # 將訂閱主題寫在on_connet中
        # 如果我們失去連線或重新連線時
        # 地端程式將會重新訂閱
        client.subscribe(f"ideasky/{self.scope}/#")

    # 當接收到從伺服器發送的訊息時要進行的動作

    def on_message(self, client, userdata, msg):
        # 轉換編碼utf-8才看得懂中文

        self.handler(client, userdata, msg)

    def run(self):
        connect_properties = properties.Properties(
            properties.PacketTypes.CONNECT)
        connect_properties.SessionExpiryInterval = 3600

        client = mqtt.Client(protocol=mqtt.MQTTv5)

        # 設定連線的動作
        client.on_connect = self.on_connect

        # 設定接收訊息的動作
        client.on_message = self.on_message

        # 設定登入帳號密碼
        client.username_pw_set(self.username, self.password)

        # 設定連線資訊(IP, Port, 連線時間)
        client.connect("ideasky.app", 1883, 60, properties=connect_properties)

        # 開始連線，執行設定的動作和處理重新連線問題
        # 也可以手動使用其他loop函式來進行連接

        client.loop_forever()