from calendar import LocaleHTMLCalendar
from flask import Flask

app =  Flask(__name__)#application object as an instance of class Flask imported from the flask package
#__name__ variable passed to the Flask class is a Python predefined variable
@app.route("/")
def Hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    
