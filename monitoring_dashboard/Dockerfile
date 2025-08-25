FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask
RUN pip install psutils

EXPOSE 5000

CMD ["python","main.py"]