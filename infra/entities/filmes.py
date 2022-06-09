from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", backref="atores", lazy="subquery")

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
