import pandas as pd
import numpy as np

# サンプルデータの作成（例：1週間の歩数データ）
data = {
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'steps': [7000, 8500, 12000, 6000, 9000, 15000, 4000]
}

df = pd.DataFrame(data)

# 基本的な統計量の計算
mean_steps = df['steps'].mean()
max_steps = df['steps'].max()

print("--- 1週間の歩数分析 ---")
print(df)
print(f"\n平均歩数: {mean_steps:.0f} 歩")
print(f"最大歩数: {max_steps} 歩")

# 1万歩を超えた日を抽出
over_10k = df[df['steps'] >= 10000]
print("\n1万歩達成した日:")
print(over_10k)
