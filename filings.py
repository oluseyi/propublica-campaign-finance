from .client import Client
from .utils import CURRENT_CYCLE


class FilingsClient(Client):

    def search(self, query, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and query string, returns information about FEC reports filed electronically
        by committees with names matching the query string
        """
        path = "{cycle}/filings/search.json?query={query}".format(cycle=cycle, query=query)
        return self.fetch(path)

    def by_date(self, year, month, day, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle and filing date, returns information about FEC reports filed electronically on that date"
        path = "{cycle}/filings/{year}/{month}/{day}.json".format(cycle=cycle, year=year, month=month, day=day)
        return self.fetch(path)

    def types(self, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle, returns a list of available form types for FEC electronic filings"
        path = "{cycle}/filings/types.json".format(cycle=cycle)
        return self.fetch(path)
        
    def by_type(self, form_type_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and form type ID, returns the most recent electronic filings for the form type
        
        Parameter	    Description
        form_type_id	F + integer. To get form type IDs, use an electronic filing form types request.
        """
        path = "{cycle}/filings/types/{form_type_id}.json".format(cycle=cycle, form_type_id=form_type_id)
        return self.fetch(path)

    def presidential_summary(self, filing_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and Form 3 Presidential Electronic Filing ID, returns summary figures from the FEC electronic filing

        Parameter	Description
        =========   ===========
        filing_id	Integer representing the ID of a Form 3 electronic filing
        """
        path = "{cycle}/filings/{filing_id}.json".format(cycle=cycle, filing_id=filing_id)
        return self.fetch(path)

    def recent_amendments(self, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle, returns the most recent filings that are amendments of earlier filings"
        path = "{cycle}/filings/amendments.json".format(cycle=cycle)
        return self.fetch(path)
