import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

demo = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_DEMO.xpt")
bmx = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_BMX.xpt")
alq = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_ALQ.xpt")
bpq = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_BPQ.xpt")
diq = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_DIQ.xpt")
smq = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_SMQ.xpt")
paq = pd.read_sas("C:/Users/李溥阳/Desktop/project_431/dataset/P_PAQ.xpt")

demo_cols = ["SEQN", "RIDAGEYR", "RIAGENDR", "RIDRETH3", "DMDEDUC2", "INDFMPIR"]
bmx_cols = ["SEQN", "BMXBMI", "BMXWAIST"]
alq_cols = ["SEQN", "ALQ111", "ALQ130"]
bpq_cols = ["SEQN", "BPQ020", "BPQ050A"]
diq_cols = ["SEQN", "DIQ010"]
smq_cols = ["SEQN", "SMQ020", "SMQ040"]
paq_cols = ["SEQN", "PAQ605", "PAQ620"]

demo_sel = demo[demo_cols]
bmx_sel = bmx[bmx_cols]
alq_sel = alq[alq_cols]
bpq_sel = bpq[bpq_cols]
diq_sel = diq[diq_cols]
smq_sel = smq[smq_cols]
paq_sel = paq[paq_cols]

merged = demo_sel.merge(bmx_sel, on="SEQN", how="inner")
merged = merged.merge(alq_sel, on="SEQN", how="inner")
merged = merged.merge(bpq_sel, on="SEQN", how="inner")
merged = merged.merge(diq_sel, on="SEQN", how="inner")
merged = merged.merge(smq_sel, on="SEQN", how="inner")
merged = merged.merge(paq_sel, on="SEQN", how="inner")

print('First five rows of data:')
print(merged.head())

print('\nOverall summary of data:')
print(merged.describe().T)

merged['RIDAGEYR'] = merged['RIDAGEYR'].astype('category')
merged['RIAGENDR'] = merged['RIAGENDR'].astype('category')
merged['RIDRETH3'] = merged['RIDRETH3'].astype('category')
merged['BMXWAIST'] = merged['BMXWAIST'].astype('category')
merged['ALQ111'] = merged['ALQ111'].astype('category')
merged['ALQ130'] = merged['ALQ130'].astype('category')
merged['BPQ020'] = merged['BPQ020'].astype('category')
merged['BPQ050A'] = merged['BPQ050A'].astype('category')
merged['DIQ010'] = merged['DIQ010'].astype('category')
merged['SMQ020'] = merged['SMQ020'].astype('category')
merged['SMQ040'] = merged['SMQ040'].astype('category')
merged['PAQ605'] = merged['PAQ605'].astype('category')
merged['PAQ620'] = merged['PAQ620'].astype('category')
