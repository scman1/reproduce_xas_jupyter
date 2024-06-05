# Example of how to use nbparameterise
import nbclient
import nbformat
from nbparameterise import (
    extract_parameters, replace_definitions, parameter_values
)

with open("Fibonacci.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

# Get a list of Parameter objects
orig_parameters = extract_parameters(nb)

# Update one or more parameters
params = parameter_values(orig_parameters, N=25)

# Make a notebook object with these definitions
new_nb = replace_definitions(nb, params)

# Execute the notebook with the new parameters
nbclient.execute(new_nb)