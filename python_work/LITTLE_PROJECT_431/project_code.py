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

col_names = ['RIAGENDR', 'RIDRETH3', 'ALQ111',
             'ALQ130','BPQ020', 'BPQ050A',
             'DIQ010', 'SMQ020', 'SMQ040',
             'PAQ605', 'PAQ620']

merged[col_names] = merged[col_names].astype('category')

print('First five rows of data:')
print(merged.head())

print('\nOverall summary of data:')
print(merged.describe().T)

print('\nThe skewness of the data(> 0 right skew, < 0 left skew):')
print(merged.skew(numeric_only = True))

print('\nMissing value statistics:')
miss_value = merged.isnull().sum()
miss_ratio = miss_value / len(merged) * 100
miss_df = pd.DataFrame({
    'Number_of_missing_values': miss_value,
    'Ratio_of_missing_values': miss_ratio.round(2)
    }).sort_values('Ratio_of_missing_values', ascending = False)

plt.figure(figsize = (12, 6))
sns.heatmap(merged.isnull(), cbar = False, cmap = 'Blues', yticklabels = False)
plt.xticks(rotation = 45)
plt.title('Missing value distribution heat map', pad = 20)
plt.show()

dupli_value = merged.duplicated().sum()
print(dupli_value)
print(merged.columns)

num_cols = merged.select_dtypes(include = 'float')
plt.figure(figsize = (15, 10))

for i, col in enumerate(num_cols.columns, 1):
    plt.subplot(2, 3, i)
    sns.histplot(merged[col], kde = True, color = 'skyblue', bins = 40)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title(f'The distribution of {col}')
    if col == 'SEQN':
        plt.xticks(rotation = 45)


plt.tight_layout()
plt.show()

category_cols = merged.select_dtypes(include = 'category')

plt.figure(figsize = (15, 10))
for i, col in enumerate(category_cols.columns, 1):
    plt.subplot(4, 3, i)
    sns.countplot(data = merged, x = col)
    plt.grid(color = '#E0E0E0', linestyle = '--', alpha = 0.7)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if col == 'ALQ130':
        plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

corr = merged.corr()
plt.figure(figsize = (14, 9))
sns.heatmap(corr, annot = True, cmap = 'coolwarm', fmt = '.2f', linewidths = 0.5)
plt.title('Variable correlation heatmap', pad = 20)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

num_cols = merged.select_dtypes(include = 'float')
corr = num_cols.corr()
plt.figure(figsize = (14, 9))
sns.heatmap(corr, annot = True, cmap = 'coolwarm', fmt = '.2f', linewidths = 0.5)
plt.title('Numerical variable correlation heatmap', pad = 20)
plt.tight_layout()
plt.show()

plt.figure(figsize = (15, 6))
for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(y = merged[col])
    plt.title(f'Outlier detection of {col}')
plt.tight_layout()
plt.show()
