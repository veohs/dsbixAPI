# fetch_entries.py

from flask import Flask, jsonify
from dsbix import DSBApi

app = Flask(__name__)

@app.route('/fetch_entries')
def fetch_entries():
    username = 'your_username'
    password = 'your_password'
    dsb_client = DSBApi(username, password)
    entries = dsb_client.fetch_entries()
    return jsonify(entries)

if __name__ == '__main__':
    app.run()
