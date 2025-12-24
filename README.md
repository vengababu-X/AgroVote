<p align="center">
  <img src="assets/BLOCK DIAGRAM1.jpg" width="700"/>
</p>

<h1 align="center">🌾 AgroVote</h1>

<p align="center">
A Hybrid IoT and Machine Learning Approach for Crop Recommendation  
Using a Voting Ensemble Model
</p>

---

## 📌 About the Project

AgroVote is a smart agriculture decision-support system designed to
recommend the most suitable crop based on soil and environmental
conditions. The system combines **IoT-based data collection** with
**machine learning ensemble models** to improve the accuracy and
reliability of crop recommendations.

This project focuses on practical implementation rather than theoretical
assumptions by integrating real-world parameters with data-driven models.

---

## 🧠 System Block Diagram

<p align="center">
  <img src="assets/BLOCK DIAGRAM2.jpg" width="650"/>
</p>

### Description
The system block diagram shows how input parameters such as:
- Nitrogen (N), Phosphorus (P), Potassium (K)
- Temperature
- Humidity
- Rainfall
- Soil pH

are processed by a **Voting Ensemble Machine Learning Model** to generate
a suitable crop recommendation.

---

## 🔁 System Workflow

<p align="center">
  <img src="assets/WORKFLOW1.jpg" width="650"/>
</p>

### Workflow Steps
1. Collection of soil and environmental data  
2. Data preprocessing and normalization  
3. Prediction using multiple ML models  
4. Decision-making using voting ensemble logic  
5. Final crop recommendation  

---

## 🤖 Machine Learning Model

<p align="center">
  <img src="assets/MACHINE LEARNING1.jpg" width="650"/>
</p>

### Models Used
- Decision Tree  
- Naive Bayes  
- Random Forest  

The predictions from individual models are combined using a **Hard Voting
Ensemble Classifier**, where the final output is selected based on
majority voting.

This approach reduces bias and improves prediction stability.

---

## 🔌 Sensors and Hardware

<p align="center">
  <img src="assets/SENSORS & HARDWARE1.jpg" width="650"/>
</p>

### Hardware Components
- ESP32 / NodeMCU  
- Soil Moisture Sensor  
- DHT11 / DHT22 (Temperature & Humidity)  
- Soil pH Sensor (optional)  
- Jumper Wires  
- Breadboard  
- Power Supply  

The sensors collect real-time data which can be transmitted to the
backend system for analysis.

---

## 📊 Sample Output / Demo

<p align="center">
  <img src="assets/Demo output.jpg" width="700"/>
</p>

This section shows a sample visualization of the crop recommendation
output. The dashboard represents how environmental data and predictions
can be presented to the user.

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

## 🌱 Applications

- Smart Agriculture  
- Precision Farming  
- Crop Planning Support  
- Academic and Research Projects  

---

## 📜 License

This project is licensed under the MIT License.
