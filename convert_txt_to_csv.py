import pandas as pd

read_file = pd.read_csv (r'Kidney_Sample_Annotations.txt',sep="\t")
read_file.to_csv (r'Kidney_Sample_Annotations.txt', index=None)
