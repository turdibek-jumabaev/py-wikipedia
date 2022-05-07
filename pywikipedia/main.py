from unittest import result
import requests

# Wikipedia API


class Wikipedia:
    """
    from pywikipedia import Wikipedia
    wiki = Wikipedia()
    print(wiki.xulosa(sorov='Математика'))

    from pywikipedia import Wikipedia
    wiki = Wikipedia(til='en')
    print(wiki.xulosa(sorov='Matematika'))

    from pywikipedia import Wikipedia
    wiki = Wikipedia()
    print(wiki.qidirmoq(sorov='Математика'))

    from pywikipedia import Wikipedia
    wiki = Wikipedia(til='en')
    print(wiki.qidirmoq(sorov='Matematika'))
    """

    def __init__(self, til='uz'):
        self.til = til
        self.url = 'https://{}.wikipedia.org/w/api.php'.format(til)
        self.params = {
            'action': 'query',
            'format': 'json',
            'titles': '',
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
        }

    def qidirmoq(self, sorov):
        result = list()
        response = requests.get(
            f"https://{self.til}.wikipedia.org/w/api.php?origin=*&action=opensearch&search={sorov}").json()
        for i in range(len(response[1])):
            result.append({'title': response[1][i], 'url': response[3][i]})
        return result

    def xulosa(self, sorov):
        self.params['titles'] = sorov
        response = requests.get(self.url, params=self.params).json()
        return response['query']['pages']
