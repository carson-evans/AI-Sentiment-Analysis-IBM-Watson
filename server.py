'''Executing this function initiates the application of Emotion Detector 
   to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''This code receives the text from the HTML interface and runs sentiment analysis over it 
       using emotion_detector() function. The output returned shows the label and its confidence 
       anger, disgust, fear, joy, sadness, dominant_emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return " Invalid text! Please try again!."
    # pylint: disable=line-too-long
    return f"'anger' : {anger}, 'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy} and 'sadness' : {sadness}. The dominant emotion is {dominant_emotion}."
    # pylint: enable=line-too-long
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
