import yfinance as yf
import pandas as pd

ticker = yf.Ticker("EMP")

def get_info(ticker):
    info = ticker.info
    indicators = {
    "Country": info.get('country'),
    "Industry": info.get('industryKey'),
    "Sector": info.get('sectorKey'),
    "Summary": info.get('longBusinessSummary'),
    "Full-Time Employees": info.get('fullTimeEmployees'),
    "DividendYield": info.get('dividendYield'),
    "Payout Ratio": info.get('payoutRatio'),
    "Five year avg dividend": info.get('fiveYearAvgDividendYield'),
    "Beta": info.get('beta'),
    "TrailingPE": info.get('trailingPE'),
    "forward PE": info.get('forwardPE'),
    "Volume": info.get('volume'),
    "Book value": info.get('bookValue'),
    "Price to book": info.get('priceToBook'),
    "Total Cash": info.get('totalCash'),
    "Total Cash par Share": info.get('totalCashPerShare'),
    "EBITDA": info.get('ebitda'),
    "Total Debt": info.get('totalDebt'),
    "Quick ratio": info.get('quickRatio'),
    "Current Ratio": info.get('currentRatio'),
    "Total Revenue": info.get('totalRevenue'),
    "Debt to Equity": info.get('debtToEquity'),
    "Revenue Per Share": info.get('revenuePerShare'),
    "Return on Asset": info.get('returnOnAssets'),
    "Return on Equity": info.get('returnOnEquity'),
    "Free Cash Flow": info.get('freeCashflow'),
    "Operating Cash Flow": info.get('operatingCashflow'),
    "Earnings Growth": info.get('earningsGrowth'),
    "Revenue Growth": info.get('revenueGrowth'),
    "Gross Margins": info.get('grossMargins'),
    "EBIT Margins": info.get('ebitMargins'),
    "Operating Margins": info.get('operatingMargins')
    }
    df = pd.DataFrame(list(indicators.items()), columns=["Indicator", "Value"])
    return df


def get_major_news(ticker):
    pass

def get_rapport(ticker):
    # Récupérer les informations des rapports
    info_sec = ticker.sec_filings
    
    # Initialiser des listes pour stocker les données des rapports
    data_8k = []
    data_10k = []
    
    # Parcourir chaque entrée dans les filings
    for i in info_sec:
        date = i.get('date')
        
        # Ajouter les rapports 8-K et 10-K à leurs listes respectives
        if i['type'] == '8-K':
            data_8k.append({
                'Date': date,
                '8-K': i['exhibits']['8-K']
            })
        elif i['type'] == '10-K':
            data_10k.append({
                'Date': date,
                '10-K': i['exhibits']['10-K']
            })
    
    # Convertir les listes en DataFrames
    df_8k = pd.DataFrame(data_8k)
    df_10k = pd.DataFrame(data_10k)
    
    # Convertir les dates en format DateTime et trier chaque DataFrame par date
    df_8k['Date'] = pd.to_datetime(df_8k['Date'])
    df_10k['Date'] = pd.to_datetime(df_10k['Date'])
    df_8k.sort_values(by='Date', inplace=True)
    df_10k.sort_values(by='Date', inplace=True)
    
    return df_8k, df_10k


print(get_info(ticker))
# print(get_rapport(ticker)[0])