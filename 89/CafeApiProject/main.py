#  Created by Simone Margio
#  www.simonemargio.im

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# Get random cafe
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,

        "amenities": {
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    })

# Search cade by location
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("location")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    print(f"New API request!\nQuery location:{query_location}\nCafe:{cafe}")

    if cafe:
        return jsonify(cafe={
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                    "has_sockets": cafe.has_sockets,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "id": cafe.id,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "map_url": cafe.map_url,
                    "name": cafe.name,
                    "seats": cafe.seats,
        })
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

# Update price of specific id cafe
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found on the database."})

# Del cafe by id
@app.route("/report-closed/<int:cafe_id>", methods=["PATCH", "GET"])
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        api_key = "TopSecretAPIKey"
        api = request.args.get("api_key")
        if api == api_key:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted the cafee."}), 200
        else:
            return jsonify(error={"Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found on the database."}), 404


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
