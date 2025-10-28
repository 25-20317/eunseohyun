import csv
movies = []

class Movie:
    count = 0

    def __init__(self, title, duration, age):
        self.title = title
        self.duration = duration
        self.age = age
        Movie.count += 1
    
    def display_info(self):
        print(f"제목: {self.title}, 러닝타임: {self.duration}, 관람 가능 나이: {self.age}")

    @classmethod
    def show_count(cls):
        print(f"현재 상영 중인 영화는 {cls.count}개 입니다.")

def load_movies(filename):
    f = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)
    print(header)

    for line in reader:
        title, duration, age = line
        movie_obj = Movie(title, duration, age)
        movies.append(movie_obj)
    
    for m in movies:
        m.display_info()

    Movie.show_count()

    f.close()

def add_movie():
    print("\n🎥 새 영화를 추가합니다.")
    title = input("영화 제목: ")
    duration = int(input("러닝타임(분): "))
    age = int(input("관람 가능 나이: "))

    new_movie = Movie(title, duration, age)
    movies.append(new_movie)

    print("\n✅ 새 영화가 추가되었습니다!")
    new_movie.display_info()

def save_movie(filename):
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)

    writer.wirterow(["title", "dureation", "age"])

    for m in movies:
        writer.writerow([m.title, m.duration, m.age])

    print(    "파일이 업데이트 되었습니다.")
    f.close()

load_movies("movie.csv")
add_movie()
save_movie("movie.csv")