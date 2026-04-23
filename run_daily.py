from app.analysis import get_top_stocks
from app.db import save_results

data = get_top_stocks()
save_results(data)
print("Done")