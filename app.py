from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Portfolio data
portfolio_data = {
    "name": "Alex Rivera",
    "title": "Creative Developer & Designer",
    "bio": "Crafting digital experiences that blend aesthetics with functionality",
    "projects": [
        {
            "id": 1,
            "title": "Digital Canvas",
            "category": "Web Design",
            "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=400&h=300&fit=crop",
            "description": "An interactive web platform for digital artists"
        },
        {
            "id": 2,
            "title": "Motion Lab",
            "category": "Animation",
            "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=400&h=300&fit=crop",
            "description": "Experimental motion graphics and interactive animations"
        },
        {
            "id": 3,
            "title": "Brand Identity",
            "category": "Branding",
            "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=400&h=300&fit=crop",
            "description": "Complete brand identity system for tech startup"
        },
        {
            "id": 4,
            "title": "Mobile Experience",
            "category": "UI/UX",
            "image": "https://images.unsplash.com/photo-1512941691920-25bde7360e5d?w=400&h=300&fit=crop",
            "description": "Intuitive mobile app design and development"
        },
        {
            "id": 5,
            "title": "Data Visualization",
            "category": "Development",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop",
            "description": "Interactive dashboards and data visualization tools"
        },
        {
            "id": 6,
            "title": "E-Commerce Platform",
            "category": "Development",
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=300&fit=crop",
            "description": "Full-stack e-commerce solution with modern features"
        }
    ],
    "skills": ["Web Design", "UI/UX", "JavaScript", "Python", "React", "CSS Animation", "Branding", "Motion Graphics"],
    "social": {
        "twitter": "https://twitter.com",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "instagram": "https://instagram.com"
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=portfolio_data['projects'])

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/projects')
def api_projects():
    return jsonify(portfolio_data['projects'])

@app.route('/api/portfolio')
def api_portfolio():
    return jsonify(portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
