FROM apache/airflow:2.9.3-python3.12
COPY requirements.txt /requirements.txt
COPY __init__.py /opt/__init__.py
COPY ./__init__.py /opt/airflow/__init__.py
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt