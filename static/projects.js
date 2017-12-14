$(document).ready(function() {
  $("#project1_onclick").click(function() {
  $("#project1 div.top").toggleClass("transparent");
  var bottom = document.getElementById("bottom");
  if(bottom.style.display == 'block')
  {
	  bottom.style.display = 'none';
  }
  else
  {
	  bottom.style.display = 'block';
  }
});
	$("#project2_onclick").click(function() {
  $("#project2 div.top").toggleClass("transparent");
  var bottom = document.getElementById("bottom2");
  if(bottom.style.display == 'block')
  {
	  bottom.style.display = 'none';
  }
  else
  {
	  bottom.style.display = 'block';
  }
});
});