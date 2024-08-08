
document.addEventListener('DOMContentLoaded', () => {
    displayCart();
});

function addItemToCart(item, quantity, price) {
    // Retrieve the cart from local storage or initialize an empty array
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Add the new item to the cart
    cart.push({ item, quantity, price });

    // Save the updated cart back to local storage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Update the cart display
    displayCart();
}

function displayCart() {
    // Retrieve the cart from local storage
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartTableBody = document.querySelector('#cart-table tbody');
    cartTableBody.innerHTML = ''; // Clear existing rows

    let totalPrice = 0;

    cart.forEach(cartItem => {
        const row = document.createElement('tr');

        const itemName = document.createElement('td');
        itemName.textContent = cartItem.item;
        row.appendChild(itemName);

        const itemQuantity = document.createElement('td');
        itemQuantity.textContent = cartItem.quantity;
        row.appendChild(itemQuantity);

        const itemPrice = document.createElement('td');
        itemPrice.textContent = `$${cartItem.price.toFixed(2)}`;
        row.appendChild(itemPrice);

        const itemTotal = document.createElement('td');
        const total = cartItem.price * cartItem.quantity;
        itemTotal.textContent = `$${total.toFixed(2)}`;
        row.appendChild(itemTotal);

        cartTableBody.appendChild(row);

        totalPrice += total;
    });

    document.getElementById('total-price').textContent = `Total Price: $${totalPrice.toFixed(2)}`;
}

function goToCheckout() {
    window.location.href = 'checkout.html';
}

function clearcart() {
    localStorage.removeItem('cart'); // Clear the cart data from local storage
    const cartTableBody = document.querySelector('#cart-table tbody');
    cartTableBody.innerHTML = ''; // Clear the cart table
    document.getElementById('total-price').textContent = 'Total Price: $0'; // Reset the total price
}
