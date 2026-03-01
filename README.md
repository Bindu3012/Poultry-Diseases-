Poultry Disease Classification Web Application

Project Overview

This project implements a **Transfer Learning-based deep learning system** to classify poultry diseases into four categories:

* 🦠 Salmonella
* 🐓 Newcastle Disease
* 🧫 Coccidiosis
* ✅ Healthy

The trained model is integrated into a **Flask-based web application**, allowing users to upload poultry images and receive:

* Disease prediction
* Confidence score
* Treatment recommendation

The goal of this project is to assist poultry farmers and veterinary professionals with faster and more accessible disease detection.


Model Details

* **Base Model:** MobileNetV2 (Pretrained on ImageNet)
* **Technique:** Transfer Learning
* **Input Size:** 224 × 224
* **Optimizer:** Adam
* **Loss Function:** Categorical Crossentropy
* **Epochs:** 10
* **Final Validation Accuracy:** **94.07%**

The pretrained base layers were frozen, and custom classification layers were added for poultry disease detection.


System Architecture

```
User
   ↓
Frontend (HTML / CSS / JavaScript)
   ↓
Flask Backend API
   ↓
Trained Deep Learning Model (MobileNetV2)
   ↓
Prediction Output (Disease + Confidence + Treatment)
```

Application Screenshots

User Interface

![UI](assets/ui.png)

Prediction Result

![Prediction](assets/result.png)

Backend Running

![Backend](assets/backend.png)

---

How to Run the Project Locally

Install Dependencies

```bash
pip install -r backend/requirements.txt
```

Run Backend Server

```bash
cd backend
py app.py
```

The backend will start at:

```
http://127.0.0.1:5000
```

Run Frontend

Open `frontend/index.html` using Live Server.

Features

* Real-time image-based disease classification
* Confidence percentage output
* Treatment recommendation suggestions
* Image preview before prediction
* Clean and simple web interface
* 94% validation accuracy

Future Improvements

* Deploy application online (Render / AWS)
* Convert into Android mobile application
* Expand dataset for improved accuracy
* Add database for prediction history
* Add symptom-based text classification system

Author 
Guntaka Bindu Sri

