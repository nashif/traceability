#!/usr/bin/env python3

import csv
import sys
import argparse

HEADER = """
/**
@page Requirements
@tableofcontents
@section Requirements

"""

FOOTER = """
*/
"""


args = None

def parse_csv(filename):
    grouped = dict()
    with open(filename) as fp:
            cr = csv.DictReader(fp)
            for row in cr:
                group = row['group']
                if row['normative'] == "FALSE":
                    continue
                if not grouped.get(group, None):
                    grouped[group] = []

                uid = row.get('uid')
                text = row.get('text').rstrip()
                name = row.get('header').rstrip()
                grouped[group].append({'id': uid, 'req': text, 'name': name})
    return grouped

def write_dox(grouped, filename="requirements.dox"):
    with open(filename, "w") as req:
        req.write(HEADER)

        for r in grouped.keys():
            comp = grouped[r]
            req.write("\n@section {}\n\n".format(r))
            for c in comp:
                req.write("@subsection {} {}: {}\n{}\n\n\n".format(c['id'], c['id'], c['name'], c['req']))

        req.write(FOOTER)


def parse_args():
    parser = argparse.ArgumentParser(
                description="Generate Requirement in various formats.")

    parser.add_argument('-c', '--csv-file',
            help="Requirements file in CSV format")

    parser.add_argument('-d', '--dox-file',
            help="Output file in DOX format for Doxygen.")

    return parser.parse_args()

def main():
    global args
    args = parse_args()

    grouped = dict()
    if args.csv_file:
        print("Parsing CSV file...")
        grouped = parse_csv(args.csv_file)

    if grouped:
        if args.dox_file is not None:
            print(f"Writing DOX file {args.dox_file}...")
            write_dox(grouped, args.dox_file)
        else:
            print("No output file given...")
    else:
        print("Nothing to do...")

if __name__ == "__main__":
    main()



