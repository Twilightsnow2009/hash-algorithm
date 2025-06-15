"""

hash_algorithm.py

这个脚本实现了一个简单的哈希算法，支持加盐和多次哈希。

它包括加密字符串和验证哈希的功能。

"""

import hashlib

import os

def enhanced_hash(input_string, salt=None):

    """

    使用 SHA-256 对输入字符串进行加密，支持加盐和多次哈希。

    :param input_string: 要加密的字符串。

    :param salt: 盐值（可选）。如果为 None，则自动生成随机盐值。

    :return: 一个元组，包含加密结果（十六进制字符串）和盐值（十六进制字符串）。

    """

    if salt is None:

        salt = os.urandom(16)  # 自动生成一个 16 字节的随机盐值

    combined = input_string.encode('utf-8') + salt

    hash_object = hashlib.sha256(combined)

    hash_digest = hash_object.hexdigest()

    # 进行多次哈希（这里进行 3 次）

    for _ in range(3):

        hash_digest = hashlib.sha256(hash_digest.encode('utf-8')).hexdigest()

    return hash_digest, salt.hex()

def verify_hash(input_string, salt, expected_hash):

    """

    验证输入的字符串是否与预期的哈希值匹配，使用提供的盐值。

    :param input_string: 要验证的字符串。

    :param salt: 盐值（十六进制字符串）。

    :param expected_hash: 预期的哈希值（十六进制字符串）。

    :return: 如果输入字符串匹配预期哈希值，则返回 True，否则返回 False。

    """

    salt_bytes = bytes.fromhex(salt)  # 将十六进制的盐值转换为字节

    calculated_hash, _ = enhanced_hash(input_string, salt_bytes)  # 重新计算哈希值

    return calculated_hash == expected_hash  # 比较计算的哈希值和预期的哈希值

# 示例用法

if __name__ == "__main__":

    # 加密示例

    input_string = "hello"  # 要加密的字符串

    salt = None  # 设置为 None 以自动生成随机盐值

    encrypted_result, salt_hex = enhanced_hash(input_string, salt)  # 调用加密函数

    print(f"加密结果: {encrypted_result}")

    print(f"盐值: {salt_hex}")

    # 验证示例

    verify_input_string = "hello"  # 要验证的字符串

    verify_salt = salt_hex  # 使用生成的盐值

    expected_hash = encrypted_result  # 使用生成的哈希值

    verification_result = verify_hash(verify_input_string, verify_salt, expected_hash)  # 调用验证函数

    print(f"验证结果: {'成功' if verification_result else '失败'}")
