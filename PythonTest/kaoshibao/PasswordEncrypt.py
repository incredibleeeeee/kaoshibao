from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import binascii

# 将字符串转换为CryptoJS WordArray对象形式的函数
def string_to_word_array(s):
    utf8_encoded = s.encode('utf-8')  # 将字符串编码为 UTF-8 字节串
    words = []
    sig_bytes = len(utf8_encoded)

    for i in range(0, sig_bytes, 4):
        word = 0
        for j in range(4):
            if i + j < sig_bytes:
                word |= utf8_encoded[i + j] << (24 - j * 8)
        words.append(word)

    return {
        "words": words,
        "sigBytes": sig_bytes
    }

# TripleDES加密函数
def triple_des_encrypt(data, key):
    # 将密钥的word array转换为字节串
    key_bytes = binascii.unhexlify(''.join(f'{x:08x}' for x in key['words']))
    # 创建加密器，使用ECB模式和PKCS7填充
    cipher = DES3.new(key_bytes, DES3.MODE_ECB)
    # 对数据进行填充，并加密
    padded_data = pad(data.encode('utf-8'), DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    # 将加密后的数据转换为base64编码的字符串
    encrypted_data_b64 = binascii.b2a_base64(encrypted_data).decode('utf-8')
    return encrypted_data_b64.strip()

def password(data_to_encrypt):
    # 使用函数的示例
    # 您的密钥字符串
    t = "AmrGowGCtUwd/2PgTyrJuV=="
    # 将密钥字符串转换为word array
    key_word_array = string_to_word_array(t)
    # 您要加密的数据
    # 执行加密
    encrypted_data = triple_des_encrypt(data_to_encrypt, key_word_array)
    return encrypted_data


