function post(notes) {
  postData = { "data": notes };
  $.ajax({
    async: false,
    url: "/notes",
    type:"POST",
    headers: { 
      "Content-Type": "application/json"
    },
    data: '{"data":"'+encodeURI(notes)+'"}',
    dataType: 'json'
  });
}

$(window).unload(function() {
  post($('#notes').val());
});

$(document).ready(function() {
  console.log("Welcome to the notes");

  $.get("/notes").done(function(r){
      $('#notes').val(decodeURI(r));
  });

  setInterval(function(){
    post($('#notes').val())
  } , 3000) 
  
  $('#notes').focusout(function(){
    post($('#notes').val());
  });

  $("#notes").mouseleave(function() {
    post($('#notes').val());
  });
});
