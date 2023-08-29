"""Script to get dataset sorted on the average time to discovery.

Example
-------

> python scripts/get_plot.py

or

> python scripts/get_plot.py -s asreview_files -o plot.png


Authors
-------
- Teijema, Jelle
"""

# version {{ version }}

import argparse
from pathlib import Path

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from asreview import open_state

def apd_plot():


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Generate an APD plot from the collected state files."
    )
    parser.add_argument(
        "-s",
        type=str,
        help="States location")
    parser.add_argument(
        "-o",
        type=str,
        help="Output location")
    args = parser.parse_args()

    # load states
    states = Path(args.s).glob("*.asreview")

    # check if states are found
    if len(list(states)) == 0:
        raise FileNotFoundError(f"No state files found in {args.s}")

    # generate plot and save results
    apd_plot(states, args.o)
