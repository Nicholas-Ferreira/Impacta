$(document).ready(function () {
  $('#btn-login').click(login)
  $('#input-ra').keyup(validateRA)
})

function validateRA() {
  $(this).removeClass('is-invalid')
}

function login() {
  const ra = $('#input-ra').val()

  if (ra.length != 7) {
    return $('#input-ra').addClass('is-invalid')
  }

  $.post('/login', { ra })
}