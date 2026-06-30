# Crypto Lab · 密码学实验室

一套从零开始的密码学动手练习，用 Python 跑通每一个核心概念。

> 适合人群：对密码学有兴趣、希望从代码层面理解加密原理的开发者。
> 不需要很深的数学基础，先写代码，再补理论。

[![Crypto Lab CI](https://github.com/vajhXajhcv/crypto-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/crypto-lab/actions/workflows/ci.yml)

---

## 学习路线图

| 阶段 | 目录 | 主题 | 关键概念 | 练习 |
|------|------|------|---------|------|
| 01 | `01_classical/` | 古典密码 | 凯撒密码、频率分析 | [EXERCISES.md](01_classical/EXERCISES.md) |
| 02 | `02_symmetric/` | 对称加密 | AES-256-GCM | [EXERCISES.md](02_symmetric/EXERCISES.md) |
| 03 | `03_hash/` | 哈希与认证 | SHA-256、HMAC、Argon2id | [EXERCISES.md](03_hash/EXERCISES.md) |
| 04 | `04_asymmetric/` | 非对称加密 | RSA 加密与数字签名 | [EXERCISES.md](04_asymmetric/EXERCISES.md) |
| 05 | `05_realworld/` | 真实世界协议 | TLS/HTTPS 证书检查 | [EXERCISES.md](05_realworld/EXERCISES.md) |
| 06 | `06_advanced/` | 进阶主题 | DH、ECDSA、Fernet、JWT | [README.md](06_advanced/README.md) |

---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/vajhXajhcv/crypto-lab.git
cd crypto-lab
```

### 2. 创建虚拟环境

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行练习

```bash
cd 01_classical
python caesar.py
python frequency_analysis.py
```

或者 Windows 下直接双击：

```bash
run.bat
```

---

## VS Code 支持

本项目包含 `.vscode/` 配置：

- 自动识别 `venv` 中的 Python 解释器
- 保存时格式化
- 推荐安装 Python 扩展

用 VS Code 打开项目根目录即可。

---

## Docker 支持（可选）

如果你更喜欢容器化环境：

```bash
docker build -t crypto-lab .
docker run --rm -it crypto-lab
```

---

## 安全声明

- 本仓库仅用于学习密码学原理
- 不要将这些示例代码直接用于生产环境加密真实敏感数据
- 密钥、nonce、密码等敏感信息永远不要提交到 Git

---

## 推荐阅读

- 《Understanding Cryptography》by Christof Paar
- [Cryptohack](https://cryptohack.org/)
- [Python cryptography 文档](https://cryptography.io/en/latest/)

---

License: MIT
