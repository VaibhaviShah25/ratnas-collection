# 👗 Ratna's Collection

**Ratna's Collection** is an e-commerce web application developed using Django, aimed at supporting and showcasing a small clothing business. The project is designed with a clean UI, product listing, cart management, and an order flow (payment integration pending). The business is actively run by my mother, and this website serves as its digital storefront.

---

## 🚀 Features

- 🛍️ Product Listings with images and prices  
- 🛒 Add to Cart and View Cart functionality  
- 📦 Order placement system  
- 🧾 Order history tracking (admin side)  
- 👩‍💼 Admin product management via Django Admin  
- 💻 Responsive design for mobile and desktop  
- ✉️ Contact form and About page  
- 🔒 Secure user login & registration system  
- 📂 Dynamic content rendering using Django templates  

> ⚠️ Payment gateway integration (Razorpay) is in progress

---

## 🏗️ Tech Stack

| Frontend  | Backend | Database  | Hosting           |
|-----------|---------|-----------|--------------------|
| HTML/CSS  | Django  | SQLite    | [PythonAnywhere](https://www.pythonanywhere.com) |

---

## 📁 Folder Structure
myproject1/
├── clotheweb/ # Main app (views, models, templates)
├── ratnascollection/ # Project config (settings, urls)
├── static/ # Static files (CSS, JS, Images)
├── templates/ # HTML templates
├── db.sqlite3 # SQLite database
└── manage.py



---

## 🔧 Installation (Local Development)

bash
# Clone the repo
git clone https://github.com/<your-github-username>/ratnascollection.git
cd ratnascollection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run the server
python manage.py runserver


🙋‍♀️ About the Business
This is a real-world project developed for my mom’s clothing business. It's an effort to bring local entrepreneurship online and make Indian prints collections accessible to a wider audience.


🧑‍💻 Developer
Vaibhavi Shah
C++ & Python Developer
AI/ML Enthusiast
Full Stack Learner
LinkedIn (https://www.linkedin.com/in/vaibhavi-shah-594335269/)
