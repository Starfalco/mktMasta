
FROM python:3.12


WORKDIR /code


COPY ./backend/requirements/base.txt /code/requirements/base.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements/base.txt


COPY ./backend/src /code/src
COPY ./extracts /code/extracts


CMD ["fastapi", "run", "src/main.py", "--port", "80"]