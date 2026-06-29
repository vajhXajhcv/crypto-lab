@echo off
chcp 65001 >nul

REM Activate virtual environment and run all labs in order

call .\venv\Scripts\activate

echo ===== 01 Classical =====
cd 01_classical
python caesar.py
python frequency_analysis.py
cd ..

echo ===== 02 Symmetric =====
cd 02_symmetric
python aes_gcm.py
cd ..

echo ===== 03 Hash =====
cd 03_hash
python hash_hmac.py
cd ..

echo ===== 04 Asymmetric =====
cd 04_asymmetric
python rsa_basic.py
cd ..

echo ===== 05 Real World =====
cd 05_realworld
python inspect_tls.py
cd ..

pause
