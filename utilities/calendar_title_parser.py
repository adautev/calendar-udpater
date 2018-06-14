import re


class CalendarTitleParser(object):
    @staticmethod
    def calendar_title_should_be_changed(title):
        return title.find('for') != -1

    @staticmethod
    def clean_up_calendar_title(title : str):
        #yes, yes, this is not optimal :D
        return re.sub('for.+','', title).rstrip(' ')
