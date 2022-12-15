from db import session, Produto, Venda

def diminuir_total(venda_id, preco_total):
  venda = session.query(Venda).filter(Venda.id == venda_id).one()
  venda.preco_total -= preco_total
  session.commit()

def somatorio_do_preco_total(produto_id, quantidade):
  produto = session.query(Produto).filter(Produto.id == produto_id).one()
  return produto.preco * quantidade

def diminuir_quantidade(produto_id, quantidade):
  produto = session.query(Produto).filter(Produto.id == produto_id).one()
  produto.quantidade = produto.quantidade - quantidade

def aumentar_quantidade(produto_id, quantidade):
  produto = session.query(Produto).filter(Produto.id == produto_id).one()
  produto.quantidade += quantidade
  session.commit()

def aumentar_total(venda_id, preco_total):
  venda = session.query(Venda).filter(Venda.id == venda_id).one()
  venda.preco_total += preco_total
  session.commit()


