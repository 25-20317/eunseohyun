import csv  # CSV 파일 읽기/쓰기 위해 csv 모듈 불러오기

pets = []  # 프로그램 실행 중 유기견 정보를 저장할 리스트

# 유기견 정보를 관리하는 클래스
class Pet:
    count = 0  # 등록된 유기견 수를 세는 클래스 변수

    # 유기견 객체 초기화
    def __init__(self, name, date, breed, zip_code):
        self.name = name          # 유기견 이름
        self.date = date          # 입소 날짜
        self.breed = breed        # 품종
        self.zip_code = zip_code  # 보호소 위치
        Pet.count += 1            # 객체 생성 시 등록 수 증가

    # 유기견 정보 출력 메서드
    def display_info(self):
        print(f"이름: {self.name}, 입소일: {self.date}, 품종: {self.breed}, 보호소위치: {self.zip_code}")

    # 등록된 유기견 수 출력 클래스 메서드
    @classmethod
    def show_count(cls):
        print(f"현재 등록된 유기견 수는 {cls.count}개 입니다.")

# CSV 파일에서 유기견 정보를 읽어 pets 리스트에 저장
def load_pets(petname):
    f = open(petname, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)  # 헤더 읽기
    print(header)          # 헤더 출력

    # CSV 파일 각 줄을 읽어 Pet 객체로 생성
    for line in reader:
        name, date, breed, zip_code = line
        pet_obj = Pet(name, date, breed, zip_code)
        pets.append(pet_obj)
    
    # 불러온 유기견 정보 출력
    for m in pets:
        m.display_info()   

    Pet.show_count()  # 현재 등록된 유기견 수 출력
    f.close()         # 파일 닫기

# 새로운 유기견 추가
def add_pet():
    print("\n 새 유기견를 추가합니다.")
    name = input("유기견 이름: ")
    date = input("입소 날짜: ")
    breed = input("품종: ")
    zip_code = input("보호소위치: ")

    new_pet = Pet(name, date, breed, zip_code)  # 새로운 Pet 객체 생성
    pets.append(new_pet)  # 리스트에 추가

    print("\n 새 유기견이 추가되었습니다!")
    new_pet.display_info()  # 추가된 유기견 정보 출력

# 기존 유기견 삭제
def delete_pet():
    print("\n 유기견를 삭제합니다.")
    input_name = input("유기견 이름: ")
    input_zip = input("보호소위치: ")

    found = False
    global pets
    new_pets = []

    # pets 리스트를 순회하며 삭제 대상 확인
    for t in pets:
        if t.name == input_name and t.zip_code == input_zip:
            print(f"\n{t.name} ({t.breed}) 해당 유기견이 삭제되었습니다!")
            Pet.count -= 1  # 삭제 시 등록 수 감소
            found = True
        else:
            new_pets.append(t)  # 삭제되지 않은 유기견은 새 리스트에 유지

    pets = new_pets  # 리스트 갱신

    if not found:
        print("\n해당 유기견을 찾을 수 없습니다.")
    else:
        print("\n삭제가 pets 리스트에 반영되었습니다.")

# 품종 검색 기능
def search_by_breed():
    print("\n유기견 품종 검색")
    search_breed = input("찾고 싶은 품종을 입력하세요: ")
    
    found = False
    # 대소문자 구분 없이 품종 검색
    for t in pets:
        if t.breed.lower() == search_breed.lower():
            t.display_info()
            found = True
    
    if not found:
        print(f"\n'{search_breed}' 품종의 유기견이 없습니다.")
    else:
        print(f"\n'{search_breed}' 품종의 유기견 정보를 모두 출력했습니다.")

# 사용자 입력에 따라 기능 선택
def manage_pet():
    action = input("\n무엇을 하시겠습니까? (add / delete/search): ")
    if action == "add":
        add_pet()
    elif action == "delete":
        delete_pet()
    elif action == "search":
        search_by_breed()
    else:
        print("\n잘못된 입력입니다. 'add', 'delete' 또는 'search'를 입력하세요.")

# pets 리스트 내용을 CSV 파일로 저장
def save_pet(filename):
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)

    # 헤더 작성
    writer.writerow(["name", "date", "breed", "zip_code"])

    # 유기견 정보 작성
    for m in pets:
        writer.writerow([m.name, m.date, m.breed, m.zip_code])

    print("파일이 업데이트 되었습니다.")
    f.close()

# 프로그램 실행 순서
load_pets("pet.csv")  # CSV 파일 불러오기
manage_pet()          # 사용자 기능 선택
save_pet("pet.csv")   # 변경 내용 CSV에 저장
