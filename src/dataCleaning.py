import pandas as pd
import numpy as np

try:
    df = pd.read_csv('2026_MCM_Problem_C_Data.csv')
    print("成功加载原始数据")
except FileNotFoundError:
    print("未找到文件，请检查文件名")
df.replace('N/A', np.nan, inplace=True)
for w in range(1, 12):
    score_cols = [f'week{w}_judge{j}_score' for j in range(1, 5)]
    df[score_cols] = df[score_cols].apply(pd.to_numeric, errors='coerce')
    temp_scores = df[score_cols].replace(0, np.nan)
    df[f'week{w}_avg_score'] = temp_scores.mean(axis=1)
industry_dummies = pd.get_dummies(df['celebrity_industry'], prefix='ind')
df_cleaned = pd.concat([df, industry_dummies], axis=1)
df_cleaned.to_csv('dataCleaning.csv', index=False)

print("--- 数据清洗完成 ---")
print("原始文件：2026_MCM_Problem_C_Data.csv(未变动)")
print("新文件：dataCleaning.csv(已生成)")