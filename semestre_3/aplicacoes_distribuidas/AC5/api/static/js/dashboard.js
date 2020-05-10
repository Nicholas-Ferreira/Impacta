const aluno = JSON.parse(localStorage.getItem('aluno'))

$(document).ready(function () {
  if (!aluno) {
    return location.replace('/')
  }
  $('.nome').html(aluno.nome)
})