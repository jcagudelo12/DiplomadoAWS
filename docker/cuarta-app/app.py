from typing import Text
from flask import Flask, request, jsonify, send_file
import boto3
import os

app = Flask(__name__)


@app.route('/voice', methods=['POST'])
def vioce():
  try:
    data = request.json
    text = data.get('text')
    voice = "Mia"
    output_format = "mp3"

    if not text:
      return jsonify({'Error': 'Text is required'}), 400

    polly = boto3.client('polly', region_name='us-east-1')

    response = polly.synthesize_speech(Text=text,
                                       OutputFormat=output_format,
                                       VoiceId=voice)

    audio_file = "output.mp3"
    with open(audio_file, 'wb') as file:
      file.write(response['AudioStream'].read())

    return send_file(audio_file, mimetype='audio/mpeg')
  except Exception as e:
    return jsonify({'Error': str(e)}), 500


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
