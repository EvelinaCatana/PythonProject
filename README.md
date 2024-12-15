# FastAPI Student Scores API

## Description
This FastAPI application provides a series of endpoints to calculate statistics for students, such as average, median, standard deviation, and other score-related data. It also includes features for processing CSV files and counting word occurrences in uploaded text files.

The project is containerized using **Docker Compose** for easy deployment.

## Main Features
1. **Calculate the average score of a student**
2. **Identify the subject with the highest score**
3. **Statistics for a subject (average, median)**
4. **Count occurrences of a word in an uploaded file**
5. **Calculate the standard deviation of a student's scores**
6. **Compare the average scores of two students**
7. **Identify the "Top N" students with the highest average scores**
8. **Process a CSV file of scores to calculate average, median, and standard deviation**

## Requirements
- **Docker** and **Docker Compose** installed on your system
- Python 3.8+ (optional for running without Docker)

## Installation

### Clone the Repository
```bash
git clone <REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

### Run with Docker Compose
1. Ensure Docker is installed and running.
2. Launch the application with the following command:
   ```bash
   docker-compose up --build
   ```
3. The application will be accessible at:
   ```
   http://localhost:8000
   ```

## Local Execution (Optional)
If you prefer running the app locally without Docker:
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn numpy scipy python-multipart
   ```
2. Start the server:
   ```bash
   uvicorn compito:app --reload
   ```
3. Access the application at `http://127.0.0.1:8000`.

## Testing
You can easily test the endpoints using the interactive Swagger UI available at:
```
http://localhost:8000/docs
```

## endpoint exp

change file path !!!

curl -X POST "http://127.0.0.1:8000/average-score" -H "Content-Type: application/json" -d '{"name": "Alice", "scores": [85, 90, 78, 92]}'

curl -X GET "http://127.0.0.1:8000/top-subject?scores=85&scores=92&scores=78&subjects=Math&subjects=Science&subjects=History"

curl -X POST "http://127.0.0.1:8000/subject-statistics" -H "Content-Type: application/json" -d '{"subject": "Physics", "scores": [70, 85, 85, 90, 100]}'

curl -X POST "http://127.0.0.1:8000/count-word-in-file" -F "file=@C:\Users\aless\Desktop\evelina\project-evelina\data.txt" -F "word=Alice"

curl -X POST "http://127.0.0.1:8000/student-standard-deviation" -H "Content-Type: application/json" -d '{"name": "Maria", "scores": [88, 92, 75, 89]}'

curl -X POST "http://127.0.0.1:8000/compare-students" -H "Content-Type: application/json" -d '{"student1": {"name": "Luca", "scores": [85, 90, 78]}, "student2": {"name": "Giulia", "scores": [88, 92, 75]}}'

curl -X POST "http://127.0.0.1:8000/top-n-students" -H "Content-Type: application/json" -d '{ "students": [{"name": "Anna", "scores": [85, 90, 78]}, {"name": "Marco", "scores": [88, 92, 75]},{"name": "Sara", "scores": [70, 80, 65]}], "top_n": 2 }'

curl -X POST "http://127.0.0.1:8000/process-scores-csv" -F "file=@C:\Users\aless\Desktop\evelina\project-evelina\data.csv"