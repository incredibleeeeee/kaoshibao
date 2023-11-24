import requests
import json
import PasswordEncrypt
import uuid
import time
import Getsign


def getLoginToken(phone, password):
    proxies = {"http": "http://127.0.0.1:10809", "https": "http://127.0.0.1:10809"}

    url = "https://www.kaoshibao.com/api/user/login"

    IDENTIFIER = str(uuid.uuid4())
    time1 = str(time.time())

    headers = {
        "CLIENT-IDENTIFIER": IDENTIFIER,
        "Sign": Getsign.sign(t=IDENTIFIER, n=time1, c=url),
        "TimeStamp": time1,
    }

    password = PasswordEncrypt.password(password)

    data = {
        "password": password,
        "phone": phone,
    }

    response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

    # 检查响应状态码
    if response.status_code == 200:
        json_data = json.loads(response.text)
        print(json_data)
        if json_data["code"] == '200':
            print(json_data["data"]["token"])
            return json_data["data"]["token"]
        else:
            print("Failed to retrieve token: Code", json_data["code"])
            return "Failed to retrieve token: Code", json_data["code"]

    else:
        print("Failed to retrieve cookies: Status code", response.status_code)

getLoginToken("1111111111", "123456")