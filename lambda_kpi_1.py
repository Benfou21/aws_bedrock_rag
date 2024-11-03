
import json
import yfinance as yf
import pandas as pd

# Fonction pour récupérer les informations du ticker
def get_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    indicators = {
        "Country": info.get('country'),
        "Industry": info.get('industry'),
        "Sector": info.get('sector'),
        "Summary": info.get('longBusinessSummary'),
        "Full-Time Employees": info.get('fullTimeEmployees'),
        "DividendYield": info.get('dividendYield'),
        "Payout Ratio": info.get('payoutRatio'),
        "Five year avg dividend": info.get('fiveYearAvgDividendYield'),
        "Beta": info.get('beta'),
        "TrailingPE": info.get('trailingPE'),
        "Forward PE": info.get('forwardPE'),
        "Volume": info.get('volume')
    }
    # Convertir les informations en DataFrame pour les formater en texte
    df = pd.DataFrame(list(indicators.items()), columns=["Indicator", "Value"])
    return df.to_string(index=False)


# Fonction Lambda principale
def lambda_handler(event, context):

    print("Événement reçu:", json.dumps(event, indent=2))

    # Extraire les paramètres de l'événement
    parameters = event.get('parameters', [])
        
    param_dict = {param['name'].lower(): param['value'] for param in parameters if 'name' in param and 'value' in param}
    
    # Extraire les valeurs en utilisant `param_dict.get`
    ticker_symbol = param_dict.get('ticker', 'AAPL')
    
    function = event.get('function', 'get_info')
    actionGroup = event.get('actionGroup', 'Finance')

    # Appeler get_info avec le ticker et obtenir le résultat formaté
    info_text = get_info(ticker_symbol)

    # Construction de la réponse pour le body du texte
    responseBody = {
        "TEXT": {
            "body": f"Les informations pour le ticker '{ticker_symbol}' sont les suivantes :\n{info_text}"
        }
    }

    # Réponse d'action
    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    # Structure de la réponse finale
    response = {'response': action_response, 'messageVersion': event.get('messageVersion', '1.0')}
    print("Response:", response)

    return response
