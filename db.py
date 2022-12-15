from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Float, NUMERIC, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "meubanco"

engine = create_engine(
    f"sqlite:///./{NOME_BANCO}.sqlite",
    echo=True,
    connect_args={"check_same_thread": False},
)
Base = declarative_base()

# Declaracao das classes


class Cliente(Base):

    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Cliente {self.nome}"

    def info(self):
        return {"id": self.id, "nome": self.nome, "endereco": self.endereco}
      
class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Produto {self.nome}"

    def info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }


class Carrinho(Base):
    __tablename__ = "carrinho"
    id = Column(Integer, primary_key=True)
    venda_id = Column(Integer, ForeignKey("venda.id"))
    produto_id = Column(Integer, ForeignKey("produto.id"))
    qtd = Column(Integer, nullable=False)
    total = Column(NUMERIC(precision=8, scale=2))
  
    def info(self):
        return {
            "id": self.id,
            "venda_id": self.venda_id,
            "produto_id": self.produto_id,
            "qtd": self.qtd,
            "total": self.total
        }


class Venda(Base):

    __tablename__ = "venda"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    preco_total = Column(Float, nullable=False)
    def info(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,  
            "preco_total": self.preco_total,
        }
        
# fim da declaracao

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
