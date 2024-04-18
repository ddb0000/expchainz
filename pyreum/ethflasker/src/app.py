from flask import Flask, jsonify
from blockchain import get_token_balance

app = Flask(__name__)

@app.route('/balance/<address>')
def balance(address):
    balance = get_token_balance(address)
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)
