import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def setup_plot_style():
    plt.style.use('dark_background')
    sns.set_style("darkgrid", {
        'axes.facecolor': '#1a1b26',
        'figure.facecolor': '#1a1b26',
        'grid.color': '#2f3447',
        'text.color': 'white'
    })

def calculate_indicators(data):
    # Calculate EMA
    data['EMA_7'] = data['Close'].ewm(span=7, adjust=False).mean()
    data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
    
    # Calculate RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    return data

def create_analysis_image(analysis_result, market_data, lang_code='tg'):
    try:
        setup_plot_style()
        
        # Create figure with subplots
        fig = plt.figure(figsize=(12, 8))
        gs = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1], hspace=0.3)
        
        # Price and EMA plot
        ax1 = fig.add_subplot(gs[0])
        market_data = calculate_indicators(market_data)
        
        # Plot price
        ax1.plot(market_data.index, market_data['Close'], label='Price', color='white', linewidth=1)
        ax1.plot(market_data.index, market_data['EMA_7'], label='EMA 7', color='#00ff00', alpha=0.7)
        ax1.plot(market_data.index, market_data['EMA_21'], label='EMA 21', color='#ff6b6b', alpha=0.7)
        
        # RSI Plot
        ax2 = fig.add_subplot(gs[1])
        ax2.plot(market_data.index, market_data['RSI'], color='#5c87ff', linewidth=1)
        ax2.axhline(y=70, color='#ff6b6b', linestyle='--', alpha=0.5)
        ax2.axhline(y=30, color='#00ff00', linestyle='--', alpha=0.5)
        ax2.fill_between(market_data.index, market_data['RSI'], 70, 
                        where=(market_data['RSI'] >= 70), color='#ff6b6b', alpha=0.3)
        ax2.fill_between(market_data.index, market_data['RSI'], 30, 
                        where=(market_data['RSI'] <= 30), color='#00ff00', alpha=0.3)
        
        # MACD Plot
        ax3 = fig.add_subplot(gs[2])
        ax3.plot(market_data.index, market_data['MACD'], label='MACD', color='#5c87ff')
        ax3.plot(market_data.index, market_data['Signal_Line'], label='Signal', color='#ff6b6b')
        ax3.fill_between(market_data.index, market_data['MACD'] - market_data['Signal_Line'], 
                        0, alpha=0.3, color='#5c87ff')
        
        # Customize plots
        for ax in [ax1, ax2, ax3]:
            ax.grid(True, alpha=0.2)
            ax.set_facecolor('#1a1b26')
        
        # Add legends and labels
        ax1.legend(loc='upper left')
        ax3.legend(loc='upper left')
        
        # Language-specific labels
        labels = {
            'tg': {'price': 'Нарх', 'rsi': 'RSI', 'macd': 'MACD'},
            'ru': {'price': 'Цена', 'rsi': 'RSI', 'macd': 'MACD'},
            'uz': {'price': 'Narx', 'rsi': 'RSI', 'macd': 'MACD'},
            'kk': {'price': 'Баға', 'rsi': 'RSI', 'macd': 'MACD'},
            'en': {'price': 'Price', 'rsi': 'RSI', 'macd': 'MACD'}
        }
        
        current_labels = labels.get(lang_code, labels['en'])
        ax1.set_title(current_labels['price'], color='white', pad=10)
        ax2.set_title(current_labels['rsi'], color='white', pad=10)
        ax3.set_title(current_labels['macd'], color='white', pad=10)
        
        # Save plot
        plt.savefig('analysis_sample.png', dpi=100, bbox_inches='tight', facecolor='#1a1b26')
        plt.close()
        
        return True
        
    except Exception as e:
        logger.error(f"Error creating analysis image: {e}")
        return False
