import os
import getpass
from dotenv import find_dotenv, load_dotenv
from htw_datalab.etl.collect_data import get_tweets_and_save

def load_envs():
    print('loading envs...')

    try:
        load_dotenv(find_dotenv())
        if "TWITTER_BEARER_TOKEN" not in os.environ:
            os.environ["TWITTER_BEARER_TOKEN"] = getpass.getpass("Enter your Twitter Beare Token: ")
        
        if "TWITTER_COMPANY_TO_CRAWL_FROM" not in os.environ:
            os.environ["TWITTER_COMPANY_TO_CRAWL_FROM"] = getpass.getpass("Enter company name: ")
        
    except:
        print('Envs were not loaded')

if __name__=="__main__":
    load_envs()
    bearer_token = os.environ['TWITTER_BEARER_TOKEN']
    company_name = os.environ['TWITTER_COMPANY_TO_CRAWL_FROM']
    print(f'crawling tweets from company: {company_name}')
    #get_tweets_and_save(bearer_token=bearer_token, company_tweet=company_name)