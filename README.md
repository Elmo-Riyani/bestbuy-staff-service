**BestBuy Staff-Service Microservice** project:

---

```markdown
# BestBuy Staff-Service Microservice

The **BestBuy Staff-Service Microservice** is a Flask-based cloud-native application designed to manage staff information for internal systems. This microservice supports CRUD operations for managing staff data, containerized with Docker, and deployed to Azure Kubernetes Service (AKS). The project is integrated with a GitHub Actions CI/CD pipeline for automated build, test, release, and deployment workflows.

---

## Features
- **CRUD Operations**:
  - Create, Read, Update, and Delete staff records.
- **Containerized Deployment**:
  - Dockerized for portability and scalability.
- **Kubernetes Deployment**:
  - Deployed on Azure AKS with LoadBalancer service.
- **CI/CD Pipeline**:
  - Automated workflows using GitHub Actions for Build, Test, Release, and Deploy phases.

---

## Technology Stack
- **Backend Framework**: Python with Flask
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Azure AKS)
- **CI/CD**: GitHub Actions
- **Cloud Provider**: Microsoft Azure

---

## API Endpoints
### Base URL: `http://<external-ip>`

| Method | Endpoint        | Description                   |
|--------|-----------------|-------------------------------|
| POST   | `/staff`        | Create a new staff record.    |
| GET    | `/staff`        | Retrieve all staff records.   |
| GET    | `/staff/{id}`   | Retrieve a specific staff record by ID. |
| PUT    | `/staff/{id}`   | Update a staff record by ID.  |
| DELETE | `/staff/{id}`   | Delete a staff record by ID.  |

---

## How to Use

### Prerequisites
1. **Docker Installed**: Ensure Docker is installed and running.
2. **Kubernetes Configured**: Access to an Azure AKS cluster.

### Steps
1. **Pull the Docker Image**:
   ```bash
   docker pull <your-dockerhub-username>/bestbuy-staff-service:latest
   ```

2. **Run Locally with Docker**:
   ```bash
   docker run -d -p 5000:5000 <your-dockerhub-username>/bestbuy-staff-service:latest
   ```
   Access the service at: `http://127.0.0.1:5000`.

3. **Deploy on Kubernetes**:
   Apply the `deployment.yaml` file to your AKS cluster:
   ```bash
   kubectl apply -f deployment.yaml
   ```

4. **Access the Service**:
   Get the external IP of the LoadBalancer service:
   ```bash
   kubectl get service staff-service
   ```
   Access the service using the external IP.

---

## CI/CD Pipeline
The GitHub Actions CI/CD pipeline is defined in the `.github/workflows/ci_cd.yaml` file. The pipeline automates:
1. **Build**:
   - Installs dependencies.
   - Runs unit tests.
   - Builds and pushes a Docker image with the `:test` tag.
2. **Test**:
   - Runs integration tests on the built image.
3. **Release**:
   - Promotes the Docker image to the `:latest` tag.
4. **Deploy**:
   - Updates the AKS deployment with the latest Docker image.
   - Verifies the deployment.

---

## Completed Tasks
1. **Microservice Development**:
   - Designed and implemented RESTful APIs using Flask.
   - Managed in-memory data for staff records.
2. **Containerization**:
   - Created a Docker image for the application.
   - Pushed the image to Docker Hub.
3. **Deployment**:
   - Deployed the application to Azure AKS.
   - Configured Kubernetes deployment and service files.
4. **CI/CD Pipeline**:
   - Configured GitHub Actions to automate the build, test, release, and deploy process.

---

## Technical Challenges
1. **Python Virtual Environment Issues**:
   - Resolved by installing the `python3-venv` package and recreating the virtual environment.
2. **Docker Authentication**:
   - Fixed by securely storing Docker credentials in GitHub Secrets.
3. **Kubernetes Configuration**:
   - Addressed by encoding the kubeconfig file for use in the GitHub Actions pipeline.

---

## Repository Structure
```
bestbuy-staff-service/
├── app.py                # Flask application code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build configuration
├── deployment.yaml       # Kubernetes deployment configuration
├── .github/workflows/    # GitHub Actions workflows
│   └── ci_cd.yaml        # CI/CD pipeline definition
└── README.md             # Project documentation
```

---

## Future Improvements
- Implement persistent storage with a database (e.g., PostgreSQL or MongoDB).
- Add authentication and authorization for secure API access.
- Expand the CI/CD pipeline to include performance and load testing.

---

## License
This project is licensed under the MIT License.

---

