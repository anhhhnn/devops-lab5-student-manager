"""Student Manager — DevOps Lab 5
Module: Main Application"""
from student import Student

def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Vi Duc Doan", 20, "K22"),
        Student("SV002", "Tran Viet Anh", 20, "K22"),
        Student("SV003", "Luong Thi Men", 20, "K22"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

if __name__ == "__main__":
    main()