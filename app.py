from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

# Carga del modelo y el tokenizador
model_name = "distilgpt2"  # Modelo gratuito y ligero
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Configuración de Flask
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({"error": "No se recibió ningún mensaje"}), 400

    # Generación de respuesta con parámetros ajustados
    inputs = tokenizer.encode(user_input, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        temperature=0.7,  # Controla la aleatoriedad (valores más bajos = respuestas más predecibles)
        top_p=0.9,  # Mantiene solo las palabras más probables
        repetition_penalty=1.2,  # Evita repeticiones
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"response": response})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
