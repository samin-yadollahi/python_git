from src.student import Student


def main():

    std = Student(std_id=1234, std_name="alice")

    std.get_lesson("python")

    print(std.name)


main()