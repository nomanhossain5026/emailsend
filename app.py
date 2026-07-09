from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        sender_email = request.form["sender_email"]
        app_password = request.form["app_password"]
        receiver_email = request.form["receiver_email"]
        subject = request.form["subject"]
        body = request.form["body"]

        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            server.quit()
            message = "Email sent successfully!"
        except Exception as e:
            message = f"Error: {e}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
