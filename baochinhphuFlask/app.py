
from flask import Flask, request
from flask import render_template
from flask import jsonify
from flask_cors import CORS 

import utils

app = Flask(__name__)
#跨域处理
CORS(app, supports_credentials=True)

@app.route('/')
def flask():
    return render_template('index.html')

@app.route('/table_data',methods=['get','post'])
def table_data():
    Country=request.get_json(silent=True)
    wordsData = utils.tableData(Country['Country'])
    return jsonify({'data': wordsData[0], 'wordsData': wordsData[1]})

@app.route('/get_searchWords',methods=['get','post'])
def get_searchWords():
    title=request.get_json(silent=True)['searchData']
    Data=utils.getWordsdata(title)
    return jsonify({'data':Data})

@app.route('/get_yearData',methods=['get','post'])
def get_yearData():
    year=request.get_json(silent=True)['year']
    Country=request.get_json(silent=True)['country']
    Data=utils.getYeardata(year,Country)
    return jsonify({'data':Data[0],'wordsData':Data[1]})

@app.route('/words_Change',methods=['get','post'])
def words_Change():
    Country = request.get_json(silent=True)['Country']
    return jsonify({'data':utils.wordsChange(Country)})

@app.route('/get_mood',methods=['get','post'])
def get_mood():
    Country = request.get_json(silent=True)['Country']
    return jsonify({'data':utils.mood_data(Country)})

if __name__ == '__main__':
    app.run(port=5555)
