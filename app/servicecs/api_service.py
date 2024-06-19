import requests

def stream_from_api(api_url):
    response = requests.get(api_url, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            yield chunk
