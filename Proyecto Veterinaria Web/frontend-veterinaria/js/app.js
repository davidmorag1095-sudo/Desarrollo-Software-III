const API_URL = "http://127.0.0.1:8000";

const loginSection = document.getElementById("loginSection");
const appSection = document.getElementById("appSection");
const messageBox = document.getElementById("messageBox");

let duenoEditando = null;
let mascotaEditando = null;
let citaEditando = null;

function showMessage(text, type = "success") {
    messageBox.textContent = text;
    messageBox.classList.remove("hidden");
    messageBox.style.background = type === "success" ? "#5cb85c" : "#d9534f";
    messageBox.style.color = "white";

    setTimeout(() => messageBox.classList.add("hidden"), 3000);
}

async function enviarSolicitud(url, options = {}) {
    const res = await fetch(url, options);
    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Ocurrió un error");
    }
    return res.json();
}

document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const login = {
        usuario: document.getElementById("usuario").value,
        clave: document.getElementById("clave").value
    };

    try {
        await enviarSolicitud(`${API_URL}/login/`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(login)
        });

        loginSection.classList.add("hidden");
        appSection.classList.remove("hidden");
        loadDuenos();
        loadMascotas();
        loadCitas();
        showMessage("Bienvenido a la clínica veterinaria");
    } catch (error) {
        showMessage(error.message, "error");
    }
});

document.getElementById("btnSalir").addEventListener("click", () => {
    appSection.classList.add("hidden");
    loginSection.classList.remove("hidden");
    document.getElementById("loginForm").reset();
});

function mostrarModulo(id) {
    document.querySelectorAll(".module-section").forEach(section => {
        section.classList.add("hidden");
    });
    document.getElementById(id).classList.remove("hidden");
}

// -------------------- DUEÑOS --------------------

async function loadDuenos(nombre = "") {
    try {
        const url = nombre
            ? `${API_URL}/duenos/?nombre=${encodeURIComponent(nombre)}`
            : `${API_URL}/duenos/`;
        const datos = await enviarSolicitud(url);
        mostrarDuenos(datos);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

function mostrarDuenos(datos) {
    const table = document.getElementById("duenosTable");
    table.innerHTML = "";

    datos.forEach(dueno => {
        table.innerHTML += `
            <tr>
                <td>${dueno.id}</td>
                <td>${dueno.nombre}</td>
                <td>${dueno.telefono}</td>
                <td>${dueno.email}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editDueno(${dueno.id}, '${dueno.nombre}', '${dueno.telefono}', '${dueno.email}')">
                        Editar
                    </button>
                    <button class="action-btn delete-btn" onclick="deleteDueno(${dueno.id})">
                        Eliminar
                    </button>
                </td>
            </tr>`;
    });
}

document.getElementById("duenoForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const datos = {
        nombre: document.getElementById("nombreDueno").value,
        telefono: document.getElementById("telefonoDueno").value,
        email: document.getElementById("emailDueno").value
    };

    const url = duenoEditando === null
        ? `${API_URL}/duenos/`
        : `${API_URL}/duenos/${duenoEditando}`;
    const method = duenoEditando === null ? "POST" : "PUT";

    try {
        await enviarSolicitud(url, {
            method,
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(datos)
        });
        showMessage(method === "POST" ? "Dueño registrado" : "Dueño actualizado");
        activarAgregarDueno();
        loadDuenos();
    } catch (error) {
        showMessage(error.message, "error");
    }
});

function editDueno(id, nombre, telefono, email) {
    duenoEditando = id;
    document.getElementById("nombreDueno").value = nombre;
    document.getElementById("telefonoDueno").value = telefono;
    document.getElementById("emailDueno").value = email;
    showMessage("Modo edición activado");
}

function activarAgregarDueno() {
    duenoEditando = null;
    document.getElementById("duenoForm").reset();
}

async function deleteDueno(id) {
    try {
        await enviarSolicitud(`${API_URL}/duenos/${id}`, {method: "DELETE"});
        showMessage("Dueño eliminado");
        loadDuenos();
    } catch (error) {
        showMessage(error.message, "error");
    }
}

document.getElementById("btnBuscarDueno").addEventListener("click", () => {
    loadDuenos(document.getElementById("buscarDueno").value.trim());
});
document.getElementById("btnListarDuenos").addEventListener("click", () => loadDuenos());

// -------------------- MASCOTAS --------------------

async function loadMascotas() {
    try {
        mostrarMascotas(await enviarSolicitud(`${API_URL}/mascotas/`));
    } catch (error) {
        showMessage(error.message, "error");
    }
}

function mostrarMascotas(datos) {
    const table = document.getElementById("mascotasTable");
    table.innerHTML = "";

    datos.forEach(mascota => {
        table.innerHTML += `
            <tr>
                <td>${mascota.codigo}</td>
                <td>${mascota.nombre}</td>
                <td>${mascota.especie}</td>
                <td>${mascota.edad}</td>
                <td>${mascota.dueno_id}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editMascota('${mascota.codigo}', '${mascota.nombre}', '${mascota.especie}', ${mascota.edad}, ${mascota.dueno_id})">
                        Editar
                    </button>
                    <button class="action-btn delete-btn" onclick="deleteMascota('${mascota.codigo}')">
                        Eliminar
                    </button>
                </td>
            </tr>`;
    });
}

