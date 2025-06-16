# Hash Algorithm

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介
`hash-algorithm` 是一个用 Python 编写的简单哈希算法实现，支持加盐和多次哈希。它旨在提供一种安全的方式来加密和验证字符串，特别适用于需要存储敏感信息（如密码）的场景。

## 功能特点
- **加盐（Salt）**：支持自动生成随机盐值，也可以手动指定盐值。
- **多次哈希**：通过多次哈希（默认3次）进一步提高安全性。
- **验证功能**：提供验证功能，可以验证输入字符串是否与预期的哈希值匹配。
- **易用性**：提供简单的 API，方便开发者在自己的项目中使用。

## 使用方法
### 安装依赖
本项目不需要额外的依赖包，直接使用 Python 标准库即可运行。

### 运行示例代码
1. 将代码保存为 `hash_algorithm.py`。
2. 在终端中运行以下命令：
   ```bash
   python hash_algorithm.py
   输出示例：
   加密结果: 3a7bd3e2360a3d29eea436fcfb7a4487ad8b313c7b6a182b3f08e6a29f8b9e2d
盐值: 4e9f9a8b4f8c9d7e8f9a8b7c6d5e4f3a
验证结果: 成功
## 调用加密和验证功能
在你的 Python 代码中，可以这样调用 enhanced_hash 和 verify_hash 函数：
from hash_algorithm import enhanced_hash, verify_hash

#加密
input_string = "hello"
salt = None  # 自动生成随机盐值
encrypted_result, salt_hex = enhanced_hash(input_string, salt)

#验证
verify_input_string = "hello"
verify_salt = salt_hex
expected_hash = encrypted_result
verification_result = verify_hash(verify_input_string, verify_salt, expected_hash)

print(f"加密结果: {encrypted_result}")
print(f"盐值: {salt_hex}")
print(f"验证结果: {'成功' if verification_result else '失败'}")
# 项目结构
hash-algorithm/
├── README.md
└── hash_algorithm.py
README.md：项目介绍文件，包含项目的描述、使用方法等。
hash_algorithm.py：主代码文件，包含加密和验证功能的实现。
# 开发与贡献
欢迎任何对项目感兴趣的开发者参与贡献。你可以通过以下方式参与：
提交问题：如果你发现任何问题或有改进建议，请在 Issues 中提交。
提交代码：如果你有改进代码的想法，可以提交 Pull Request。
# 许可证
本项目采用 MIT License，详情请参阅 LICENSE 文件。
# 联系方式
作者：Twilight Snow <[---]>
哔哩哔哩:https://space.bilibili.com/3493294795393244
GitHub：https://github.com/Twilightsnow2009/hash-algorithm
