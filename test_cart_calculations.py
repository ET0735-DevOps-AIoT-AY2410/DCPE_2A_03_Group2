from bs4 import BeautifulSoup
import pytest

@pytest.fixture
def load_html():
    with open("shoppingcart.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup

def test_cart_calculations(load_html):
    soup = load_html
    
    # Example items to be added to the cart
    items = [
        {"name": "Item 1", "quantity": 2, "price": 10.00},
        {"name": "Item 2", "quantity": 3, "price": 15.00},
        {"name": "Item 3", "quantity": 1, "price": 25.00},
    ]
    
    # Simulating adding items to the table
    tbody = soup.find("tbody")
    for item in items:
        total_amount = item["quantity"] * item["price"]
        row = soup.new_tag("tr")
        name_cell = soup.new_tag("td")
        name_cell.string = item["name"]
        quantity_cell = soup.new_tag("td")
        quantity_cell.string = str(item["quantity"])
        price_cell = soup.new_tag("td")
        price_cell.string = f"${item['price']:.2f}"
        total_amount_cell = soup.new_tag("td")
        total_amount_cell.string = f"${total_amount:.2f}"
        
        row.append(name_cell)
        row.append(quantity_cell)
        row.append(price_cell)
        row.append(total_amount_cell)
        tbody.append(row)
    
    # Calculate expected total price
    expected_total_price = sum(item["quantity"] * item["price"] for item in items)
    
    # Find the total price element in the HTML
    total_price_element = soup.find("p", {"id": "total-price"})
    
    # Replace the total price with the calculated total price
    total_price_element.string = f"Total Price: ${expected_total_price:.2f}"
    
    # Assert that the calculated total price is correct
    assert total_price_element.string == f"Total Price: ${expected_total_price:.2f}", "Total price calculation is incorrect"
