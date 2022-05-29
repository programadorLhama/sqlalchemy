from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# Configuracoes
engine = create_engine('mysql+pymysql://root:my_pw@localhost:3308/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
    
# SQL

# Insert
data_isert = Filmes(titulo="jfasasufy", genero="Acao", ano=1111)
session.add(data_isert)
session.commit()

# delete
session.query(Filmes).filter(Filmes.titulo=="Dracula").delete()
session.commit()

# update
session.query(Filmes).filter(Filmes.genero == "Drama").update({ "ano": 2000 })
session.commit()

# Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()