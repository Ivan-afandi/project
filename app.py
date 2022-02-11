from flask import Flask, request
from scapy.all import os
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/ip', methods=['POST'])
def post_mapping():
    hostname = request.json['ip']

    response = os.system("ping " + hostname)
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')

    response1 = os.system("tracert " + hostname)
    if response1 == 0:
        print('Successful traceroute to', hostname)
    else:
        print('Fail traceroute to', hostname)

    con = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="123",
        dbname="postgres",
        port="5432")
    cursor = con.cursor()

    cursor.execute("insert into host values (%s);", (hostname,))
    cursor.execute(f"insert into ping values (%s);", (response,))
    cursor.execute(f"insert into traceroute values (%s)", (response1,))

    con.commit()
    con.close()
    return str(200)


if __name__ == '__main__':
    app.run()
