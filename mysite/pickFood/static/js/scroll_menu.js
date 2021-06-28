//$(document).ready(function(){
$(function() {

  var $good = $('.parent > .div3 > #good'),
    $contents = $('.fullpage > div');

  $good.click(function(event) {
    event.preventDefault();
    $('html,body').animate({
      scrollTop: $(this.hash).offset().top
    }, 500);
  });


});
