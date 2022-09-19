from serp import SerpSDK

class SerpGoogleReverseImage(SerpSDK):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.engine = 'google_reverse_image'
        self.api_url = 'https://serp.shifter.io/v1'
        self.is_serp_api = True

    def set_device(self, value: str):
        """
        Set parameter device

        :param value: The device used for your google search. Must be a value from ["desktop","mobile","tablet"]
        """
        self.params['device'] = value

    def set_image_url(self, value: str):
        """
        Set parameter image_url

        :param value: The image URL of the image that you are searching for. 
        """
        self.params['image_url'] = value

    def set_location(self, value: str):
        """
        Set parameter location

        :param value: Defines where do you want the search to originate from. Please use SerpLocations to obtain a location.
        """
        self.params['location'] = value

    def set_uule(self, value: str):
        """
        Set parameter uule

        :param value: The google encoded location that you want to use for your search. 
        """
        self.params['uule'] = value

    def set_lr(self, value: str):
        """
        Set parameter lr

        :param value: The languages as a list separated through |. For example: lang_en|lang_ar .
        """
        self.params['lr'] = value

    def set_hl(self, value: str):
        """
        Set parameter hl

        :param value: The language you want to use for your google search. 
        """
        self.params['hl'] = value

    def set_gl(self, value: str):
        """
        Set parameter gl

        :param value: The country you want to use for your google search. 
        """
        self.params['gl'] = value

    def set_google_domain(self, value: str):
        """
        Set parameter google_domain

        :param value: Represents the domain from google that you want to use for your search. 
        """
        self.params['google_domain'] = value

    def get_device(self) -> str:
        """
        Get parameter device

        :return: Returns parameter device
        """
        return self.params['device']

    def get_image_url(self) -> str:
        """
        Get parameter image_url

        :return: Returns parameter image_url
        """
        return self.params['image_url']

    def get_location(self) -> str:
        """
        Get parameter location

        :return: Returns parameter location
        """
        return self.params['location']

    def get_uule(self) -> str:
        """
        Get parameter uule

        :return: Returns parameter uule
        """
        return self.params['uule']

    def get_lr(self) -> str:
        """
        Get parameter lr

        :return: Returns parameter lr
        """
        return self.params['lr']

    def get_hl(self) -> str:
        """
        Get parameter hl

        :return: Returns parameter hl
        """
        return self.params['hl']

    def get_gl(self) -> str:
        """
        Get parameter gl

        :return: Returns parameter gl
        """
        return self.params['gl']

    def get_google_domain(self) -> str:
        """
        Get parameter google_domain

        :return: Returns parameter google_domain
        """
        return self.params['google_domain']