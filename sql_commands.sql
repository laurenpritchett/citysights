CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(64), NOT NULL,
	last_name VARCHAR(64), NOT NULL,
	email VARCHAR(64), NOT NULL,
	password VARCHAR(64), NOT NULL
	);

CREATE TABLE photos(
	photo_id VARCHAR(200) PRIMARY KEY,
	img_src VARCHAR(200) NOT NULL
	);

CREATE TABLE users_photos(
	users_photos_id SERIAL PRIMARY KEY,
	user_id INTEGER
		REFERENCES users,
	photo_id VARCHAR(200)
		REFERENCES photos
	);