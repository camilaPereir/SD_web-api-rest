from flask import Flask, jsonify, request
from db import session, Cliente
from db import Cliente, Produto, Venda, Carrinho
from carrinho import somatorio_do_preco_total, diminuir_quantidade,diminuir_total,aumentar_total,aumentar_quantidade

app = Flask(__name__)
#Feito por Camila Pereira, Alison Mozer, Raphael Macedo Bernardino

@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201


@app.route("/cliente", methods=["GET", "POST"])
def clientes():
    if request.method == "GET":
        return jsonify(
            [cliente.info() for cliente in session.query(Cliente).all()]), 200
    elif request.method == "POST":
        cliente = request.get_json()
        session.add(Cliente(nome=cliente["nome"],
                            endereco=cliente["endereco"]))
        session.commit()
        return jsonify((cliente), 201)


@app.route('/cliente/<int:cliente_id>',
           methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cliente(cliente_id):
    if request.method == 'GET':
        cliente = session.query(Cliente).filter(Cliente.id == cliente_id).one()
        return jsonify(cliente.info()), 200

    elif request.method == 'PUT':
        cliente = request.get_json()
        query = session.query(Cliente).filter(Cliente.id == cliente_id)
        query.update({
            'nome': cliente['nome'],
            'endereco': cliente['endereco']
        })
        cliente = query.one().info()
        session.commit()
        return jsonify(cliente), 200

    elif request.method == 'PATCH':
        cliente = request.get_json()
        query = session.query(Cliente).filter(Cliente.id == cliente_id)
        query.update(cliente)
        cliente = query.one().info()
        session.commit()
        return jsonify(cliente), 200

    elif request.method == 'DELETE':
        query = session.query(Cliente).filter(Cliente.id == cliente_id)
        cliente = query.one().info()
        query.delete()
        session.commit()
        return jsonify(cliente), 200


# PRODUTO


@app.route("/produto", methods=["GET", "POST"])
def produtos():
    if request.method == "GET":
        return jsonify(
            [produto.info() for produto in session.query(Produto).all()]), 200
    elif request.method == "POST":
        produto = request.get_json()
        session.add(
            Produto(nome=produto["nome"],
                    preco=produto["preco"],
                    quantidade=produto["quantidade"]))
        session.commit()
        return jsonify((produto), 201)


@app.route('/produto/<int:produto_id>',
           methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def produto(produto_id):
    if request.method == 'GET':
        produto = session.query(Produto).filter(Produto.id == produto_id).one()
        return jsonify(produto.info()), 200

    elif request.method == 'PUT':
        produto = request.get_json()
        query = session.query(Produto).filter(Produto.id == produto_id)
        query.update({
            "nome": produto["nome"],
            "preco": produto["endereco"],
            "quantidade": produto["quantidade"]
        })
        produto = query.one().info()
        session.commit()
        return jsonify(produto), 200

    elif request.method == 'PATCH':
        produto = request.get_json()
        query = session.query(Produto).filter(Produto.id == produto_id)
        query.update(produto)
        produto = query.one().info()
        session.commit()
        return jsonify(produto), 200

    elif request.method == 'DELETE':
        query = session.query(Produto).filter(Produto.id == produto_id)
        produto = query.one().info()
        query.delete()
        session.commit()
        return jsonify(produto), 200


# VENDA


@app.route("/venda", methods=["GET", "POST"])
def vendas():
    if request.method == "GET":
        return jsonify([venda.info()
                        for venda in session.query(Venda).all()]), 200
    elif request.method == "POST":
        venda = request.get_json()
        session.add(
            Venda(cliente_id=venda["cliente_id"],
                  preco_total=venda["preco_total"]))
        session.commit()
        return jsonify((venda), 201)


@app.route('/venda/<int:venda_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def venda(venda_id):
    if request.method == 'GET':
        venda = session.query(Venda).filter(Venda.id == venda_id).one()
        return jsonify(venda.info()), 200
    
    elif request.method == 'PUT':
        venda = request.get_json()
        query = session.query(Venda).filter(Venda.id == venda_id)
        query.update({
            "cliente_id": venda["cliente_id"],
            "preco_total": venda["preco_total"]
        })
        venda = query.one().info()
        session.commit()
        return jsonify(venda), 200

    elif request.method == 'PATCH':
        venda = request.get_json()
        query = session.query(Venda).filter(Venda.id == venda_id)
        query.update(venda)
        venda = query.one().info()
        session.commit()
        return jsonify(venda), 200

    elif request.method == 'DELETE':
        query = session.query(Venda).filter(Venda.id == venda_id)
        venda = query.one().info()
        query.delete()
        session.commit()
        return jsonify(venda), 200

# CARRINHO

@app.route("/carrinho", methods=["GET", "POST"])
def carrinhos():
    if request.method == "GET":
      return jsonify([carrinho.info()
      for carrinho in session.query(Carrinho).all()]), 200
    elif request.method == "POST":
      carrinho = request.get_json()
      #decrease_stock(shopping_cart['product_id'], shopping_cart['quantity'])
      diminuir_quantidade(int(carrinho["produto_id"]), int(carrinho["qtd"]))
      total = somatorio_do_preco_total(carrinho["produto_id"], float(carrinho["qtd"]))
      aumentar_total(carrinho["venda_id"],total)
      session.add(Carrinho(
        venda_id = carrinho["venda_id"],
        produto_id = carrinho["produto_id"],
        qtd = carrinho["qtd"],
        total = total
      ))
      session.commit()
      return jsonify(carrinho), 201


@app.route('/carrinho/<int:carrinho_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def carrinho(carrinho_id):
    if request.method == 'GET':
        carrinho = session.query(Carrinho).filter(Carrinho.id == carrinho_id).one()
        return jsonify(carrinho.info()), 200

    elif request.method == 'PUT':
        carrinho = request.get_json()
        query = session.query(Carrinho).filter(Carrinho.id == carrinho_id)
        query.update({
            "venda_id": carrinho["venda_id"],
            "produto_id": carrinho["produto_id"],
            "qtd": carrinho["qtd"]
        })
        carrinho = query.one().info()
        session.commit()
        return jsonify(carrinho), 200

    elif request.method == 'PATCH':
        carrinho = request.get_json()
        query = session.query(Carrinho).filter(Carrinho.id == carrinho_id)
        query.update(carrinho)
        carrinho = query.one().info()
        session.commit()
        return jsonify(carrinho), 200

    elif request.method == 'DELETE':
        query = session.query(Carrinho).filter(Carrinho.id == carrinho_id)
        carrinho = query.one().info()
        aumentar_quantidade(carrinho["produto_id"],carrinho["qtd"])
        diminuir_total(carrinho["venda_id"],float(carrinho["total"]))
        query.delete()
        session.commit()
        return jsonify(carrinho), 200
      
app.run(host="0.0.0.0", port=8080)
