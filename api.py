import string
import random
from quart import Quart, jsonify, send_file
from quart_cors import cors
from generate import captcha
import os

app = Quart(__name__)
app = cors(app)

@app.get("/captcha")
async def generate_captcha():

    text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    
    if not os.path.exists(f"./captchas/{text}.png"):
        captcha(text)

    return jsonify({
        "text": text,
        "url": f"http://localhost:5000/captchas/{text}"
    })

@app.get("/captchas/<string:captcha_text>")
async def serve_captcha(captcha_text):
    return await send_file(f"captchas/{captcha_text}.png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)