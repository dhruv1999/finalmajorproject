from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import render_template
from file2 import makePrediction
from disease import makePrediction2
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
def funcPost():
    c = None
    if request.method == 'POST':
        try:
            age = int(request.form['group0'])
            age2 = age

        except:
            age = 1

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        sleep = dict1[request.form['group1']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        depressed = dict1[request.form['group2']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        reading = dict1[request.form['group3']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        academics = dict1[request.form['group4']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        pressure = dict1[request.form['group5']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        socialmedia = dict1[request.form['group6']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        annoyed = dict1[request.form['group7']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        afraid = dict1[request.form['group8']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        relaxing = dict1[request.form['group9']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        temper = dict1[request.form['group10']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        alone = dict1[request.form['group11']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        anxiety = dict1[request.form['group12']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        dead = dict1[request.form['group13']]

        result = sleep + depressed + reading + academics + pressure + socialmedia + \
            annoyed + afraid + relaxing + temper + alone + anxiety + dead

        dict1 = {0: "Not at all", 1: "Moderately", 2: "Severely"}
        if result <= 8:
            result = 0
        elif result >= 9 and result <= 15:
            result = 1
        else:
            result = 2
        return render_template('results.html', result=dict1[result])
    return render_template('survey.html', result=c)


@app.route('/')
def index():
    return render_template('index.html')


class HelloWorld(Resource):
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
            c = makePrediction2(np.array(arr1, dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)


@app.route('/diseasesurvey', methods=['POST', 'GET'])
def funcPostdisease():
    c = None
    if request.method == 'POST':

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        talk = dict1[request.form['group1']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        active = dict1[request.form['group2']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        highlow = dict1[request.form['group3']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        selfconfidence = dict1[request.form['group4']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        work = dict1[request.form['group5']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        angry = dict1[request.form['group6']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        dull = dict1[request.form['group7']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        tearful = dict1[request.form['group8']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        distracted = dict1[request.form['group9']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        social = dict1[request.form['group10']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        hyper = dict1[request.form['group11']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        vomitting = dict1[request.form['group12']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        dead = dict1[request.form['group13']]

        result = talk + active + highlow + selfconfidence + work + \
            angry + dull + tearful + distracted + social + hyper + vomitting + dead

        dict1 = {0: "No bipolar", 1: "bipolar"}
        if result < 12:
            result = 0

        else:
            result = 1
        return render_template('diseaseresult.html', result=dict1[result])
    return render_template('diseasesurvey.html', result=c)


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
            c = makePrediction2(np.array(arr1, dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)


@app.route('/schisurvey', methods=['POST', 'GET'])
def schisurvey():
    c = None
    if request.method == 'POST':
        try:
            age = int(request.form['group0'])
            age2 = age

        except:
            age = 1

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        think = dict1[request.form['group1']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        hear = dict1[request.form['group2']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        express = dict1[request.form['group3']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        see = dict1[request.form['group4']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        trust = dict1[request.form['group5']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        oraganize = dict1[request.form['group6']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        tracked = dict1[request.form['group7']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        jealous = dict1[request.form['group8']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        head = dict1[request.form['group9']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        speaking = dict1[request.form['group10']]

        dict1 = {"Not at all": 0, "Moderately": 1, "Severely": 2}
        medical = dict1[request.form['group11']]

        result = think + head + express + see + trust + oraganize + \
            tracked + jealous + head + speaking + medical

        dict1 = {0: "No schi", 1: "schi"}
        if result < 12:
            result = 0

        else:
            result = 1
        return render_template('schiresult.html', result=dict1[result])
    return render_template('schisurvey.html', result=c)


api.add_resource(HelloWorld, '/testing')


if __name__ == "__main__":
    app.run(debug=True)
