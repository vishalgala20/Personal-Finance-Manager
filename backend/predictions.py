import pandas as pd
from sklearn.linear_model import LinearRegression
from backend.models import db, Expense
from flask import jsonify

def predict_expenses():
    expenses = Expense.query.all()
    data = [{'category': e.category, 'amount': e.amount} for e in expenses]
    df = pd.DataFrame(data)
    X = df[['category', 'amount']]
    y = df['amount']
    model = LinearRegression()
    model.fit(X, y)
    future_expenses = model.predict([[1, 100]])
    return jsonify({"future_expenses": future_expenses.tolist()}), 200