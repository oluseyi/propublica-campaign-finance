"""
Utility functions and error classes used throughout client classes
"""
import datetime
import math
import six


class CampaignFinanceError(Exception):
    """
    Exception for general CampaignFinance API errors
    """
    def __init__(self, message, response=None, url=None):
        super(CampaignFinanceError, self).__init__(message)
        self.message = message
        self.response = response
        self.url = url


class NotFound(CampaignFinanceError):
    """
    Exception for things not found
    """


def get_cycle(year):
    "Return the most recent Campaign Finance cycle for a given year"
    if year < 1996:
        raise CampaignFinanceError('The CampaignFinance API only supports even-numbered years from 1996 to the present.')

    return year - (year % 2)


def parse_date(s):
    """
    Parse a date using dateutil.parser.parse if available,
    falling back to datetime.datetime.strptime if not
    """
    if isinstance(s, (datetime.datetime, datetime.date)):
        return s
    try:
        from dateutil.parser import parse
    except ImportError:
        parse = lambda d: datetime.datetime.strptime(d, "%Y-%m-%d")
    return parse(s)


def u(text, encoding='utf-8'):
    "Return unicode text, no matter what"

    if isinstance(text, six.binary_type):
        text = text.decode(encoding)

    # it's already unicode
    text = text.replace('\r\n', '\n')
    return text


CURRENT_CYCLE = get_cycle(datetime.datetime.now().year)