$(document).ready(function () {
  $('.btn-grupo').click(onAtaque)
  $('.btn-defender').click(onDefender)
})

function onAtaque() {
  $('#modal_ataque').modal('show')
}

function onDefender() {
  $('#modal_defender').modal('show')
}