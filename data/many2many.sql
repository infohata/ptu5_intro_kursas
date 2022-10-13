CREATE TABLE skills (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50)
);

INSERT INTO "skills" ("name") VALUES ('Python');
INSERT INTO "skills" ("name") VALUES ('JS');
INSERT INTO "skills" ("name") VALUES ('CSS');
INSERT INTO "skills" ("name") VALUES ('Go');
INSERT INTO "skills" ("name") VALUES ('AWS');
INSERT INTO "skills" ("name") VALUES ('Linux');

CREATE TABLE coders_skills (
	coder_id INTEGER,
	skill_id INTEGER,
	FOREIGN KEY (coder_id) REFERENCES coders(id),
	FOREIGN KEY (skill_id) REFERENCES skills(id)
);

INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('1', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '2');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('2', '3');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('3', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '1');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('4', '6');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '4');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('5', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '5');
INSERT INTO "coders_skills" ("coder_id", "skill_id") VALUES ('6', '6');

-- i6štraukiam programuotojus pagal skillsus
SELECT first_name, last_name, skills.name FROM coders_skills
JOIN coders ON coder_id = coders.id
JOIN skills ON skill_id = skills.id;

