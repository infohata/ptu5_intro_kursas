CREATE TABLE coder (
	first_name VARCHAR(50),
	last_name VARCHAR(100),
	email VARCHAR(255),
	age INTEGER,
	xp_years INTEGER
);

CREATE TABLE teams (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE coders (
	id INTEGER PRIMARY KEY NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	email VARCHAR(255) UNIQUE,
	age INTEGER CHECK (age > 17 AND age < 75),
	xp_years INTEGER CHECK (xp_years > 0 AND xp_years < 50),
	team_id INTEGER,
	FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE tasks (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(255) NOT NULL,
	description TEXT,
	coder_id INTEGER,
	FOREIGN KEY (coder_id) REFERENCES coders(id)
)

-- SQLite sucks, nepalaiko
-- ALTER TABLE coders ADD CONSTRAINT fk_coders_teams FOREIGN KEY (team_id) REFERENCES teams (id);

INSERT INTO "teams" ("name") VALUES ('Back End');
INSERT INTO "teams" ("name") VALUES ('DevOps');
INSERT INTO "teams" ("name") VALUES ('Front End');

INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Jonas', 'Jonaitis', 'jj@gmail.com', '20', '1');
INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Antanas', 'Antanaitis', 'aa@gmail.com', '25', '1');
INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Juozas', 'Juozaitis', 'jj@hotmail.com', '30', '2');
INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Petras', 'Petraitis', 'pp@mail.lt', '29', '2');
INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Virgis', 'Virgutis', 'vv@gmail.com', '21', '3');
INSERT INTO "coders" ("first_name", "last_name", "email", "age", "team_id") VALUES ('Tomas', 'Aidietis', 'ta@imone.lt', '35', '3');

INSERT INTO "tasks" ("name", "coder_id") VALUES ('Sutvarkyti DB', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti dizainą', '1');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti formas', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti tvarkykles', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perkrauti serverius', '5');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti bibliotekas', '6');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Pakeisti logotipus', '2');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Atnaujinti dokumentaciją', '3');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Ištestuoti programą', '4');
INSERT INTO "tasks" ("name", "coder_id") VALUES ('Perdaryti API', '4');

UPDATE coders SET xp_years = round((age - 18)/2);
