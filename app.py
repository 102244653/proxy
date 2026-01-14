import time

from flask import Flask, request, jsonify, render_template
import json
import requests

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')


@app.route('/sh')
def sh_page():
    """首页，显示API使用说明和测试表单"""
    return render_template('sh.html')


@app.route('/jw')
def jw_page():
    """首页，显示API使用说明和测试表单"""
    return render_template('jw.html')


@app.route('/api/data', methods=['POST'])
def receive_json():
    json_data = request.json
    url = 'https://testpinpai.zgysmjw.cn/api/product/list'
    headers = {
        'Content-Type': 'application/json',
        'dnt': '1',
        'Referer': 'https://h5.zgysmjw.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.1528.49'
    }

    data = requests.post(url, headers=headers, json=json_data)
    if data.status_code == 200:
        # 返回成功响应
        return json.dumps(data.json(), indent=4, ensure_ascii=False)
    else:
        _d = {
                "code": 0,
                "msg": "品拍请求失败",
                "time": str(time.time()),
                "data": {"total": 0,"per_page": "1","current_page": 1,"last_page": 1,"data": []}
            }
        return json.dumps(_d, indent=4, ensure_ascii=False)


@app.route('/health', methods=['GET'])
def health():
    # 返回成功响应
    return jsonify({
        "status": "success",
        "message": "健康",
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)