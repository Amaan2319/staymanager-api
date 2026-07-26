import time
from functools import wraps

def time_logger(func):
  @wraps(func)
  def wrapper(*args,**kwargs):
    start_time = time.perf_counter()
    
    func(*args,**kwargs)
    
    end_time = time.perf_counter()
    
    exec_time = end_time-start_time
    
    print(f"function {func.__name__} took {exec_time:.6f} seconds to run.")
  return wrapper  