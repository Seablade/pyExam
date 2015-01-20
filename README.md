Python Exam Script
==================

The purpose of this script is just to simplify building worksheets and exams using latex to render the final documents.

Example:
--------
python exam.py worksheets/thea334.1-2.yaml --answers | pdflatex --output-directory=build

This will build the thea332.1-2.yaml document into a latex document with outputting answers enabled, and then pipe that output into pdflatex to build the actual pdf, and put the output into the build directory.

Don't forget if using virtualenv to `source bin/activate`.

Requisites
----------
To be installed by pip:

pyyaml
jinja2

