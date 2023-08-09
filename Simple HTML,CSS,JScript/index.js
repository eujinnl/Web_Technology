
function addProject() {
  const project = document.getElementById('proj').value
  var ul = document.getElementById("list");
  var li = document.createElement("li");

  //li.innerHTML = "<li> project </li>"
  li.appendChild(document.createTextNode(project));
  ul.appendChild(li)
  var form = document.getElementById("myForm");
  function handleForm(event) { event.preventDefault(); } 
  form.addEventListener('submit', handleForm);
 }