"""
Punto de entrada para ejecutar
la versión web del sistema

Flujo de trabajo:
HTML -> Flask -> Service -> repository -> MYSQL

"""
import flask
from flask import Flask, render_template, request, flash, redirect, url_for

from Desk_mysql_clientes.Desk_mysql_clientes.service.cliente_service import ClienteService

app = Flask(__name__)
app.secret_key = "clave_didactica_cliente"

cliente_service = ClienteService()

@app.route("/")
def index():
    clientes = cliente_service.consultar_clientes()
    return render_template("index.html", clientes=clientes)

@app.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        exito, mensaje = cliente_service.registrar_cliente(cedula, nombre, correo, telefono, direccion)
        flask.flash(mensaje)

        if exito:
            return redirect(url_for("index"))
        return render_template("formulario_cliente.html")
    return None


@app.route("/clientes/editar/<int:id_cliente>", methods=["GET", "POST"])
def editar_cliente(id_cliente):
    cliente = cliente_service.buscar_cliente_por_id(id_cliente)
    if cliente is None:
        flash("Error: no existe un cliente con ese ID")
        return redirect(url_for("index"))
    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        exito, mensaje = cliente_service.actualizar_cliente(id_cliente,cedula, nombre, correo, telefono, direccion)
        flask.flash(mensaje)
        if exito:
            return redirect(url_for("index"))
    return render_template("editar_cliente.html", cliente=cliente)

@app.route("/clientes/eliminar/<int:id_cliente>", methods=["GET", "POST"])
def eliminar_cliente(id_cliente):
    exito, mensaje = cliente_service.eliminar_cliente(id_cliente)
    flash(mensaje)
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug=True)