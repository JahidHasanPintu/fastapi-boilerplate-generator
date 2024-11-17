# **FastAPI Enterprise Boilerplate Generator**

This repository contains scripts to quickly create an enterprise-level folder structure for a **FastAPI** project. The boilerplate includes a well-organized directory layout, example files, and configurations to help developers kick-start their FastAPI projects.

---

## **Features**

- **Dynamic Project Naming**: The user can provide a custom project name during script execution.
- **Enterprise-Grade Structure**:
  - Pre-configured directories for **models**, **schemas**, **services**, **repositories**, **utils**, **middlewares**, **api**, and more.
  - Supports API versioning with `v1` routing included.
- **Pre-created example files**:
  - `main.py` with basic route setup
  - `settings.py` for environment configuration
  - Example unit tests with `pytest`
- **Generated configuration files**:
  - `.gitignore`
  - `requirements.txt`
  - `README.md`
- **Support for Docker**: Includes `Dockerfile` and `docker-compose.yml` for easy containerization.
- Automatically installs FastAPI dependencies in the `requirements.txt`.

---

## **System Requirements**

To use these scripts, make sure your system has:

1. **Python**: Version 3.8 or later.
2. **Bash**: Installed (for running the Bash script).
3. **Git**: For initializing and pushing the project to a GitHub repository (optional).
4. **Docker** (optional): To use the included Docker setup.

---

## **Setup and Usage**

You can use either the **Bash script** or the **Python script** to generate the boilerplate. Below are detailed instructions for both.

---

### **1. Using the Bash Script**

#### **Steps**:

1. Save the `create_fastapi_project.sh` script to your local system.

   - Example: Download it or copy the code into a file named `create_fastapi_project.sh`.

2. Make the script executable by running the following command:

   ```bash
   chmod +x create_fastapi_project.sh
   ```

3. Run the script::

   ```bash
   ./create_fastapi_project.sh
   ```

4. Enter your desired project name when prompted. For example:

   ```bash
   Enter your project name: my_fastapi_project
   ```

5. Navigate to the project folder:

   ```bash
   cd my_fastapi_project
   ```

### **2. Using the Python Script**

#### **Steps**:

1. Save the `create_fastapi_structure.py` script to your local system.

   - Example: Download it or copy the code into a file named `create_fastapi_structure.py`

2. Run the script using Python :

   ```bash
   python create_fastapi_structure.py
   ```

3. Enter your desired project name when prompted. For example:

   ```bash
   Enter your project name: my_fastapi_project
   ```

4. Navigate to the project folder:

   ```bash
   cd my_fastapi_project
   ```

## **Contributing**

Feel free to contribute by opening issues, submitting bug reports, or creating pull requests. Contributions are always welcome!

---

## **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute this script.

---

## **Feedback**

If you find this repository helpful or encounter any issues, please feel free to reach out or leave a star ⭐ on the GitHub repository.

---
