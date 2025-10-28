import csv
pets = []

class Pet:
    count = 0

    def __init__(self, name, date, breed, zip_code):
        self.name = name
        self.date = date
        self.name = breed
        self.zip_code = zip_code
        Pet.count += 1 

    def display_info(self):
        print(f"이름: {self.name}, 입소일: {self.date}, 품종: {self.breed}, 보호소위치: {self.zip_code}")

    @classmethod
    def show_count(cls):
        print(f"현재 등록된 유기견 수는 {cls.count}개 입니다.")

def load_pets(petname):
    f = open(petname, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)
    print(header)

    for line in reader:
        name, date, breed, zip_code = line
        pet_obj = Pet(name, date, breed, zip_code)
        pets.append(pet_obj)
    
    for m in pets:
        m.display_info()   

    Pet.show_count()

    f.close()

def add_pet():
    print("\n 새 유기견를 추가합니다.")
    name = input("유기견 이름: ")
    date = int(input("입소 날짜: "))
    breed = int(input("품종: "))
    zip_code = int (input("보호소위치: "))

    new_pet = Pet(name, date, breed, zip_code)
    pets.append(new_pet)

    print("\n 새 유기견이 추가되었습니다!")
    new_pet.display_info()

def delete_pet(petname):
    print("\n 유기견를 삭제합니다.")
    name = input("유기견 이름: ")
    zip_code = int (input("보호소위치: "))

    delete_pet = Pet(name, zip_code)

    f = open(petname, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)
    print(header)

    for line in reader:
        name, date, breed, zip_code = line
        pet_obj = Pet(name, date, breed, zip_code)
        if pet_obj.name == name and pet_obj.zip_code == zip_code:
            Pet.count -= 1
            print("\n 해당 유기견이 삭제되었습니다!")
            continue
        else:
            pets.append(pet_obj)
    
    for p in pets:
        print(p.name)
    
    f.close() 

def manage_pet():
    action = input("\n무엇을 하시겠습니까? (add / delete): ")
    if action == "add":
        add_pet()
    elif action == "delete":
        delete_pet()
    else:
        print("\n잘못된 입력입니다. 'add' 또는 'delete'를 입력하세요.")

def save_pet(filename):
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)

    writer.wirterow(["name", "date", "breed", "zip_code"])

    for m in pets:
        writer.writerow([m.name, m.date, m.breed, m.zip_code])

    print(    "파일이 업데이트 되었습니다.")
    f.close()

load_pets("pet.csv")
manage_pet("pet.csv")
save_pet("pet.csv")
