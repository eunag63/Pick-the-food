$(function() {

  expireDate = new Date
  expireDate.setMonth(expireDate.getMonth() + 6)
  jcount = eval(cookieVal("jaafarCounter"))
  jcount++
  document.cookie = "jaafarCounter=" + jcount + ";expires=" + expireDate.toGMTString()


  function page_counter() {

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
      }
    })



});
