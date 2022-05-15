from pydoc import doc
from flask import Flask, render_template, make_response, jsonify, request 

doctor = Flask(__name__)

PORT = 3200 #Definimos el puerto
HOST = '0.0.0.0' #Corremos en local host

#Definimos un Json de Doctor
PRUEBA = {
    "Doctor1":{
        "Id": "0",
        "Nombre": "Jorge",
        "Apellido": "Jimenez",
        "Especialidad": "Neurología"
    },
    "Doctor2":{
        "Id": "1",
        "Nombre": "Maria Paula",
        "Apellido": "Castañeda",
        "Especialidad": "Psicología"
    },
    "Doctor3":{
        "Id": "2",
        "Nombre": "Carlos",
        "Apellido": "Osorio",
        "Especialidad": "Pediatría"
    }
}

#METODO GET
@doctor.route("/")
def home():
    return "<h1 style='color:blue'> Bienvenido al home!!</h1>"

@doctor.route("/temp")
def template():
    return render_template("RegistroM.html") #retornar el HTML del FE

@doctor.route("/qstr")
def query_string():
    if request.args: #Revisar si el request tiene algún argumento
        req=request.args
        res = {}
        for key, value in req.items(): #Regresar el elemento de forma más estética
            res[key] = value
        res = make_response(jsonify(res),200)
        return res
    
    res = make_response(jsonify({"error": "No hay query String"}),400) #Enviar un mensaje de error
    return res

@doctor.route("/json")
def get_json():
    res = make_response(jsonify(PRUEBA), 200)
    return res

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    doctor.run(host=HOST, port=PORT) #Pasamos el local host y el puerto