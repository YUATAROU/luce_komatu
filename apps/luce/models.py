from apps.app import db

class Category(db.Model):
  __tablename__= "categories"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, unique=True)

  menus = db.relationship('Menu', backref='category', lazy=True)
  
  def __repr__(self):
        return f'<Category {self.name}>'


class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f'<Menu {self.name} - {self.price}円>'
