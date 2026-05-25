import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url,json=myobj, headers=headers)
    response_json = json.loads(response.text)
    anger = response_json['emotionPredictions'][0]['emotion']['anger']
    disgust = response_json['emotionPredictions'][0]['emotion']['disgust']
    fear = response_json['emotionPredictions'][0]['emotion']['fear']
    joy = response_json['emotionPredictions'][0]['emotion']['joy']
    sadness = response_json['emotionPredictions'][0]['emotion']['sadness']
    emotions = [anger, disgust, fear, joy, sadness]
    emotions_names = ["Anger", "Disgust", "Fear", "Joy", "Sadness"]
    dominant_emotion = emotions[0]
    index = 0
    for i, emotion in enumerate(emotions):
        if(emotion > dominant_emotion):
            dominant_emotion = emotion
            index = i
    response_formatted = {'anger': anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness":sadness, "dominant_emotion": emotions_names[index] }   
    return response_formatted