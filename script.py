from flask import Flask, flash, request, render_template, url_for, redirect, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from newspaper import Article
from flask import Flask, request, render_template
import joblib
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
model = joblib.load("Fake_News_Detector(LogesticRegression).pkl")



@app.route("/")
def home():
    return render_template("index.html")


def extract_text_from_link(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('article')

        if article:

            paragraphs = article.find_all('p')
            text = ' '.join([p.get_text() for p in paragraphs])
            return text
       
    else:
        return None


@app.route("/detect", methods=["POST", "GET"])
def detect():
    if request.method == "POST":
        web_link_verif = request.form.get("web-link")
        in_text_verif = request.form.get("in-text")

        if web_link_verif and in_text_verif:
            return render_template('detect1.html', error1= True)
        # Prioritize web link if both are provided
        elif "web-link" in request.form and request.form["web-link"]:
            web_link = request.form["web-link"]
            input_text = extract_text_from_link(web_link)
            if input_text is None:
                return render_template('detect1.html', error2 = True)
        elif "in-text" in request.form and request.form["in-text"]:
            input_text = request.form["in-text"]    
        else:
            return render_template('detect1.html', error = True)
           
        
        # Debugging: Print the extracted input text
        # print("Extracted input text:", input_text)
        
        prediction = model.predict([input_text])
        prediction_proba = model.predict_proba([input_text])[0]
        
        # Convert prediction to a readable format
        result = "Vraies Nouvelles" if prediction[0] == 1 else "Fausses Nouvelles"
        
        return render_template('detect1.html', prediction_text=result, real_prediction_proba=round(prediction_proba[1], 2)*100, fake_prediction_proba=round(prediction_proba[0], 2)*100)
    else:
        return render_template("detect1.html")


if __name__ == "__main__":
    app.run(debug=True)
