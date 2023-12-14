function setOpen(open) {
    var modal = document.getElementById('modal');
    if (open) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Evitar que el fondo sea desplazable cuando el modal está abierto
    } else {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto'; // Restaurar el desplazamiento del fondo cuando se cierra el modal
    }
}
