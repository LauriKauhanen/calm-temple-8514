window.addEventListener("DOMContentLoaded", function () {
var form = document.getElementById("quiz");
document.getElementsByName("answer").addEventListener("click", function () {
  form.submit();
});
});
