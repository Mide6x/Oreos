#Calculating script's prediction on 53 samples.

product_names = [
    "Pilau Rice", "Finas Avena con choco leche biscuits", "Sugar free zero CHOC chip cookies", "Plain Basmati Rice",
    "Thai Jasmine Rice", "Poundo yam iyan", "Poundo iyan", "Poundo iyan", "Poundo iyan", "Poundo yam", "Poundo yam",
    "Black Beans", "Chick Peas", "Italian Chopped Tomatoes", "Italian Peeled Plum Tomatoes", "Bacon & Tomato",
    "Cheese and Onion", "Lightly Sea Salted", "Roast Rib of Beef", "Sea Salt and Aspall Cyder Vinegar",
    "Sea Salt and Black Pepper", "Green Tea Lemon & Honey", "Lemon Green Tea", "Green Tea The Vert",
    "Lemon & Honey Green Tea", "Green Tea Lemon & Honey", "Pure Camomile", "Pure Camomile Infusion",
    "Pure Camomile", "Camomile Honey & Vanilla", "Camomile Honey & Vanilla", "Camomile Honey & Vanilla",
    "USA Easy Cook Rice", "American Cook Rice", "White Chocolate Oaty Bars", "Milk Chocolate Oaty Bars",
    "Caramel Oaty Bars", "Avengers Chocolate", "Chocolate Stars", "Strawberry Breakfast Drink", "Chocolate Breakfast Drink",
    "Chocolate Breakfast Drink", "Chocolate", "Vanilla", "Vanilla Breakfast Drink", "Strawberry Breakfast Drink",
    "Banana Breakfast Drink", "Banana", "Caffe Latte Breakfast Drink", "Crunchy Weeties", "Whole Gain Careals", "Chocolate"
]

product_categories = [
    "Grains & Rice", "Biscuits, Chin Chin & Cookies", "Sugar, Honey & Sweeteners", "Grains & Rice", "Grains & Rice",
    "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina",
    "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Unknown Product Type", "Unknown Product Type",
    "Unknown Product Type", "Unknown Product Type", "Oats & Instant Cereals", "Butter, Cheese & Other Spreads",
    "Salt & Seasoning Cubes", "Coffee", "Salt & Seasoning Cubes", "Salt & Seasoning Cubes", "Everyday Tea", "Everyday Tea",
    "Everyday Tea", "Everyday Tea", "Everyday Tea", "Unknown Product Type", "Unknown Product Type", "Unknown Product Type",
    "Oats & Instant Cereals", "Oats & Instant Cereals", "Oats & Instant Cereals", "Cooking Oils", "Cooking Oils",
    "Chocolates & Sweets", "Milk", "Unknown Product Type", "Chocolates & Sweets", "Chocolates & Sweets", "Fizzy Drinks & Malt",
    "Chocolates & Sweets", "Chocolates & Sweets", "Chocolates & Sweets", "Unknown Product Type", "Fizzy Drinks & Malt",
    "Fizzy Drinks & Malt", "Fizzy Drinks & Malt", "Unknown Product Type", "Fizzy Drinks & Malt", "Unknown Product Type",
    "Unknown Product Type", "Chocolates & Sweets"
]

#correct categories for the products
correct_categories = [
    "Grains & Rice", "Biscuits, Chin Chin & Cookies", "Biscuits, Chin Chin & Cookies", "Grains & Rice", "Grains & Rice",
    "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina",
    "Poundo, Wheat & Semolina", "Poundo, Wheat & Semolina", "Unknown Product Type", "Unknown Product Type",
    "Unknown Product Type", "Unknown Product Type", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Herbal Teas", "Herbal Teas", "Herbal Teas", "Herbal Teas", "Herbal Teas", "Herbal Teas", "Herbal Teas",
    "Herbal Teas", "Herbal Teas", "Herbal Teas", "Grains & Rice", "Grains & Rice", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries", "Snacks & Confectioneries",
    "Snacks & Confectioneries", "Snacks & Confectioneries"
]


correct_predictions = 0
incorrect_predictions = []

for i in range(len(product_names)):
    if product_categories[i] == correct_categories[i]:
        correct_predictions += 1
    else:
        incorrect_predictions.append((product_names[i], product_categories[i], correct_categories[i]))

total_products = len(product_names)
accuracy = correct_predictions / total_products

correct_predictions, total_products, incorrect_predictions, accuracy
