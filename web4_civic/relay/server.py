from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for cards
cards = {}

@app.route('/cards', methods=['POST'])
def submit_card():
    card = request.json
    card_hash = card.get('hash')
    if not card_hash:
        return jsonify({"error": "Card must have a hash"}), 400
    cards[card_hash] = card
    return jsonify({"message": "Card submitted successfully"}), 201

@app.route('/cards/<card_hash>', methods=['GET'])
def get_card(card_hash):
    card = cards.get(card_hash)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(card)

@app.route('/sync', methods=['POST'])
def sync_cards():
    data = request.json
    known_hashes = set(data.get('known_hashes', []))
    missing_hashes = [h for h in cards if h not in known_hashes]
    missing_cards = [cards[h] for h in missing_hashes]
    return jsonify({"missing_hashes": missing_hashes, "cards": missing_cards})

@app.route('/heads', methods=['GET'])
def get_heads():
    # Placeholder for Merkle heads
    return jsonify({"heads": []})

@app.route('/query', methods=['GET'])
def query_cards():
    # Placeholder for query functionality
    return jsonify({"results": []})

if __name__ == '__main__':
    app.run(debug=True, port=5000)