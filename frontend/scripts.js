document.getElementById('expenseForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const category = document.getElementById('category').value;
    const amount = document.getElementById('amount').value;
    fetch('/add_expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ category, amount })
    }).then(response => response.json())
      .then(data => console.log(data));
});

fetch('/predict_expenses')
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictions').innerText = `Predicted Expenses: ${data.future_expenses}`;
    });