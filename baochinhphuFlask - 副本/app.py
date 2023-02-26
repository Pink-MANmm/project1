import json

from flask import Flask, request
from flask import render_template
from flask import jsonify

import utils

app = Flask(__name__)


@app.route('/')
def flask():
    return render_template('yuenan.html')

@app.route('/越南')
def yuenan():
    return render_template('yuenan.html')

@app.route('/巴基斯坦')
def pakistan():
    return render_template('pakistan.html')

@app.route('/印度')
def yindu():
    return render_template('yindu.html')

@app.route('/get_dbLength',methods=['get','post'])
def get_dbLength():
    Country=json.loads(request.form.get('Country'))
    return jsonify({'data': utils.dbLength(Country)})

@app.route('/table_data',methods=['get','post'])
def table_data():
    Country=json.loads(request.form.get('Country'))
    wordsData = utils.tableData(Country)
    return jsonify({'data': wordsData[0], 'wordsData': wordsData[1]})

@app.route('/get_searchWords',methods=['get','post'])
def get_searchWords():
    words=json.loads(request.form.get('searchData'))
    Data=utils.getWordsdata(words)
    return jsonify({'data':Data})

@app.route('/get_yearData',methods=['get','post'])
def get_yearData():
    year=json.loads(request.form.get('year'))
    Country=json.loads(request.form.get('Country'))
    Data=utils.getYeardata(year,Country)
    return jsonify({'data':Data[0],'wordsData':Data[1]})

@app.route('/words_Change',methods=['get','post'])
def words_Change():
    Country = json.loads(request.form.get('Country'))
    return jsonify({'data':utils.wordsChange(Country)})

@app.route('/get_mood',methods=['get','post'])
def get_mood():
    Country = json.loads(request.form.get('Country'))
    return jsonify({'data':utils.mood_data(Country)})

@app.route('/wordsChange_Init',methods=['get','post'])
def wordsChange_Init():
    utils.wordsChange_Init()
    return None

if __name__ == '__main__':
    app.run(port=5555)
