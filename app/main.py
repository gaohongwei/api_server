from flask import Blueprint, request, Response
from .handlers.api_handler import llm_stream_proxy

main = Blueprint('main', __name__)

# Define route(s) using the Blueprint object
@main.route('/api/llm_stream', methods=['POST'])
def llm_stream_proxy_route():
    return llm_stream_proxy()



