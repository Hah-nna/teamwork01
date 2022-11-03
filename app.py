# 가상환경 설정하기
# venv로 가상환경을 설정했습니다. flask, pymongo, dnspython

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://admin:adminshow@cluster0.3luh09a.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.db



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hana')
def hana():
    return render_template('Hana.html')

@app.route("/hana/post", methods=["POST"])
def hana_post():
    name = request.form['name']
    text = request.form['text']
    doc = {
        'name': name,
        'text': text
    }
    db.commentsHana.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/hana/delete", methods=["DELETE"])
def hana_delete():
    _id = request.form['_id']
    db.commentsHana.find_one_and_delete({'_id': ObjectId(_id)})
    return jsonify({'msg': '삭제'})

@app.route("/hana/get", methods=["GET"])
def hana_get():
    comment_list = list(db.commentsHana.find({}))
    for i in comment_list:
        i['_id'] = str(i['_id'])
    return jsonify({'comments': comment_list})

# jeongik

@app.route('/jeongik')
def jeongik():
    return render_template('Jeongik.html')

@app.route("/jeongik/post", methods=["POST"])
def jeongik_post():
    name = request.form['name']
    text = request.form['text']
    doc = {
        'name': name,
        'text': text
    }
    db.commentsJeongik.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/jeongik/get", methods=["GET"])
def jeongik_get():
    comment_list = list(db.commentsJeongik.find({}))
    for i in comment_list:
        i['_id'] = str(i['_id'])
    return jsonify({'comments': comment_list})

@app.route("/jeongik/delete", methods=["DELETE"])
def jeongik_delete():
    _id = request.form['_id']
    db.commentsJeongik.find_one_and_delete({'_id': ObjectId(_id)})
    return jsonify({'msg': '삭제'})

# sanghyun

@app.route('/sanghyun')
def sanghyun():
    return render_template('Sanghyun.html')

@app.route("/sanghyun/post", methods=["POST"])
def sanghyun_post():
    name = request.form['name']
    text = request.form['text']
    doc = {
        'name': name,
        'text': text
    }
    db.commentsSanghyun.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/sanghyun/delete", methods=["DELETE"])
def sanghyun_delete():
    _id = request.form['_id']
    db.commentsSanghyun.find_one_and_delete({'_id': ObjectId(_id)})
    return jsonify({'msg': '삭제'})

@app.route("/sanghyun/get", methods=["GET"])
def sanghyun_get():
    comment_list = list(db.commentsSanghyun.find({}))
    for i in comment_list:
        i['_id'] = str(i['_id'])
    return jsonify({'comments': comment_list})

# yujin

@app.route('/yujin')
def yujun():
    return render_template('Yujin.html')

@app.route("/yujin/post", methods=["POST"])
def yujin_post():
    name = request.form['name']
    text = request.form['text']
    doc = {
        'name': name,
        'text': text
    }
    db.commentsYujin.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/yujin/delete", methods=["DELETE"])
def yujin_delete():
    _id = request.form['_id']
    db.commentsYujin.find_one_and_delete({'_id': ObjectId(_id)})
    return jsonify({'msg': '삭제'})

@app.route("/yujin/get", methods=["GET"])
def yujin_get():
    comment_list = list(db.commentsYujin.find({}))
    for i in comment_list:
        i['_id'] = str(i['_id'])
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
