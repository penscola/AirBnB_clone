# AirBnB clone - The console

## Description
This repository contains a group project,AirBnB clone, for the ALX SE programme.
The task is to build a clone of the popular AirBnB website.
This first task is to create a the base classes for data modelling and a command-line interface to handle the data.

## Installation

* Clone this repository: `git clone "https://github.com/penscola/AirBnB_clone"`
* Run hbnb(interactively): `./console <command>`
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Usage
The console can be run in both interactive mode and non-interactive mode.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Show help for a command | ```(hbnb) help <command>```
Create an object| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```
Destroy an object | ```(hbnb) destroy <class> <id>```

Working in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
all  count  create  destroy  help  quit  show  update
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
```

## Files

File | Description 
---- | ----------- 
[base_model.py](./models/base_model.py) | Super class defining base model
[user.py](./models/user.py) | User class models user information
[amenity.py](./models/amenity.py) | Amenity class models amenity information
[city.py](./models/city.py) | City class models location information
[state.py](./models/state.py) | State class models location information
[place.py](./models/place.py) | Place class models accomodation information
[review.py](./models/review.py) | Review class models user/host review information
[file_storage.py](./models/engine/file_storage.py) | Handles serialization and deserialization of objects

## Authors

- [Felix Kiprotic](https://github.com/penscola)
- [Azzeddine Naceur](https://github.com/azeadrr)
