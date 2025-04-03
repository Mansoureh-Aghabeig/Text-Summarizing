# Text-Summarizing

# Text Summarizer - Project Structure

## Root Directory Files
- .gitignore  
- app.py  
- Dockerfile  
- main.py  
- params.yaml  
- README  
- setup.py  
- template.py  

## Folders
- github/
- artifact/
- config/
  - config.yaml
- log/
- research/
  - notebook/

## Project Structure
- src/
  - textsummarizer/
    - __init__.py  
    - config/
      - __init__.py  
      - configuration.py  
    - component/
      - __init__.py  
      - data_ingestion.py  
      - data_validation.py  
    - constant/
      - __init__.py  
    - entity/
      - __init__.py  
    - logging/
      - __init__.py  
    - pipeline/
      - __init__.py  
      - data_ingestion.py  
      - data_validation.py  
    - utils/
      - __init__.py  
      - common.py


## Project Workflow Overview

The overall workflow of the **Text Summarizer** project is structured and modular. Here's a step-by-step explanation of how different parts of the project interact:

1. **Define the Configuration Structure**  
   The process starts by defining the overall configuration structure inside the `config/config.yaml` file. This file contains all necessary parameters and paths needed for various stages of the pipeline, such as data ingestion and validation.

2. **Create Entity Classes**  
   Based on the configuration file, we define entity classes inside the `entity` module. These classes act as data models that help structure the configuration data in a clean, object-oriented format.

3. **Load Configurations into Entity Classes**  
   Inside the `src/textsummarizer/config/configuration.py`, the configuration file (`config.yaml`) is read. The relevant sections are parsed and used to instantiate and populate the previously defined entity classes. This bridges the raw YAML config file and the actual working code.

4. **Component-Level Implementation**  
   Inside the `component` module (e.g., `data_ingestion.py`, `data_validation.py`), we implement the core logic for each stage of the pipeline. These modules perform the actual data-related operations, such as downloading and validating data.

5. **Pipeline Execution**  
   The `pipeline` module orchestrates the process in a sequential manner. For example, within the data ingestion pipeline:
   - The configuration is first read.
   - The relevant entity class is populated using the parsed configuration.
   - Then the corresponding component (e.g., `DataIngestion`) is called to perform its task.

This clean separation of concerns ensures that each part of the project is well-organized and scalable. By managing configurations, data structures, core logic, and execution flow separately, the project becomes easier to maintain and extend.



# Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py
