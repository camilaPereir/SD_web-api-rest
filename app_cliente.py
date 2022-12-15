import requests

url = "http://127.0.0.1:8080"

clientes = [{
    "nome": "Amanda",
    "endereco": "Rua 456"
}, {
    "nome": "Carolina",
    "endereco": "Rua asd"
}, {
    "nome": "Daniel",
    "endereco": "Rua dfg"
}, {
    "nome": "Viviane",
    "endereco": "Rua 4d"
}, {
    "nome": "Theo",
    "endereco": "Rua dfgg6"
}, {
    "nome": "Ricardo",
    "endereco": "Rua dfgg"
}, {
    "nome": "Antonio",
    "endereco": "Rua dfggd"
}, {
    "nome": "Giovanna",
    "endereco": "Rua :)"
}]

produtos = [{
    "nome": "Arroz",
    "preco": 10,
    "quantidade": 200
}, {
    "nome": "Feijao",
    "preco": 15,
    "quantidade": 200
}]

vendas =[{
    "cliente_id": "8",
    "preco_total": "20"
}]

for cliente in clientes:
    requests.post(f"{url}/cliente", json=cliente)


for produto in produtos:
  requests.post(f"{url}/produto", json=produto)
  
for venda in vendas:
  requests.post(f"{url}/venda", json=venda)