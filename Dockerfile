
FROM python:3.10.3

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y nmap && \
    apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "bin/configure.sh && python main.py"]