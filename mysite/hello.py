from flask import Flask, render_template
# from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# 上下文控制
@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # return '<p> Your browser is %s</p>'%user_agent
    # return '<br>'
    return '<h2>welcome to WEB</h2>'
    # 设置状态码
    # return '<h2>welcome to back</h2>', 400
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    # 重定向
    # return redirect('https://www.example.com')
    # URL 中 动态参数 id 对应的用户不存在，就返回状态码 404
    # 注意，abort 不会把控制权交还给调用它的函数，而是抛出异常把控制权交给 Web 服 务器。
    # user = load_user(id)
    # if not user:
    # 	abort(404)
    # return '<h1>Hello, %s</h1>' % user.name
# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', user=name, Title='Flask')
'''
# 带参数的动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>'%name
'''

if __name__ == '__main__':
    # manager = Manager(app)
    app.run(debug=True)
