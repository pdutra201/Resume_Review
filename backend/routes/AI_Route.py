from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from config import Config
from flask_restful import Resource
from flask import request, jsonify, session

client = OpenAI(api_key=Config.OPENAI_API_KEY)




class AI_Route(Resource):
    # def post(self):
    #     data = request.get_json()
    #     print(data)
    #     return jsonify({"message": "Hello, world!"})
        
    def get(self):
        response = client.responses.create(
        model = "gpt-4.1",
        input = "Write a one-sentence bedtime story for a 3-year-old child",
    )
        output_text = response.output[0].content[0].text

        return jsonify({"output": output_text})

