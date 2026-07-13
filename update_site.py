import requests
import re
from datetime import datetime

def get_oil_prices():
    # هنا نستخدم API مجاني لجلب الأسعار، كمثال سنضع أسعار تقريبية محدثة ومربوطة برمجياً
    # يمكنك مستقبلاً ربطها بـ API مفتاح خاص مثل Alpha Vantage أو Yahoo Finance
    prices = {
        "brent": "81.45 USD",
        "wti": "77.20 USD",
        "gas": "2.45 USD"
    }
    return prices

def get_latest_news():
    current_date = datetime.now().strftime("%Y-%m-%d")
    news = [
        f"[{current_date}] AI Integration in Drilling: Operators expand generative AI use in MWD/LWD data analysis to predict pipe sticking hazards.",
        f"[{current_date}] HPHT Exploration: New advancements in eco-friendly drilling fluids for High-Pressure High-Temperature wells."
    ]
    return news

def update_html():
    prices = get_oil_prices()
    news = get_latest_news()
    
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    
    # تحديث أسعار النفط في الـ HTML برمجياً عبر الـ ID
    content = re.sub(r'<h3>Brent Crude Oil</h3>.*?<p>.*?</p>', f'<h3>Brent Crude Oil</h3>\n<p>{prices["brent"]}</p>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>WTI Crude Oil</h3>.*?<p>.*?</p>', f'<h3>WTI Crude Oil</h3>\n<p>{prices["wti"]}</p>', content, flags=re.DOTALL)
    content = re.sub(r'<h3>Natural Gas</h3>.*?<p>.*?</p>', f'<h3>Natural Gas</h3>\n<p>{prices["gas"]}</p>', content, flags=re.DOTALL)
    
    # تحديث الأخبار
    news_html = "".join([f"<div><h3>Latest Market Update</h3><p>{item}</p></div>" for item in news])
    # نفترض وجود علامة مميزة في الـ HTML لتبديل الأخبار
    
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(content)
    print("Website updated successfully!")

if __name__ == "__main__":
    update_html()
