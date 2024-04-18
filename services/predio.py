from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

predios=Blueprint('Predio',__name__)

@predios.route('/predios/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@predios.route('/predios/v1/listar',methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()    
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los contactos sin inconvenientes"
    return jsonify(result),200

@predios.route('/predios/v1/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    predios=Predio(id_tipo_predio,descripcion,ruc, telefono, correo, direccion, idubigeo)
    db.session.add(predios)
    db.session.commit()
    result["data"]=predios
    result["status_code"]=201
    result["msg"]="Se agrego el contacto"
    return jsonify(result),201

@predios.route('/predios/v1/update',methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    contacto=Predio.query.get(id_predio)
    if not predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    predios.id_tipo_predio=id_tipo_predio
    predios.descripcion=descripcion
    predios.ruc=ruc
    predios.telefono=telefono    
    predios.correo=correo    
    predios.direccion=direccion  
    predios.idubigeo=idubigeo 
    db.session.commit()
    
    result["data"]=contacto
    result["status_code"]=202
    result["msg"]="Se modificó el contacto"
    return jsonify(result),202

@predios.route('/predios/v1/delete',methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')    
    if not id_predio:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    
    predios=Predio.query.get(id_predio)
    if not predios:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(predios)
    db.session.commit()
    
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se eliminó el contacto"
    return jsonify(result),200