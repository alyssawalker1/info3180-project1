from . import db

class Property(db.Model):
    
    __tablename__= 'properties'
    
    property_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    num_bedrooms = db.Column(db.Integer)
    num_baths = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    prop_type = db.Column(db.String(80))
    Desc = db.Column(db.String(400))
    photo = db.Column(db.String(100))
    
    def __init__(self, title, num_bedrooms, num_baths, location, price, prop_type, Desc, photo):
        self.title = title
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.location = location
        self.price = price
        self.prop_type = prop_type
        self.Desc = Desc
        self.photo = photo
