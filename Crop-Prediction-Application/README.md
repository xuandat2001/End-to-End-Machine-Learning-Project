
# Crop Prediction Web Application

This is a simple web application that allows farmers to upload crop images and predict the **variety**, **disease**, or **age** using machine learning models. It has a user-friendly React frontend and a Flask backend with trained TensorFlow models.

---

## What You Need

### General Requirements
- **Python 3.12+**
- **Node.js (LTS version)**
---
## How to Set Up (for Non-IT Users)

### For Windows

1. **Install Python**
   - Download: https://www.python.org/downloads/windows/
   - During installation, **tick** the box: **Add Python to PATH**
   - Open Command Prompt and run:
     ```
     python --version
     ```

2. **Install Node.js**
   - Download: https://nodejs.org
   - Choose the **LTS version**



### For macOS

1. **Install Python**
   - Open Terminal and run:
     ```
     brew install python
     ```

2. **Install Node.js**
   - Run:
     ```
     brew install node
     ```



##  Folder Structure

```
Crop-Prediction-Application/
├── Crop-Prediction-Application-Front-end/   ← React + Vite frontend
└── Crop-Prediction-Application-Back-end/    ← Flask backend with models
```
##  How to Run the App

### 1. Run the Backend (Flask)

>For Window:  Go to the backend folder and right click "Crop-Prediction-Application-Back-end folder" and  Open in terminal .
>For MacOs:  Go to the backend folder and right click(or Control + click) "Crop-Prediction-Application-Back-end folder" and  Select "Services" -> "New Terminal at Folder" from the menu.


```
cd Crop-Prediction-Application-Back-end
```

> Install required Python packages:

```
pip install flask tensorflow pillow
```
Install the Flask-cors: 
```
pip install flask-cors


> Start the Flask server:

```
python app.py
```

Note for macOS users
On some macOS systems, python may point to Python 2. If you get an error, try using:
```
python3 app.py
```


> The server should run at `http://localhost:5000`

---

### 2. Run the Frontend (React + Vite)

> For Window :Go to the frontend folder and right click "Crop-Prediction-Application-Front-end folder" and  Open in terminal .
> For MacOs: Go to the frontend folder and right click(or Control + click) "Crop-Prediction-Application-Front-end folder" and  Select "Services" -> "New Terminal at Folder" from the menu.
```
cd Crop-Prediction-Application-Front-end
```

> Install dependencies:

```
npm install
```

> Start the React app:

```
npm run dev
```

> The app should run at `http://localhost:5173`

---

##  Using the App

1. Open your browser and go to `http://localhost:5173`
2. Select a prediction task (Variety, Disease, or Age)
3. Upload a crop image (JPG or PNG)
4. Click **Upload & Predict**
5. The result will be shown below the image

---

##  Notes

- All models are pre-trained and saved as `.keras` files in the backend.
- Images are not stored in a database, only temporarily used for prediction.

---

##  Troubleshooting

- **If you get `'pip' is not recognized`**:
  - On Windows: Reinstall Python and check "Add to PATH"
- **If the frontend shows "Prediction failed"**:
  - Make sure Flask backend is running at `localhost:5000`
- **Need Help?**
  - Ask the project owner or search the error on Google/ChatGPT 😊

---

## Author
If you have questions, reach out to the developer of this app.
