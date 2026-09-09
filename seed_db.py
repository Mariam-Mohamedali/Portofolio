import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import Project, Skill, Certificate

def run_seed():
    print("Clearing old data...")
    Project.objects.all().delete()
    Skill.objects.all().delete()
    Certificate.objects.all().delete()
    
    print("Seeding Projects...")
    projects_data = [
        {
            "title": "Women for a Man Recipes",
            "description": "High-end recipe management platform built with Django. It combines a premium UI with a robust backend to provide users with a seamless experience for discovering, sharing, and managing Middle Eastern and international culinary delights.",
            "tech_stack": "Django, Python, HTML, CSS, JavaScript, MySQL",
            "category": "django",
            "start_date": "March 2026",
            "end_date": "May 2026",
            "featured": True,
            "order": 1,
            "github_url": "https://github.com/mariammohamedali127/Women-for-a-man-recipes"
        },
        {
            "title": "SCCI Season 26 Platform",
            "description": "Built the official SCCI Season 26 website — fully responsive, serving as the central hub for all student events and activities. Bridges the gap between academic technical life and the practical market.",
            "tech_stack": "HTML, CSS, JavaScript, PHP, MySQL",
            "category": "frontend",
            "start_date": "January 2026",
            "end_date": "April 2026",
            "featured": True,
            "order": 2,
            "github_url": "https://github.com/mariammohamedali127/SCCI-Platform"
        },
        {
            "title": "Smart Finance",
            "description": "Full-stack web application empowering women with personal finance management tools: budgeting, expense tracking, and smart financial insights.",
            "tech_stack": "Django, Python, HTML, CSS, JavaScript, MySQL",
            "category": "django",
            "start_date": "January 2026",
            "end_date": "April 2026",
            "featured": True,
            "order": 3,
            "github_url": "https://github.com/mariammohamedali127/Smart-Finance"
        },
        {
            "title": "Mafioso Game",
            "description": "Console-based detective game built with Java, applying OOP principles across multiple classes (Suspect, Crime, Crime Game). Demonstrates strong Java and object-oriented design skills.",
            "tech_stack": "Java, OOP",
            "category": "java",
            "start_date": "March 2026",
            "end_date": "",
            "featured": False,
            "order": 4,
            "github_url": "https://github.com/mariammohamedali127/Mafioso-Game"
        },
        {
            "title": "Audio Player",
            "description": "Functional audio player with play, pause, and track navigation — demonstrates C++ systems programming proficiency.",
            "tech_stack": "C++",
            "category": "cpp",
            "start_date": "May 2025",
            "end_date": "",
            "featured": False,
            "order": 5,
            "github_url": "https://github.com/mariammohamedali127/Audio-Player"
        }
    ]
    
    for p in projects_data:
        Project.objects.create(**p)

    print("Seeding Certificates...")
    certs_data = [
        {"title": "Deep Learning Certificate", "issuer": "NVIDIA Deep Learning Institute", "date": "September 2025", "order": 1},
        {"title": "Machine Learning Certificate (90 hrs)", "issuer": "National Telecommunications Institute (NTI)", "date": "September 2025", "order": 2},
        {"title": "Project Achievement Certificate", "issuer": "SCCI Season 26", "date": "February 2026", "order": 3},
    ]
    for c in certs_data:
        Certificate.objects.create(**c)

    print("Seeding Skills...")
    skills_data = [
        {"name": "Python", "category": "language", "percentage": 90},
        {"name": "Java", "category": "language", "percentage": 85},
        {"name": "C++", "category": "language", "percentage": 80},
        {"name": "JavaScript", "category": "language", "percentage": 85},
        {"name": "Django", "category": "backend", "percentage": 95},
        {"name": "PHP", "category": "backend", "percentage": 75},
        {"name": "HTML & CSS", "category": "frontend", "percentage": 90},
        {"name": "MySQL", "category": "database", "percentage": 85},
        {"name": "Figma", "category": "tools", "percentage": 75},
        {"name": "Git & GitHub", "category": "tools", "percentage": 90},
    ]
    for s in skills_data:
        Skill.objects.create(**s)
        
    print("Seeding complete! 🚀")

if __name__ == '__main__':
    run_seed()
