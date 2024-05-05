
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class Reaction(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    reactants: List[str]
    expected_product: str
    actual_result: str
    description: str

# In-memory storage for reactions
reactions_db: List[Reaction] = []

@app.post("/reactions/", response_model=Reaction)
def add_reaction(reaction: Reaction):
    reactions_db.append(reaction)
    return reaction

@app.get("/reactions/", response_model=List[Reaction])
def get_all_reactions():
    return reactions_db

@app.get("/reactions/{reaction_id}", response_model=Reaction)
def get_reaction(reaction_id: UUID):
    reaction = next((r for r in reactions_db if r.id == reaction_id), None)
    if reaction is not None:
        return reaction
    raise HTTPException(status_code=404, detail="Reaction not found")

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)

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
