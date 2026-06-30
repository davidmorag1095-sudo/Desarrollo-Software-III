const API_URL = "http://127.0.0.1:8000/students/";

const form = document.getElementById("studentForm");
const tableBody = document.getElementById("studentsTable");
const messageBox = document.getElementById("messageBox");
const btnLoad = document.getElementById("btnLoad");
const btnSearch = document.getElementById("btnSearch");
let carnetEditando = null;

// Mostrar mensajes
function showMessage(text, type = "success") {
    messageBox.textContent = text;
    messageBox.classList.remove("hidden");
    messageBox.style.background = type === "success" ? "#5cb85c" : "#d9534f";
    messageBox.style.color = "white";

    setTimeout(() => {
        messageBox.classList.add("hidden");
    }, 3000);
}

// Cargar estudiantes
async function loadStudents() {
    try {
        const res = await fetch(API_URL);

        if (!res.ok) {
            throw new Error("Error al consultar la API");
        }

        const data = await res.json();

        tableBody.innerHTML = "";

        data.forEach(student => {
            const row = `
                <tr>
                    <td>${student.carnet}</td>
                    <td>${student.name}</td>
                    <td>${student.age}</td>
                    <td>
                        <button 
                        class="action-btn edit-btn" 
                        onclick="editStudent('${student.carnet}', '${student.name}', ${student.age})">
                        Editar
                        </button>
                        <button 
                        class="action-btn delete-btn" 
                        onclick="deleteStudent('${student.carnet}')">
                        Eliminar
                        </button>
                    </td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error(error);
        showMessage("No se pudieron cargar los estudiantes", "error");
    }
}

// Agregar o actualizar estudiante
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const carnet = document.getElementById("carnet").value;
    const name = document.getElementById("name").value;
    const age = parseInt(document.getElementById("age").value);

    const studentData = { carnet, name, age };

    // Si existe, actualizar
    let url = API_URL;
    let method = "POST";

    // Si existe carnetEditando, entonces actualiza
    if (carnetEditando === null) {
        url = API_URL;
        method = "POST";
    } else {
        url = API_URL + carnetEditando;
        method = "PUT";
    }

    try {
        const res = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(studentData)
        });

        if (res.ok) {
            if (method === "POST") {
                showMessage("Estudiante agregado correctamente");
                activarModoAgregar();
            } else {
                showMessage("Estudiante actualizado correctamente");
                activarModoAgregar();
            }

            carnetEditando = null;
            form.reset();
            document.getElementById("carnet").disabled = false;
            loadStudents();

        } else {
            const errorData = await res.json();
            console.error(errorData);
            showMessage("Error al guardar o actualizar", "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexión con la API", "error");
    }
});
function activarModoAgregar() {
    carnetEditando = null;
    document.getElementById("carnet").disabled = false;
    form.reset();
}

// Editar estudiante
function editStudent(carnet, name, age) {
    carnetEditando = carnet;

    document.getElementById("carnet").value = carnet;
    document.getElementById("name").value = name;
    document.getElementById("age").value = age;

    // No permitimos cambiar el carnet porque es la llave primaria
    document.getElementById("carnet").disabled = true;

    showMessage("Modo edición activado");
}

async function searchStudent() {

    const carnet =
        document.getElementById("searchCarnet")
            .value
            .trim();

    if (!carnet) {
        showMessage(
            "Ingrese un carnet",
            "error"
        );
        return;
    }

    try {

        const res = await fetch(
            API_URL + carnet
        );

        if (!res.ok) {
            throw new Error(
                "Estudiante no encontrado"
            );
        }

        const student =
            await res.json();

        tableBody.innerHTML = "";

        tableBody.innerHTML = `
            <tr>
                <td>${student.carnet}</td>
                <td>${student.name}</td>
                <td>${student.age}</td>
                <td>
                    <button
                        class="action-btn edit-btn"
                        onclick="editStudent(
                            '${student.carnet}',
                            '${student.name}',
                            ${student.age}
                        )">
                        Editar
                    </button>

                    <button
                        class="action-btn delete-btn"
                        onclick="deleteStudent(
                            '${student.carnet}'
                        )">
                        Eliminar
                    </button>
                </td>
            </tr>
        `;

    } catch (error) {

        showMessage(
            "Estudiante no encontrado",
            "error"
        );

        tableBody.innerHTML = "";
    }
}

// Eliminar estudiante
async function deleteStudent(carnet) {
    try {
        const res = await fetch(API_URL + carnet, {
            method: "DELETE"
        });

        if (res.ok) {
            showMessage("Estudiante eliminado");
            loadStudents();

            if (carnetEditando === carnet) {
                carnetEditando = null;
                form.reset();
                document.getElementById("carnet").disabled = false;
            }

        } else {
            showMessage("Error al eliminar", "error");
        }

    } catch (error) {
        console.error(error);
        showMessage("Error de conexión con la API", "error");
    }
}

btnLoad.addEventListener("click", loadStudents);
btnSearch.addEventListener(
    "click",
    searchStudent
);

// Cargar al inicio
loadStudents();
