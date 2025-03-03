from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_accessibility():
    url = request.form['url']
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        if "alt=" not in content:
            return f"Accessibility Issue Found: Missing 'alt' tags in images for {url}"
        else:
            return f"No Accessibility Issues Found for {url}"
    else:
        return "Failed to fetch the URL. Please check the website link."

if __name__ == '__main__':
    app.run(debug=True)
