from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

students = []
jobs = []

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added"}), 200

@app.route('/add_job', methods=['POST'])
def add_job():
    data = request.json
    jobs.append(data)
    return jsonify({"message": "Job added"}), 200

@app.route('/match_jobs', methods=['POST'])
def match_jobs():
    student_skills = request.json['skills']
    job_descriptions = [", ".join(job['required_skills']) for job in jobs]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([", ".join(student_skills)] + job_descriptions)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    matches = sorted(zip(jobs, similarities), key=lambda x: x[1], reverse=True)
    top_matches = [{"job": match[0], "score": round(match[1], 2)} for match in matches[:5]]
    return jsonify(top_matches), 200

if __name__ == '__main__':
    app.run(debug=True)
