from flask import Flask, render_template, request, json, jsonify, make_response
import requests
import re
from flask import Markup

app = Flask(__name__)


# ホーム
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


# Ajax
@app.route('/ajax_test', methods=["GET", "POST"])
def ajax_test():
    datas = list()
    datas.append({'id': '1'
                 ,'name': 'nagao'
                 })
    datas.append({'id': '2'
                 ,'name': 'akatomo'
                 })
    return jsonify(datas)

# アプリ起動
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
