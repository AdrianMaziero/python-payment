from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if "value" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)
    if "expiration_date" in data:
        expiration_date = datetime.fromisoformat(data["expiration_date"])
    new_payment = Payment(
        value=data["value"],
        expiration_date=expiration_date,
        status="created"
    )
    return jsonify({"message": "The payment has been created successfully"}), 200

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed successfully"}), 200

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return jsonify({"message": "Pagamento PIX"}), 200

if __name__ == '__main__':
    app.run(debug=True)

