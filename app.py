#From Flask, I want to import Flask, render_template and request
from flask import Flask, render_template, request

#Declare the app
app = Flask(__name__)

# Start an app route wich is '/'
@app.route('/')
#Declare the main function
def main():
    return render_template('app.html')

