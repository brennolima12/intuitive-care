from sqlalchemy import Integer, Column, Text, Date, DECIMAL
from database import Base
class RelatorioCadop(Base):
    __tablename__ = 'relatorio_cadop'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Registro_ANS = Column(Text)
    CNPJ = Column(Text)
    Razao_Social = Column(Text)
    Nome_Fantasia = Column(Text)
    Modalidade = Column(Text)
    Logradouro = Column(Text)
    Numero = Column(Text)
    Complemento = Column(Text)
    Bairro = Column(Text)
    Cidade = Column(Text)
    UF = Column(Text)
    CEP = Column(Text)
    DDD = Column(Text)
    Telefone = Column(Text)
    Fax = Column(Text)
    Endereco_eletronico = Column(Text)
    Representante = Column(Text)
    Cargo_Representante = Column(Text)
    Regiao_de_Comercializacao = Column(Text)
    Data_Registro_ANS = Column(Date)