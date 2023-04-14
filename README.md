# DataFlow
DataFlow is a user-friendly, web-based data automation application that streamlines data processing tasks for businesses and individuals. It simplifies data importing, cleaning, transformation, and exporting while offering automation and scheduling features. Designed for scalability, DataFlow can handle growing data needs, making it a valuable tool for users in various industries who seek to increase efficiency and reduce manual work in their data processing tasks.

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Install Python and the necessary Python packages by running pip install -r backend/requirements.txt.
3. Install Julia and the necessary Julia packages by running julia install.jl.
4. Copy the .env.example file in the backend/ directory to .env and modify the environment variables as needed.
5. Initialize the Flask app by running flask run in the backend/ directory.
6. Install Node.js and the necessary Node.js packages by running npm install in the frontend/ directory.
7. Start the Vue.js app by running npm run serve in the frontend/ directory.

## Project Structure
The project is structured as follows:

```graphql
data-automation-app/
├── backend/
│   ├── app/                     # Flask application
│   │   ├── api/                 # API routes and logic
│   │   ├── data_processing/     # Data processing modules, including Julia code
│   │   ├── models/              # Database models
│   │   ├── utils/               # Utility functions and helpers
│   │   ├── __init__.py          # Flask app initialization
│   │   └── extensions.py        # Custom Flask extensions
│   ├── migrations/              # Database migrations
│   ├── tests/                   # Test files for the backend
│   ├── .env                     # Environment variables
│   ├── .flaskenv                # Flask-specific environment variables
│   ├── requirements.txt         # Backend dependencies
│   └── wsgi.py                  # Entry point for the backend app
├── frontend/
│   ├── src/                     # Vue.js source files
│   ├── public/                  # Public folder for static files
│   ├── package.json             # Frontend dependencies and scripts
│   └── vue.config.js            # Vue.js configuration file
├── vercel.json                  # Vercel configuration file
└── README.md                    # This README file
```

## API Routes
The following API routes are available:

- `/api/signup` - Signup a new user
- `/api/login` - Login an existing user
- `/api/import` - Import data into DataFlow
- `/api/export` - Export data from DataFlow
- `/api/clean` - Clean data using Julia functions
- `/api/transform` - Transform data using Julia functions
- `/api/integrate` - Integrate data with third-party tools using Julia functions
- `/api/schedule` - Schedule data processing tasks for automated execution
- `/api/user` - Manage user account information

## Data Processing
Data processing tasks are handled by Julia functions in the backend/app/data_processing/ directory. These functions can be called from Python using the PyJulia package. To add new data processing functions, create a new Julia file in the data_processing/ directory and add the functions to the __init__.py file.

## Contributing
To contribute to the project, follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch for your changes.