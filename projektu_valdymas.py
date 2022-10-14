from projekto_modelis import Projektas, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

def print_projects():
    print("--- PROJEKTAI ---")
    print("(#, Pavadinimas, Kaina, Sukurta)")
    projects = session.query(Projektas).all()
    for project in projects:
        print(project)

def new_project():
    print("--- Naujas Projektas ---")
    try:
        name = input("Pavadinimas: ")
        price = float(input("Kaina: "))
    except ValueError:
        print("KLAIDA: Kaina turi būti skaičius.")
        return
    else:
        project = Projektas(name, price)
        session.add(project)
        session.commit()
        print(f"Projektas {project} sukurtas sėkmingai")

def input_project():
    print_projects()
    try:
        project_id = int(input("Įveskite projekto ID: "))
    except ValueError:
        print("KLAIDA: ID turi būti skaičius.")
        return None
    else:
        return project_id

def update_project():
    project_id = input_project()
    if project_id:
        project = session.query(Projektas).get(project_id)
        if project:
            # -- updating here
            try:
                name = input(f"Pavadinimas ({project.name}): ")
                price = float(input(f"Kaina ({project.price}): ") or 0)
            except ValueError:
                print("KLAIDA: kaina turi būti skaičius.")
            else:
                if len(name) > 0:
                    project.name = name
                if price:
                    project.price = price
                session.commit()
                print(f"Projektas {project} atnaujintas sėkmingai.")
            # -- end of updating
        else:
            print(f"KLAIDA: Projektas su ID: {project_id} neegzistuoja.")

def delete_project():
    project_id = input_project()
    if project_id:
        trinamas = session.query(Projektas).get(project_id)
        if trinamas:
            # -- deleting here
            session.delete(trinamas)
            session.commit()
            print(f"Projektas {trinamas} ištrintas sėkmingai")
            # -- end of deleting
        else:
            print(f"KLAIDA: Projektas su ID: {project_id} neegzistuoja")

while True:
    print("=== Projektų valdymo duomenų bazė ===")
    print("- q: išeiti")
    print("- r: rodyti visus projektus")
    print("- n: naujas projektas")
    print("- u: pakeisti projekto duomenis")
    print("- d: trinti projektą")
    pasirinkimas = input("Pasirinkite: ").casefold()
    if pasirinkimas == "q":
        print("Viso gero!")
        break
    elif pasirinkimas == "r":
        print_projects()
    elif pasirinkimas == "n":
        new_project()
    elif pasirinkimas == "u":
        update_project()
    elif pasirinkimas == "d":
        delete_project()
    else:
        print("KLAIDA: Blogas pasirinkimas, rinkitės iš naujo!")
