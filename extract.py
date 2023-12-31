"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.reader(infile)
        # Skip header (first row)
        next(reader)
        for row in reader:
            # Extract necessary info
            designation = row[3]
            name = row[4]
            diameter = row[15]
            hazardous = True if row[7].lower() == 'y' else False
            
            # Instantiate NEO
            neo = NearEarthObject(designation, name=name, diameter=diameter, \
                                hazardous=hazardous)
            
            # Append to the list
            neos.append(neo)
            
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    CAObjs = []
    with open(cad_json_path, 'r') as infile:
        # Load json file to Python obj
        cad = json.load(infile)
        # Some necessary attributes in "fields"
        fieldsAttr = ['des', 'cd', 'dist', 'v_rel']
        # Find corresponding idexes of these fieldsAttr
        AttIdx = [cad['fields'].index(attr) for attr in fieldsAttr]
        
        for data in cad['data']:
            # Extract data corresponding fields attribute indexes 
            # Then initiate CloseApproach() obj
            ca = CloseApproach(designation=data[AttIdx[0]], time=data[AttIdx[1]], \
                            distance=data[AttIdx[2]], velocity=data[AttIdx[3]])
            # Append the CloseApproach() obj to the list
            CAObjs.append(ca)
    return CAObjs
