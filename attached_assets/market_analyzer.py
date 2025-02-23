import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
import time
from config import MESSAGES

TIMEFRAMES = [1, 5, 15, 30, 60]  # Added 60-minute timeframe
logger = logging.getLogger(__name__)

class MarketAnalyzer:
    def __init__(self, symbol):
        self.symbol = symbol
        self.error_messages = MESSAGES['tg']['ERRORS']
        logger.info(f"Initialized MarketAnalyzer for {symbol}")

    def set_language(self, lang_code):
        self.error_messages = MESSAGES[lang_code]['ERRORS']
        logger.info(f"Language set to {lang_code}")

    def calculate_ema(self, data, period):
        return data.ewm(span=period, adjust=False).mean()

    def calculate_rsi(self, data, period=14):
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_macd(self, data):
        exp1 = data.ewm(span=12, adjust=False).mean()
        exp2 = data.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        return macd, signal

    def calculate_bollinger_bands(self, data, period=20):
        sma = data.rolling(window=period).mean()
        std = data.rolling(window=period).std()
        upper_band = sma + (std * 2)
        lower_band = sma - (std * 2)
        return upper_band, lower_band

    def get_market_data(self, minutes=60):  # Increased default timeframe
        try:
            end_time = datetime.now()
            start_time = end_time - timedelta(minutes=minutes * 2)

            try:
                ticker = yf.Ticker(self.symbol)
                df = ticker.history(start=start_time, end=end_time, interval='1m')

                if df.empty or not all(col in df.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume']):
                    return None, self.error_messages['NO_DATA']

                df = df.reset_index()
                if 'Datetime' not in df.columns:
                    return None, self.error_messages['NO_DATA']

                df.set_index('Datetime', inplace=True)
                return df.tail(minutes), None

            except Exception as e:
                logger.error(f"Error fetching data: {str(e)}")
                return None, self.error_messages['TIMEOUT_ERROR']

        except Exception as e:
            logger.error(f"Critical error: {str(e)}")
            return None, self.error_messages['GENERAL_ERROR']

    def analyze_timeframe(self, df, minutes):
        if df is None or len(df) < minutes:
            return 'NEUTRAL', 0, {'confidence': 50, 'expiration': minutes}, None

        try:
            recent_data = df.tail(minutes)
            close_prices = recent_data['Close']
            volume = recent_data['Volume']

            # Enhanced Technical Indicators
            ema_7 = self.calculate_ema(close_prices, 7)
            ema_21 = self.calculate_ema(close_prices, 21)
            ema_50 = self.calculate_ema(close_prices, 50)  # Added longer EMA
            rsi = self.calculate_rsi(close_prices)
            macd, macd_signal = self.calculate_macd(close_prices)
            upper_band, lower_band = self.calculate_bollinger_bands(close_prices)

            # Price Analysis
            start_price = close_prices.iloc[0]
            end_price = close_prices.iloc[-1]
            price_change = ((end_price - start_price) / start_price) * 100

            # Volume Analysis
            avg_volume = volume.mean()
            current_volume = volume.iloc[-1]
            volume_ratio = current_volume / avg_volume
            volume_strength = (
                3 if volume_ratio > 2.0 else
                2 if volume_ratio > 1.5 else
                1 if volume_ratio > 1.0 else
                0
            )

            # Trend Analysis
            trend_signals = []

            # EMA Signals
            if ema_7.iloc[-1] > ema_21.iloc[-1] > ema_50.iloc[-1]:
                trend_signals.append(2)  # Strong uptrend
            elif ema_7.iloc[-1] < ema_21.iloc[-1] < ema_50.iloc[-1]:
                trend_signals.append(-2)  # Strong downtrend
            elif ema_7.iloc[-1] > ema_21.iloc[-1]:
                trend_signals.append(1)  # Moderate uptrend
            elif ema_7.iloc[-1] < ema_21.iloc[-1]:
                trend_signals.append(-1)  # Moderate downtrend

            # MACD Signal
            if macd.iloc[-1] > macd_signal.iloc[-1] and macd.iloc[-1] > 0:
                trend_signals.append(2)
            elif macd.iloc[-1] < macd_signal.iloc[-1] and macd.iloc[-1] < 0:
                trend_signals.append(-2)

            # Bollinger Bands Signal
            if close_prices.iloc[-1] < lower_band.iloc[-1]:
                trend_signals.append(1)  # Potential oversold
            elif close_prices.iloc[-1] > upper_band.iloc[-1]:
                trend_signals.append(-1)  # Potential overbought

            # RSI Signal
            last_rsi = rsi.iloc[-1]
            if last_rsi < 30:
                trend_signals.append(2)  # Oversold
            elif last_rsi > 70:
                trend_signals.append(-2)  # Overbought
            elif 30 <= last_rsi <= 45:
                trend_signals.append(1)  # Approaching oversold
            elif 55 <= last_rsi <= 70:
                trend_signals.append(-1)  # Approaching overbought

            # Calculate overall trend strength
            trend_strength = sum(trend_signals)

            # Volume impact
            trend_strength *= (1 + (volume_strength * 0.2))

            # Signal determination with more granular confidence
            if abs(trend_strength) >= 4:
                confidence = min(95, 75 + (abs(trend_strength) - 4) * 5)
                signal = 'BUY' if trend_strength > 0 else 'SELL'
            elif abs(trend_strength) >= 2:
                confidence = min(75, 60 + (abs(trend_strength) - 2) * 5)
                signal = 'BUY' if trend_strength > 0 else 'SELL'
            else:
                confidence = 50
                signal = 'NEUTRAL'

            indicators = {
                'confidence': round(confidence, 1),
                'expiration': minutes,
                'trend_strength': trend_strength,
                'volume_strength': volume_strength,
                'rsi': round(last_rsi, 2),
                'macd': round(macd.iloc[-1], 4),
                'bb_position': 'oversold' if close_prices.iloc[-1] < lower_band.iloc[-1] else 
                             'overbought' if close_prices.iloc[-1] > upper_band.iloc[-1] else 'normal'
            }

            return signal, price_change, indicators, None

        except Exception as e:
            logger.error(f"Analysis error: {str(e)}")
            return 'NEUTRAL', 0, {'confidence': 50, 'expiration': minutes}, str(e)

    def analyze_market(self):
        try:
            logger.info(f"Starting market analysis for {self.symbol}")
            df, error_message = self.get_market_data(minutes=max(TIMEFRAMES) + 5)
            if error_message:
                logger.error(f"Market data error for {self.symbol}: {error_message}")
                return {'error': error_message}

            if df is None or df.empty:
                logger.error(f"No market data available for {self.symbol}")
                return {'error': self.error_messages['NO_DATA']}

            current_price = df['Close'].iloc[-1]
            timeframe_analysis = {}

            for minutes in TIMEFRAMES:
                logger.info(f"Analyzing {minutes}min timeframe for {self.symbol}")
                signal, change, indicators, error = self.analyze_timeframe(df, minutes)
                if error:
                    logger.error(f"Error analyzing {minutes}min timeframe: {error}")

                timeframe_analysis[minutes] = {
                    'signal': signal,
                    'change': change,
                    'indicators': indicators
                }
                logger.info(f"{minutes}min analysis complete - Signal: {signal}, Change: {change:.2f}%")

            return {
                'current_price': current_price,
                'timeframes': timeframe_analysis,
                'timestamp': datetime.now()
            }

        except Exception as e:
            logger.error(f"Market analysis error for {self.symbol}: {str(e)}")
            return {'error': self.error_messages['GENERAL_ERROR']}