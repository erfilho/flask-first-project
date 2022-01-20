from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_temp():
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/5522/").content
    soup = BeautifulSoup(html, 'html.parser')
    temp = (soup.find("span", class_="-bold -gray-dark-2 -font-55 _margin-l-20 _center").string)[:-2]
    return temp
@app.route('/')
def index():
    return render_template('index.html', temp=get_temp())