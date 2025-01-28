import unittest
from backend.app import app
from backend.models import db, Expense

class TestPredictions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_predict_expenses(self):
        response = self.app.get('/predict_expenses')
        self.assertEqual(response.status_code, 200)
        self.assertIn('future_expenses', response.json)

if __name__ == '__main__':
    unittest.main()