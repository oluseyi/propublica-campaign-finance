"""
A Python client for the ProPublica Campaign Finance API
Based on the Python client for the ProPublica Congress API by Chris Amico
https://github.com/eyeseast/propublica-congress/

API docs: https://projects.propublica.org/api-docs/campaign-finance/
"""
__author__ = "Oluseyi Sonaiya (oluseyi@oluseyi.info)"
__version__ = "0.1.0"

import os

from .client import Client
from .utils import CampaignFinanceError, NotFound, CURRENT_CYCLE

# subclients
from candidates import CandidatesClient
from committees import CommitteesClient
from electioneering import ElectioneeringClient
from filings import FilingsClient
from independent_spending import IndependentSpendingClient
from presidential import PresidentialClient


__all__ = ('CampaignFinance', 'CampaignFinanceError', 'NotFound', 'CURRENT_CYCLE')


class CampaignFinance(Client):
    """
    Implements the public interface for the ProPublica Campaign Finance API

    Methods are namespaced by topic (though some have multiple access points).
    Everything returns decoded JSON, with fat trimmed.

    In addition, the top-level namespace is itself a client, which
    can be used to fetch generic resources, using the API URIs included
    in responses. This is here so you don't have to write separate
    functions that add on your API key and trim fat off responses.

    Create a new instance with your API key, or set an environment
    variable called ``PROPUBLICA_API_KEY``.

    Campaign Finance uses `httplib2 <https://github.com/httplib2/httplib2>`_, and caching is pluggable. 
    By default, it uses `httplib2.FileCache <https://httplib2.readthedocs.io/en/latest/libhttplib2.html#httplib2.FileCache>`_,
    in a directory called ``.cache``, but it should also work with memcache
    or anything else that exposes the same interface as FileCache (per httplib2 docs).
    """

    def __init__(self, apikey=None, cache='.cache', http=None):
        if apikey is None:
            apikey = os.environ.get('PROPUBLICA_API_KEY')

        super(CampaignFinance, self).__init__(apikey, cache, http)
        self.candidates = CandidatesClient(self.apikey, cache, self.http)
        self.committees = CommitteesClient(self.apikey, cache, self.http)
        self.electioneering = ElectioneeringClient(self.apikey, cache, self.http)
        self.filings = FilingsClient(self.apikey, cache, self.http)
        self.independent_spending = IndependentSpendingClient(self.apikey, cache, self.http)
        self.presidential = PresidentialClient(self.apikey, cache, self.http)
