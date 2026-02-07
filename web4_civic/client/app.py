from flask import Flask, render_template, jsonify, request, redirect, url_for
import os

app = Flask(__name__)

# Mock data for feed (replace with relay fetch later)
feed_data = [
    {
        "title": "Water Outage",
        "text": "Scheduled water outage in Katy area from 8 AM to 5 PM.",
        "topic": "utilities",
        "jurisdiction": "tx.harris.katy"
    },
    {
        "title": "School Closure",
        "text": "Katy ISD schools closed due to weather.",
        "topic": "schools",
        "jurisdiction": "tx.harris.katy"
    }
]

# Add more cards to the feed for demonstration purposes
feed_data.extend([
    {
        "title": "Road Construction",
        "text": "Main Street will be closed for construction from Feb 10 to Feb 20.",
        "topic": "traffic",
        "jurisdiction": "tx.harris.houston"
    },
    {
        "title": "Community Cleanup Event",
        "text": "Join us for a community cleanup event this Saturday at the park.",
        "topic": "events",
        "jurisdiction": "tx.harris.katy"
    },
    {
        "title": "Power Outage Update",
        "text": "Power has been restored to 90% of the affected areas.",
        "topic": "utilities",
        "jurisdiction": "tx.harris.katy"
    },
    {
        "title": "New School Opening",
        "text": "A new elementary school is opening in Brookshire next month.",
        "topic": "schools",
        "jurisdiction": "tx.waller.brookshire"
    }
])

trusted_keys = []

@app.route('/')
def home():
    return render_template('index.html', feed=feed_data)

@app.route('/api/feed', methods=['GET'])
def get_filtered_feed():
    search = request.args.get('search', '').lower()
    topic = request.args.get('topic', '')
    jurisdiction = request.args.get('jurisdiction', '')

    filtered_feed = [
        item for item in feed_data
        if (search in item['title'].lower() or search in item['text'].lower())
        and (topic == '' or item['topic'] == topic)
        and (jurisdiction == '' or item['jurisdiction'] == jurisdiction)
    ]

    # Redirect to home with filtered feed
    return render_template('index.html', feed=filtered_feed, trusted_keys=trusted_keys)

@app.route('/api/submit', methods=['POST'])
def submit_card():
    new_card = {
        "title": request.form['title'],
        "text": request.form['text'],
        "topic": request.form['topic'],
        "jurisdiction": request.form['jurisdiction']
    }
    feed_data.append(new_card)
    return redirect(url_for('home'))

@app.route('/api/trust', methods=['POST'])
def add_trusted_key():
    key = request.form['key']
    if key not in trusted_keys:
        trusted_keys.append(key)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)