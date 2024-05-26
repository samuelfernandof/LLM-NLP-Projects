# Lab 2 - Backend

# Imports
from flask import Flask, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# App
app = Flask(__name__)

# Carrega o tokenizador
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Carrega o modelo
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Método post usado para comunicação com a app
@app.route('/predict', methods=['POST'])
def predict():

    # Recebe os dados de entrada (prompt)
    data = request.get_json()

    # Extrai o texto dos dados e aplica o tokenizador
    inputs = tokenizer.encode(data['text'], return_tensors = 'pt')

    # Gera o texto a partir da entrada
    outputs = model.generate(inputs, max_length = 500, num_return_sequences = 1)

    # Faz o decode do texto gerado
    text = tokenizer.decode(outputs[0], skip_special_tokens = True)

    return {'text': text}

# Bloco principal da app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
