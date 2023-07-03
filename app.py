import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template
import io
import base64

plt.switch_backend('agg')

amazon_data = pd.read_csv('amazon.csv', encoding = 'latin1')
apple_data = pd.read_csv('APPLE_iPhone_SE.csv', encoding = 'latin1')
flipkart_data = pd.read_csv('flipkart.csv', encoding = 'latin1')
myntra_data = pd.read_csv('myntra.csv',encoding = 'latin1')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Amazon",  methods=['GET', 'POST'])
def Amazon():
    return render_template("Amazon.html")

@app.route("/Apple")
def Apple():
    return render_template("Apple.html")

@app.route("/Flipkart")
def Flipkart():
    return render_template("Flipkart.html")

@app.route("/Myntra")
def Myntra():
    return render_template("Myntra.html")

app.run(debug= True)
