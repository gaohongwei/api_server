from flask import Flask, request, Response
import requests
import json


apiUrl = "http://47.100.205.81:8888/ollama/api/chat"
authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgwNWM4OTVmLWIxNTUtNDNlOS1iZWY0LWZmOTA1YzZkMGJhNSJ9.t4VtVnRDBJUKKS32wb0HaVg2LeIQR7-P1L214ClAI8s"

def llm_stream_proxy():
    # Prepare the URL and headers for the target API
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {authToken}",
    }

    # Convert the incoming request data to JSON
    json_data = request.get_json()

    import pdb;pdb.set_trace()
    # Stream the request to the target API
    def generate():
        with requests.post(
            url=apiUrl,
            headers=headers,
            json=json_data,
            stream=True
        ) as resp:
            resp.raise_for_status()
            for chunk in resp.iter_content(chunk_size=8192):
                yield chunk

    # Return a streaming response
    return Response(generate(), content_type='application/octet-stream')