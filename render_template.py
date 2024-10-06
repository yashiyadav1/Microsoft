from jinja2 import Environment, FileSystemLoader
from app import app, skills, projects, experience, education

# Load templates from the 'templates' directory
env = Environment(loader=FileSystemLoader('templates'))

# Get the template
template = env.get_template('index.html')

# Render the template with your data
with app.app_context():
    rendered_html = template.render(
        skills=skills,
        projects=projects,
        experience=experience,
        education=education
    )

# Write the rendered HTML to a file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print("index.html has been generated.")
