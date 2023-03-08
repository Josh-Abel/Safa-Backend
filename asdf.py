import configparser

config = configparser.ConfigParser()
config.read('config.ini')

scraper = config.get('SCRAPER', 'SITE')
i = 1
print(f"{scraper}{i}")
