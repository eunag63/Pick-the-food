$(function() {

  var count = 0;
  var inter;

  function add() {
    count += 1;
    $('#count').html(count)
  }

  $(document).ready(function() {
    $('#plus').on('mousedown', function() {
      inter = setInterval(add, 70)
    })

    $('#plus').on('mouseup', function() {
      clearInterval(inter)
    })
  })



});
