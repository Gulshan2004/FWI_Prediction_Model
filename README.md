# 🔥 FWI Prediction Web App (Forest Fire Risk)

This is a Machine Learning web application that predicts the **Fire Weather Index (FWI)** — an important metric used to assess the risk of forest fires based on various weather and environmental features.

Built with **Flask** for the backend and **HTML** for the frontend, this project brings ML models like **Ridge**, **Lasso**, and **ElasticNet** into a deployable and interactive web format.

---

## 📌 Features

- Predicts Fire Weather Index (FWI) based on environmental data
- Takes user input through a simple web UI
- Supports Ridge, Lasso, and ElasticNet Regression models
- Shows instant output after submission
- Clean and minimal frontend using plain HTML

---

## 🧰 Tech Stack

| Layer       | Tools/Frameworks                    |
|-------------|-------------------------------------|
| ML Model    | Scikit-learn (Ridge, Lasso, ElasticNet) |
| Backend     | Python, Flask                       |
| Frontend    | HTML, CSS                           |
| Data Used   | Algerian Forest Fire Dataset        |
| Deployment  | Localhost (can be extended to Heroku, Render, etc.) |

---

## 📊 Input Features

- Temperature (°C)
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain (mm)
- FFMC (Fine Fuel Moisture Code)
- DMC (Duff Moisture Code)
- DC (Drought Code)
- ISI (Initial Spread Index)
- BUI (Build-Up Index)
- Region (converted to numerical)

📈 **Target:** Fire Weather Index (FWI)

---

## 🚀 How to Run Locally

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. Create a virtual environment & activate it:
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt 

4. Run the Flask App:
   python application.py

5. Visit in Browser:
   http://127.0.0.1:5000/predictdata
   
📁 Project Structure
pgsql
Copy
Edit
📦 your-repo-name/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (if any)
├── models/
│   └── trained_model.pkl
├── requirements.txt
└── README.md

📌 Screenshots / Demo
<img width="1919" height="1077" alt="Screenshot 2025-07-24 204323" src="https://github.com/user-attachments/assets/9dd81b4c-29c7-4b94-8755-e4fbc9626b68" />
<img width="1916" height="1077" alt="Screenshot 2025-07-24 204339" src="https://github.com/user-attachments/assets/56f5461c-a0b2-4bfd-a463-8e48b16da36b" />

🤝 Acknowledgements
Dataset: UCI Algerian Forest Fire Dataset

ML Algorithms from scikit-learn

📬 Contact
Gulshan Kumar
Aspiring ML Engineer | BTech CSE Student
🔗 www.linkedin.com/in/gulshan-kumar-a10237293
📫 gulshankumar1923070@gmail.com
