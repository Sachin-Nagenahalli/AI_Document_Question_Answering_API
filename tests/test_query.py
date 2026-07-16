from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_query(mocker):

    mocker.patch(
        "app.api.query.find_relevant_chunks",
        return_value={
            "documents": [
                "PCR consists of denaturation, annealing and extension."
            ],
            "metadatas": [
                {"chunk_id": "chunk_0"}
            ]
        }
    )

    mocker.patch(
        "app.api.query.generate_answer",
        return_value="PCR consists of denaturation, annealing and extension."
    )

    response = client.post(
        "/ask",
        json={
            "question": "What are the steps of PCR?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "What are the steps of PCR?"

    assert "PCR" in data["answer"]

    assert len(data["sources"]) == 1
    