
# Sample Data Plotter

This is a Python GUI application for plotting data from a CSV file using `matplotlib`, `pandas`, and `tkinter`.

## Features

- Load a CSV file containing tabular data.
- Select X and Y columns to plot.
- Visualize the data using line plots.
- Simple and interactive graphical user interface.

## Requirements

- Python 3.x
- pandas
- matplotlib

You can install the required packages using pip:

```bash
pip install pandas matplotlib
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Use the GUI to:
   - Browse and load a CSV file.
   - Select columns for X and Y axes.
   - Click "Plot" to generate the graph.

## Notes

- Ensure the CSV file has a header row with column names.
- Columns with non-numeric data cannot be plotted on the Y axis.

## Example

A sample CSV file format:

```csv
Date,Value
2024-01-01,10
2024-01-02,15
2024-01-03,20
```

## License

This project is open source and available under the MIT License.
