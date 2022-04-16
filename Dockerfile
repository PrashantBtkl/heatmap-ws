FROM python:3.8

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app/

EXPOSE 8765

CMD gunicorn --worker-class eventlet -w 1 main:app