# (ง •_•)ง Multi-Threaded Dataset Search Script  

This Python script allows you to search through a large dataset using multiple threads for improved performance. You can specify the column and the item you want to search for. The script uses the `pandas` library for efficient data loading and manipulation.

## Prerequisites

- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

1. Place your dataset file in the same directory as the script or provide the correct path to your dataset file.
2. Modify the script as needed to customize the search operation.

### Configuration

Open the script file (`multi_threaded_search.py`) in a text editor and modify the following parameters:

- `search_column`: The name of the column you want to search in.
- `search_item`: The item you want to search for.
- `num_threads`: The number of threads you want to use for the search.

### Running the Script

```bash
python multi_threaded_search.py
