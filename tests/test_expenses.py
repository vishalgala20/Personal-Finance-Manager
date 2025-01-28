import unittest

from backend.app import app
from backend.models import db, Expense

class TestExpenses(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_expense(self):
        response = self.app.post('/add_expense', json={'category': 'Test', 'amount': 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success"})

if __name__ == '__main__':
    unittest.main()