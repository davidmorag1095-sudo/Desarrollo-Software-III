from flask import Flask, render_template, request

#Crea la aplicacion Flask
app = Flask(__name__)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=
#ruta principal
#Muestra el formulario HTML
#=-==-=-=-=-=-=-=-=-=-==-=-=
@app.route('/')
def inicio():
    #muestra la vista del formulario
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    #obtiene los datos del formulario
    nombre = request.form['nombre']
    correo = request.form['correo']

    #muestra los datos en la consola

    print(f'nombre: {nombre} | correo: {correo}')


    #respuesta del servidor

    return f'''
    <h2>Datos recibidos correctamente</h2>
    <p>Nombre: {nombre}</p>
    <p>Correo: {correo}</p>
    <a href="/"> Volver</a>
    '''

#=--=-=-==-=-=--==-=--=-=-==--==-=-
#Punto de inicio de la aplicacion
#=-=--==-=-=-=-=-=-=-=-=-==--==--=-

if __name__ == '__main__':
    #Inicia el servidor
    app.run(debug=True)

