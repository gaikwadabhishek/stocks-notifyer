from nsetools import Nse
import time
import smtplib, ssl
import datetime
 
currentDT = datetime.datetime.now()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "abhishekgaikwadstocks@gmail.com"  # Enter your address
receiver_email = "abhishekgaikwadstocks@gmail.com"  # Enter receiver address
password = 'All!swell'
context = ssl.create_default_context()

nse = Nse()

stocks_low = {
	'JSWSTEEL' : 145,
	'SBIN': 190,
	'AXISBANK' : 295,
	'HDFCBANK' : 745,
	'ICICIBANK' : 275,
	'RELIANCE' : 1030,
	'TATASTEEL' : 255,
	'UNIONBANK' : 25,
	'TATAMOTORS' : 65,
	'TATASTEEL' : 255,
	'KOTAKBANK' : 1050,
	'INDUSINDBK' : 250,
	'JINDALSTEL' : 85,
	'MARUTI' : 4500,
	'ZEEL' : 127,
	'INFY' : 550,
	'WIPRO' : 165,
	'IRCTC' : 800,
	'ULTRACEMCO' : 3160
}
stocks_now = {}
stocks_list = ['HINDPETRO', 'BAJFINANCE', 'HDFCAMC', 'BANKINDIA', 'AMARAJABAT', 'HDFC', 'DMART', 'ASHOKLEY', 'CESC', 'ICICIPRULI', 'NTPC', 'ADANITRANS', 'SUNTV', 'TECHM', 'MANAPPURAM', 'VOLTAS', 'POWERGRID', 'ICICIGI', 'TORNTPHARM', 'RBLBANK', 'RELIANCE', 'CUMMINSIND', 'DRREDDY', 'GODREJCP', 'SIEMENS', 'DLF', 'JINDALSTEL', 'HDFCLIFE', 'NMDC', 'MFSL', 'SBILIFE', 'PETRONET', 'HINDALCO', 'JSWSTEEL', 'APOLLOTYRE', 'PAGEIND', 'ESCORTS', 'MRF', 'SRTRANSFIN', 'ZEEL', 'BRITANNIA', 'UNIONBANK', 'IBULHSGFIN', 'EXIDEIND', 'AUROPHARMA', 'NBCC', 'SRF', 'CASTROLIND', 'ADANIPORTS', 'DABUR', 'UPL', 'NATIONALUM', 'NESTLEIND', 'DIVISLAB', 'BEL', 'IGL', 'SBIN', 'JUBLFOOD', 'BERGEPAINT', 'TCS', 'HINDUNILVR', 'BHARTIARTL', 'NIFTY MIDCAP 50', 'BPCL', 'HEXAWARE', 'GRASIM', 'TATACONSUM', 'INFY', 'ACC', 'CONCOR', 'GAIL', 'CHOLAFIN', 'PIDILITIND', 'IDFCFIRSTB', 'MARUTI', 'HINDZINC', 'MOTHERSUMI', 'NAUKRI', 'PGHH', 'BALKRISIND', 'ULTRACEMCO', 'MUTHOOTFIN', 'TITAN', 'HCLTECH', 'ADANIPOWER', 'LT', 'WIPRO', 'NIACL', 'GMRINFRA', 'BAJAJHLDNG', 'NIFTY 50', 'INDIGO', 'ITC', 'OFSS', 'BAJAJFINSV', 'BIOCON', 'SHREECEM', 'BHARATFORG', 'MCDOWELL-N', 'PNB', 'MGL', 'L&TFH', 'BATAINDIA', 'MARICO', 'TORNTPOWER', 'BAJAJ-AUTO', 'HEROMOTOCO', 'IDEA', 'LICHSGFIN', 'TATASTEEL', 'APOLLOHOSP', 'TATAPOWER', 'GICRE', 'M&MFIN', 'KOTAKBANK', 'ASIANPAINT', 'TVSMOTOR', 'TATAMOTORS', 'HDFCBANK', 'AMBUJACEM', 'EICHERMOT', 'NIFTY NEXT 50', 'FEDERALBNK', 'VEDL', 'AXISBANK', 'BANKBARODA', 'CADILAHC', 'COLPAL', 'BOSCHLTD', 'RAMCOCEM', 'INDUSINDBK', 'ONGC', 'NHPC', 'CANBK', 'BANDHANBNK', 'OIL', 'MINDTREE', 'BHEL', 'GLENMARK', 'ICICIBANK', 'INFRATEL', 'LUPIN', 'RECLTD', 'HAVELLS', 'COALINDIA', 'PFC', 'UBL', 'SAIL', 'IOC', 'PEL', 'CIPLA', 'M&M', 'SUNPHARMA']
stocks_low = {}
stocks_lowest = {}

stocks = {}
for i in stocks_list:
    stock = None
    try:
        stock = (nse.get_quote(i))
    except:
        stock = None
    #Right time to buy?
    if stock != None:
        stock_high = stock['high52']
        stock_low = stock['low52']
        stock_price = stock['buyPrice1']
        print(i+'\t'+str(stock_price))
        if stock_high != None and stock_low != None and stock_price != None:
            stock_overall_range = stock['high52'] - stock['low52']
            stock_low_percent = (stock['buyPrice1']-stock['low52'])/stock_overall_range
            if stock_low_percent < 0.05:
                stocks_lowest[i] = stock_price
                print("VERY LOW ->\t",i)
            elif stock_low_percent < 0.15:
                stocks_low[i] = stock_price
                print("LOW ->\t",i)

print(stocks_lowest)
print(stocks_low)
message = """\
Subject: Stocks Low and Lowest 
Hi Abhishek,
These Stocks are listed low today -"""+str(stock_low)+"""
These Stocks are listed lowest today -"""+str(stocks_lowest)+"""
Best,
Abhishek 
				"""
print("Message Sent - ",message)
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	print("here")
	server.sendmail(sender_email, receiver_email, message)


while(1):
	for i in stocks_low.keys():
		buy_price = None
		try:
			buy_price = nse.get_quote(i)['buyPrice1']
			print(i,'\t\t',buy_price,'\t',stocks_low[i])
			stocks_now[i] = buy_price
		except:
			print(i,'\t\t-\t',stocks_low[i])
		if buy_price!= None:
			#print(buy_price)
			if stocks_low[i] > buy_price:
				message = """\
Subject: Stocks Test
Hi Abhishek,

Stocks for """+i+""" have reached below the limit ("""+str(stocks_low[i])+") and are currently valued at "+str(buy_price)+". \nTime: "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+""".
Please take a look! Have a great day!

Best,
Abhishek 
				"""
				print("Message Sent - ",message)
				with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
					server.login(sender_email, password)
					print("here")
					server.sendmail(sender_email, receiver_email, message)

				stocks_low[i] = stocks_low[i]*0.9
	print("Stocks Now - ", stocks_now)
	time.sleep(30)
	