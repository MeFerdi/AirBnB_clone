# Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## Command Interpreter
The command interpreter is a Python-based tool that serves as the backend of the Airbnb clone. It allows users to interact with the platform through a command-line interface, performing various actions such as searching for accommodations, making bookings, managing listings, and more.

## How to Start
Clone the repository to your local machine:

### bash
Copy code
git clone https://github.com/your_username/airbnb_clone.git
Navigate to the project directory:

### bash
Copy code
cd airbnb_clone
Install any necessary dependencies:

Copy code
pip install -r requirements.txt
Run the command interpreter:

Copy code
python interpreter.py
How to Use
Once the command interpreter is running, users can enter commands to interact with the Airbnb clone platform. Here are some common commands and their descriptions:

search <location>: Search for accommodations in the specified location.
book <listing_id> <check-in_date> <check-out_date>: Book a listing for the specified dates.
list: List all available accommodations.
...
For a full list of available commands and their usage, refer to the documentation or run help within the command interpreter.

Examples
Example 1: Searching for accommodations in Nairobi City

sql
Copy code
search Nairobi City
Example 2: Booking a listing with ID 123 for a stay from January 1st to January 7th

yaml
Copy code
book 123 2024-01-01 2024-01-07

## Authors
The following individuals have contributed to the development of this project:

Ferdynand Odhiambo<ferdinandodhis254@gmail.com>
Emmanuel Wesa<princewesa@gmail.com>