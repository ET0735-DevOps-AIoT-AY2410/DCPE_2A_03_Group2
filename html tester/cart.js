document.addEventListener('DOMContentLoaded', () => {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartTableBody = document.querySelector('#cart-table tbody');
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
        
        
        cartTableBody.appendChild(row);

        totalPrice += total;
    });

    document.getElementById('total-price').textContent = `Total Price: $${totalPrice.toFixed(2)}`;
});

function goToCheckout() {
     window.location.href = 'checkout.html';
}
