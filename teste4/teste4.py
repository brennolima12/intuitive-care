from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.middleware.cors import CORSMiddleware
from models import RelatorioCadop
from database import SessionLocal
from sqlalchemy.orm import Session
from datetime import date

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # ou ["*"] para testes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class RelatorioCadopBase(BaseModel):
    Registro_ANS: str
    CNPJ: str
    Razao_Social: str
    Nome_Fantasia: str
    Modalidade: str
    Logradouro: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    UF: str
    CEP: str
    DDD: str
    Telefone: str
    Fax: str
    Endereco_eletronico: str
    Representante: str
    Cargo_Representante: str
    Regiao_de_Comercializacao: str
    Data_Registro_ANS: date
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/cadop", response_model=List[RelatorioCadopBase])
def listar_cadop(db: db_dependency):
    return db.query(RelatorioCadop).all()

class RelatorioCadopSchema(RelatorioCadopBase):
    id: int

@app.get("/cadop/{razao_social}", response_model=List[RelatorioCadopSchema])
def buscar_nome(razao_social: str, db: db_dependency):
    termo_like = f"%{razao_social}%"
    resultados = db.query(RelatorioCadop).filter(
        RelatorioCadop.Razao_Social.ilike(termo_like)
    ).all()
    return resultados




