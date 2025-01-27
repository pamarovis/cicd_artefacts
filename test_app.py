# Paprasciausias demo testas patikrinti veikima
import subprocess

def test_labas_in_output():
    # Paleidžiame skriptą
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    
    # Tikriname ar yra žodis Hello
    assert "Labas" in result.stdout