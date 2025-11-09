import pandas as pd
from Levenshtein import distance
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import numpy as np

df = pd.read_csv