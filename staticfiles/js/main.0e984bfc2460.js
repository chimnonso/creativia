
$(document).ready(function(){
  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a").on('click', function(event) {

   // Make sure this.hash has a value before overriding default behavior
  if (this.hash !== "") {

    // Prevent default anchor click behavior
    event.preventDefault();

    // Store hash
    var hash = this.hash;

    // Using jQuery's animate() method to add smooth page scroll
    // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 900, function(){

      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;
      });
    } // End if
  });

  $('#event_form').on('submmit', function(e){
    e.preventDefault();
    console.log('Submitted');
    create_post();
  })

})

$(window).scroll(function() {
  $(".slideanim").each(function(){
    var pos = $(this).offset().top;

    var winTop = $(window).scrollTop();
    if (pos < winTop + 600) {
      $(this).addClass("slide");
    }
  });
});


function create_post() {
  var data = {
    'first_name': $('#first_name').val(),
    'subject': $('#subject').val(),
    'email': $('#email').val(),
    'last_name': $('#last_name').val(),
    'company_name': $('#company_name').val(),
  }
  $.ajax({
    url: 'contact/event',
    type: "POST",
    data: { data },

    success: function(json) {
      console.log(json)
      console.log('success')
    }
  });
}