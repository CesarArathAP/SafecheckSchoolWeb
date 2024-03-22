function eliminarNotificacion(event) {
    const botonCerrar = event.currentTarget;
    const tarjeta = botonCerrar.closest('.card');
    if (tarjeta) {
        tarjeta.remove();
    }
}

document.querySelectorAll('.btn-close').forEach(boton => {
    boton.addEventListener('click', eliminarNotificacion);
});