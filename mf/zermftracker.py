from kiteconnect import KiteConnect

# Replace with your actual API key and API secret from Zerodha


kite = KiteConnect(api_key=api_key)

print(kite.login_url())

# You need to generate a request token via Zerodha login flow and set it here


# Generate access token
data = kite.generate_session(request_token, api_secret=api_secret)
access_token = data["access_token"]

# Set the access token
kite.set_access_token(access_token)

kite.profile()

# Example: Get mutual fund holdings
mf_holdings = kite.mf_holdings()
print("Mutual Fund Holdings:")
for holding in mf_holdings:
    print(f"Scheme: {holding['fund']}, Units: {holding['quantity']}, Value: {holding['last_price']}")
