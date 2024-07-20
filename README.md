<h1 align="center">Fairy Cake Blog</h1>

<p align="center">
  <img src="http://www.fairycakeblog.social/landingpage" alt="Logo">
</p>

<p align="center">
  A blog website for cake enthusiasts, built with Python, Flask, and SQLAlchemy.
</p>

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **User Authentication**: Register, log in securely.
- **Create and Edit Posts**: Write and manage your cake blogs.
- **Profile Management**: Update your information easily.
- **About Page**: Learn about the website and its purpose.

---

## Technologies Used

- **Backend**: Python, Flask, Flask SQLAlchemy
- **Frontend**: HTML, CSS
- **Database**: SQLite (for development)

---

## Installation

1. Clone the repository: 
    git clone https://github.com/samarelshamey/FairyCakeBlog.git
2. Create a virtual environment and activate it: 
    python -m venv venv
    source venv/bin/activate (on Windows use venv\Scripts\activate)
3. Install dependencies:
    pip install -r requirements.txt
4. Set up the database:
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
5. Run the application:
    flask run
6. Open your browser and go to `http://localhost:5000` to view the website.

## Usage

- **Register**: Create a new account.
- **Log In**: Access your account with your credentials.
- **Create Post**: Share your cake experiences.
- **Edit Profile**: Update your information.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## Authors

- [Samar Elshamy](https://github.com/samarelshamey) - Developer

---