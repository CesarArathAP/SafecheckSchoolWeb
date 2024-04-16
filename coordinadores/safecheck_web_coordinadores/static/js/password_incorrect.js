function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

// Verificar si hay un error de contraseña en la URL
var error = getParameterByName('error');
if (error === 'password') {
    // Mostrar mensaje de SweetAlert si hay un error de contraseña
    Swal.fire({
        icon: "error",
        title: "Contraseña incorrecta",
        text: "La contraseña ingresada es incorrecta. Por favor, inténtelo de nuevo.",
        footer: '<a href="#">¿Por qué tengo este problema?</a>'
    });
}