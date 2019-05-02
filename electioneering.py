from .client import Client
from .utils import CURRENT_CYCLE


class ElectioneeringClient(Client):

    def recent(self, cycle=CURRENT_CYCLE):
        path = "{cycle}/electioneering_communications.json".format(cycle=cycle)
        return self.fetch(path)
    
    def by_date(self, year, month, day, cycle=CURRENT_CYCLE):
        """
        Parameter	Description
        =========   ===========
        year	    The four-digit year from 2008-2016
        month	    The two-digit month from 01-12
        day	        The two-digit day from 01-31
        """
        path = "{cycle}/electioneering_communications/{year}/{month}/{day}".format(
            cycle=cycle,
            year=year,
            month=month,
            day=day
        )
        self.fetch(path)
