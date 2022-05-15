import collections
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

#METODOS GET
@doctor.route("/")
def template():
    return render_template("RegistroM.html") #retornar el HTML del FE

@doctor.route("/qstr")
def query_string():
    if request.args: #Revisar si el request tiene algún argumento
        req=request.args
        res = {}
        for key, value in req.items(): #Regresar el elemento de forma más estética
            res[key] = value
        res = make_response(jsonify(res),200) #Retornar el query
        return res
    
    res = make_response(jsonify({"error": "No hay query String"}),400) #Enviar un mensaje de error
    return res

@doctor.route("/json") #Retornar el objeto completo
def get_json():
    res = make_response(jsonify(PRUEBA), 200)
    return res

@doctor.route("/json/<collection>/<member>") #Llamar algún miembro dentro de las colecciones
def get_data(collection,member):
    if collection in PRUEBA: #Verificar si la coleccion existe
        member = PRUEBA[collection].get(member)
        if member: #Si existe el miembro
            res = make_response(jsonify({"res": member}), 200)
            return res

        res = make_response(jsonify({"error": "Miembro no encontrado"}),400) #Enviar un mensaje de error
        return res
        
    res = make_response(jsonify({"error": "Colección no encontrada"}),400) #Enviar un mensaje de error
    return res


if __name__ == "__main__":
    print("El servidor está corriendo en el puerto %s"%(PORT))
    doctor.run(host=HOST, port=PORT) #Pasamos el local host y el puerto