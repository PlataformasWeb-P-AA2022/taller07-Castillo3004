from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open("data/datos_clubs.txt", "r")
registro = archivo.readlines()

# se crea un objetos de tipo Club 

for r in registro:
    nombre = r.split(";")[0]
    deporte = r.split(";")[1]
    fundacion = r.split(";")[2].replace("\n","")
    club = Club(nombre=nombre, deporte=deporte, \
        fundacion=fundacion)
    session.add(club)


session.commit()
