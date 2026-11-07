from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, Docker World!</h1><p>내 프로그램이 컨테이너에서 정상 작동 중입니다.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
