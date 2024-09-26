class StockAnalyzer:
        def __init__(self, price, roe, roce, pe, market_cap):
                self.price = float(price)
                self.roe = float(roe)
                self.roce = float(roce)
                self.pe = float(pe)
                self.market_cap = float(market_cap)

        def analyze(self):
                recommendations = []
                
                # Basic thresholds for evaluation
                roe_threshold = 15  # Return on Equity should be at least 15%
                roce_threshold = 15  # Return on Capital Employed should be at least 15%
                pe_threshold = 20  # Price to Earnings ratio should be less than 20
                market_cap_threshold = 1000  # Market capitalization in crores
                
                # Evaluate each metric
                if self.roe >= roe_threshold:
                    recommendations.append("Good ROE")
                else:
                    recommendations.append("Low ROE")
                
                if self.roce >= roce_threshold:
                    recommendations.append("Good ROCE")
                else:
                    recommendations.append("Low ROCE")
                
                if self.pe <= pe_threshold:
                    recommendations.append("Reasonable P/E ratio")
                else:
                    recommendations.append("High P/E ratio")
                
                if self.market_cap >= market_cap_threshold:
                    recommendations.append("Large Market Cap")
                else:
                    recommendations.append("Small Market Cap")
                
                # Decision making based on the metrics
                good_metrics_count = sum([
                    self.roe >= roe_threshold,
                    self.roce >= roce_threshold,
                    self.market_cap >= market_cap_threshold
                ])
                
                if self.pe <= pe_threshold and good_metrics_count >= 2:
                    return "Buy", recommendations
                else:
                    return "Do not buy", recommendations
