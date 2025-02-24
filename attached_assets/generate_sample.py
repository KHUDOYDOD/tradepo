import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

def create_analysis_image(analysis_result, market_data, lang_code='tg'):
    try:
        # Create figure and axis
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8), height_ratios=[3, 1, 1])
        fig.subplots_adjust(hspace=0.3)

        # Plot price data
        dates = market_data.index
        ax1.plot(dates, market_data['Close'], label='Price', color='blue', linewidth=1)

        # Add EMA lines
        ema_7 = market_data['Close'].ewm(span=7, adjust=False).mean()
        ema_21 = market_data['Close'].ewm(span=21, adjust=False).mean()
        ax1.plot(dates, ema_7, label='EMA 7', color='orange', linewidth=0.8)
        ax1.plot(dates, ema_21, label='EMA 21', color='red', linewidth=0.8)

        # Add Bollinger Bands
        sma = market_data['Close'].rolling(window=20).mean()
        std = market_data['Close'].rolling(window=20).std()
        upper_band = sma + (std * 2)
        lower_band = sma - (std * 2)
        ax1.fill_between(dates, upper_band, lower_band, alpha=0.1, color='gray')
        ax1.plot(dates, upper_band, color='gray', linestyle='--', alpha=0.5)
        ax1.plot(dates, lower_band, color='gray', linestyle='--', alpha=0.5)

        # Customize price chart
        ax1.set_title('Price Analysis', fontsize=10)
        ax1.legend(loc='upper left', fontsize=8)
        ax1.grid(True, alpha=0.3)

        # Plot RSI
        rsi = analysis_result['timeframes'][5]['indicators'].get('rsi', 50)
        rsi_data = market_data['Close'].diff()
        gain = (rsi_data.where(rsi_data > 0, 0)).rolling(window=14).mean()
        loss = (-rsi_data.where(rsi_data < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi_series = 100 - (100 / (1 + rs))

        ax2.plot(dates, rsi_series, color='purple', linewidth=1)
        ax2.axhline(y=70, color='r', linestyle='--', alpha=0.3)
        ax2.axhline(y=30, color='g', linestyle='--', alpha=0.3)
        ax2.fill_between(dates, 70, 30, alpha=0.1, color='gray')
        ax2.set_title('RSI', fontsize=10)
        ax2.grid(True, alpha=0.3)

        # Plot MACD
        exp1 = market_data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = market_data['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        ax3.plot(dates, macd, label='MACD', color='blue', linewidth=1)
        ax3.plot(dates, signal, label='Signal', color='red', linewidth=1)
        ax3.bar(dates, histogram, color=['green' if h > 0 else 'red' for h in histogram], alpha=0.3)
        ax3.set_title('MACD', fontsize=10)
        ax3.legend(loc='upper left', fontsize=8)
        ax3.grid(True, alpha=0.3)

        # Format x-axis
        for ax in [ax1, ax2, ax3]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            plt.setp(ax.get_xticklabels(), rotation=45)

        # Save the plot
        plt.savefig('analysis_sample.png', dpi=300, bbox_inches='tight')
        plt.close()
        return True

    except Exception as e:
        print(f"Error generating chart: {str(e)}")
        return False
