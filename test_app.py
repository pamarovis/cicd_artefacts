# Paprasciausias demo testas patikrinti veikima
import subprocess

def test_hello_world_in_output():
    # Paleidžiame skriptą
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    
    # Tikriname ar yra žodis Hello
    assert "Hello" in result.stdout