FROM python:3.12
COPY ./backend/requirements/base.txt /code/requirements/base.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements/base.txt