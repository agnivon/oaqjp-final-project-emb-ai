import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_p = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=json_p, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        emotions = data["emotionPredictions"][0]['emotion']
        emotions_reversed = dict(zip(emotions.values(), emotions.keys()))
        dominant_emotion = max(emotions_reversed.keys())
        return emotions | {'dominant_emotion': emotions_reversed[dominant_emotion]}
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        