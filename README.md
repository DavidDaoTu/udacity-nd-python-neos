# udacity-nd-python-neos
Udacity Nano Degree: Near-Earth Objects

## Project Rubric
### I. Functionality
1. Produce classes that represent near-Earth objects and their close approaches. (Task 1: models.py file)

The NearEarthObject class represents a near-Earth object.
- The constructor assigns attributes for:
    + **designation**: The NEO’s primary designation.
    + **name**: The NEO’s IAU name (could be empty, or None)
    + **diameter**: The NEO’s diameter, in kilometers, or NaN.
    + **hazardous**: Whether the NEO is potentially hazardous
    + **approaches**: A collection of this NEO’s CloseApproaches (initially an empty collection). 

The CloseApproach class represents a close approach to Earth by an NEO.
- The constructor assigns attributes for:
    + **time**: The date and time, in UTC, at which the NEO passes closest to Earth.
    + **distance**: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
    + **velocity**: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
    + **neo**: A reference to the NearEarthObject that is making the close approach (initially None).

An additional attribute, to store the NEO’s primary designation before the CloseApproach is linked to its NearEarthObject
Additionally, each of these classes should implement a __str__ method that produces a human-readable description of the contents of the object.

2. Load data from CSV and JSON files into Python objects. (Task 2a: extract.py and database.py)
3. Link together Python objects and any required metadata in a database wrapper that supports basic inspection. (Task 2b: extract.py and database.py)
4. Convert user-specified criteria to a collection of filters. (Task 3a)
5. Query the collection of CloseApproach with a collection of filters. (Task 3b)
6. Limit the values produced by an iterator to at most a maximum number. (Task 3c)
7. Write data from Python to CSV files or JSON files. (Task 4)
8. Produce error-free code.


### II. Style (Mechanics)
1. Produce Python code that satisfies PEP 8.
2. Write Python comments that satisfy PEP 257.
3. Submit code free from starter code markings.


### III. Style (Design)
1. Divide attributes appropriately among the NearEarthObject class and the CloseApproach class.
2. Attach functionality to classes only when appropriate.
3. Design a coherent system to filter objects by user-specified criteria.
4. Consume and produce streams of data as iterables.