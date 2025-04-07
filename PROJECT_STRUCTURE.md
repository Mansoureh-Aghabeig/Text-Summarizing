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
- **Uvicorn** for running the ASGI server
- **Transformers** by Hugging Face for text summarization
- **PyYAML** for reading configuration files
- **Jinja2** (optional) for templating
- **Pydantic** for data validation
- **Docker** for containerized deployment

---

This modular structure makes the project clean, testable, and easy to scale. Each part of the project has a clear responsibility, allowing smooth debugging, collaboration, and future extensions.


