const LOADING = '<div class="spinner-border" role="status" style="width:20px;height:20px"></div>'

$(document).ready(function () {
  localStorage.removeItem('aluno')
  $('#btn-login').click(login)
  $('#input-ra').keyup(validateRA)
})

function validateRA() {
  $(this).removeClass('is-invalid')
  $(this).removeClass('is-valid')
  $(this).html('')
}

function login() {
  const ra = $('#input-ra').val()

  if (ra.length != 7) {
    return $('#input-ra').addClass('is-invalid')
  }

  loading(true)
  $.get(`/alunos/${ra}`)
    .done(function (aluno) {
      $('#input-ra').addClass('is-valid')
      localStorage.setItem('aluno', JSON.stringify(aluno))
      location.href = 'dashboard'
    })
    .fail(function () {
      $('#input-ra').addClass('is-invalid')
      $('.invalid-feedback').html('Aluno não encontrado')
    })
    .always(function () {
      loading(false)
    });
}

function loading(status) {
  $('#btn-login').html(status ? LOADING : 'Entrar')
}