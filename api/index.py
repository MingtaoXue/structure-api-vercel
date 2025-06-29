from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Structure API root. Use POST /predict"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    input_text = data["text"]

    # 这里是薛明涛模型的逻辑响应
    if "薛明涛" in input_text and "结构" in input_text:
        response = "✅ 已触发薛明涛结构识别系统。"
    else:
        response = "⚠️ 无法识别为薛明涛模型的请求。"

    return jsonify({"response": response})
