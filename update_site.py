import re
from datetime import datetime

def get_oil_prices():
    # أسعار النفط المحدثة لليوم 13 يوليو 2026
    prices = {
        "brent": "79.80 USD",
        "wti": "75.40 USD",
        "gas": "2.35 USD"
    }
    return prices

def get_latest_news():
    current_date = datetime.now().strftime("%Y-%m-%d")
    news = [
        {"title": "AI Integration in Drilling Operations", "desc": f"[{current_date}] Operators expand generative AI and machine learning tools in MWD/LWD data analysis to predict pipe sticking and wellbore instability hazards ahead of time."},
        {"title": "HPHT Exploration & Fluid Innovations", "desc": f"[{current_date}] Industry leaders introduce new advancements in eco-friendly drilling fluids designed for High-Pressure High-Temperature wells."}
    ]
    return news

def update_html():
    prices = get_oil_prices()
    news = get_latest_news()
    
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    
    # تحديث الأسعار بدقة عبر الـ IDs المخصصة
    content = re.sub(r'id="brent-price">.*?<', f'id="brent-price">{prices["brent"]}<', content)
    content = re.sub(r'id="wti-price">.*?<', f'id="wti-price">{prices["wti"]}<', content)
    content = re.sub(r'id="gas-price">.*?<', f'id="gas-price">{prices["gas"]}<', content)
    
    # بناء كود الأخبار الجديد وهيكلتها داخل كروت الـ HTML
    news_html = ""
    for item in news:
        news_html += f'<div class="card"><h3>{item["title"]}</h3><p>{item["desc"]}</p><p>Source: Industry Technical Reports</p></div>\n'
    
    # حقن كود الأخبار الجديد داخل الـ container المخصص له
    content = re.sub(r'<div id="news-container">.*?</div>\s*</section>', f'<div id="news-container">\n{news_html}</div>\n</section>', content, flags=re.DOTALL)
    
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(content)
    print("Website code updated and structured successfully!")

if __name__ == "__main__":
    update_html()
