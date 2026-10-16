"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách.

    Args:
        students: Danh sách sinh viên hiện tại
        student_id: Mã sinh viên
        name: Họ tên
        age: Tuổi
        grade: Khóa

    Returns:
        Danh sách sinh viên đã được cập nhật
    """
    # Kiểm tra trùng mã sinh viên
    for s in students:
        if s.student_id == student_id:
            print(f"❌ Mã sinh viên {student_id} đã tồn tại!")
            return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"✅ Đã thêm sinh viên: {new_student}")
    return students


def find_student_by_id(students: list, student_id: str):
    """Tìm sinh viên theo mã sinh viên (chính xác).

    Args:
        students: Danh sách sinh viên
        student_id: Mã sinh viên cần tìm

    Returns:
        Đối tượng Student nếu tìm thấy, ngược lại trả về None
    """
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def search_students(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo từ khóa (chứa trong tên hoặc mã sinh viên).

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        Danh sách sinh viên phù hợp
    """
    keyword_lower = keyword.strip().lower()
    results = [
        s for s in students 
        if keyword_lower in s.student_id.lower() or keyword_lower in s.name.lower()
    ]
    return results


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Tran Viet Anh", 20, "K20"),
        Student("SV002", "Vi Duc Doan", 21, "K20"),
        Student("SV003", "Luong Thi Men", 19, "K21"),
    ]

    # Thêm sinh viên mới
    students = add_student(students, "SV004", "Pham Thi D", 22, "K19")

    # Hiển thị toàn bộ danh sách
    print("\n--- Danh sách sinh viên ---")
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

    # Demo 1: Tìm chính xác theo mã sinh viên
    print("\n" + "=" * 50)
    print("🔍 TÌM KIẾM THEO MÃ SINH VIÊN (SV002)")
    print("=" * 50)
    found_student = find_student_by_id(students, "SV002")
    if found_student:
        print(f"Kết quả: {found_student}")
    else:
        print("❌ Không tìm thấy sinh viên!")

    # Demo 2: Tìm kiếm tương đối theo từ khóa (tên hoặc mã)
    print("\n" + "=" * 50)
    print("🔍 TÌM KIẾM THEO TỪ KHÓA ('Van')")
    print("=" * 50)
    search_results = search_students(students, "Van")
    if search_results:
        for item in search_results:
            print(f"  {item}")
    else:
        print("❌ Không tìm thấy sinh viên nào phù hợp!")


if __name__ == "__main__":
    main()