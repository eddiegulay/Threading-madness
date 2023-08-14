from mad_thread import *


dataset = pd.read_csv("your_dataset.csv")  # Change to your file path

search_column = "column_name_to_search"
search_item = "item_to_search"
num_threads = 10

search_results = parallel_search(search_column, search_item, dataset, num_threads)
if search_results:
    print("Search result found:")
    print(search_results[0])
else:
    print("Search result not found.")