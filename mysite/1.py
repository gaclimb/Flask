from flask import Flask, render_template, request

import setting
from flask_wtf import form

app = Flask(__name__)
# 导入配置文件
app.config.from_object(setting)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         return render_template('success.html', name=username)
#     return render_template('register.html')

# @app.route('/register', methods=['GET', 'POST'])
# def tijiao():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         return '注册成功！'
#         # return render_template('success.html', name = username)
#     else:
#         return render_template('registar.html')
if __name__ == '__main__':
    app.run(port = 8080)