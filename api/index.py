import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/internal/contact', methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    phone = data.get("phone")

    if not all([name, email, message]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        sender_email = "vinussuperstore@gmx.com"
        password = "C00pperWood"

        receiver_email = "k.saseelan@hotmail.com"
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone or 'Not Given'}\n\nMessage:\n{message}"

        msg = MIMEMultipart()

        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg["Reply-To"] = email

        msg.attach(MIMEText(full_message, "plain"))

        with smtplib.SMTP("smtp.gmx.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        print("Email send error:", e)
        return jsonify({"error": "Email failed to send"}), 500