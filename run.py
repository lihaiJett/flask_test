# coding:utf-8
from app import app
from app.dept import dept
app.register_blueprint(dept, url_prefix='/dept')
if __name__ == '__main__':
    app.run()