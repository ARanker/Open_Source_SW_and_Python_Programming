do = 1
score = 0
grade = 0
count_grade = 0
score_sumit = 0
l = 0

while do != 2:
    print("작업을 선택하세요.")
    print("   1. 입력")
    print("   2. 계산")

    do = int(input())

    if do == 1:
        print("학점을 입력하세요:")
        k = int(input())
        score += k

        print("평점을 입력하세요:")
        input_grade = input()
        count_grade += k

        if input_grade == "A+":
            grade += 4.5 * k
        if input_grade == "A":
            grade += 4.0 * k
        if input_grade == "B+":
            grade += 3.5 * k
        if input_grade == "B":
            grade += 3.0 * k
        if input_grade == "C+":
            grade += 2.5 * k
        if input_grade == "C":
            grade += 2.0 * k
        if input_grade == "D+":
            grade += 1.5 * k
        if input_grade == "D":
            grade += 1.0 * k
        if input_grade == "F":
            grade += 0.0 * k
            score_sumit += k
            l += k

        print("입력되었습니다.\n")

print(
    "제출용:",
    score - score_sumit,
    "학점 (GPA:",
    round(grade / (count_grade - l), 2),
    ")",
)
print("열람용:", score, "학점 (GPA:", round(grade / count_grade, 2), ")\n")

print("프로그램을 종료합니다.")

# 아맞다 ㅋㅋ 저본바보
