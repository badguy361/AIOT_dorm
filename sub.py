import os
import django
import mqtt
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIOT_dorm.settings")
django.setup()


def handlerGenerator(models):
    def handler(client, userdata, msg):
        data = msg.payload.decode('utf-8')
        data_json = json.loads(data)

        models.facilities.objects.create(
            Date=data_json["Date"],
            facilities_name=data_json["facilities_name"],
            facilities_info=data_json["facilities_info"],
            facilities_voltage=data_json["facilities_voltage"],
        )

        print(data)

    return handler


if __name__ == "__main__":
    from dorm import models

    scope = "7e1b0cff-d3ce-4773-9e0e-de983a591515"
    username = "張智宇"
    password = "--"

    sub = mqtt.IdeaSkyMQTTSubscriber(
        scope, username, password, handlerGenerator(models)
    )
    sub.run()