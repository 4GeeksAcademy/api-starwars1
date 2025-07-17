from flask import Blueprint, jsonify, request
from models import db, User, People, Planet, Favorite

api = Blueprint('api', __name__)


@api.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    print('mensaje')
    person = People.query.get(people_id)

    if person == None:
        return jsonify({"msg": "Person not exist"}), 200
    else:
        return jsonify({"id": person.id, "name": person.name}), 200


@api.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([{"id": p.id, "name": p.name} for p in people]), 200


@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([{"id": p.id, "name": p.name} for p in planets]), 200


@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet == None:
        return jsonify({"msg": "planet not exist"}), 200
    else:
        return jsonify({"id": planet.id, "name": planet.name}), 200


@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username} for u in users]), 200


@api.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Simulación de usuario actual (id=1)
    user = User.query.get(1)
    if not user:
        return jsonify({"msg": "User not found"}), 200
    favorites = []
    for fav in user.favorites:
        if fav.people_id:
            favorites.append({"people_id": fav.people_id})
        if fav.planet_id:
            favorites.append({"planet_id": fav.planet_id})
    return jsonify(favorites), 200


@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.get(1)
    if not user:
        return jsonify({"msg": "User not found"}), 200
    favorite = Favorite(user_id=user.id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"msg": "Planet added to favorites"}), 201


@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user = User.query.get(1)
    if not user:
        return jsonify({"msg": "User not found"}), 200
    favorite = Favorite(user_id=user.id, people_id=people_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"msg": "People added to favorites"}), 201


@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user = User.query.get(1)
    if user == None:
        return jsonify({"msg": "User not found"}), 200
    favorite = Favorite.query.filter_by(
        user_id=user.id, planet_id=planet_id).first()
    if not favorite:
        return jsonify({"msg": "Favorite not found"}), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite planet deleted"}), 200


@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user = User.query.get(1)
    if user == None:
        return jsonify({"msg": "User not found"}), 200
    favorite = Favorite.query.filter_by(
        user_id=user.id, people_id=people_id).first()
    if not favorite:
        return jsonify({"msg": "Favorite not found"}), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite people deleted"}), 200

# Crear un nuevo People


@api.route('/people', methods=['POST'])
def create_people():
    data = request.get_json()
    new_people = People(name=data.get('name'))
    db.session.add(new_people)
    db.session.commit()
    return jsonify({"id": new_people.id, "name": new_people.name}), 201

# Modificar un People


@api.route('/people/<int:people_id>', methods=['PUT'])
def update_people(people_id):
    data = request.get_json()
    people = People.query.get_or_404(people_id)
    people.name = data.get('name', people.name)
    db.session.commit()
    return jsonify({"id": people.id, "name": people.name}), 200

# Eliminar un People


@api.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people(people_id):
    people = People.query.get_or_404(people_id)
    db.session.delete(people)
    db.session.commit()
    return jsonify({"msg": "People eliminado"}), 200

# Crear un nuevo Planet


@api.route('/planets', methods=['POST'])
def create_planet():
    data = request.get_json()
    new_planet = Planet(name=data.get('name'))
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"id": new_planet.id, "name": new_planet.name}), 201

# Modificar un Planet


@api.route('/planets/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.get_json()
    planet = Planet.query.get_or_404(planet_id)
    planet.name = data.get('name', planet.name)
    db.session.commit()
    return jsonify({"id": planet.id, "name": planet.name}), 200

# Eliminar un Planet


@api.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg": "Planet eliminado"}), 200
