import sys
import requests

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')

headers = {
    "cookie": "gcl_au=1.1.462093030.1749376357; _fbp=fb.2.1749376356923.374791880730403188; _ga_QHXRKWW9HH=GS2.3.s1750066535$o2$g0$t1750066535$j60$l0$h0; _ga=GA1.1.573241470.1749376357; _ga_5HTJMW67XK=GS2.1.s1750258781$o31$g0$t1750258790$j51$l0$h0; _ga_08NPRH5L4M=GS2.1.s1750262395$o41$g0$t1750262395$j60$l0$h0; _t=oy6DA6a24GdzRf0p70uAh9QNiW8gADpkZD9mNVo9OzPoFelGFu4Rwp4az5%2FhtlSu6hvoASpg3kRbhe3AZnElAmcEyiz2DfNsywWv7%2FxdayPdCTVjfJtDC5VO%2B89JHzK%2BiNIEWTObPFb0X0o1dQ8u0VdHe6wIYYz%2BO0pjSVpM8uFmob5ERlRn4rtcSINcMYaFGVYVWHa1lVBaDtyc2m7yCUgAo7bkP4JggTguoHFJS94A0g2xUJkZpkplC%2BOhrxIFlydptKpIlF3RWsATdgMu1EAKwYCwkOlH55GuPxiwCIm4Ujd6rwh%2FYW9RtgDiAK1SCE8r9w%3D%3D--okdOCCmdv%2FkdgjPl--%2Bwh8NJ8CSrZn0RQGtge2Gw%3D%3D; _forum_session=Yfiqq%2F%2BrfcpPKB%2BS67nmdtf5hn6CHmv3ESeOuAn2YogvPP8GsA%2FkongY54FIONvdNqPwrWSUJPnc5mkpq4htek%2BzZvH1s72n6efkp6npJIp4Z7Gw%2F07FKHFLHQPZ46SYrJrnbMH58ea9BgoJOPaHn%2F1OvDdRCE6wVKmfVOHjqrSA7ij%2Bga889SjuiCjenDO0yhxxU%2F2IXDtzOsEiebZZLfD27sTX1tJ9vNMKuZg97bUkT3aoQSplEn56nVwCZpyayyqKxq8qoLMXK9%2Bm98yyAXaf3jsaZA%3D%3D--hJGX4%2F0%2B5tbjV92p--Hux1mqfQijaoslGq%2FQM67Q%3D%3D",
    "x-csrf-token": "k56CeSVpYSNXjoFtjnFp50IWT0uYsNByX3pJZllDEUo_lOuMpQEsApWw7UW7OwU7M-zQtIUeZs9Gxj85bE-2eg",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get("https://discourse.onlinedegree.iitm.ac.in/latest.json", headers=headers)
print(response.json())
