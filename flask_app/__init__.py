from flask import Flask, render_template
#from flask_app.config import DevelopmentConfig
import os

# app = Flask(__name__)
# app.config["SOME_CONFIG"] = "configured __init__.py"
# config.cfgファイルから構成設定を読み込む
#app.config.from_pyfile("config.cfg", silent=True)

# 環境変数で指定したファイルから構成設定を読み込む
#app.config.from_envvar("ANOTHER_CONFIG_FILE")

# Pythonのオブジェクトから構成設定を読み込む（文字列指定）
# app.config.from_object("flask_app.config.DevelopmentConfig")

# Pythonのオブジェクトから構成設定を読みこむ（クラスオブジェクト指定）
#app.config.from_object(DevelopmentConfig)

# from_objectメソッドを使った構成設定の読み込みの理想形
# app.config.from_object("flask_app.config.Config") # デフォルトの構成値
# app.config.from_pyfile(os.environ["APP_SETTINGS"]) # 環境固有の構成値
# app.config.from_envvar("APP_SETTINGS") # 環境固有の構成値

# インスタンスフォルダを使用した構成
app = Flask(__name__, instance_relative_config = True)
print(app.instance_path)
app.config.from_object("flask_app.config.Config")  # デフォルト
app.config.from_pyfile("config.cfg") # var/{APP_NAME}-instance/config.cfgファイルから読み込み


@app.route("/")
def index():
    return render_template("index.html", config=app.config.items())