//Obtiene el formulario por id

const formulario = document.getElementById("Formulario");

//Evento submit
//Se ejecuta cuando el usuario presiona enviar

formulario.addEventListener("sumit", function(event)){
    //Muestra mensaje en la consola
    consola.log("Formulario")

    //Obtiene los valores de los campos
    const nombre = document.getElementById("nombre").value;
    const correo = document.getElementById("correo").value;

    //Validación basica
    if (nombre === ""  || correo === ""){
        alert("Todos los campos son obligatorios");
        //Cancela el envio
        event.preventDefault();
    }
}
