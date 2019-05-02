from .client import Client
from .utils import CURRENT_CYCLE


class PresidentialClient(Client):

    def totals(self, cycle=CURRENT_CYCLE):
        path = "{cycle}/president/totals.json".format(cycle=cycle)
        return self.fetch(path)

    def candidates(self, cycle=CURRENT_CYCLE, candidate_name=None, fec_id=None):
        """
        Takes a cycle and candidate last name or FEC ID, returns a presidential candidate in the given cycle.
        Use either a candidate's name or an FEC ID, but not both.

        Parameter	    Description
        =========       ===========
        candidate-name	The last name of a presidential candidate, in lower case.
        fec_id	        The FEC-assigned 9-character ID of a presidential candidate's main committee.
                        To find a committee's official FEC ID, use the presidential totals request or 
                        `the FEC web site`_.
        """
        path = "{cycle}/president/candidates".format(cycle=cycle)
        if candidate_name:
            path = path + "/{candidate_name}.json".format(candidate_name=candidate_name)
        elif fec_id:
            path = path + "/{fec_id}.json".format(fec_id=fec_id)
        else:
            raise ValueError("Must specify ONE of `candidate_name` or `fec_id`")
        return self.fetch(path)

    def state_totals(self, state, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and a 2-letter state abbreviation, returns total individual itemized 
        contributions to presidential candidates in the specified state for the specified cycle
        """
        path = "{cycle}/president/states/{state}.json".format(cycle=cycle, state=state)
        return self.fetch(path)
    
    def zip_totals(self, zip, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle and a 5-digit ZIP code, returns total individual itemized 
        contributions to presidential candidates in the specified ZIP code for the specified cycle
        """
        path = "{cycle}/president/zips/{zip}.json".format(cycle=cycle, zip=zip)
        return self.fetch(path)
