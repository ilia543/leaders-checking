let conteiner = document.getElementById("conteiner");
let cartProducts = document.getElementById("products_in_cart");
let ec = document.getElementById("ec");
let products_number = document.getElementById("products_number")

let cart = [];


fetch("https://fakestoreapi.com/products").then(res => res.json()).then(data => {
    data.forEach(product => {
        const div = document.createElement("div");
        div.className = "prod";
        div.innerHTML = `
            <img src="${product.image}">
            <h2>${product.title}</h2>
            <p>${product.price}</p>
            <button onclick='addproduct(${JSON.stringify(product)})'>add</button>
        `;
        conteiner.appendChild(div);
    });
});


function cartpr() {
    cartProducts.innerHTML = "";
    products_number.textContent = cart.length;
    cart.forEach(el => {
        const div = document.createElement("div");
        div.className = "cartitem";
        div.innerHTML = `
            <span>${el.title}</span>
            <button onclick="removeproduct(${el.id})">x</button>
        `;
        cartProducts.appendChild(div);
    });
}

function addproduct(product){
    cart.push(product)
    cartpr()
}
function removeproduct(id){
    cart = cart.filter(item => item.id !== id)
    cartpr()
}

