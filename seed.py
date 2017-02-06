from sqlalchemy import func
from model import City, connect_to_db, db


def load_cities():
    """Load cities from seed_data.txt into database."""

    print "Cities"

    City.query.delete()

    for row in open("seed_data/cities_data.txt"):
        row = row.rstrip()
        city_id, name, lat, lng, country, iso2, province = row.split("|")
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



if __name__ == '__main__':
    connect_to_db(app)

    # Create tables if they haven't been created yet.
    db.create_all()

    #Import cities data and set the id value for the next city added.
    load_cities()
