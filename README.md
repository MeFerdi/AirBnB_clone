# Welcome to the AirBnB clone project!
A team project to build a clone of AirBnB(https://www.airbnb.com/)

# General concepts in review
As you navigate this code base, it is great to note the following concepts, while completing this project.

1.How to create a Python package

2.How to create a command interpreter in Python using the cmd module

3.What is Unit testing and how to implement it in a large project

4.How to serialize and deserialize a Class

5.How to write and read a JSON file

6.How to manage datetime

7.What is an UUID

8.What is *args and how to use it

9.What is **kwargs and how to use it

10.How to handle named arguments in a function

# Files and Directories

*models* directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
*console.py* file is the entry point of our command interpreter.
*models/base_model.py* file is the base class of all our models. It contains common elements:
*attributes*: id, created_at and updated_at
*methods*: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.
The project's implementation will happen in the following phases:

## Phase One
The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, I will:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of my future instances

create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

create the first abstracted storage engine of the project: File storage.

create all unittests to validate all our classes and storage engine

Create a data model

Manage (create, update, destroy, etc) objects via a console/command interpreter

Store and persist objects to files (JSON files)

# Description of the command interpreter
|Commands	|Description|
|-----|-----------------------------------------------------------------------------|
quit	Quits the console
Ctrl+D	Quits the console
help or help <command>	Displays all commands or Displays instructions for a specific command
create <class>	Creates an object of type , saves it to a JSON file, and prints the objects ID
show <class> <ID>	Shows string representation of an object
destroy <class> <ID>	Deletes an objects
all or all <class>	Prints all string representations of all objects or Prints all string representations of all objects of a specific class
update <class> <id> <attribute name> "<attribute value>"	Updates an object with a certain attribute (new or existing)
<class>.all()	Same as all <class>
<class>.count()	Retrieves the number of objects of a certain class
<class>.show(<ID>)	Same as show <class> <ID>
<class>.destroy(<ID>)	Same as destroy <class> <ID>
<class>.update(<ID>, <attribute name>, <attribute value>	Same as update <class> <ID> <attribute name> <attribute value>)
<class>.update(<ID>, <dictionary representation>)	Updates an objects based on a dictionary representation of attribute names and values

# General Execution
*Your shell should work like this in interactive mode:*

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
# Command Interpreter
The command interpreter is a Python-based tool that serves as the backend of the Airbnb clone. It allows users to interact with the platform through a command-line interface, performing various actions such as searching for accommodations, making bookings, managing listings, and more.

## How to Start
Clone the repository to your local machine:

### bash
Copy code
git clone https://github.com/MeFerdi/AirBnB_clone.git
Navigate to the project directory:

# bash
Copy code
cd airbnb_clone
Install any necessary dependencies:

Copy code
pip install -r requirements.txt
Run the command interpreter:

Copy code

python interpreter.py

# How to Use

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

# Authors
The following individuals have contributed to the development of this project:

Ferdynand Odhiambo <ferdinandodhis254@gmail.com>

Emmanuel Wesa <princewesa@gmail.com>