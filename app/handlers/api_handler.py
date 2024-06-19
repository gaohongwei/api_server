from flask import Response, stream_with_context
from app.services.api_service import stream_from_api

def handle_stream_proxy():
    api_url = 'https://example.com/api/stream'  # Replace with the actual streaming API URL
    return Response(stream_with_context(stream_from_api(api_url)), content_type='text/plain; charset=utf-8')
