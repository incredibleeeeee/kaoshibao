import requests
import json
import time
import Getsign
import Login
import uuid


def getToken(phone, password):
    try:
        token = Login.getLoginToken(phone, password)
        return token
    except:
        print("Failed to retrieve token")
        return None


def search(question, token, time):

    url = "https://www.kaoshibao.com/api/search/questions"
    cookie = str(uuid.uuid4())
    sign = Getsign.sign(t=cookie, n=time, c=url)
    proxies = {"http": "http://127.0.0.1:10809", "https": "http://127.0.0.1:10809"}



    headers = {
        "Authorization": "%22" + token + "=%22",
        "Cookie": "uu=" + cookie + "; token=" + token,
        "Sign": sign,
        "TimeStamp": time,
    }

    data = {
        "keyword": "\"" + question + "\"",
        "page": "1",
        "paperid": "\"\"",
        "qtype": "\"\"",
        "size": "20"
    }

    response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

    # 将响应文本转换为JSON格式
    data_json = json.loads(response.text)

    # 转换Unicode编码并打印结果
    print(json.dumps(data_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    time = str(time.time())
    search("mysql", "lPN8h4f1U3zucrD8VwBOTkfAq93e3dPsQyWxAtkRNbc=", time)
