# Iris Classification App

This repository contains an app for classifying Iris species based on input features such as sepal length, sepal width, petal length, and petal width. The model is trained using a **Support Vector Classifier (SVC)** from `scikit-learn`, with hyperparameter optimization and experiment tracking via **MLflow**. The app is built using **FastAPI** and is containerized using **Docker**.

## Project Overview

- **Model**: Trained using **Support Vector Classifier (SVC)** from `scikit-learn` on the Iris dataset, which contains the following features:
  - `sepalLength` (sepal length in cm)
  - `sepalWidth` (sepal width in cm)
  - `petalLength` (petal length in cm)
  - `petalWidth` (petal width in cm)

- **Model Accuracy**: Achieved a classification accuracy of 98% on the test data.

- **Tools & Libraries**:
  - Python 3.9.19
  - `scikit-learn` for building the SVC classifier
  - `Optuna` for hyperparameter optimization
  - `MLflow` for tracking experiments and model versioning
  - `LIME` for model explainability
  - `FastAPI` for building the web app
  - `HTML` for the web page structure
  - `Docker` for containerizing the application

## Installation & Setup

### 1. Create a Python Environment

Create a new Python environment (recommended using `venv` or `conda`) and install the required dependencies. <br>
*Note: Python 3.9.19 recommended*

```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment

# On Windows
#venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt
```

### 2. Start MLflow Server

MLflow is used for experiment tracking, including the hyperparameter optimization of the SVC model.

To start the MLflow server, run:

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

This will start the MLflow server at `http://127.0.0.1:5000`, where you can view and track experiments.

### 3. Train the Model

Run the `iris-classification-svc.ipynb` notebook to train the model. The notebook includes steps for:

- Loading and preparing the data
- Training the Support Vector Classifier (SVC)
- Performing hyperparameter optimization using Optuna
- Tracking experiments using MLflow
- Generating model explanations using LIME

After running the notebook, a trained model pickle file (`svc_model.pkl`) will be saved in the `app/` directory.

*Note: The trained model is already available in the `app/` directory. If you want to replace it with a new model, you can retrain it by running the notebook again.*

### 4. Test the App

To test the FastAPI app, run the following command:

```bash
cd app/
python app.py
```

Once the app is running, it will be accessible via the following URLs:

- **Main App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Swagger UI (for API documentation)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Dockerize the Application

After training the model, you can containerize the app using Docker.

#### a) Build the Docker Image

Navigate to the root directory of the project and build the Docker image using the following command:

```bash
docker build -t iris-classification-app .
```

#### b) Run the Docker Container

Once the image is built, run the Docker container:

```bash
docker run -p 8000:8000 iris-classification-app
```

This will start the FastAPI app inside a container and expose it on `http://127.0.0.1:8000/`.

---

## Folder Structure

```
├── .github/
│   ├── workflows/
│       ├── ci-cd-pipeline.yml 
├── app/
│   ├── templates/
│       ├── home.html 
│   ├── images/
│       ├── Iris-setosa.jpg 
│       ├── Iris-versicolor.jpg 
│       ├── Iris-virginica.jpg 
│   ├── tests/
│       ├── test_app.py
│   ├── app.py                  # FastAPI application
│   ├── reg_model.pkl           # Trained Logistic Regression model (Pickle file)
├── dataset/                    # Dataset to train the model
│   ├── Iris.csv
├── Dockerfile                  # Dockerfile to build the container
├── heart-disease-prediction-logistic-regression.ipynb  # Jupyter notebook for training
├── requirements.txt            # Required Python packages
└── README.md                   # This file
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
```

This README is structured similarly to your previous one and tailored for your Iris Classification App. You can copy and paste this into your `README.md` file.


