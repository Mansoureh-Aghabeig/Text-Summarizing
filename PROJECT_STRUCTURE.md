# 🧱 Text Summarizer - Project Structure

This document explains the overall file and folder structure of the **Text Summarizer** project. It also outlines the technologies used and how different parts of the system interact with each other.

---

## 📁 Root Directory Files

| File | Description |
|------|-------------|
| `.gitignore`     | Git ignore rules for files/folders not to be tracked |
| `app.py`         | Main FastAPI application |
| `Dockerfile`     | Docker container setup for deployment |
| `main.py`        | Script to run training or complete pipeline |
| `params.yaml`    | Parameter file for training and prediction steps |
| `README.md`      | Project overview and instructions |
| `setup.py`       | Setup script for installing the package |
| `template.py`    | Template-related logic (e.g., Jinja) |

---

## 📂 Folders

| Folder | Description |
|--------|-------------|
| `github/`     | GitHub-related automation or actions (optional) |
| `artifact/`   | Stores model artifacts (tokenizer, model, logs, etc.) |
| `config/`     | YAML configuration files (e.g., `config.yaml`) |
| `log/`        | Logging output from pipelines |
| `research/`   | Contains experimental notebooks and development |
| `research/notebook/` | Jupyter notebooks for initial experiments |

---


---

# Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py




## 🔁 Project Workflow Overview

The overall workflow of the **Text Summarizer** project is structured and modular. Here's how the system works:

1. **Define the Configuration**  
   - All configurations (paths, model names, parameters) are written in `config/config.yaml`.

2. **Entity Class Creation**  
   - Configuration values are loaded into structured data classes (entities) in the `entity/` folder for type-safe handling.

3. **Configuration Parsing**  
   - The file `configuration.py` reads the YAML config and maps values to the entity classes.

4. **Component Logic**  
   - In `component/`, core functions like downloading datasets or validating them are written. These functions do the actual work.

5. **Pipeline Execution**  
   - The `pipeline/` module calls components in a proper sequence, using configuration + entity objects.

6. **API Integration**  
   - `app.py` exposes `/train` and `/predict` endpoints using FastAPI, allowing users to trigger model training and summarization through HTTP.

---

## ⚙️ Technologies Used

- **FastAPI** for building the web API
- **Transformers** by Hugging Face for text summarization
- **PyYAML** for reading configuration files
- **Docker** for containerized deployment

---

This modular structure makes the project clean, testable, and easy to scale. Each part of the project has a clear responsibility, allowing smooth debugging, collaboration, and future extensions.



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 623932780522.dkr.ecr.us-east-2.amazonaws.com/text-s

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
