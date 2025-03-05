from flask import Flask, jsonify, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)

base_path = os.path.join(os.getcwd(), 'data')
df_equity = pd.read_csv(os.path.join(base_path, 'EQUITY-Complete.csv'))
df_mutualfund = pd.read_csv(os.path.join(base_path, 'MUTUALFUND-Complete.csv'))
df_crypto = pd.read_csv(os.path.join(base_path, 'CryptoCurrency-Complete.csv'))
df_currency = pd.read_csv(os.path.join(base_path, 'Currency-Complete.csv'))
df_indices = pd.read_csv(os.path.join(base_path, 'INDICES-Complete.csv'))
df_futures = pd.read_csv(os.path.join(base_path, 'Futures-Data-Complete.csv'))
df_etf = pd.read_csv(os.path.join(base_path, 'ETF-Data-Complete.csv'))

# ================= FRONTEND ROUTES =================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/equity')
def equity_page():
    return render_template('equity.html')

@app.route('/mutualfund')
def mutualfund_page():
    return render_template('mutualfund.html')

@app.route('/crypto')
def crypto_page():
    return render_template('crypto.html')

@app.route('/currency')
def currency_page():
    return render_template('currency.html')

@app.route('/indices')
def indices_page():
    return render_template('indices.html')

@app.route('/futures')
def futures_page():
    return render_template('futures.html')

@app.route('/etf')
def etf_page():
    return render_template('etf.html')

@app.route('/research')
def research_page():
    return render_template('research.html')

# ================= API ROUTES =================
@app.route('/api/equity', methods=['GET'])
def get_equity():
    exchange = request.args.get('exchange')
    if exchange:
        filtered_df = df_equity[df_equity['Exchange'] == exchange]
    else:
        filtered_df = df_equity
    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/api/mutualfund', methods=['GET'])
def get_mutualfund():
    exchange = request.args.get('exchange')
    if exchange:
        filtered_df = df_mutualfund[df_mutualfund['Exchange'] == exchange]
    else:
        filtered_df = df_mutualfund
    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/api/crypto', methods=['GET'])
def get_crypto():
    
    return jsonify(df_crypto.to_dict(orient='records'))

@app.route('/api/currency', methods=['GET'])
def get_currency():
    
    return jsonify(df_currency.to_dict(orient='records'))

@app.route('/api/indices', methods=['GET'])
def get_indices():
    exchange = request.args.get('exchange')
    if exchange:
        filtered_df = df_indices[df_indices['Exchange'] == exchange]
    else:
        filtered_df = df_indices
    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/api/futures', methods=['GET'])
def get_futures():
    exchange = request.args.get('exchange')
    if exchange:
        filtered_df = df_futures[df_futures['Exchange'] == exchange]
    else:
        filtered_df = df_futures
    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/api/etf', methods=['GET'])
def get_etf():
    exchange = request.args.get('exchange')
    if exchange:
        filtered_df = df_etf[df_etf['Exchange'] == exchange]
    else:
        filtered_df = df_etf
    return jsonify(filtered_df.to_dict(orient='records'))

# Route to demonstrate file download (e.g., a PDF)
@app.route('/api/download-paper', methods=['GET'])
def download_paper():
    paper_path = os.path.join(os.getcwd(), 'ResearchPaper.pdf')
    return send_file(paper_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
