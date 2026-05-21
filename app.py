from flask import Flask
from flask_cors import CORS
from routes.usuarios import usuarios_bp

# Inicializa o servidor Flask
app = Flask(__name__)

# Permite que o React acesse a API
CORS(app)

# Registra as rotas de usuários
app.register_blueprint(usuarios_bp)

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)