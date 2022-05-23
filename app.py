from crypt import methods
from distutils.log import debug
from pickle import GET
from flask import Flask, render_template,request
from requests import post

app = Flask(__name__)#instanciate class

@app.route("/index",methods['GET','POST'])  #
def index():
    return 'form data'

#if __name__ == '__main__':
    #app.run(debug = True)

if '__main__' == (__name__): #actualise port server 5000 
    app.run(host="localhost", debug= True, port=5000)




















# from calendar import LocaleHTMLCalendar
# from flask import Flask

# app =  Flask(__name__)#application object as an instance of class Flask imported from the flask package
# #__name__ variable passed to the Flask class is a Python predefined variable
# @app.route("/") # two strange @app.route lines above the function are decorators, a unique feature of the Python language
# def Hello():
#     return "Hello world"

# if __name__ == '__main__':
#     app.run(host="localhost", port=8000, debug=True)
