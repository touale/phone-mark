
from configManage import ConfigManager
from controller import Controller
from flask import Flask
import os
configManage = ConfigManager()
app = Flask(__name__)
app.secret_key = os.urandom(24)
controller = Controller(configManage.isDebug)

@app.route('/select/<phone>',methods = ['get'])
def select(phone):
    res = controller.select(phone)
    print(res)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5801, threaded=False)


