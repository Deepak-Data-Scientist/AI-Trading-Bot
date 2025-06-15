# Main entry to run the bot
from flask import Flask, request, jsonify
from webhook_listener import process_signal

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or 'signal' not in data:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400
    
    signal = data['signal']
    process_signal(signal)
    
    return jsonify({'status': 'success', 'message': f'Signal {signal} received'}), 200

if __name__ == '__main__':
    print("🚀 Webhook listener started on http://0.0.0.0:5000/webhook")
    app.run(host='0.0.0.0', port=5000)
