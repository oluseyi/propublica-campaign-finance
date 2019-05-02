from .client import Client
from .utils import CURRENT_CYCLE


class IndependentSpendingClient(Client):

    def get(self, cycle=CURRENT_CYCLE, offset=None):
        """
        Takes a campaign cycle and an optional offset in multiples of 20, 
        returns the 200 most recent independent expenditures
        """
        path = "{cycle}/independent_expenditures.json"
        if offset:
            path = path + "?offset={offset}".format(offset=offset)
        return self.fetch(path)

    def by_date(self, year, month, day, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and a date (the date of activity, not the 
        date filed with the FEC), returns all independent expenditures on 
        the specified date

        Parameter	Description
        =========   ===========
        year	    The four-digit year from 2008-2016
        month	    The two-digit month from 01-12
        day	        The two-digit day from 01-31
        """
        path = "{cycle}/independent_expenditures/{year}/{month}/{day}.json".format(
            cycle=cycle,
            year=year,
            month=month,
            day=day
        )
        return self.fetch(path)
    
    def by_committee(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and an FEC-assigned 9-character committee identifier, returns
        the 20 most recent independent expenditures by the given committee

        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a committee. To find a committee official FEC ID,
                    use a committee search request or `the FEC web site, <https://www.fec.gov/>`_.
        """
        path = "{cycle}/committees/{fec_id}/independent_expenditures.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def by_candidate(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and an FEC-assigned 9-character candidate identifier, returns
        the 200 most recent independent expenditures in support of or opposition to the 
        specified candidate

        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a candidate. To find a committee official FEC ID,
                    use a candidate search request or `the FEC web site, <https://www.fec.gov/>`_.
        """
        path = "{cycle}/candidates/{fec_id}/independent_expenditures.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def by_presidential(self, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle, returns the 200 most recent independent expenditures in 
        support of or opposition to any presidential candidate
        """
        path = "{cycle}/president/independent_expenditures.json".format(cycle=cycle)
        return self.fetch(path)

    def by_office(self, office, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and an elected office (either House, Senate or President), 
        returns the amount of money spent in independent expenditures for a given office

        Parameter	Description
        =========   ===========
        office	    one of `house`, `senate` or `president`
        """
        path = "{cycle}/independent_expenditures/race_totals/{office}.json".format(cycle=cycle, office=office)
        return self.fetch(path)

    def committee_race_totals(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and an FEC-assigned 9-character committee identifier, returns
        the total amounts of money that a given committee has spent on individual races 
        (consisting of a state, office and district) during a cycle

        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a committee. To find a committee official FEC ID,
                    use a committee search request or `the FEC web site, <https://www.fec.gov/>`_.
        """
        path = "{cycle}/committees/{fec_id}/independent_expenditures/races.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)
