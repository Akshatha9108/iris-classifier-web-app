# iris-classifier-web-app
---
**Iris Classifier Web App**

This repository contains a Flask-based web application designed to classify Iris flowers based on their sepal and petal dimensions. The app utilizes a pre-trained machine learning model to predict the class of Iris flowers and provides a user-friendly interface for interacting with the model.

### Features
- **Web Interface**: A simple HTML form allows users to input sepal and petal dimensions.
- **Machine Learning Integration**: Uses a pre-trained model (saved as `saved_model.sav`) to make predictions based on user input.
- **Prediction Results**: Displays the predicted Iris class in a readable format.

### Technologies Used
- **Python**: Core programming language for backend development.
- **Flask**: Web framework used to create the web application.
- **Pickle**: Library for loading and using the pre-trained machine learning model.
- **HTML**: Used for creating the frontend form to capture user inputs.

### Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-classifier-web-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd iris-classifier-web-app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

### Usage
- Open a web browser and navigate to `http://127.0.0.1:5000/`.
- Enter the sepal and petal dimensions into the form and click the "Predict" button to see the classification result.

### Contribution
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!

---

This description provides a clear overview of what the project does, the technologies used, and how others can set up and use the application.
