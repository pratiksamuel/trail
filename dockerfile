FROM python:3

WORKDIR /usr/src/app2

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python","app.py"]
