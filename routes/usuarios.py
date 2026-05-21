from flask import Blueprint, request, jsonify
import json
import os

# Cria o Blueprint de usuários
usuarios_bp = Blueprint("usuarios", __name__)

# Caminho do arquivo de persistência
ARQUIVO_USUARIOS = "usuarios.json"


# ─── Funções auxiliares ───────────────────────────────────────────

def ler_usuarios():
    """Lê o arquivo JSON e retorna a lista de usuários"""
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_usuarios(usuarios):
    """Salva a lista de usuários no arquivo JSON"""
    try:
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return False


# ─── CREATE — Cadastro ────────────────────────────────────────────

@usuarios_bp.route("/cadastro", methods=["POST"])
def cadastro():
    """Cria uma nova conta de usuário"""
    try:
        dados = request.get_json()

        # Validação: campos obrigatórios
        for campo in ["nome", "email", "senha"]:
            if not dados.get(campo):
                return jsonify({"erro": f"O campo '{campo}' é obrigatório"}), 400

        # Validação: email precisa ter @
        if "@" not in dados["email"]:
            return jsonify({"erro": "E-mail inválido"}), 400

        # Validação: senha precisa ter pelo menos 6 caracteres
        if len(dados["senha"]) < 6:
            return jsonify({"erro": "A senha precisa ter pelo menos 6 caracteres"}), 400

        usuarios = ler_usuarios()

        # Validação: email já cadastrado
        for usuario in usuarios:
            if usuario["email"] == dados["email"]:
                return jsonify({"erro": "E-mail já cadastrado"}), 409

        # Cria o novo usuário
        novo_usuario = {
            "nome": dados["nome"],
            "email": dados["email"],
            "senha": dados["senha"]
        }

        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)

        return jsonify({"mensagem": "Conta criada com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


# ─── READ — Login ─────────────────────────────────────────────────

@usuarios_bp.route("/login", methods=["POST"])
def login():
    """Verifica email e senha e retorna os dados do usuário"""
    try:
        dados = request.get_json()

        # Validação: campos obrigatórios
        for campo in ["email", "senha"]:
            if not dados.get(campo):
                return jsonify({"erro": f"O campo '{campo}' é obrigatório"}), 400

        usuarios = ler_usuarios()

        # Busca o usuário pelo email e senha
        for usuario in usuarios:
            if usuario["email"] == dados["email"] and usuario["senha"] == dados["senha"]:
                return jsonify({
                    "mensagem": "Login realizado com sucesso!",
                    "nome": usuario["nome"],
                    "email": usuario["email"]
                }), 200

        return jsonify({"erro": "E-mail ou senha incorretos"}), 401

    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


# ─── UPDATE — Atualizar perfil ────────────────────────────────────

@usuarios_bp.route("/usuario/<email>", methods=["PUT"])
def atualizar_usuario(email):
    """Atualiza o nome ou senha de um usuário"""
    try:
        dados = request.get_json()
        usuarios = ler_usuarios()

        for usuario in usuarios:
            if usuario["email"] == email:
                # Atualiza só os campos que vieram na requisição
                if dados.get("nome"):
                    usuario["nome"] = dados["nome"]
                if dados.get("senha"):
                    if len(dados["senha"]) < 6:
                        return jsonify({"erro": "A senha precisa ter pelo menos 6 caracteres"}), 400
                    usuario["senha"] = dados["senha"]

                salvar_usuarios(usuarios)
                return jsonify({"mensagem": "Dados atualizados com sucesso!"}), 200

        return jsonify({"erro": "Usuário não encontrado"}), 404

    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500


# ─── DELETE — Deletar conta ───────────────────────────────────────

@usuarios_bp.route("/usuario/<email>", methods=["DELETE"])
def deletar_usuario(email):
    """Deleta a conta de um usuário pelo email"""
    try:
        usuarios = ler_usuarios()
        usuarios_filtrados = [u for u in usuarios if u["email"] != email]

        if len(usuarios_filtrados) == len(usuarios):
            return jsonify({"erro": "Usuário não encontrado"}), 404

        salvar_usuarios(usuarios_filtrados)
        return jsonify({"mensagem": "Conta deletada com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500