from fredapi import Fred
import matplotlib.pyplot as plt

# Replace 'your_api_key_here' with your actual FRED API key
fred = Fred(api_key='d66de7c5af7a46d06db6324d625f9052')

# Retrieve economic data series
GDP = fred.get_series('GDP')
Inflation = fred.get_series('CPIAUCSL')
Growth_rate = fred.get_series('A191RL1Q225SBEA')
Federal_Funds_Rate = fred.get_series('FEDFUNDS')
VIX = fred.get_series('VIXCLS')
Personal_Consumption_Expenditures = fred.get_series('PCE')
Private_Investment = fred.get_series('GPDIC1')
Unemployment_Rate = fred.get_series('UNRATE')
Y_Treasury_Yield = fred.get_series('DGS10')
M2_Money_Supply = fred.get_series('M2SL')
Industrial_Production = fred.get_series('INDPRO')
Housing_Starts = fred.get_series('HOUST')
Consumer_Confidence = fred.get_series('UMCSENT')

# Create a dictionary for all data series
data_series = {
    'Gross Domestic Product (GDP)': GDP,
    'Inflation (CPI)': Inflation,
    'Real GDP Growth Rate': Growth_rate,
    'Federal Funds Rate': Federal_Funds_Rate,
    'CBOE Volatility Index (VIX)': VIX,
    'Personal Consumption Expenditures (PCE)': Personal_Consumption_Expenditures,
    'Private Fixed Investment (Gross)': Private_Investment,
    'Unemployment Rate': Unemployment_Rate,
    '10-Year Treasury Yield': Y_Treasury_Yield,
    'M2 Money Supply': M2_Money_Supply,
    'Industrial Production Index': Industrial_Production,
    'Housing Starts': Housing_Starts,
    'Consumer Sentiment Index': Consumer_Confidence
}

# Define colors for each plot
colors = ['blue', 'orange', 'green', 'red', 'purple', 'blue', 'brown', 'darkblue',
          'darkgreen', 'teal', 'darkred', 'gray', 'pink']

# Create a 5x3 grid layout to accommodate 13 subplots
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(18, 22))
fig.suptitle("Key Economic Indicators", fontsize=20)

# Flatten the axes array for easier indexing
axes = axes.flatten()

# Plot each indicator
for i, (title, series) in enumerate(data_series.items()):
    axes[i].plot(series, color=colors[i])
    axes[i].set_title(title)
    axes[i].set_xlabel("Date")
    axes[i].set_ylabel("Value")

# Hide any extra subplots if there are empty slots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Adjust layout for better spacing
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
