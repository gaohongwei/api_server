from flask import Blueprint
from app.handlers.api_handler import handle_stream_proxy

main = Blueprint('main', __name__)

main.add_url_rule('/api/stream', 'handle_stream_proxy', handle_stream_proxy)
