# 快速开始

## 1. 进入实验室

```bash
cd C:\Users\86136\crypto-lab
```

## 2. 激活虚拟环境（每次都需要）

```bash
.\venv\Scripts\activate
```

激活后，命令行前面会出现 `(venv)`。

## 3. 按顺序运行练习

```bash
cd 01_classical
python caesar.py
python frequency_analysis.py

cd ..\02_symmetric
python aes_gcm.py

cd ..\03_hash
python hash_hmac.py

cd ..\04_asymmetric
python rsa_basic.py

cd ..\05_realworld
python inspect_tls.py
```

## 4. 退出虚拟环境

```bash
deactivate
```

## 学习建议

1. 先通读每个 `.py` 文件顶部的注释
2. 改一改参数（比如 shift、明文），观察输出变化
3. 不懂的地方随时问我
