import sys

# EIA API URL Token Strings
API_KEY = sys.argv[1]
SERIES_TOKEN = "&series_id={}"
CATAGORY_TOKEN = "&category_id={}"
URL = 'http://api.eia.gov/series/?api_key={}'.format(sys.argv[1])
