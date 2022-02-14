import sys

# EIA API URL Token Strings
API_KEY = sys.argv[1]
SERIES_TOKEN = "&series_id={}"
CATAGORY_TOKEN = "&category_id={}"
SERIES_INDICATOR = "series"
CATAGORY_INDICATOR = "catagory"
URL = 'https://api.eia.gov/{}/?api_key={}'
SERIES_URL = URL.format(SERIES_INDICATOR, sys.argv[1])
CATAGORY_URL = URL.format(CATAGORY_INDICATOR, sys.argv[1])
