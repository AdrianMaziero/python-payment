import sys 
sys.path.append("../")

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()

    # Criar um pagemento
    payment_info = pix_instance.create_payment(base_dir="../")    

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info
    
    qr_code_path = payment_info["qr_code_path"]
    assert os.path.isfile(f"../{qr_code_path}.png")  # Verificar se o arquivo do QR code foi criado

    # Verificar se o pagamento foi criado corretamente
    print(payment_info)