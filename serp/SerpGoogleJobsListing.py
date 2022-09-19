from serp import SerpSDK

class SerpGoogleJobsListing(SerpSDK):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.engine = 'google_jobs_listing'
        self.api_url = 'https://serp.shifter.io/v1'
        self.is_serp_api = True
        
    def set_q(self, value: str):
        """
        Set parameter q

        :param value: The terms that you are searching for (the query). 
        """
        self.params['q'] = value

    def get_q(self) -> str:
        """
        Get parameter q

        :return: Returns parameter q
        """
        return self.params['q']