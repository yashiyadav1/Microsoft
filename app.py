from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    skills = [
        {"name": "Python", "icon": "🐍"},
        {"name": "Java", "icon": "☕"},
        {"name": "C++", "icon": "➕"},
        {"name": "JavaScript", "icon": "🌐"},
        {"name": "React.js", "icon": "⚛️"},
        {"name": "Node.js", "icon": "🟩"},
        {"name": "TensorFlow", "icon": "🧠"},
        {"name": "NumPy", "icon": "🔢"},
        {"name": "Pandas", "icon": "🐼"},
        {"name": "NLTK", "icon": "🗣️"},
        {"name": "PyTorch", "icon": "🔥"},
        {"name": "scikit-learn", "icon": "🧪"},
        {"name": "Azure", "icon": "☁️"},
        {"name": "Docker", "icon": "🐳"},
        {"name": "Kubernetes", "icon": "⚓"},
        {"name": "GitOps", "icon": "🔄"},
        {"name": "ArgoCD", "icon": "🚢"},
        {"name": "Git", "icon": "🐙"},
        {"name": "Gitea", "icon": "🌿"},
        {"name": "FastAPI", "icon": "⚡"},
        {"name": "RESTful APIs", "icon": "🔗"},
        {"name": "Microservices", "icon": "🔬"},
        {"name": "SQL", "icon": "🗃️"},
        {"name": "MongoDB", "icon": "🍃"},
        {"name": "PostgreSQL", "icon": "🐘"},
        {"name": "PowerBI", "icon": "📊"},
        {"name": "Linux", "icon": "🐧"},
        {"name": "UNIX", "icon": "🖥️"},
        {"name": "Windows", "icon": "🪟"}
    ]
    
    projects = [
        {
            "title": "Adaptive Reading Companion (ARC)",
            "description": "Chrome extension for bionic reading and text assistance, using NLP techniques.",
            "link": "#"
        },
        {
            "title": "Jerry: The Virtual Assistant",
            "description": "AI-powered voice assistant using ChatGPT API and PyTorch for voice recognition.",
            "link": "#"
        },
        {
            "title": "Hateful Speech Classification",
            "description": "Content moderation system using CNN and BERT models, achieving 93.50% accuracy.",
            "link": "#"
        },
        {
            "title": "ASL Recognition",
            "description": "Real-time hand gesture recognition using CNN and LSTM for video-based ASL.",
            "link": "#"
        }
    ]

    experience = [
        {
            "date": "May 2024 - Present",
            "title": "Software QA Intern",
            "company": "Nokia, Sunnyvale, CA",
            "description": "Developed RESTful API using FastAPI for XR Edge Cloud management. Implemented AI model deployment POC in microservices architecture.",
            "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-500"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>'
        },
        {
            "date": "August 2023 - December 2024",
            "title": "Graduate Research Assistant",
            "company": "Purdue University Fort Wayne, IN",
            "description": "Designed and implemented a deep learning model for steganographic applications using TensorFlow. Developed custom DWT-based convolutional layer, improving image hiding capacity by 30%.",
            "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-green-500"><path d="M10 2v7.31"></path><path d="M14 9.3V1.99"></path><path d="M8.5 2h7"></path><path d="M14 9.3a6.5 6.5 0 1 1-4 0"></path><path d="M5.58 16.5h12.85"></path></svg>'
        },
        {
            "date": "May 2022 – August 2022",
            "title": "D365 Developer Intern",
            "company": "Vera Bradley, Roanoke, IN",
            "description": "Enhanced Microsoft Dynamics 365 by resolving ITR/Bugs backlogs. Designed Power Automate Flows for alerts on critical Batch Jobs in D365.",
            "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-500"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>'
        }
    ]

    education = [
        {
            "date": "August 2023 - December 2024",
            "degree": "Master of Science in Computer Science",
            "school": "Purdue University, Fort Wayne, IN",
            "description": "Relevant Coursework: Applications of Deep Learning, Database Design and Systems, Analysis of Algorithms, Quantum Computing, Full Stack Development, Machine Learning",
            "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-red-500"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>'
        },
        {
            "date": "May 2023",
            "degree": "Bachelor of Science in Computer Science",
            "school": "Purdue University, Fort Wayne, IN",
            "description": "Minor: Mathematics. Awards: Dean's and Semester's Honors List 2021, 2022 | Top 50 Award Recipient | Honor's Pin recipient, 2022",
            "icon": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-red-500"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>'
        }
    ]
    
    return render_template('index.html', skills=skills, projects=projects, experience=experience, education=education)

if __name__ == '__main__':
    app.run(debug=True)