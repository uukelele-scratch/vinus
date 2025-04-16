import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#sk gC3cu-KfzLi-bwtMj-xvu4d

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)