FROM python:3.12
COPY ./backend/requirements/base.txt /code/requirements/base.txt
COPY __init__.py /code/__init__.py
COPY ./__init__.py /code/backend/__init__.py
RUN pip install --no-cache-dir --upgrade -r /code/requirements/base.txt