# Times Series Visualization
# Line Types
# Plot Types
# Subplots
import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv('../Dataset/Pandas Foundations/sp500.csv', parse_dates=True, index_col='Date')
print(sp500.head())
# sp500['Close'].plot()
# plt.ylabel('Closing Price (US Dollars)')
# plt.show()
########### One Week ###############
# Style Format String
	# Color (k:black)
	# marker (.:dot)
	# linetype: - (solid)
sp500.loc['2015-4-1':'2015-4-7','Close'].plot(style='k.-',title='S&P500')
plt.ylabel('Closing Price (US Dollars)')
# plt.show()
# More Plot Styles
# COLOR  |  MARKER  |  LINE
# b:blue |  o:circle|  : dotted
# g:green|  *:start |  - dashed
# r:red  |  s:square|  : dotted
# c:cyan |  + plus  |  

# Area Plot
sp500['Close'].plot(kind='area', title='S&P500')
plt.ylabel('Closing Price (US Dollars)')
#plt.show()

# Multiple Columns
sp500.loc['2015', ['Close','Volume']].plot(title = 'S&P500')

# Subplots
sp500.loc['2015', ['Close', 'Volume']].plot(subplots = True)
plt.show()