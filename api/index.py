from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Structure API root. Use POST /predict to query."})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        user_input = data.get("user_input", "")
        # 你可以在这里调用模型逻辑，返回结果
        return jsonify({
            "result": f"已收到输入：{user_input}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
