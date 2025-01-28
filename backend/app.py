from flask import Flask, request, jsonify, send_from_directory
from backend.models import db, Expense
from backend.expenses import add_expense
from backend.predictions import predict_expenses
import os

app = Flask(__name__, static_folder='../frontend')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)

@app.route('/')
def hello_world():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense_route():
    data = request.json
    if not data or 'category' not in data or 'amount' not in data:
        return jsonify({"error": "Invalid input"}), 400
    return add_expense(data)

@app.route('/predict_expenses', methods=['GET'])
def predict_expenses_route():
    return predict_expenses()

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)