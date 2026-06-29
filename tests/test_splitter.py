import unittest

from src.splitter import parse_report_text


class SplitterTests(unittest.TestCase):
    def test_parse_report_text_converts_pdf_text_to_structured_chunk(self):
        raw_text = """The Football Association
Extraordinary Incident Report
Fixture Details
Fixture:
Thornton Rangers FC vs Millbrook United FC
Competition:
FA Vase
Match Date:
05/04/2026
Is Match Abandoned:
No
Report Details
Club:
Home Team
Report Details:
I have to report that in the 63rd minute of this game, following the award of a free kick to Millbrook United FC on the edge of the penalty area, the above-named player, Daniel Hartley, approached the opposing player Marcus Webb and deliberately struck him on the left side of his face with his open right hand. Webb immediately fell to the ground and required treatment from the away team physiotherapist for approximately four minutes before being able to continue. I asked Hartley for his name, informed him he was being dismissed from the field of play for violent conduct under Law 12 (S2), and showed him the red card. Hartley accepted the dismissal without protest and left the field. I restarted play with the original free kick. The match concluded without further extraordinary incident. Final score: Thornton Rangers FC 1-2 Millbrook United FC.
Match Official Details
Referee Name:
Sarah Jennings
Is Referee U18?:
No
Submission Date:
06/04/2026
Report Submitted By:
Sarah Jennings
"""

        parsed = parse_report_text(raw_text)

        self.assertEqual(parsed["fields"]["Fixture"], "Thornton Rangers FC vs Millbrook United FC")
        self.assertEqual(parsed["fields"]["Competition"], "FA Vase")
        self.assertEqual(parsed["fields"]["Club"], "Home Team")
        self.assertEqual(parsed["fields"]["Referee Name"], "Sarah Jennings")
        self.assertIn("Document Type: Extraordinary Incident Report", parsed["text"])
        self.assertIn("Fixture: Thornton Rangers FC vs Millbrook United FC", parsed["text"])
        self.assertIn("Report Details:", parsed["text"])
        self.assertIn("Daniel Hartley", parsed["text"])


if __name__ == "__main__":
    unittest.main()
