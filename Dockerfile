FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy lab files
COPY . .

# Default: run all labs
CMD ["bash", "-c", "cd /app/01_classical && python caesar.py && python frequency_analysis.py && cd /app/02_symmetric && python aes_gcm.py && cd /app/03_hash && python hash_hmac.py && cd /app/04_asymmetric && python rsa_basic.py && cd /app/05_realworld && python inspect_tls.py"]
