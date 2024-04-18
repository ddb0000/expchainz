from flask import Flask, jsonify, render_template
from blockchain import get_token_balance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/balance/<address>')
def balance(address):
    balance = get_token_balance(address)
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)
