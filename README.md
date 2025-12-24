# 🌾 AGROVOTE

### A Hybrid IoT and Machine Learning Approach for Crop Recommendation  
### Using a Voting Ensemble Model

---

## 📌 About the Project

AgroVote is a smart agriculture decision-support system designed to
recommend the most suitable crop based on soil and environmental
conditions. The system integrates **IoT-based data collection** with
**machine learning ensemble techniques** to improve the accuracy and
reliability of crop recommendations.

The project focuses on practical implementation by combining real-world
parameters such as soil nutrients and weather conditions with data-driven
machine learning models.

---

## 🧠 System Block Diagram

![System Block Diagram](assets/BLOCK%20DIAGRAM1.jpg)

![System Block Diagram - Extended](assets/BLOCK%20DIAGRAM2.jpg)

### Description

The system block diagram illustrates how the following input parameters
are collected and processed:

- Nitrogen (N), Phosphorus (P), Potassium (K)
- Temperature
- Humidity
- Rainfall
- Soil pH

These parameters are analyzed using a **Voting Ensemble Machine Learning
Model** to recommend the most suitable crop for cultivation.

---

## 🔁 System Workflow

![System Workflow](assets/WORKFLOW1.jpg)

![System Workflow - Detailed](assets/WORKFLOW2.jpg)

### Workflow Steps

1. Collection of soil and environmental data  
2. Data preprocessing and normalization  
3. Feature extraction  
4. Prediction using multiple machine learning models  
5. Decision making using voting ensemble logic  
6. Final crop recommendation  

---

## 🤖 Machine Learning Model

![Machine Learning Models](assets/MACHINE%20LEARNING1.jpg)

![Random Forest Example](assets/MACHINE%20LEARNING2.jpg)

![Ensemble Model](assets/MACHINE%20LEARNING3.jpg)
### Models Used

- Decision Tree  
- Naive Bayes  
- Random Forest  

The outputs of individual models are combined using a **Hard Voting
Ensemble Classifier**, where the final prediction is selected based on
majority voting. This approach reduces bias and improves prediction
stability compared to single-model systems.

---

## 🔌 Sensors and Hardware

![Sensors and Hardware](assets/SENSORS%20%26%20HARDWARE1.jpg)

![Sensors and Hardware - Setup](assets/SENSORS%20%26%20HARDWARE2.jpg)

![Sensors and Hardware - Field View](assets/SENSORS%20%26%20HARDWARE3.jpg)

### Hardware Components

- ESP32 / NodeMCU  
- Soil Moisture Sensor  
- DHT11 / DHT22 (Temperature & Humidity)  
- Soil pH Sensor (optional)  
- Jumper Wires  
- Breadboard  
- Power Supply  

The sensors collect real-time environmental and soil data which can be
transmitted to the backend system for analysis.

---

## 📊 Sample Output / Demo

![Demo Output](assets/Demo%20output.jpg)

![Demo Output 1](assets/Demo%20output1.jpg)

![Demo Output 2](assets/Demo%20output2.jpg)

This section shows a sample visualization of crop recommendation results
and environmental insights.  
*(Prototype / demonstration purpose)*

---

## 🧩 Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- Arduino IDE  
- ESP32  

---

🌱 Applications
●Smart Agriculture
●Precision Farming
●Crop Planning Support
●Academic and Research Projects

---
## 📁 Project Structure

```text
AgroVote/
├── assets/
│   ├── BLOCK DIAGRAM1.jpg
│   ├── BLOCK DIAGRAM2.jpg
│   ├── WORKFLOW1.jpg
│   ├── WORKFLOW2.jpg
│   ├── MACHINE LEARNING1.jpg
│   ├── MACHINE LEARNING2.jpg
│   ├── MACHINE LEARNING3.jpg
│   ├── SENSORS & HARDWARE1.jpg
│   ├── SENSORS & HARDWARE2.jpg
│   ├── SENSORS & HARDWARE3.jpg
│   ├── Demo output.jpg
│   ├── Demo output1.jpg
│   └── Demo output2.jpg
│
├── iot/
│   └── esp32_sensors.ino
│
├── ml/
│   ├── dataset.csv
│   ├── train_model.py
│   └── model.pkl
│
├── server/
│   └── app.py
│
├── README.md
├── requirements.txt
└── LICENSE




