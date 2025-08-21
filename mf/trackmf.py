from flask import Flask, render_template
import pandas as pd
from mftool import Mftool

app = Flask(__name__)

class MutualFundTracker:
    def __init__(self):
        self.mf = Mftool()

    def get_fund_nav(self, fund_id):
        try:
            nav_data = self.mf.get_scheme_quote(fund_id)
            return nav_data
        except Exception as e:
            return {"error": str(e)}

@app.route('/')
def home():
    tracker = MutualFundTracker()
    active_fund_ids = ['118469', '118419', '118834','127042' ,'152651', '122639', '102920', '153198' ,'119788', '149775']
    inactive_fund_ids = ['125305', '118537', '119826', '119063', '152584', '119648', '120586', '152712', '145552', '152651', '120826']

    active_funds_data = []
    for fund_id in active_fund_ids:
        data = tracker.get_fund_nav(fund_id)
        if 'error' not in data:
            active_funds_data.append({
                'scheme_name': data['scheme_name'],
                'nav': data['nav'],
                'date': data['last_updated']
            })

    inactive_funds_data = []
    for fund_id in inactive_fund_ids:
        data = tracker.get_fund_nav(fund_id)
        if 'error' not in data:
            inactive_funds_data.append({
                'scheme_name': data.get('scheme_name'),
                'nav': data.get('nav'),
                'date': data.get('last_updated')
            })

    return render_template('index.html', active_funds_data=active_funds_data, inactive_funds_data=inactive_funds_data)

if __name__ == '__main__':
    app.run(debug=True)