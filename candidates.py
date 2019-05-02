from .client import Client
from .utils import CURRENT_CYCLE


class CandidatesClient(Client):

    def search(self, query, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle and a candidate first or last name, returns matching candidates"
        path = "{cycle}/candidates/search.json?query={query}".format(cycle=cycle, query=query)
        return self.fetch(path)

    def get(self, fec_id, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle and an FEC-assigned 9-character ID, returns a candidate"
        path = "{cycle}/candidates/{fec_id}.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def leader_categories(self):
        """
        Enumerates the available financial categories recognized for campaign contributions and reporting

        The possible category values are as follows:

        Category	            Value
        ========                =====
        Candidate Loan	        candidate-loan
        Contribution Total	    contribution-total
        Debts Owed	            debts-owed
        Disbursements Total	    disbursements-total
        End Cash	            end-cash
        Individual Total	    individual-total
        PAC Total	            pac-total
        Receipts Total	        receipts-total
        Refund Total	        refund-total
        """
        return ['candidate-loan', 'contribution-total', 'debts-owed', 'disbursements-total',
                'end-cash', 'individual-total', 'pac-total', 'receipts-total', 'refund-total']

    def leaders(self, category, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and financial category, returns the top 20 candidates within the category for a given campaign cycle

        See `leader_categories()` for the labels and descriptions of the available categories
        """
        path = "{cycle}/candidates/leaders/{category}.json".format(cycle=cycle, category=category)
        return self.fetch(path)

    def races(self, state=None, chamber=None, district=None, cycle=CURRENT_CYCLE):
        """
        Returns an array of FEC candidates for a given state (and optional chamber and district)

        Parameter	Description
        =========   ===========
        state	    Two-letter state abbreviation
        chamber	    `house` or `senate` (optional)
        district	Specify the district number. Don't include for states with a single representative 
                    (AL, DE, DC, MT, ND, SD, VT).
                    (House requests only - districts with Senate requests will be ignored.)
        """
        path = "{cycle}/races/{state}"
        if chamber:
            path = path + "/{chamber}"
        if district:
            path = path + "/{district}"
        path = path + ".json"
        path.format(state=state, chamber=chamber, district=district)
        return self.fetch(path)

    def late_contributions(self, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle, returns the most recent late contributions to candidates"
        path = "{cycle}/contributions/48hour.json".format(cycle=cycle)
        return self.fetch(path)

    def late_candidate_contributions(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and FEC-assigned 9-character candidate ID,
        returns the most recent late contributions to a specific candidate
        """
        path = "{cycle}/candidates/{fec_id}/48hour.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def late_committee_contributions(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and FEC-assigned 9-character committee ID,
        returns the most recent late contributions to a specific committee
        """
        path= "{cycle}/committees/{fec-id}/48hour.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)
    
    def late_contributions_by_date(self, year, month, day, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and date, returns late contributions from that date

        Parameter	Description
        =========   ===========
        year	    The four-digit year from 2010-2018
        month	    The two-digit month from 01-12
        day	        The two-digit day from 01-3
        """
        path = "{cycle}/contributions/48hour/{year}/{month}/{day}.json".format(cycle=cycle, year=year, month=month, day=day)
        return self.fetch(path)
