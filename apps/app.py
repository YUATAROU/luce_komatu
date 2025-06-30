from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apps.config import config


# SQLAlchemyをインスタンス化する
db = SQLAlchemy()

# create_app関数を作成する
def create_app(config_key):
  # Flaskインスタンス生成
  app = Flask(
    __name__,
    static_folder='static',        
    static_url_path='/static'     
)
  
  # config_keyにマッチする環境のコンフィグクラスを読み込む
  app.config.from_object(config[config_key])
  # SQLAlchemyとアプリを連携する
  db.init_app(app)
    # Migrateとアプリを連携する
  Migrate(app, db)
  
  # fictionからviewsをimport
  from apps.luce import views as fic_views
  #register_blueprintを使いviewsのfictionをアプリへ登録する
  app.register_blueprint(fic_views.luce, url_prefix="/")
  from apps.luce import models 
  return app