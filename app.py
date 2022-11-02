# 가상환경 설정하기
# venv로 가상환경을 설정했습니다. flask, pymongo, dnspython

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('(하나님 MongoDB Link 여기 넣습니다.)')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # 클라이언트에서 서버로 받은 정보
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name' : name_receive,
        'comment' :
            comment_receive
    }
    db.homework.insert_one(doc)
    return jsonify({'msg':'스포: 핀과 제이크는 셜미와 베스로 환생합니다.'})

@app.route("/homework", methods=["GET"])
def homework_get():
    saying_list = list(db.homework.find({}, {'_id': False}))
    return jsonify({'saying': saying_list})

if __name__ == '__main__':
    print('hello world!')
    # help(Flask)
    help(MongoClient)

#    app.run('0.0.0.0', port=5000, debug=True)
