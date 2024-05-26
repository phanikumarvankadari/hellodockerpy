from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    response_text = "Hello, Docker.py!"
    return Response(response_text, status=200, content_type='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
