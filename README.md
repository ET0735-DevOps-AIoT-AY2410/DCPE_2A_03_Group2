SUPERMARKET SELF_CHECKOUT WITH PAYMENT FUNCTION AND WEB-APP
Description:

Online Purchases
        In addition to purchasing the items in the store, customers also have the option to
        purchase the items online via a Smartphone App or website.
        For items purchased online, the customer then has the option to pick up the items from
        the supermarket themselves or deliver directly to their homes with a delivery fee of
        $4.00
        Online customers that opt to collect their items from the supermarket will receive a QR
        code after online payment that they will need to show to the supermarket staff to
        collect their items
In-Store Purchases
        The system is based on a camera that is used to read the bar codes on the products
        Each product has a barcode which contains a 10 digit unique identifier
        In a central database, the product IDs are mapped to the price of the product as well as
        several other attributes related to the product
        Each time a product’s barcode is scanned, the LCD screen shall display the product name
        as well as the price and the current cumulative total on the last line of the LCD
The system supports the following payment modes
        ATM via pin code on the numeric keypad
        “PayWave” via the RFID card reader

Hardware requirements
    Main Menu:
        1. When Bar-code scanner is first powered ON, the main menu with the text below shall be displayed on the LCD screen:
            Line 1 = “1. Scanner Start”
            Line 2 = “2. Power Off”
        2. In the main menu defined in REQ-01, if the option “1. Scanner Start” is selected on the keypad, then the following menu shall be displayed on the LCD screen
            Line 1 = “Scan ready”
            Line 2 = blank
        3. In the main menu defined in REQ-01, if the option “2. Power off” is selected, the LCD should display the following text for 2 seconds and then turn off the LCD display and back light and enter the LOW Power Mode state
    Scanner:
        4. From REQ-02, PICAM is implemented to scan and read barcode to find the 10 unique identifier numbers to be mapped to a product on the database.
        5. From REQ-04, Upon Scanning and successful read of barcode to find the 10 numbers, Buzzer turns on for 2 second in default tone before turning off until another barcode is scanned and read.
        6. From REQ-04, use the price of product found to calculate total cumulative pricing. LCD will display the Product name; Price of product; Total sum; Payment in the following format
            Line 1 = “Name: Price”
            Line 2 = “Total, Payment”
    Payment:
        7. From REQ-06, LCD Display will show as follows:
            Line 1 = “1 - PAYWAVE”
            Line 2 = “2 - ATMPIN”
            Numpad is used to select the payment type. 
            To select PayWave Payment Type by RFID, press 1 on the Numpad Input.
            To select ATMPIN Payment Type, press 2 on the Numpad input
Non-functional Requirement:
    Auto-cancellation:
        10. If no inputs have been detected from REQ-2 onwards, for 1     minute, code will return to REQ-1
    Database:
        11. Creation of Database for products to be scanned by PICAM. Table contains relevant information of 1. Name of product. 2. Product ID. 3. Price of product
        12. Creation of barcode and barcode image.
        
Software requirements
    Web application:
        Purchasing and checkout:
            8. Choose item through website  When adding items to cart, system will display total price and quantity of items. 
            - Pay for all the items (assume they have account and will automatically deduct money from there). 
            - After paying will Choosing of items through the website when finished, can choose from self-pick up or delivery. 
            - When delivery is chosen will inform that there is cost of $4 delivery charge. 
            - If customer chose self-pick up, system will produce a QR code which will be sent after payment. Show QR code to verify the order and collect 
        Authentication Service
            9. Choosing of items through the website when finished, can choose from self-pick up or delivery. 
            - When delivery is chosen, the system will inform that there is a delivery charge of $4 
            - No charge if customer chose self-pick up
Workload Distribution:
    Xavier (P2302874):
    WoonYeung (P2319485):
    Frinze (P2319795):
    Zhengjie (P2319430):

Installation and Running Procedures:
    Explanation:

Link to Video Demo:








