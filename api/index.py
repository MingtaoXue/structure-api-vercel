from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_input = data.get("text", "")

    if "薛明涛" in user_input:
        response = "✅ 已触发主干节拍链（薛明涛结构系统）"
    elif "珠子" in user_input or "节拍" in user_input:
        response = "⚙️ 已识别珠子节拍关键词，构建局部结构响应"
    else:
        response = "⚠️ 未识别关键词，无法建立结构链"

    return jsonify({"response": response})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "结构预测 API 已部署成功，等待关键词调用。"})
