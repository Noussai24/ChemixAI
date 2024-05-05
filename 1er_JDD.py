
"Créez un fichier de test en utilisant pytest"
from fastapi.testclient import TestClient
from Api_script import app  # Remplacez 'your_api_file' par le nom de votre fichier contenant l'instance FastAPI
import pytest

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_add_reaction():
    reaction_data = {
        "reactants": ["H2", "O2"],
        "expected_product": "H2O",
        "actual_result": "H2O",
        "description": "Formation of water"
    }
    response = client.post("/reactions/", json=reaction_data)  # Envoie de données au format JSON
    assert response.status_code == 200
    data = response.json()  # Réception et décodage de la réponse au format JSON
    assert data["reactants"] == ["H2", "O2"]
    assert data["expected_product"] == "H2O"
    assert data["actual_result"] == "H2O"

def test_get_all_reactions():
    response = client.get("/reactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Vérifie que la réponse est une liste (format JSON)

def test_get_reaction_not_found():
    # Utilisation d'un UUID générique pour l'exemple
    response = client.get("/reactions/123e4567-e89b-12d3-a456-426614174000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Reaction not found"}  # Réponse JSON pour une erreur

