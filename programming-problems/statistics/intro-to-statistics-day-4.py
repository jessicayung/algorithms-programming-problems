# Intro to Statistics
# Day 4: Normal Distribution and The Central Limit Theorem

from scipy import stats

# 4.1
# Given X ~ N(30,4)
# P(X < 40) = P(Z < (40-30)/4) = P(Z < 2.5)
# P(X > 21) = P(X < 39) = P(Z < 9/4) = P(Z < 2.25)
# P(30 < X < 35) = P(X < 35) - P(X > 30) = P(Z < 5/4) - P(Z < 0)

nd = stats.norm(30,4)
print(nd.cdf(35)-nd.cdf(30))

# 4.2: Similar

# 4.3
# Find P(X < 9800), where X = 49Y, Y ~ N(205,15).
# X ~ N(49*205, 49*15^2)
nd = stats.norm(49*205, sqrt(49*225))
print(nd.cdf(9800))

# 4.4
# X ~ N(2.4,2.0)
# Y = 100X => Y ~ N(240, 20)
# Find P(Y =< 250)
nd = stats.norm(240,20)
print(nd.cdf(250))