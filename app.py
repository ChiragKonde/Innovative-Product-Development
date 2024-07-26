import requests
import json
from flask import Flask
from firebase_admin import credentials, initialize_app, db

# Path to the service account key file
SERVICE_ACCOUNT_KEY_PATH = "D:\ipd\mirage-main\mirage-main\ipd0-6e264-firebase-adminsdk-pruwz-5d051dd728.json"

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
initialize_app(cred, {
    'databaseURL': 'https://ipd0-6e264-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route("/", methods=['GET'])
def genReport():
    id = input("Enter an ID: ")
    url = input("Enter the URL: ")

    try:
        # Fetch data from the live website
        response = requests.get(url)
        if response.status_code == 200:
            # Extract data from the response
            web_html = response.text
            # Process the data as needed
            # For demonstration, just storing the raw HTML data
            db.reference('/privacy/' + id).update({'data': web_html, 'status': 'DONE'})
        else:
            db.reference('/privacy/' + id).update({'status': 'ERROR'})
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        db.reference('/privacy/' + id).update({'status': 'ERROR'})

    return "True"

@app.route("/api2/", methods=['GET'])
def scaperApi():
    id = input("Enter an ID: ")
    url = input("Enter the URL: ")

    try:
        # Fetch data from the live website
        response = requests.get(url)
        if response.status_code == 200:
            # Extract data from the response
            output2 = response.text
            # Process the data as needed
            # For demonstration, just storing the raw HTML data
            db.reference('/gdpr/' + id).update({'data': output2, 'status': 'DONE'})
        else:
            db.reference('/gdpr/' + id).update({'status': 'ERROR'})
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        db.reference('/gdpr/' + id).update({'status': 'ERROR'})

    return "True"

if __name__ == '__main__':
    app.run(debug=True)
