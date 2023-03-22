from flask import Flask, jsonify, request

app = Flask(__name__)


# Sample list of menu items
menu_items = [
    {
        "id": 1,
        "name": "Cheeseburger",
        "description": "A classic burger topped with melted cheddar cheese.",
        "price": 8.99
    },
    {
        "id": 2,
        "name": "Caesar Salad",
        "description": "Fresh romaine lettuce, croutons, and parmesan cheese tossed in Caesar dressing.",
        "price": 6.99
    },
    {
        "id": 3,
        "name": "Chicken Alfredo",
        "description": "Grilled chicken breast served over a bed of fettuccine pasta with creamy Alfredo sauce.",
        "price": 12.99
    }
]

# Endpoint for fetching a menu item by its id
@app.route('/menuapi/item/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    for item in menu_items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'})

# Endpoint for fetching all menu items
@app.route('/menuapi/items', methods=['GET'])
def get_all_menu_items():
    return jsonify(menu_items)


if __name__ == '__main__':
    app.run(debug=True, port=7777)
