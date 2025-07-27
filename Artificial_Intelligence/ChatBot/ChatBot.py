
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable cross-origin for frontend

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep!'"
]

quotes = {
    "funny": [
        "I'm on a seafood diet. I see food and I eat it!",
        "Life is short. Smile while you still have teeth.",
        "If you think nobody cares if you're alive, try missing a couple of payments."
    ],
    "sad": [
        "Tears come from the heart and not from the brain.",
        "It’s sad when someone you know becomes someone you knew.",
        "Sometimes, the person who tries to keep everyone happy is the most lonely one."
    ],
    "love": [
        "Love is not about how much you say 'I love you', but how much you prove it's true.",
        "In the end, we only regret the chances we didn’t take for love.",
        "You don't find love, it finds you. It's got a little bit to do with destiny."
    ]
}

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '').lower()

    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hello!👋 How can I help you today?"
    elif "how are you" in user_msg:
        reply = "I'm just a bot, but I'm doing great! How about you?😊"
    elif "your name" in user_msg:
        reply = "I'm ChatBot 1.0, your friendly assistant."
    elif "time" in user_msg:
        from datetime import datetime
        reply = "The current time is " + datetime.now().strftime("%H:%M:%S")
    elif "weather" in user_msg:
        reply = "I can't access real-time weather⛅, but it's always sunny in my world!"
    elif "help" in user_msg:
        reply = "You can ask me about time, weather, jokes, or quotes — I'm here to assist!"
    elif "thank you" in user_msg:
        reply = "your welcome! If you have anything else, feel free to ask 😇."
    elif "quotes" in user_msg:
        reply = "what kind of quotes are you looking for? I can provide funny 😂, sad😔, or love❤️ quotes."
    elif "joke" in user_msg:
        reply = random.choice(jokes)
    elif "funny" in user_msg:
        reply = random.choice(quotes["funny"])
    elif "😂" in user_msg:
        reply = random.choice(quotes["funny"])
    elif "sad" in user_msg:
        reply = random.choice(quotes["sad"])
    elif "😔" in user_msg:
        reply = random.choice(quotes["sad"])
    elif "love" in user_msg:
        reply = random.choice(quotes["love"])
    elif "❤️" in user_msg:
        reply = random.choice(quotes["love"])
    elif "bye" in user_msg or "bye" in user_msg:
        reply = "Goodbye! Have a nice day."
    else:
        reply = "Oops! Server error."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
