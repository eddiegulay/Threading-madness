import threading
import pandas as pd

# This function is used to search for a specific item in a column of a dataset
def search_thread(start_idx, end_idx, search_column, search_item, dataset, result_holder, thread_event):
    for idx in range(start_idx, end_idx):
        if thread_event.is_set():
            return
        if dataset.loc[idx, search_column] == search_item:
            result_holder.append(dataset.iloc[idx])
            thread_event.set()  # Signal other threads to stop
            return

def parallel_search(search_column, search_item, dataset, num_threads=10):
    dataset_size = len(dataset)
    chunk_size = dataset_size // num_threads
    
    result_holder = []
    thread_event = threading.Event()  # Event to signal threads to stop
    
    threads = []
    
    # Create and start the threads
    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else dataset_size
        thread = threading.Thread(target=search_thread, args=(start_idx, end_idx, search_column, search_item, dataset, result_holder, thread_event))
        thread.start()
        threads.append(thread)
    
    # Wait for any thread to finish
    for thread in threads:
        thread.join()
    
    return result_holder