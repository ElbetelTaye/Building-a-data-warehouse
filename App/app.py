from flask import Flask, jsonify, request, abort
from sqlalchemy.orm import Session
from database import get_db
from crud import get_messages, create_message
from schemas import TelegramMessage, TelegramMessageCreate
from models import Base
from database import engine

# Initialize Flask app
app = Flask(__name__)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.route("/", methods=["GET"])
def read_root():
    """Root endpoint"""
    return jsonify({"message": "Welcome to the Telegram Messages API"})

@app.route("/messages/", methods=["GET"])
def read_messages():
    """Read messages with optional skip and limit query parameters"""
    skip = request.args.get("skip", 0, type=int)
    limit = request.args.get("limit", 10, type=int)
    db = next(get_db())
    try:
        messages = get_messages(db, skip=skip, limit=limit)
        return jsonify([TelegramMessage.from_orm(msg).dict() for msg in messages])
    finally:
        db.close()

@app.route("/messages/", methods=["POST"])
def create_message_endpoint():
    """Create a new message"""
    db = next(get_db())
    try:
        data = request.get_json()
        message_data = TelegramMessageCreate(**data)
        new_message = create_message(db, message_data)
        return jsonify(TelegramMessage.from_orm(new_message).dict()), 201
    except Exception as e:
        abort(400, description=str(e))
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
