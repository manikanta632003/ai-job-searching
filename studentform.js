import React, { useState } from 'react';
import axios from 'axios';

function StudentForm() {
  const [skills, setSkills] = useState("");

  const submitStudent = () => {
    axios.post("http://localhost:5000/add_student", {
      name: "John Doe",
      email: "john@example.com",
      programming_skills: skills.split(",")
    }).then(res => alert("Student Added"));
  };

  return (
    <div>
      <h3>Enter Skills</h3>
      <input onChange={e => setSkills(e.target.value)} placeholder="Python, Java" />
      <button onClick={submitStudent}>Submit</button>
    </div>
  );
}

export default StudentForm;
