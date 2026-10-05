import pandas as pd

mydataframe = {
    "student_id": ["001","002","003","004"],
    "CGPA": [3.75,3.87,3.6,3.88]
}

print(pd.DataFrame(mydataframe))