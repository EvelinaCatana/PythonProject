## endpoint exp

change file path 

curl -X POST "http://127.0.0.1:8000/average-score" -H "Content-Type: application/json" -d '{"name": "Alice", "scores": [85, 90, 78, 92]}'

curl -X GET "http://127.0.0.1:8000/top-subject?scores=85&scores=92&scores=78&subjects=Math&subjects=Science&subjects=History"

curl -X POST "http://127.0.0.1:8000/subject-statistics" -H "Content-Type: application/json" -d '{"subject": "Physics", "scores": [70, 85, 85, 90, 100]}'

curl -X POST "http://127.0.0.1:8000/count-word-in-file" -F "file=@C:\Users\aless\Desktop\evelina\project-evelina\data.txt" -F "word=Alice"

curl -X POST "http://127.0.0.1:8000/student-standard-deviation" -H "Content-Type: application/json" -d '{"name": "Maria", "scores": [88, 92, 75, 89]}'

curl -X POST "http://127.0.0.1:8000/compare-students" -H "Content-Type: application/json" -d '{"student1": {"name": "Luca", "scores": [85, 90, 78]}, "student2": {"name": "Giulia", "scores": [88, 92, 75]}}'

curl -X POST "http://127.0.0.1:8000/top-n-students" -H "Content-Type: application/json" -d '{ "students": [{"name": "Anna", "scores": [85, 90, 78]}, {"name": "Marco", "scores": [88, 92, 75]},{"name": "Sara", "scores": [70, 80, 65]}], "top_n": 2 }'

curl -X POST "http://127.0.0.1:8000/process-scores-csv" -F "file=@C:\Users\aless\Desktop\evelina\project-evelina\data.csv"