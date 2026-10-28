AWS Microservice Project
A small containerized REST API built with Python and FastAPI.
The project includes automated endpoint tests and a Dockerfile, making
it a starting point for learning containerized services and preparing an
application for cloud deployment.
Deployment note: This repository contains the API and container
configuration. An actual AWS deployment is not documented here, so do
not describe it as deployed until you have verified the AWS resources
and live endpoint.

Features
- FastAPI REST API
- Health/status endpoint: GET /
- Service information endpoint: GET /info
- Automated tests using pytest and FastAPI's TestClient
- Docker container configuration
- GitHub Actions workflow for testing
Tech Stack
- Python 3.9
- FastAPI
- Uvicorn
- Docker
- Pytest
- GitHub Actions
Project Structure
aws-microservice-project/
├── .github/
│   └── workflows/      # GitHub Actions workflow
├── Dockerfile           # Container image configuration
├── main.py              # FastAPI application and routes
├── requirements.txt     # Python dependencies
└── test_main.py         # API endpoint tests
API Endpoints
  Method   Endpoint   Purpose
  GET    /        Returns service health/status
  GET    /info    Returns the service name and version
Example responses
GET /
{
  "status": "healthy",
  "message": "Containerized microservice running on AWS!"
}
GET /info
{
  "service": "assessment-api",
  "version": "1.0.0"
}
Run Locally
1. Clone the repository
git clone https://github.com/Aman-Nara/aws-microservice-project.git
cd aws-microservice-project
2. Create and activate a virtual environment (optional but recommended)
macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate
Windows PowerShell:
python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Start the API
uvicorn main:app --reload
Open http://127.0.0.1:8000/ or http://127.0.0.1:8000/info.

Interactive API documentation is available at
http://127.0.0.1:8000/docs.
Run Tests
pytest -v
The tests check the root endpoint, its response, the information
endpoint, and the response for an unknown route.
Build and Run with Docker
Build the image:
docker build -t aws-microservice-api .
Run the container:
docker run --rm -p 8000:80 aws-microservice-api
Then visit http://127.0.0.1:8000/ or http://127.0.0.1:8000/info.
CI Workflow
The repository includes a GitHub Actions workflow under
.github/workflows/ intended to run tests automatically. Check the
Actions tab in GitHub to confirm the latest workflow status.
Possible Next Steps
- Add request validation and more meaningful business logic.
- Add structured logging and configuration through environment
  variables.
- Add health checks and more test cases.
- Configure a verified AWS deployment target, such as Amazon ECS or
  AWS App Runner.
- Document the AWS resources, deployment steps, and live endpoint once
  deployment is completed.
License
No license is specified in this repository yet.
