CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(64), NOT NULL,
	last_name VARCHAR(64), NOT NULL,
	email VARCHAR(64), NOT NULL,
	password VARCHAR(64), NOT NULL
	);

CREATE TABLE users_photos(
	users_photos_id SERIAL PRIMARY KEY,
	user_id 
	photo_id
	);