// En static/js/validaciones.js
document.querySelector('form').addEventListener('submit', function(e) {
  let campos = this.querySelectorAll('[required]');
  let valido = true;
  
  campos.forEach(campo => {
      if (!campo.value) {
          campo.classList.add('is-invalid');
          valido = false;
      } else {
          campo.classList.remove('is-invalid');
      }
  });
  
  if (!valido) {
      e.preventDefault();
      Swal.fire('Error', 'Todos los campos son obligatorios', 'error');
  }
});