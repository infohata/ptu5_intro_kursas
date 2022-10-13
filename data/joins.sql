SELECT * FROM person;
SELECT * FROM car;
SELECT * FROM company;
-- sujungiame lenteles
SELECT first_name, last_name, plate FROM person, car WHERE person.car_id = car.id;
SELECT person.first_name, person.last_name, car.plate FROM person, car WHERE person.car_id = car.id;
SELECT first_name, make || " " || model AS "car make model", name AS "company name" FROM person, car, company 
	WHERE person.car_id = car.id AND person.company_id = company.id ORDER BY name;
SELECT first_name, make || " " || model AS "car make model", name AS "company name" FROM person, car, company 
	WHERE person.car_id = car.id AND person.company_id = company.id AND make="Ford";

-- naudojam JOIN
SELECT first_name, last_name, plate FROM person JOIN car ON car_id = car.id;
SELECT person.first_name, person.last_name, car.plate FROM person JOIN car ON person.car_id = car.id;

-- su trimis lentelėmis JOIN
SELECT person.first_name, person.last_name, car.make, car.model, company.name FROM person
	JOIN car ON person.car_id = car.id
	JOIN company ON person.company_id = company.id
	WHERE car.make = "Ford"
	ORDER BY company.name;

-- grupuojame su JOIN
SELECT company.name, count(*) FROM person
	JOIN company ON person.company_id = company.id
	GROUP BY company.name;
	
-- rodom tik daugiau negu 3 darbuotojus
SELECT company.name, count(*) FROM person
	JOIN company ON person.company_id = company.id
	GROUP BY company.name
	HAVING count(*) > 3;

-- surandam Apple kompanijos darbuotojų auto valstybinius numerius
SELECT name, plate FROM person
	JOIN company ON person.company_id = company.id
	JOIN car ON person.car_id = car.id
	WHERE company.name = "Apple";

-- išrenkam darbuotojų vardus/pavardes, mašinų gamintojus ir įmones, pagal įmonių sąrašą, kuriose dirba iki 3 darbuotojų
SELECT first_name, last_name, make AS car_maker, name AS company_name FROM person
	JOIN company ON person.company_id = company.id
	JOIN car ON person.car_id = car.id
	WHERE company_id IN (
		SELECT company_id FROM person
			GROUP BY company_id
			HAVING count(*) <= 3
		)
	ORDER BY company.name;

SELECT first_name, last_name, make AS car_maker, name AS company_name FROM person
	JOIN company ON person.company_id = company.id
	JOIN car ON person.car_id = car.id
	WHERE make IN (
		SELECT make FROM car WHERE make LIKE "_o%" GROUP BY make
	)
	ORDER BY company.name;

SELECT first_name, last_name, make AS car_maker, name AS company_name FROM person
	JOIN company ON person.company_id = company.id
	JOIN car ON person.car_id = car.id
	WHERE make IN (
		SELECT make FROM car GROUP BY make HAVING count(*) >= 2
	)
	ORDER BY company.name;

-- LEFT JOIN, išrinksim ir darbuotojus be automobilių
SELECT first_name, last_name, make, model 
	FROM person	LEFT JOIN car ON person.car_id = car.id;

SELECT first_name, name FROM person RIGHT JOIN company ON company_id=company.id;
