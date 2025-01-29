from flask import Flask, request, jsonify
import rasa
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

# Cargar el modelo de Rasa
interpreter = RasaNLUInterpreter('models/nlu-2025-01-27-18-17-40.tar.gz')
agent = Agent.load('models/dialogue', interpreter=interpreter)

@app.route('/chat', methods=['POST'])
def chat():
    # Obtener el mensaje del usuario desde la solicitud JSON
    user_message = request.json.get('message')
    
    # Procesar el mensaje del usuario
    responses = agent.handle_text(user_message)
    
    # Retornar la respuesta del chatbot
    return jsonify({'response': responses[0]['text']})

if __name__ == '__main__':
    app.run(debug=True)
