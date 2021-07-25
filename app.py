from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import render_template
from biploar import makePredictionbipolar
from disease import makePrediction
from schi import makePredictionschi

import numpy as np

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('age', type=str)
parser.add_argument('sleep', type=str)
parser.add_argument('depressed', type=str)
parser.add_argument('reading', type=str)
parser.add_argument('academics', type=str)
parser.add_argument('pressure', type=str)
parser.add_argument('socialmedia', type=str)
parser.add_argument('annoyed', type=str)
parser.add_argument('afraid', type=str)
parser.add_argument('relaxing', type=str)
parser.add_argument('temper', type=str)
parser.add_argument('alone', type=str)
parser.add_argument('anxiety', type=str)
parser.add_argument('dead', type=str)
parser.add_argument('talk', type=str)
parser.add_argument('active', type=str)
parser.add_argument('highlow', type=str)

parser.add_argument('selfconfidence', type=str)
parser.add_argument('work', type=str)
parser.add_argument('angry', type=str)
parser.add_argument('dull', type=str)
parser.add_argument('tearful', type=str)
parser.add_argument('distracted', type=str)
parser.add_argument('social', type=str)
parser.add_argument('hyper', type=str)
parser.add_argument('vomitting', type=str)
parser.add_argument('think', type=str)
parser.add_argument('hear', type=str)
parser.add_argument('express', type=str)
parser.add_argument('see', type=str)
parser.add_argument('trust', type=str)
parser.add_argument('organize', type=str)
parser.add_argument('tracked', type=str)
parser.add_argument('jealous', type=str)
parser.add_argument('head', type=str)
parser.add_argument('speaking', type=str)
parser.add_argument('medical', type=str)


@app.route('/survey', methods=['POST', 'GET'])
@app.route('/')
def index():
    return render_template('index.html')


class MentalStateCheck(Resource):
    def get(self):
        args = parser.parse_args()
        # un = str(args['username'])
        # pw = str(args['password'])
        age = int(args['age'])
        sleep = int(args['sleep'])
        depressed = int(args['depressed'])
        reading = int(args['reading'])
        academics = int(args['academics'])
        pressure = int(args['pressure'])
        socialmedia = int(args['socialmedia'])
        annoyed = int(args['annoyed'])
        afraid = int(args['afraid'])
        relaxing = int(args['relaxing'])
        temper = int(args['temper'])
        alone = int(args['alone'])
        anxiety = int(args['anxiety'])
        dead = int(args['dead'])
        arr1 = [sleep, depressed, reading, academics, pressure,
                socialmedia, annoyed, afraid, relaxing, temper, alone, anxiety, dead]
        try:
            c = makePrediction(np.array(arr1, dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)


class diseaseprediction(Resource):
    def gets(self):
        args = parser.parse_args()
        talk = int(args['talk'])
        active = int(args['active'])
        highlow = int(args['highlow'])
        selfconfidence = int(args['selfconfidence'])
        work = int(args['work'])
        angry = int(args['angry'])
        dull = int(args['dull'])
        tearfull = int(args['tearfull'])
        distracted = int(args['distracted'])
        social = int(args['social'])
        hyper = int(args['hyper'])

        arr1 = [talk, active, highlow, selfconfidence, work,
                angry, dull, tearfull, distracted, social, hyper]
        try:
            c = makePredictionbipolar(np.array(arr1, dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)


@app.route('/diseasesurvey', methods=['POST', 'GET'])
class schidiseaseprediction(Resource):
    def gets(self):
        args = parser.parse_args()
        think = int(args['talk'])
        hear = int(args['active'])
        express = int(args['highlow'])
        see = int(args['selfconfidence'])
        trust = int(args['work'])
        organize = int(args['angry'])
        tracked = int(args['dull'])
        jealous = int(args['tearfull'])
        head = int(args['distracted'])
        speaking = int(args['social'])
        medical = int(args['hyper'])

        arr1 = [think, hear, express, see, trust,
                organize, tracked, jealous, head, speaking, medical]
        try:
            c = makepredictionschi(np.array(arr1, dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)


@app.route('/schisurvey', methods=['POST', 'GET'])
api.add_resource(HelloWorld, '/testing')


if __name__ == "__main__":
    app.run(debug=True)
