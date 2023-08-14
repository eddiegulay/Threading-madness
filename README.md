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
```

The script will output whether the search item was found or not, and if found, it will display the corresponding row(s) from the dataset.


# Important Notes
This script is designed for searching through large datasets using multiple threads. Keep in mind that the effectiveness of multi-threading depends on the nature of the search operation and the dataset size.
Carefully review and test the script for your specific use case before deployment.
The script assumes that the dataset is in CSV format. If your dataset is in a different format, modify the data loading part accordingly. (sorry though, I'm too lazy to do it for you 😪)

# Author
- [Eddie Gulay](eddiegulay.me)

For question and support please contact me at [edgargulay@outlook.com](mailto:edgargulay@outlook.com) or [on X(twitter) @eddiegulay]

