from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/purchases', methods=['POST'])
def add_purchase():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phoneNumber_receive = request.form['phoneNumber_give']

    purchase = {
        'name': name_receive,
        'number': number_receive,
        'address': address_receive,
        'phoneNumber': phoneNumber_receive
    }

    db.purchases.insert_one(purchase)
    return jsonify({'result': 'success'})

@app.route('/purchases', methods=['GET'])
def find_purchase():
    purchases = list(db.purchases.find({}, {'_id': 0}))
 
    return jsonify({'result': 'success', 'purchases': purchases})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
