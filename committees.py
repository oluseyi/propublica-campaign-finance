from .client import Client
from .utils import CURRENT_CYCLE


class CommitteesClient(Client):

    def search(self, query, cycle=CURRENT_CYCLE):
        "Takes a query string, returns all FEC-recognized campaign committees with matching names"
        path = "{cycle}/committees/search.json?query={query}".format(cycle=cycle, query=query)
        return self.fetch(path)

    def get(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes an FEC-assigned 9-character committee identifier and campaign cycle,
        returns the specified FEC committee for the given cycle
        """
        path = "{cycle}/committees/{fec-id}.json".format(fec_id=fec_id, cycle=cycle)
        return self.fetch(path)

    def recently_added(self, cycle=CURRENT_CYCLE):
        "Takes a campaign cycle, returns the 20 most recently added FEC committees in the specified cycle"
        path = "{cycle}/committees/new.json".format(cycle=cycle)
        return self.fetch(path)

    def recently_added_superpacs(self, cycle=CURRENT_CYCLE):
        """
        Takes a campaign cycle, returns the 20 most recently added FEC independent 
        expenditure-only committees, known as "super PACs," in the specified cycle
        """
        path = "{cycle}/committees/superpacs.json".format(cycle=cycle)
        return self.fetch(path)

    def recent_committee_filings(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a committee. To find a committee official FEC ID,
                    use a committee search request or the FEC web site, https://www.fec.gov/.
        """
        path = "{cycle}/committees/{fec_id}/filings.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def leadership_committees(self, cycle=CURRENT_CYCLE):
        """
        Returns committees designated as "leadership PACs"-- 
        https://www.fec.gov/finance/disclosure/metadata/metadataLeadershipPacList.shtml --
        by the FEC
        """
        path = "{cycle}/committees/leadership.json".format(cycle=cycle)
        return self.fetch(path)

    def communications(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes an FEC-assigned 9-character committee identifier and a campaign cycle, returns 
        the most recent broadcast advertisements by the specified committee that identify one 
        or more federal candidates (and have aired 30 days before a primary election and 60 
        days before the general election)

        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a committee. To find a committee official FEC ID,
                    use a committee search request or `the FEC web site, <https://www.fec.gov/>`_.
        """
        path = "{cycle}/committees/{fec_id}/electioneering_communications.json".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)

    def bundlers(self, fec_id, cycle=CURRENT_CYCLE):
        """
        Takes an FEC-assigned 9-character committee identifier and a campaign cycle, returns 
        the most recent lobbyist bundlers reported by the specified committee in the given cycle

        Parameter	Description
        =========   ===========
        fec_id	    The FEC-assigned 9-character ID of a committee. To find a committee official FEC ID,
                    use a committee search request or `the FEC web site, <https://www.fec.gov/>`_.
        """
        path = "{cycle}/committees/{fec_id}/lobbyist_bundlers.sjon".format(cycle=cycle, fec_id=fec_id)
        return self.fetch(path)
