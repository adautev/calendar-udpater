from unittest import TestCase
from utilities.calendar_title_parser import CalendarTitleParser

class TestCalendarTitleParser(TestCase):
    def test_calendar_title_should_be_changed(self):
        self.assertFalse(CalendarTitleParser.calendar_title_should_be_changed('Зелен офис'))
        self.assertTrue(CalendarTitleParser.calendar_title_should_be_changed('Зелен офис for Андрей 0000'))

    def test_clean_up_calendar_title(self):
        self.assertEquals(CalendarTitleParser.clean_up_calendar_title('Зелен офис for Андрей 0000'), 'Зелен офис за Андрей')
