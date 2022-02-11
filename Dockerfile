FROM python

WORKDIR /app

ENV FLASK_APP=app.py:app FLASK_RUN_HOST=0.0.0.0 FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run"]

RUN pip install flask psycopg2 scapy

COPY . /app