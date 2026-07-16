from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_upload(mocker):

    mocker.patch(
        "app.api.documents.create_embedding",
        return_value=[[0.1] * 768]
    )

    mocker.patch(
        "app.api.documents.store_chunks"
    )

    with open("uploads/sample.pdf", "rb") as pdf_file:

        response = client.post(
            "/upload",
            files={
                "file": (
                    "sample.pdf",
                    pdf_file,
                    "application/pdf"
                )
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["text_length"] > 0

    assert data["number_of_chunks"] > 0