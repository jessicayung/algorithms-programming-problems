# Intro to Statistics
# Day 5: Correlation
from scipy import stats

# 5.1
# Find Pearson and Spearman correlation coefficients
a = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]  
b = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
print(stats.linregress(a, b)[2])
print(stats.spearmanr(a, b))

# 5.2 
# Find expected s when m = 80.
m = [95, 85, 80, 70, 60]z
s = [85, 95, 70, 65, 70]
print(stats.linregress(m,s)[1]+80*stats.linregress(m,s)[0])
