from pathlib import Path
from src.utils import get_michelin_star_data_path

# Create data seed file

NUMBER_OF_MICHELIN_STAR = 3
for i in range(1, NUMBER_OF_MICHELIN_STAR + 1):
  path = get_michelin_star_data_path(i)
  file = Path(path)
  file.touch(exist_ok=True)
  f = open(file)
