/**
 * Función para agregar un género
 */
function agregarGenero() {
    const genero = {
        nombre: document.getElementById('txtGenero').value
    };
    
    fetch("/genero/", {
        method: "POST",
        body: JSON.stringify(genero),
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.estado) {
            location.href = "/generos/";
        } else {
            swal.fire("Agregar Género", resultado.mensaje, "warning");
        }
    })
    .catch(error => {
        console.error(error);
    });
}

/**
 * Función para agregar una película
 */
function agregarPelicula() {
    const pelicula = {
        codigo: document.getElementById('txtCodigo').value,
        titulo: document.getElementById('txtTitulo').value,
        protagonista: document.getElementById('txtProtagonista').value,
        duracion: document.getElementById('txtDuracion').value,
        resumen: document.getElementById('txtResumen').value,
        genero: {
            id: document.getElementById('cbGenero').value
        },
        foto: ''
    };
    
    fetch("/pelicula/", {
        method: "POST",
        body: JSON.stringify(pelicula),
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.estado) {
            location.href = "/peliculas/";
        } else {
            swal.fire("Agregar Película", resultado.mensaje, "warning");
        }
    })
    .catch(error => {
        console.error(error);
    });
}

// Funciones para editar y eliminar (similar a las anteriores)