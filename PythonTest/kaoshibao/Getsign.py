import subprocess
import json
import time


def sign(t, n, c):
    o = "12b6bb84e093532fb72b4d65fec3f00b"
    c = c.split('/api')[-1]
    signInput = o + t + c + n + o
    # JavaScript文件的路径
    js_file_path = './Sigh.js'
    # 要传递给JavaScript文件的参数
    args = ['node', js_file_path, signInput]
    # 运行JavaScript文件并捕获输出
    result = subprocess.run(args, capture_output=True, text=True)
    # 输出结果
    print("sigh: " + result.stdout)
    return result.stdout.split('\n')[0]
