from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent').lower()
    is_mobile = 'iphone' in user_agent or 'android' in user_agent
    return render_template("index.html", is_mobile=is_mobile)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
