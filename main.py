# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.instagram.com/{}/"

# def scarpe(username):
#     full_url = URL.format(username)
#     r = requests.get(full_url)
#     s = BeautifulSoup(r.text,"lxml")

#     tag = s.find("meta",attrs= {"name":"description"})
#     text = tag.attrs['content']
#     main_text = text.split("-")[0]

#     return main_text

# USERNAME = 'anujajadhav636'
# data = scarpe(USERNAME)
# print(data)




from flask import Flask,request,json,render_template,redirect,url_for
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=5000)