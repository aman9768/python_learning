from loguru import logger
student_name_with_marks={"Alex":95,"John":80,"Marie":70}
# logger.info(student_name_with_marks.items())
# logger.info(student_name_with_marks.values())

for name in student_name_with_marks:
    print(name,student_name_with_marks[name])


for key,value in student_name_with_marks.items():
    print(f"{key},{value}")

# student_name_with_marks.update({"Glenn":88,"Robin":54})
# print(student_name_with_marks.keys())
