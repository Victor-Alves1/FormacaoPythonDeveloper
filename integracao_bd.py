from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, select
from sqlalchemy.ext.indexable import index_property
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite://")

base = declarative_base()

class Clientes(base):
    __tablename__="customers"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    account = relationship("Conta", back_populates="account")

    def __repr__(self):
        return f"Clientes(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(base):
    __tablename__="account"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero_conta = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("customers.id"))
    saldo = Column(DECIMAL)

    customers = relationship("Clientes", back_populates="customers")
    customers = relationship("Clientes", back_populates="customers")


    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero_conta={self.numero_conta}, id_cliente={self.id_cliente}, saldo={self.saldo})"
    
with Session(engine) as session:

    victor = Clientes(
        nome="victor",
        cpf="1111",
        endereco="rua",
        tipo=[Conta(tipo="conta-corrente")],
        agencia=[Conta(agencia="001")],
        numero_conta=123,
        saldo=10.10,
    )

    mario = Clientes(
        nome="mario",
        cpf="2222",
        endereco="avenida",
        tipo=[Conta(tipo="conta-corrente")],
        agencia=[Conta(agencia="001")],
        numero_conta=124,
        saldo=20.20,
    )

    igor = Clientes(
        nome="igor",
        cpf="3333",
        endereco="beco",
        tipo=[Conta(tipo="conta-corrente")],
        agencia=[Conta(agencia="001")],
        numero_conta=125,
        saldo=30.30,
    )
    session.add_all([victor, mario, igor])
    session.commit()

session = Session(engine)

stmt = select(Clientes)

for cliente in session.scalars(stmt):
    print(cliente)