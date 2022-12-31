"""
twitter_api.py

This file contains the definition of the classes used to 
handle the requests to the Twittwer API.
"""
# importing modules
import logging
import json_helper

# use a logger to help debugging
logger = logging.getLogger('twitter_api_logger')

# set logger level
logger.setLevel(logging.ERROR)

# twitter recent search api url
TWITTER_API_SEARCH_URL = 'https://api.twitter.com/2/tweets/search/recent'
    
class HttpConnect:
    """
    This base class represents any Http connection.
    
    Attributes:
        config  (dict): Dict with the config parameters for authentication.
    """
    config = None

    def __init__(self, config):
        """
        The constructor for HttpConnect class.
  
        Parameters:
            config  (dict): Dict with the config parameters for authentication.
        """
        self.config = config

    def get_bearer_auth(self, r):
        """
        Method required by bearer token authentication.
        
        Parameters:
            r (dict): Dict with required parameters for Bearer auth.
        """
        if self.config is None:
            raise Exception('Unable to create Bearer authorization object.')

        r.headers['Authorization'] = f"Bearer { self.config['BEARER_TOKEN'] }"
        r.headers['User-Agent'] = 'v2RecentSearchPython'

        return r

    def connect_endpoint(self, url, params_dict={}):
        """
        This method connects to the endpoint given by the input.
        
        Parameters:
            url          (str): String with the request url.
            params_dict (dict): Dict with endpoint parames.
        """
        response = requests.get(url, auth=self.get_bearer_auth, params=params_dict)

        if response is None:
            raise Exception('Invalid response.')

        logger.info(response.status_code)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.json()

class TwitterApi(HttpConnect):
    """
    This class handles the Twitter API requests.
    
    Attributes:
        config  (dict): Dict with the config parameters for authentication.
    """
    last_response = None
    config = None

    def __init__(self, config):
        """
        The constructor for TwitterApi class.

        Parameters:
            config  (dict): Dict with the config parameters for authentication.
        """
        HttpConnect.__init__(self, config)

    def search_tweets(self, params={}, max_pages=10):
        """
        This method uses Twitter's API to search for recent tweets based on the input query.

        Parameters:
            params   (dict): Twitter's recent search API params.
            max_pages (int): Max pages to go over in case of result pagination.
        Returns:
            tweets_list (lst): List of retrieved tweets.
        """        
        tweets_list = []
        if self.run_request(self.TWITTER_API_SEARCH_URL, params):
            tweets_list, next_token = self.extract_tweets()
            count=1

            if next_token is not None and count < max_pages:
                url = f'{ self.TWITTER_API_SEARCH_URL }?next_token={next_token}'
                if self.run_request(url, params):
                    next_tweets_list, next_token = self.extract_tweets()
                    tweets_list+= next_tweets_list
                    count+=1
                else:
                    next_token = None

        print(f"{ len(tweets_list) } tweets retrieved!")

        return tweets_list
    
    def run_request(self, url, params={}):
        """
        Auxiliary method to perform the request.

        Parameters:
            url     (str): String with the request url.
            params (dict): Twitter's API params.
        Returns:
            ret (bol): True if request returned successfully, False otherwise.
        """         
        ret = False
        try:
            self.last_response = self.connect_endpoint(url, params)
            ret = True
        except Exception as e:
            logger.error(e)
        return ret

    def parse_response(self):
        """
        Auxiliary method to parse the response.

        Returns:
            meta (dict), data (lst): Dict with the metadata and list with the requested data.
        """ 
        resp = self.last_response        

        meta = None
        if 'meta' in resp.keys():
            meta = resp['meta']
        
        data = None
        if 'data' in resp.keys():
            data = resp['data']

        return meta, data

    def extract_tweets(self):
        """
        Auxiliary method to extract the returned tweets and next token to continue the iteration, if any.

        Returns:
            tweets_list (lst), next_token (str): List of retrieved tweets, next token for further tweets.
        """         
        meta, data = self.parse_response()
        
        if meta is None or data is None:
            return [], None
        
        tweets_set = set()
        for t in data:
            tweets_set.add(t['text'])

        tweets_list = list(tweets_set)
        next_token = None
        if 'next_token' in meta.keys():
            next_token = meta['next_token']

        return tweets_list, next_token
        
    def save_result_to_file(self, outfile):
        """
        Auxiliary method to save the response into a file.

        Parameters:
            outfile (str): Full file path.
        """  
        json_helper = JsonHelper(self.last_response)
        json_helper.to_file(outfile)
