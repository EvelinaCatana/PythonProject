from fastapi import FastAPI, Query, UploadFile, File, Form
from pydantic import BaseModel
from typing import List
import numpy as np
from scipy import stats
import csv
import io

app = FastAPI()

class Student(BaseModel):
    name: str
    scores: List[float]

class SubjectScores(BaseModel):
    subject: str
    scores: List[float]

class StudentsList(BaseModel):
    students: List[Student]
    top_n: int


@app.post("/average-score")
async def average_score(student: Student):
    average = np.mean(student.scores)
    return {"Student": student.name, "Average Score": average}

@app.get("/top-subject")
async def top_subject(scores: List[float] = Query(...), subjects: List[str] = Query(...)):
    if len(scores) != len(subjects):
        return {"error": "Mismatch between scores and subjects"}
    max_index = np.argmax(scores)
    return {"Top Subject": subjects[max_index], "Score": scores[max_index]}

@app.post("/subject-statistics")
async def subject_statistics(data: SubjectScores):
    scores_array = np.array(data.scores)
    average = np.mean(scores_array)
    median = np.median(scores_array)
    
    return {
        "Subject": data.subject,
        "Average": average,
        "Median": median,
    }

@app.post("/count-word-in-file")
async def count_word_in_file(word: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    content_decoded = content.decode("utf-8")
    count = content_decoded.lower().split().count(word.lower())
    return {"Word": word, "Occurrences": count}


@app.post("/student-standard-deviation")
async def student_standard_deviation(student: Student):
    std_dev = np.std(student.scores)
    return {"Student": student.name, "Standard Deviation": std_dev}

@app.post("/compare-students")
async def compare_students(student1: Student, student2: Student):
    avg1 = np.mean(student1.scores)
    avg2 = np.mean(student2.scores)
    if avg1 > avg2:
        result = f"{student1.name} has a higher average score."
    elif avg1 < avg2:
        result = f"{student2.name} has a higher average score."
    else:
        result = "Both students have the same average score."
    return {
        "Student1": {"Name": student1.name, "Average": avg1},
        "Student2": {"Name": student2.name, "Average": avg2},
        "Result": result
    }

@app.post("/top-n-students")
async def top_n_students(data: StudentsList):
    averages = [(student.name, np.mean(student.scores)) for student in data.students]
    sorted_students = sorted(averages, key=lambda x: x[1], reverse=True)
    top_students = sorted_students[:data.top_n]
    return {"Top Students": top_students}

@app.post("/process-scores-csv")
async def process_scores_csv(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode('utf-8')
    reader = csv.reader(io.StringIO(decoded))
    scores = []
    for row in reader:
        try:
            score = float(row[1])
            scores.append(score)
        except (ValueError, IndexError):
            continue  
    if not scores:
        return {"error": "No valid scores found in the CSV file"}
    scores_array = np.array(scores)
    average = np.mean(scores_array)
    median = np.median(scores_array)
    std_dev = np.std(scores_array)
    return {
        "Average": average,
        "Median": median,
        "Standard Deviation": std_dev,
    }