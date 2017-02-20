from sqlalchemy import func
from model import City, User, connect_to_db, db
from server import app


def load_cities():
    """Load cities from seed_data.txt into database."""

    print "Cities"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    City.query.delete()

    for row in open("seed_data/cities_data.txt"):
        row = row.rstrip()
        city_id, name, lat, lng, country, iso2, province = row.split("|")
        lat = float(lat)
        lng = float(lng)
        city = City(city_id=city_id,
                    name=name,
                    lat=lat,
                    lng=lng,
                    country=country,
                    iso2=iso2,
                    province=province)

        # Add the cities to the session
        db.session.add(city)

    #commit the added rows
    db.session.commit()


def load_users():
    """Load users from users_data into database."""

    print "Users"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read u.user file and insert data
    for row in open("seed_data/users_data.txt"):
        row = row.rstrip()
        user_id, first_name, last_name, email, password = row.split("|")

        user = User(user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id})
    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app)

    # Create tables if they haven't been created yet.
    db.create_all()

    # Import cities data.
    load_cities()

    # Import users data and set the id value for the next user added.
    load_users()

    set_val_user_id()
