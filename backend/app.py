from flask import Flask, request
import sqlalchemy as db
from bs4 import BeautifulSoup
import requests

engine = db.create_engine("mysql+pymysql://user:password@db:3306/mydatabase")
app = Flask(__name__)

@app.route('/newEntry', methods=['POST'])
def testing():
    request_data = request.get_json()
    print(request_data)
    return 'Data received'

@app.route('/bs-test', methods=['POST'])
def test():
    url="https://awesomewritingprompts.tumblr.com"
    request_result=requests.get( url ) 
    soup = BeautifulSoup(request_result.text, "html.parser") 
    print(soup)
    return soup

@app.route('/getEntry')
def index():
    select_stmt = 'SELECT * FROM users'
    result = engine.connect().execute(
        db.text(select_stmt)
    )
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)