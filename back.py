from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ============================================================
# ページルート
# ============================================================

@app.route("/")
def index():
    return render_template("index.html")

# ============================================================
# API ルート
# ============================================================

@app.route("/api/hello", methods=["GET"])
def api_hello():
    """動作確認用のシンプルなAPIエンドポイント"""
    return jsonify({"message": "Hello from Flask!", "status": "ok"})

# POST の例
@app.route("/api/echo", methods=["POST"])
def api_echo():
    """受け取ったJSONをそのまま返すエコーエンドポイント"""
    data = request.get_json(force=True, silent=True) or {}
    return jsonify({"echo": data})

# ============================================================
# エントリーポイント
# ============================================================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
