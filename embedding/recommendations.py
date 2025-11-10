import pandas as pd
from Levenshtein import distance
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path

test_parquet_path = Path(r'C:\Users\abuud\Desktop\cw-aneng-project\seeds\kaggle-steam-data-2\steam_games_parquet_files\parquet_output_2_extras_with_names\10.parquet')
df = pd.read_parquet(test_parquet_path, engine='auto')

df.head(2)