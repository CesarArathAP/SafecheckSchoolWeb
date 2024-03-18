function updateSelectedCarreras() {
    var carrerasSeleccionadas = '';
    var checkboxes = document.querySelectorAll('input[name="carrera[]"]:checked');
    checkboxes.forEach(function(checkbox) {
        carrerasSeleccionadas += checkbox.nextElementSibling.textContent + '\n';
    });
    document.getElementById('carreraSeleccionada').value = carrerasSeleccionadas;
}