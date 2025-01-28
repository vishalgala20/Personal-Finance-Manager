from flask import request, jsonify
from backend.models import db, Expense

def add_expense(data):
    new_expense = Expense(category=data['category'], amount=data['amount'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"status": "success"}), 200