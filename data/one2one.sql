CREATE TABLE passwords (
	id INTEGER PRIMARY KEY NOT NULL,
	coder_id INTEGER UNIQUE,
	pwd VARCHAR(255),
	FOREIGN KEY (coder_id) REFERENCES coders(id)
);

INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('1', '12345');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('2', 'verisykret');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('3', 'qwerty');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('4', 'uauauai');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('5', 'slaptazodis');
INSERT INTO "passwords" ("coder_id", "pwd") VALUES ('6', 'barzda');

SELECT first_name, pwd FROM coders
JOIN passwords ON passwords.coder_id = coders.id;

SELECT first_name, pwd FROM passwords
JOIN coders ON passwords.coder_id = coders.id;
