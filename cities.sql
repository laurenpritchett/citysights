CREATE TABLE cities(
  city_id SERIAL PRIMARY KEY
, name VARCHAR(33) DEFAULT NULL
, lat NUMERIC(12,9) DEFAULT NULL
, lng NUMERIC(13,9) DEFAULT NULL
, country VARCHAR(32) DEFAULT NULL
, iso2 VARCHAR(3) DEFAULT NULL
, province VARCHAR(43) DEFAULT NULL
);

INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Paris',48.86669293,2.333335326,'France','FR','Ile-de-France');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Berlin',52.52181866,13.40154862,'Germany','DE','Berlin');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('New York',40.74997906,-73.98001693,'United States of America','US','New York');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Los Angeles',33.98997825,-118.1799805,'United States of America','US','California');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('San Francisco',37.74000775,-122.4599777,'United States of America','US','California');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Tokyo',35.68501691,139.7514074,'Japan','JP','Tokyo');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Shanghai',31.21645245,121.4365047,'China','CN','Shanghai');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Denpasar',-8.650028871,115.2199849,'Indonesia','ID','Bali');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Seattle',47.57000205,-122.339985,'United States of America','US','Washington');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Honolulu',21.30687644,-157.8579979,'United States of America','US','Hawaii');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Phoenix',33.53997988,-112.0699917,'United States of America','US','Arizona');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('San Diego',32.82002382,-117.1799899,'United States of America','US','California');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Dallas',32.82002382,-96.84001693,'United States of America','US','Texas');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Miami',25.7876107,-80.22410608,'United States of America','US','Florida');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Atlanta',33.83001385,-84.39994938,'United States of America','US','Georgia');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Chicago',41.82999066,-87.75005497,'United States of America','US','Illinois');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Denver',39.73918805,-104.984016,'United States of America','US','Colorado');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Washington, D.C.',38.89954938,-77.00941858,'United States of America','US','District of Columbia');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Salt Lake City',40.7750163,-111.9300519,'United States of America','US','Utah');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Stockholm',59.35075995,18.09733473,'Sweden','SE','Stockholm');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Seoul',37.5663491,126.999731,'South Korea','KR','Seoul');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Sao Paulo',-23.55867959,-46.62501998,'Brazil','BR','Sao Paulo');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Sydney',-33.92001097,151.1851798,'Australia','AU','New South Wales');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Lagos',6.443261653,3.391531071,'Nigeria','NG','Lagos');
INSERT INTO cities (name,lat,lng,country,iso2,province) VALUES ('Cairo',30.04996035,31.24996822,'Egypt','EG','Al Qahirah');
