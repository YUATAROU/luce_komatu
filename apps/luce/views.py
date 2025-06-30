from flask import Blueprint, render_template, current_app
from flask import request, session, flash
from apps.luce.models import Category, Menu
import os

# Blueprintでfictionアプリを生成
luce = Blueprint("luce", __name__, template_folder="templates",
                    static_folder="static")

@luce.route("/")
def index():
  return render_template("index.html")

@luce.route("/menu")
def menu():
    categories = Category.query.all()
    return render_template("menu.html", categories=categories, selected_category=None)

@luce.route("/menu/category/<int:category_id>")
def menu_by_category(category_id):
    categories = Category.query.all()
    selected_category = Category.query.get_or_404(category_id)
    return render_template("menu.html", categories=categories, selected_category=selected_category)

@luce.route("course")
def course():
  return render_template("course.html")

@luce.route("access")
def access():
  return render_template("access.html")

@luce.route("/picture")
def picture():
    img_folder = os.path.join(current_app.root_path, '..', 'static', 'img')
    img_folder = os.path.abspath(img_folder)

    image_files = [
        f for f in os.listdir(img_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]
    return render_template("picture.html", images=image_files)