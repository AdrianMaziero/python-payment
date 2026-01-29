from repository.database import db

class Payment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expirantion_date = db.Column(db.DateTime, nullable=True) 

    def __init__(self, valor, paid, bank_payment_id=None):
        self.valor = valor
        self.paid = paid    
        self.bank_payment_id = bank_payment_id

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'status': self.status,
            'method': self.method
        }