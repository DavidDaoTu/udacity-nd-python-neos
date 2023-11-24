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

The **load_neos** function loads NEO data from a CSV file.

    + The function opens the given file for reading.
    + The function uses the ***csv*** module to parse the file contents into a standard Python data structure (e.g. list, dict, etc).
    + The function converts this raw data into a collection of ***NearEarthObjects***
    + The function returns a collection of ***NearEarthObjects***

The **load_approaches** method loads close approach data from a JSON file.

    + The function opens the given file for reading.
    + The function uses the json module to parse the file contents into a dict.
    + The function converts this raw data into a collection of CloseApproach objects.
    + The function returns a collection of CloseApproach objects.
Data from the extraneous columns (CSV) and fields (JSON) shouldn’t be bound to the constructed NearEarthObjects and CloseApproaches.




3. Link together Python objects and any required metadata in a database wrapper that supports basic inspection. (Task 2b: extract.py and database.py)

The NEODatabase constructor captures and preprocesses a collection of NEOs and close approaches.

    + The constructor captures and saves its arguments, a collection of NearEarthObject and a collection of CloseApproaches.
    + The constructor precomputes auxiliary data structures to assist with the get_neo_by_designation and get_neo_by_name methods.
    + At the end of the constructor, the .neo attribute is set on each close approach to the matching NearEarthObject.
    + At the end of the constructor, the .approaches attribute is populated for each NearEarthObject with a collection of its close approaches.
    + The get_neo_by_designation method fetches an NEO by its primary designation, or returns None if no matches are found.
    + The get_neo_by_name method fetches an NEO by its name, or returns None if no matches are found.



4. Convert user-specified criteria to a collection of filters. (Task 3a: filters.py)

The **create_filters** function produces a collection that can be used by the query method to perform a search of close approaches.

    + The function respects the --date filter mode.
    + The function respects the --start-date filter mode.
    + The function respects the --end-date filter mode.
    + The function respects the --min-distance filter mode.
    + The function respects the --max-distance filter mode.
    + The function respects the --min-velocity filter mode.
    + The function respects the --max-velocity filter mode.
    + The function respects the --min-diameter filter mode.
    + The function respects the --max-diameter filter mode.
    + The function respects the --hazardous and --not-hazardous filter modes.
The filters accurately produce results based on the user-specified options.



5. Query the collection of CloseApproach with a collection of filters. (Task 3b: database.py)

The NEODatabase’s query method generates a stream of CloseApproaches that match the filters returned by create_filters.

    + A CloseApproach is generated if and only if it passes all predicates.
    + The method generates a stream of matching results, and doesn’t precompute all matching results up front.



6. Limit the values produced by an iterator to at most a maximum number. (Task 3c: filters.py)

The limit function slices an iterator to its first n elements, at most.

    + The function is correct even if the first argument isn’t an in-memory buffered aggregate data type (i.e. list, tuple, etc). That is, the function doesn’t slice directly into the iterator.
    + The function doesn’t limit the results if the second argument is 0 or None.


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