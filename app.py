from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import os

app = Flask(__name__)

response = ""

@app.route('/', methods = ['GET', 'POST'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    # return("This is the USSD Sample Code for AfricasTalking")
    if text == '':
        response = "CON This is the Menu"
        response += "1. Display Name"
        response += "2. Display Country"
    elif text == "1":
        response = "END My Name is Suman Gangopadhyay"
    elif text == '2':
        response = "END My Country is India"


if __name__ == '__main__':
    app.run(port="5000")
