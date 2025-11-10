"""
BotInterface - Flask Backend Application
Serves the chat interface and handles bot API communication
"""

from flask import Flask, render_template, request, jsonify, session
import requests
import os
from datetime import datetime
import uuid

app = Flask(__name__, 
            static_folder='stactic',
            static_url_path='/static',
            template_folder='templates')

# Secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Bot API configuration (update with your actual bot API)
BOT_API_URL = os.environ.get('BOT_API_URL', 'http://localhost:5001/api/generate')
BOT_API_TIMEOUT = int(os.environ.get('BOT_API_TIMEOUT', '30'))

# In-memory storage for conversations (replace with database in production)
conversations = {}


@app.route('/')
def index():
    """Serve the landing page"""
    return render_template('landing.html')


@app.route('/app')
def app_index():
    """Serve the chat application (moved to /app)"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat messages from frontend
    POST body: { "message": "user message", "session_id": "optional" }
    Returns: { "reply": "bot response", "session_id": "session_id" }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message manquant'}), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({'error': 'Message vide'}), 400
        
        # Get or create session ID
        session_id = data.get('session_id') or session.get('session_id')
        if not session_id:
            session_id = str(uuid.uuid4())
            session['session_id'] = session_id
        
        # Initialize conversation history for new sessions
        if session_id not in conversations:
            conversations[session_id] = []
        
        # Save user message
        user_msg = {
            'role': 'user',
            'content': user_message,
            'timestamp': datetime.utcnow().isoformat()
        }
        conversations[session_id].append(user_msg)
        
        # Call bot API
        try:
            bot_response = call_bot_api(user_message, session_id)
        except Exception as bot_error:
            app.logger.error(f'Bot API error: {bot_error}')
            return jsonify({
                'error': 'Erreur lors de la communication avec le bot',
                'details': str(bot_error)
            }), 502
        
        # Save bot response
        bot_msg = {
            'role': 'assistant',
            'content': bot_response,
            'timestamp': datetime.utcnow().isoformat()
        }
        conversations[session_id].append(bot_msg)
        
        return jsonify({
            'reply': bot_response,
            'session_id': session_id
        })
        
    except Exception as e:
        app.logger.error(f'Error in /api/chat: {e}')
        return jsonify({
            'error': 'Erreur serveur interne',
            'details': str(e)
        }), 500


@app.route('/api/history', methods=['GET'])
def history():
    """
    Get conversation history for current session
    Returns: { "messages": [...], "session_id": "session_id" }
    """
    try:
        session_id = session.get('session_id')
        
        if not session_id or session_id not in conversations:
            return jsonify({
                'messages': [],
                'session_id': None
            })
        
        return jsonify({
            'messages': conversations[session_id],
            'session_id': session_id
        })
        
    except Exception as e:
        app.logger.error(f'Error in /api/history: {e}')
        return jsonify({'error': 'Erreur lors de la récupération de l\'historique'}), 500


def call_bot_api(message: str, session_id: str) -> str:
    """
    Call the external bot API
    
    Args:
        message: User message
        session_id: Current session ID
    
    Returns:
        Bot response text
    
    Raises:
        Exception: If bot API fails
    """
    # TEMP: Mock response for development (remove when bot API is ready)
    if BOT_API_URL == 'http://localhost:5001/api/generate':
        return mock_bot_response(message)
    
    # Real bot API call
    try:
        response = requests.post(
            BOT_API_URL,
            json={
                'message': message,
                'session_id': session_id,
                'context': get_conversation_context(session_id)
            },
            timeout=BOT_API_TIMEOUT,
            headers={'Content-Type': 'application/json'}
        )
        
        response.raise_for_status()
        
        data = response.json()
        return data.get('reply', data.get('response', 'Désolé, je n\'ai pas de réponse.'))
        
    except requests.Timeout:
        raise Exception('Timeout: Le bot n\'a pas répondu à temps')
    except requests.ConnectionError:
        raise Exception('Erreur de connexion: Impossible de contacter le bot')
    except requests.HTTPError as e:
        raise Exception(f'Erreur HTTP {e.response.status_code}: {e.response.text}')
    except Exception as e:
        raise Exception(f'Erreur inattendue: {str(e)}')


def get_conversation_context(session_id: str, max_messages: int = 10) -> list:
    """
    Get recent conversation context for the bot
    
    Args:
        session_id: Current session ID
        max_messages: Maximum number of messages to include
    
    Returns:
        List of recent messages
    """
    if session_id not in conversations:
        return []
    
    return conversations[session_id][-max_messages:]


def mock_bot_response(message: str) -> str:
    """
    Mock bot response for development/testing
    Remove this when connecting to real bot API
    """
    message_lower = message.lower()
    
    responses = {
        'bonjour': 'Bonjour ! Je suis BotInterface, votre assistant intelligent. Comment puis-je vous aider aujourd\'hui ?',
        'comment': 'Je suis un assistant conçu pour répondre à vos questions et vous aider dans diverses tâches. Je peux discuter de nombreux sujets !',
        'aide': 'Je peux vous aider avec des questions, fournir des informations, et discuter de divers sujets. Que souhaitez-vous savoir ?',
        'merci': 'Je vous en prie ! N\'hésitez pas si vous avez d\'autres questions.',
    }
    
    for keyword, response in responses.items():
        if keyword in message_lower:
            return response
    
    return f'J\'ai bien reçu votre message : "{message}". Je suis actuellement en mode démo. Connectez une vraie API de bot pour des réponses intelligentes !'


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Route non trouvée'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    app.logger.error(f'Internal error: {error}')
    return jsonify({'error': 'Erreur serveur interne'}), 500


if __name__ == '__main__':
    # Development server
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', '5000'))
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode
    )
