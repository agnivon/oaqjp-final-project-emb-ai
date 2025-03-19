"""server.py"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emmtion Detector")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """detect emotion"""
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    if result['dominant_emotion']:
        return f"For the given statement, \
        the system response is \
        'anger': {result['anger']}, \
        'disgust': {result['disgust']}, \
        'fear': {result['fear']}, \
        'joy': {result['joy']} and \
        'sadness': {result['sadness']}.\
         The dominant emotion is {result['dominant_emotion']}."
    return 'Invalid text! Please try again!.', 400

@app.route("/", methods=["GET"])
def index():
    """index"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
