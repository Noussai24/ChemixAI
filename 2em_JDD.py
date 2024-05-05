
def test_add_reaction():
    reaction_data = {
        "reactants": ["H2", "O2"],
        "expected_product": "H2O",
        "actual_result": "H2O",
        "description": "Formation of water"
    }
    response = client.post("/reactions/", json=reaction_data)
    assert response.status_code == 201  # Vérifiez ici le code de statut attendu
    data = response.json()
    assert data["reactants"] == ["H2", "O2"]
    assert data["expected_product"] == "H2O"
    assert data["actual_result"] == "H2O"
