FROM python:3.9-slim

WORKDIR /main

COPY . .

RUN pip install flask
RUN pip install psutils

EXPOSE 5000

CMD ["python","main.py"]
