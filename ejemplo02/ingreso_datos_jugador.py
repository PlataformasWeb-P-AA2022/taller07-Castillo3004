from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Jugador, Club

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo2 = open("data/datos_jugadores.txt", "r")
registro2 = archivo2.readlines()
# se crea un objetos de tipo Club 

for r in registro2:
    club = session.query(Club).filter_by(nombre = r.split(";")[0]).one()
    posicion = r.split(";")[1]
    dorsal = r.split(";")[2]
    nombre = r.split(";")[3].replace("\n","")
    jugador = Jugador(club = club, posicion = posicion, dorsal = dorsal, \
       nombre = nombre)      
    session.add(jugador)  


session.commit()
