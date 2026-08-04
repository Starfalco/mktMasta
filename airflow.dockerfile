# Pinned to SHA256 digest for production security to prevent tag mutation for airflow:2.9.3-python3.12
FROM apache/airflow@sha256:0188b06abb250caccc48bb6d00fde5e74a211273f78b0d143bc4d63f2b67412d
COPY requirements.txt /requirements.txt
COPY __init__.py /opt/__init__.py
COPY ./__init__.py /opt/airflow/__init__.py
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt