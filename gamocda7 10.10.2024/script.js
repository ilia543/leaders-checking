let todo = document.getElementById("ToDo");
let addbut = document.getElementById("addElement");
let dolist = document.getElementById("listelements");

addbut.addEventListener("click", function(){
    
    let button = document.createElement('button');
    let br = document.createElement('br');
    let br1 = document.createElement('br');

    button.classList.add('button-styling');
    button.innerText = todo.value;

    dolist.appendChild(button);
    dolist.appendChild(br);
    dolist.appendChild(br1);

    todo.value = "";

    button.addEventListener('click', function(){

    button.style.textDecoration = "line-through";

    })

    button.addEventListener('dblclick', function(){

        dolist.removeChild(button);
        dolist.removeChild(br);
        dolist.removeChild(br1);

    })
})
