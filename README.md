 🛠️ Flask & MongoDB Atlas Integration Project

A beginnerfriendly fullstack project that uses Flask as the backend and MongoDB Atlas as the cloud database. This app features a frontend form that stores user data to the cloud and an API endpoint that returns data from a JSON file.



 📌 Features

 /api route that serves a JSON list from a backend file (data.json)
 Form submission to MongoDB Atlas
 Redirect to a success page after successful submission
 Inline error message handling if form submission fails



 🧰 Technologies Used

 Python 3.x
 Flask
 PyMongo
 MongoDB Atlas (Cloud NoSQL DB)
 HTML (Jinja2 templating)



 🗂️ Project Structure



flask\_mongo\_project/
│
├── app.py                  Flask backend
├── data.json               Static backend data
├── requirements.txt        Python dependencies
└── templates/
├── form.html           HTML form page
└── success.html        Success message page





 ⚙️ Setup Instructions

 1. Clone the Repository
bash
git clone https://github.com/yourusername/flask_mongo_project.git
cd flask_mongo_project


 2. Install Dependencies

bash
pip install r requirements.txt


 3. Set Up MongoDB Atlas

 Create a free cluster at [mongodb.com](https://www.mongodb.com/)
 Whitelist your IP and create a database user
 Copy your connection string and replace it in app.py:

python
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/flaskdb?retryWrites=true&w=majority")


 4. Run the Flask App

bash
python app.py


 Access the form: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
 Access the API: [http://127.0.0.1:5000/api](http://127.0.0.1:5000/api)


 ✅ What's Included

 Clean and minimal codebase
 Cloudconnected MongoDB integration
 Form with both success and error feedback
 Easily customizable for larger projects



 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and improve the code.