document.getElementById("mascotaForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const datos = {
        codigo: document.getElementById("codigoMascota").value,
        nombre: document.getElementById("nombreMascota").value,
        especie: document.getElementById("especieMascota").value,
        edad: parseInt(document.getElementById("edadMascota").value),
        dueno_id: parseInt(document.getElementById("duenoMascota").value)
    };

    const url = mascotaEditando === null
        ? `${API_URL}/mascotas/`
        : `${API_URL}/mascotas/${mascotaEditando}`;
    const method = mascotaEditando === null ? "POST" : "PUT";

    try {
        await enviarSolicitud(url, {
            method,
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(datos)
        });
        showMessage(method === "POST" ? "Mascota registrada" : "Mascota actualizada");
        activarAgregarMascota();
        loadMascotas();
    } catch (error) {
        showMessage(error.message, "error");
    }
});

function editMascota(codigo, nombre, especie, edad, duenoId) {
    mascotaEditando = codigo;
    document.getElementById("codigoMascota").value = codigo;
    document.getElementById("codigoMascota").disabled = true;
    document.getElementById("nombreMascota").value = nombre;
    document.getElementById("especieMascota").value = especie;
    document.getElementById("edadMascota").value = edad;
    document.getElementById("duenoMascota").value = duenoId;
    showMessage("Modo edición activado");
}

function activarAgregarMascota() {
    mascotaEditando = null;
    document.getElementById("mascotaForm").reset();
    document.getElementById("codigoMascota").disabled = false;
}

async function buscarMascota() {
    const codigo = document.getElementById("buscarMascota").value.trim();
    if (!codigo) {
        showMessage("Ingrese un código", "error");
        return;
    }

    try {
        const mascota = await enviarSolicitud(`${API_URL}/mascotas/${codigo}`);
        mostrarMascotas([mascota]);
    } catch (error) {
        showMessage(error.message, "error");
        mostrarMascotas([]);
    }
}

async function deleteMascota(codigo) {
    try {
        await enviarSolicitud(`${API_URL}/mascotas/${codigo}`, {method: "DELETE"});
        showMessage("Mascota eliminada");
        loadMascotas();
    } catch (error) {
        showMessage(error.message, "error");
    }
}

document.getElementById("btnBuscarMascota").addEventListener("click", buscarMascota);
document.getElementById("btnListarMascotas").addEventListener("click", loadMascotas);

// -------------------- CITAS --------------------

async function loadCitas() {
    try {
        mostrarCitas(await enviarSolicitud(`${API_URL}/citas/`));
    } catch (error) {
        showMessage(error.message, "error");
    }
}

function mostrarCitas(datos) {
    const table = document.getElementById("citasTable");
    table.innerHTML = "";

    datos.forEach(cita => {
        table.innerHTML += `
            <tr>
                <td>${cita.id}</td>
                <td>${cita.codigo_mascota}</td>
                <td>${cita.fecha}</td>
                <td>${cita.hora}</td>
                <td>${cita.motivo}</td>
                <td>${cita.estado}</td>
                <td>
                    <button class="action-btn edit-btn"
                        onclick="editCita(${cita.id}, '${cita.codigo_mascota}', '${cita.fecha}', '${cita.hora}', '${cita.motivo}', '${cita.estado}')">
                        Editar
                    </button>
                    <button class="action-btn delete-btn" onclick="deleteCita(${cita.id})">
                        Eliminar
                    </button>
                </td>
            </tr>`;
    });
}

document.getElementById("citaForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const datos = {
        codigo_mascota: document.getElementById("mascotaCita").value,
        fecha: document.getElementById("fechaCita").value,
        hora: document.getElementById("horaCita").value,
        motivo: document.getElementById("motivoCita").value,
        estado: document.getElementById("estadoCita").value
    };

    const url = citaEditando === null
        ? `${API_URL}/citas/`
        : `${API_URL}/citas/${citaEditando}`;
    const method = citaEditando === null ? "POST" : "PUT";

    try {
        await enviarSolicitud(url, {
            method,
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(datos)
        });
        showMessage(method === "POST" ? "Cita registrada" : "Cita actualizada");
        citaEditando = null;
        document.getElementById("citaForm").reset();
        loadCitas();
    } catch (error) {
        showMessage(error.message, "error");
    }
});

function editCita(id, mascota, fecha, hora, motivo, estado) {
    citaEditando = id;
    document.getElementById("mascotaCita").value = mascota;
    document.getElementById("fechaCita").value = fecha;
    document.getElementById("horaCita").value = hora;
    document.getElementById("motivoCita").value = motivo;
    document.getElementById("estadoCita").value = estado;
    showMessage("Modo edición activado");
}

async function deleteCita(id) {
    try {
        await enviarSolicitud(`${API_URL}/citas/${id}`, {method: "DELETE"});
        showMessage("Cita eliminada");
        loadCitas();
    } catch (error) {
        showMessage(error.message, "error");
    }
}

document.getElementById("btnListarCitas").addEventListener("click", loadCitas);

// -------------------- REPORTES --------------------

async function loadReportes() {
    try {
        const especies = await enviarSolicitud(`${API_URL}/reportes/mascotas-por-especie`);
        const estados = await enviarSolicitud(`${API_URL}/reportes/citas-por-estado`);

        document.getElementById("reporteEspecies").innerHTML = especies
            .map(dato => `<li>${dato.especie}: ${dato.cantidad}</li>`).join("");
        document.getElementById("reporteEstados").innerHTML = estados
            .map(dato => `<li>${dato.estado}: ${dato.cantidad}</li>`).join("");
    } catch (error) {
        showMessage(error.message, "error");
    }
}

document.getElementById("btnReportes").addEventListener("click", loadReportes);

