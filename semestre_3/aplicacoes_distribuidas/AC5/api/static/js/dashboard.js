const aluno = JSON.parse(localStorage.getItem('aluno'))

$(document).ready(function () {
  if(!aluno){
    return location.replace('/')
  }
console.log(aluno)
  $('.nome').html(aluno.nome)
})