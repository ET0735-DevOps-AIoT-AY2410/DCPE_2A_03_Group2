let cart = [];


function addToCart(item, price, quantityId) {
    const quantity = document.getElementById(quantityId).value;
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const existingItem = cart.find(cartItem => cartItem.item === item);
    if (existingItem) {
        existingItem.quantity += parseInt(quantity);
    } else {
        cart.push({ item, price, quantity: parseInt(quantity) });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    alert(`${item} added to cart`);
}
