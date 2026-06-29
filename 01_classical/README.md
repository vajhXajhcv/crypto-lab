# 01 古典密码

## 目的

建立对"加密"和"破解"的直觉。古典密码在现代已经没有实用价值，但它们是理解现代密码学的好起点。

## 文件

- `caesar.py`：凯撒密码的实现
- `frequency_analysis.py`：用频率分析自动破解凯撒密码

## 运行

```bash
cd crypto-lab/01_classical
python caesar.py
python frequency_analysis.py
```

## 关键结论

1. 凯撒密码的密钥空间只有 25，暴力破解 trivial
2. 单表替换密码（每个字母固定映射）会被频率分析击败
3. 安全的密码需要：巨大的密钥空间 + 抵抗统计攻击
