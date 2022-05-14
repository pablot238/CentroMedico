from flask import Flask, render_template, make_response, jsonify, request 

doctor = Flask(__name__)

PORT = 3200 #Definimos el puerto
HOST = '0.0.0.0' #Corremos en local host

#Definimos un Json de Doctor
PRUEBA = {
    "Doctor1":{
        "Id: ": "0",
        "Nombre: ": "Jorge",
        "Apellido: ": "Jimenez",
        "Especialidad: ": "Neurología"
    },
    "Doctor2":{
        "Id: ": "1",
        "Nombre: ": "Maria Paula",
        "Apellido: ": "Castañeda",
        "Especialidad: ": "Psicología"
    },
    "Doctor3":{
        "Id: ": "2",
        "Nombre: ": "Carlos",
        "Apellido: ": "Osorio",
        "Especialidad: ": "Pediatría"
    }
}

#METODO GET
@doctor.route("/temp")
def template():
    return render_template("RegistroM.html") #retornar el HTML del FE

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    doctor.run(host=HOST, port=PORT) #Pasamos el local host y el puerto