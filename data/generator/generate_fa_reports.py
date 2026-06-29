"""
FA Extraordinary Incident Report Generator
==========================================
Generates realistic FA Extraordinary Incident Report PDFs using authentic
referee language as per The Football Association's Guide to Misconduct Report Writing.

Usage:
    python generate_fa_reports.py

Output:
    One PDF per report in OUTPUT_DIR. Edit REPORTS list to add more fixtures.

Dependencies:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle

# ── Configuration ─────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "output", "fa_reports"))

# ── Colour palette (matching FA branding) ─────────────────────────────────────

FA_RED   = colors.Color(0.78, 0.04, 0.04)
FA_DARK  = colors.Color(0.10, 0.10, 0.10)
MID_GREY = colors.Color(0.50, 0.50, 0.50)
LT_GREY  = colors.Color(0.88, 0.88, 0.88)

# ── Report data ───────────────────────────────────────────────────────────────
# Each dict represents one Extraordinary Incident Report.
# 'report_details' reads exactly as a referee would write it:
#   first-person, factual, time-stamped, distance-aware, quoting exact
#   language where relevant, and concluding with the action taken.

REPORTS = [
    # ── 01 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Thornton Rangers FC vs Millbrook United FC",
        "competition":"FA Vase",
        "match_date": "05/04/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 63rd minute of this game, following the award "
            "of a free kick to Millbrook United FC on the edge of the penalty area, the "
            "above-named player, Daniel Hartley (shirt no. 7, Thornton Rangers FC), "
            "approached the opposing player Marcus Webb (shirt no. 8), who had taken the "
            "kick, and deliberately struck him on the left side of his face with his open "
            "right hand. At the time of this incident I was approximately 8 metres away "
            "and had a clear and unobstructed view. Webb immediately fell to the ground "
            "and required treatment from the away team physiotherapist for approximately "
            "four minutes before being able to continue. I asked Hartley for his name, "
            "informed him he was being dismissed from the field of play for violent "
            "conduct under Law 12 (S2), and showed him the red card. Hartley accepted "
            "the dismissal without protest and left the field. I restarted play with "
            "the original free kick. The match concluded without further extraordinary "
            "incident. Final score: Thornton Rangers FC 1-2 Millbrook United FC."
        ),
        "referee":          "Sarah Jennings",
        "ref_u18":          "No",
        "submission_date":  "06/04/2026",
        "submitted_by":     "Sarah Jennings",
    },

    # ── 02 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Ashford Town FC vs Weston Rovers FC",
        "competition":"FA Cup Extra Preliminary Round",
        "match_date": "12/04/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 78th minute of this game, the above-named "
            "player, Luke Pemberton (shirt no. 9, Ashford Town FC), challenged for a "
            "loose ball inside the penalty area and, in doing so, left the ground with "
            "both feet raised and made contact with the right ankle of the opposing "
            "goalkeeper, Marcus Ellison (Weston Rovers FC). In my opinion Pemberton "
            "used excessive force and endangered the safety of an opponent. I was "
            "approximately 12 metres from the incident and had a clear and uninterrupted "
            "view. Ellison received treatment on the pitch for approximately seven "
            "minutes and was subsequently unable to continue; he was replaced by the "
            "substitute goalkeeper, Nathan Cole. I dismissed Pemberton from the field "
            "of play for serious foul play under Law 12 (S1) and showed him the red "
            "card. I awarded a direct free kick to Weston Rovers FC from the point of "
            "the offence. The match concluded without further extraordinary incident. "
            "Final score: Ashford Town FC 2-1 Weston Rovers FC."
        ),
        "referee":          "Mark Thompson",
        "ref_u18":          "No",
        "submission_date":  "13/04/2026",
        "submitted_by":     "Mark Thompson",
    },

    # ── 03 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Brentwood Athletic FC vs Colchester Wanderers FC",
        "competition":"Essex Senior League",
        "match_date": "19/04/2026",
        "abandoned":  "Yes",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 54th minute of this game, with the score at "
            "Brentwood Athletic FC 2-1 Colchester Wanderers FC, a group of approximately "
            "12 spectators breached the advertising hoarding behind the home goal and "
            "entered the playing surface. I immediately halted play and instructed both "
            "sets of players to retreat to the centre circle. I was positioned near the "
            "centre spot and had a clear view of the encroachment. I requested that the "
            "home club stewards intervene; however, they were unable to clear the playing "
            "area within a reasonable time. I consulted with the fourth official, "
            "Mr Dean Griffiths, and with both captains, Ryan O'Brien (home, shirt no. 6) "
            "and James Kavanagh (away, shirt no. 5). Both captains confirmed they were "
            "not satisfied that player safety could be guaranteed. After a delay of "
            "approximately 14 minutes I took the decision to formally abandon the match "
            "at 55 minutes 20 seconds in accordance with my powers under Law 5. I "
            "informed both managers of my decision and of their right to report the "
            "matter to their County Football Association. I notified the Essex County "
            "FA the same evening. Score at abandonment: Brentwood Athletic FC 2-1 "
            "Colchester Wanderers FC."
        ),
        "referee":          "David Osei",
        "ref_u18":          "No",
        "submission_date":  "20/04/2026",
        "submitted_by":     "David Osei",
    },

    # ── 04 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Halesowen Town FC vs Stourbridge FC",
        "competition":"Southern League Division One Midlands",
        "match_date": "22/04/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 44th minute of this game, the above-named "
            "player, Jermaine Campbell (shirt no. 10, Stourbridge FC), approached me "
            "at a stoppage in play and informed me that a spectator in the home "
            "enclosure adjacent to the technical areas had directed a racially abusive "
            "remark towards him. Campbell stated the remark was made at approximately "
            "the 41st minute when he was in possession near the touchline. I immediately "
            "halted play and spoke to both captains, Kyle Marsh (home, shirt no. 4) "
            "and Campbell. I then addressed the home club steward and requested the "
            "individual be identified and removed. I made a public address to spectators "
            "via the stadium tannoy, warning that further discriminatory behaviour would "
            "result in the match being abandoned under FA protocol. The individual was "
            "removed from the enclosure by club officials. I consulted with Campbell "
            "again, who confirmed he was willing to continue. Play resumed after a delay "
            "of approximately nine minutes. No further discriminatory incidents came to "
            "my attention during the remainder of the match. A full written report has "
            "been submitted to the West Midlands County FA. Final score: "
            "Halesowen Town FC 1-1 Stourbridge FC."
        ),
        "referee":          "Claire Hutchins",
        "ref_u18":          "No",
        "submission_date":  "23/04/2026",
        "submitted_by":     "Claire Hutchins",
    },

    # ── 05 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Whitby Town FC vs Scarborough Athletic FC",
        "competition":"Northern Premier League East Division",
        "match_date": "28/04/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 72nd minute of this game, following a robust "
            "but in my opinion fair challenge by home player Ryan Sutcliffe (shirt no. 3, "
            "Whitby Town FC) on away forward Callum Reid (shirt no. 11), Sutcliffe "
            "immediately placed both hands on Reid's chest and pushed him forcefully to "
            "the ground. I was approximately 6 metres from the incident and had a clear "
            "and unobstructed view. Reid remained on the ground briefly but did not "
            "require treatment and was able to continue. A number of players from both "
            "sides gathered around the incident. I addressed both captains and instructed "
            "all players to disperse, which they did. I cautioned two players, one from "
            "each side, for failing to retreat when instructed to do so. I then dismissed "
            "Sutcliffe from the field of play for violent conduct under Law 12 (S2), "
            "confirmed his name and showed him the red card. Sutcliffe left the field "
            "without further protest. I restarted play with a direct free kick to "
            "Scarborough Athletic FC from the point of the offence. The remainder of the "
            "match passed without further extraordinary incident. Final score: "
            "Whitby Town FC 2-2 Scarborough Athletic FC."
        ),
        "referee":          "Paul Nicholson",
        "ref_u18":          "No",
        "submission_date":  "29/04/2026",
        "submitted_by":     "Paul Nicholson",
    },

    # ── 06 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Corby Town FC vs Kettering Town FC",
        "competition":"Northamptonshire FA Senior Cup",
        "match_date": "02/05/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 58th minute of this game, the above-named "
            "player, Craig Desmond (shirt no. 7, Kettering Town FC), having been fairly "
            "dispossessed by home defender Jamie Walsh (shirt no. 5), turned and "
            "deliberately kicked Walsh on the back of the right calf with considerable "
            "force whilst the ball was out of play, having gone out for a throw-in "
            "approximately two seconds prior to the contact. I was approximately 10 "
            "metres from both players and had a clear and uninterrupted view of the "
            "incident. Walsh required treatment from the home physiotherapist for "
            "three minutes but was able to continue. I immediately asked Desmond for "
            "his full name, informed him he was dismissed from the field of play for "
            "violent conduct under Law 12 (S2), and showed him the red card. Desmond "
            "expressed verbal dissent, stating 'that is an absolute joke, I barely "
            "touched him', but then left the field of play without further incident. "
            "I restarted play with a throw-in to Corby Town FC. The match concluded "
            "without further extraordinary incident. Final score: Corby Town FC 3-0 "
            "Kettering Town FC."
        ),
        "referee":          "James Hawkins",
        "ref_u18":          "No",
        "submission_date":  "03/05/2026",
        "submitted_by":     "James Hawkins",
    },

    # ── 07 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "FC Clacton vs Haverhill Rovers FC",
        "competition":"Thurlow Nunn League Premier Division",
        "match_date": "06/05/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report an incident involving a team official that occurred "
            "immediately following the final whistle of this game. As players were "
            "leaving the field of play, my assistant referee Mr Daniel Cross informed "
            "me that the home team manager, Alan Price, had approached him near the "
            "halfway line and said 'you're a bloody cheat, you cost us that game.' "
            "Mr Cross confirmed he heard these words clearly and that Price was "
            "approximately one metre from him at the time. I approached Price and "
            "asked for his name. Price repeated to me, 'your assistant has cheated us, "
            "I want his details.' I informed Price that I was reporting this matter to "
            "the County Football Association and that he should raise any formal "
            "grievance through the appropriate channels. Price then walked away towards "
            "the home dressing rooms without further incident. As the final whistle had "
            "already been blown I was unable to issue a card; however, this incident is "
            "reported under Law 5 for the consideration of the Essex County FA. "
            "I have obtained a written statement from Mr Cross in support of this "
            "report. Final score: FC Clacton 2-2 Haverhill Rovers FC."
        ),
        "referee":          "Rachel Forster",
        "ref_u18":          "No",
        "submission_date":  "07/05/2026",
        "submitted_by":     "Rachel Forster",
    },

    # ── 08 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Tiverton Town FC vs Tavistock AFC",
        "competition":"Southern League Division One South",
        "match_date": "09/05/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 38th minute of this game, the above-named "
            "player, Lewis Fairweather (shirt no. 14, Tavistock AFC), deliberately "
            "spat at home midfielder Aaron Blake (shirt no. 6) following a foul by "
            "Blake, for which I had already awarded a free kick to Tavistock AFC. "
            "At the time of the incident I was approximately 8 metres from both "
            "players and had a clear and unobstructed view; I clearly saw Fairweather "
            "turn towards Blake and direct saliva at his face. Blake did not retaliate. "
            "I immediately asked Fairweather for his full name, informed him he was "
            "dismissed from the field of play for spitting at an opponent under Law 12 "
            "(S3), and showed him the red card. Fairweather accepted the dismissal "
            "without protest and left the field of play. I restarted with the original "
            "free kick. The match continued without further extraordinary incident. "
            "Final score: Tiverton Town FC 1-1 Tavistock AFC."
        ),
        "referee":          "Stuart Barnes",
        "ref_u18":          "No",
        "submission_date":  "10/05/2026",
        "submitted_by":     "Stuart Barnes",
    },

    # ── 09 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Bamber Bridge FC vs Clitheroe FC",
        "competition":"Northern Premier League West Division",
        "match_date": "13/05/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report an incident involving a spectator that occurred in the "
            "67th minute of this game. Whilst my assistant referee Mr Simon Hartley "
            "was positioned on the far touchline, a spectator in the home enclosure "
            "directly behind him threw a plastic drinks cup which struck Mr Hartley "
            "on the right shoulder. Mr Hartley immediately drew this to my attention "
            "by raising his flag. I halted play and approached the touchline. Mr Hartley "
            "confirmed what had occurred and indicated the approximate location of the "
            "individual within the stand. I informed the home club steward on duty and "
            "requested the individual be identified and removed. After a delay of "
            "approximately six minutes, club officials confirmed the individual had been "
            "escorted from the ground. I addressed both captains, Danny Walsh (home, "
            "shirt no. 4) and Nathan Greaves (away, shirt no. 6), and informed them "
            "that any further missile throwing from spectators would result in the match "
            "being abandoned. Play resumed and no further incidents of this nature "
            "occurred. Mr Hartley confirmed he was uninjured and willing to continue. "
            "This matter has been reported to the Lancashire County FA. Final score: "
            "Bamber Bridge FC 0-0 Clitheroe FC."
        ),
        "referee":          "Michael Daley",
        "ref_u18":          "No",
        "submission_date":  "14/05/2026",
        "submitted_by":     "Michael Daley",
    },

    # ── 10 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Merthyr Town FC vs Cinderford Town AFC",
        "competition":"Southern League Division One South",
        "match_date": "16/05/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report a serious injury to an away team player that required "
            "the match to be temporarily suspended. In the 51st minute, the above-named "
            "player, Marcus Ellison (shirt no. 3, Cinderford Town AFC), received the "
            "ball on the left wing and was challenged fairly by home defender Paul Grant "
            "(shirt no. 2). Following the challenge, Ellison remained on the ground and "
            "it was apparent he was in considerable pain. I halted play immediately and "
            "permitted the away team physiotherapist to enter the field. Ellison received "
            "treatment on the pitch for approximately nine minutes. It became clear he was "
            "unable to continue and he was substituted. During treatment the physiotherapist "
            "indicated the injury may be serious in nature and requested additional time. "
            "I consulted with both captains and both managers, all of whom agreed to a "
            "short further delay. Ellison was assisted from the field. The match "
            "subsequently resumed and concluded without further extraordinary incident. "
            "I am reporting this matter in accordance with FA guidelines on serious "
            "player injuries sustained during play. Final score: Merthyr Town FC 2-0 "
            "Cinderford Town AFC."
        ),
        "referee":          "Alison Wright",
        "ref_u18":          "No",
        "submission_date":  "17/05/2026",
        "submitted_by":     "Alison Wright",
    },

    # ── 11 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Leamington FC vs Alvechurch FC",
        "competition":"Southern League Premier Division Central",
        "match_date": "20/05/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 17th minute of this game, the above-named "
            "player, Carl Dawson (shirt no. 2, Leamington FC), contested a header with "
            "away winger Tyrese Grant (shirt no. 7) approximately 30 metres from the "
            "home goal. In doing so, Dawson deliberately drove his right elbow into the "
            "left side of Grant's face. At the time of the incident the ball had already "
            "been cleared from the area and neither player was challenging for it. I was "
            "approximately 15 metres from the incident and had a clear and uninterrupted "
            "view. Grant received treatment from the away physiotherapist for five minutes "
            "before being able to continue. I asked Dawson for his name, informed him he "
            "was dismissed from the field of play for violent conduct under Law 12 (S2), "
            "and showed him the red card. Dawson made no verbal response and left the "
            "field without protest. I restarted play with a direct free kick to "
            "Alvechurch FC from the point of the offence. The remainder of the match "
            "concluded without further extraordinary incident. Final score: "
            "Leamington FC 1-3 Alvechurch FC."
        ),
        "referee":          "Kevin Brady",
        "ref_u18":          "No",
        "submission_date":  "21/05/2026",
        "submitted_by":     "Kevin Brady",
    },

    # ── 12 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Didcot Town FC vs Highworth Town FC",
        "competition":"Hellenic League Premier Division",
        "match_date": "23/05/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 33rd minute of this game, the above-named "
            "player, Scott Norris (shirt no. 10, Highworth Town FC), following the "
            "disallowance of a goal for offside, turned towards me and used offensive "
            "and abusive language directed at me as the match official. The player was "
            "approximately 5 metres from my position at the time and I clearly heard "
            "the words, which I am recording in a sealed envelope in accordance with FA "
            "guidance. No other players were in the immediate vicinity at the time. "
            "I asked Norris for his full name, informed him he was dismissed from the "
            "field of play for using offensive, insulting or abusive language directed "
            "at a match official under Law 12 (S6), and showed him the red card. "
            "Norris continued to protest verbally as he walked from the field but "
            "directed no further language towards me or my assistants. I restarted "
            "play with an indirect free kick to Didcot Town FC from the position of "
            "the offside player. The remainder of the match passed without further "
            "extraordinary incident. Final score: Didcot Town FC 2-2 Highworth Town FC."
        ),
        "referee":          "Peter Groves",
        "ref_u18":          "No",
        "submission_date":  "24/05/2026",
        "submitted_by":     "Peter Groves",
    },

    # ── 13 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Dunston UTS FC vs Hebburn Town FC",
        "competition":"Northern League Division One",
        "match_date": "26/05/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 87th minute of this game, the above-named "
            "player, Aaron Stokes (shirt no. 11, Dunston UTS FC), having been fairly "
            "dispossessed by Gary Bell (shirt no. 6, Hebburn Town FC), and whilst the "
            "ball was out of play for a throw-in awarded to the away team, deliberately "
            "directed saliva at Bell's face from a distance of approximately one metre. "
            "I was approximately 7 metres from both players and had a clear and "
            "unobstructed view of the incident. Bell did not retaliate. I immediately "
            "stopped play, asked Stokes for his full name, informed him he was dismissed "
            "from the field of play for spitting at an opponent under Law 12 (S3), and "
            "showed him the red card. Stokes stated 'I never did that, check your "
            "assistant' before leaving the field. I am satisfied from my own clear and "
            "unobstructed view that the incident occurred as described above. I restarted "
            "play with the throw-in to Hebburn Town FC. The match concluded without "
            "further extraordinary incident. Final score: Dunston UTS FC 1-2 "
            "Hebburn Town FC."
        ),
        "referee":          "Thomas Reid",
        "ref_u18":          "No",
        "submission_date":  "27/05/2026",
        "submitted_by":     "Thomas Reid",
    },

    # ── 14 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Bracknell Town FC vs Hartley Wintney FC",
        "competition":"Combined Counties League Premier Division South",
        "match_date": "29/05/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report an incident involving the away team manager that occurred "
            "in the 85th minute of this game. Following the award of a penalty kick to "
            "Bracknell Town FC, the above-named manager, Steve Curry (Hartley Wintney "
            "FC), left his technical area without my permission and entered the field of "
            "play, approaching me directly. He said 'that is never a penalty, you have "
            "been against us all day.' I asked Curry to return to his technical area "
            "immediately. He continued to remonstrate and said 'you are an absolute "
            "disgrace, referee.' I informed Curry he was being dismissed from the "
            "technical area under Law 5 and made a written note of his name. Curry "
            "refused to leave and it was necessary for the fourth official, Mr Lee "
            "Craven, and the away team assistant manager, Barry Clough, to guide him "
            "from the field. The delay lasted approximately four minutes. The penalty "
            "was subsequently taken and scored. I am reporting this matter to the Berks "
            "and Bucks County FA. Final score: Bracknell Town FC 3-1 Hartley Wintney FC."
        ),
        "referee":          "Fiona Ashby",
        "ref_u18":          "No",
        "submission_date":  "30/05/2026",
        "submitted_by":     "Fiona Ashby",
    },

    # ── 15 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Shildon AFC vs Bishop Auckland FC",
        "competition":"Northern League Division One",
        "match_date": "01/06/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 29th minute of this game, the above-named "
            "player, Jason Reed (shirt no. 8, Shildon AFC), received a second caution "
            "in the same match and was consequently dismissed from the field of play. "
            "The first caution was issued in the 14th minute for unsporting behaviour "
            "(C1), specifically for deliberately handling the ball to prevent an "
            "opposing player receiving a pass. The second caution was issued in the "
            "29th minute for dissent by word and action (C2), following the award of "
            "a free kick to Bishop Auckland FC. Reed approached me, pointed directly "
            "at my face from a distance of approximately 3 metres and stated 'you are "
            "giving them everything today, referee.' I clearly heard the words and "
            "observed the action. I reminded Reed of his first caution, showed him the "
            "yellow card for the second cautionable offence and then immediately showed "
            "him the red card, making clear he was dismissed for receiving a second "
            "caution in the same match under Law 12 (S7). Reed departed the field "
            "without further protest. I restarted play with the original free kick. "
            "The remainder of the match concluded without further extraordinary "
            "incident. Final score: Shildon AFC 3-3 Bishop Auckland FC."
        ),
        "referee":          "Ian Fellows",
        "ref_u18":          "No",
        "submission_date":  "02/06/2026",
        "submitted_by":     "Ian Fellows",
    },

    # ── 16 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Sholing FC vs Moneyfields FC",
        "competition":"Wessex League Premier Division",
        "match_date": "04/06/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 76th minute of this game, the above-named "
            "player, Kai Dorset (shirt no. 9, Moneyfields FC), denied an obvious "
            "goalscoring opportunity to Sholing FC by deliberately handling the ball "
            "on the goal line. Home striker Gary Hallett (shirt no. 11) had beaten "
            "the last defender and had a clear run on goal when Dorset, positioned on "
            "the goal line, deliberately extended his right arm and deflected the ball "
            "around the post. I was approximately 10 metres from the incident, inside "
            "the penalty area, and had a clear and uninterrupted view. I awarded a "
            "penalty kick to Sholing FC and dismissed Dorset from the field of play "
            "under Law 12 (S4) for denying an obvious goalscoring opportunity by "
            "deliberately handling the ball, showing him the red card. Dorset did not "
            "protest and left the field immediately. The penalty was taken and scored "
            "by Hallett. The match concluded without further extraordinary incident. "
            "Final score: Sholing FC 2-1 Moneyfields FC."
        ),
        "referee":          "Natalie Brooks",
        "ref_u18":          "No",
        "submission_date":  "05/06/2026",
        "submitted_by":     "Natalie Brooks",
    },

    # ── 17 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Guiseley AFC vs Brighouse Town FC",
        "competition":"Northern Premier League East Division",
        "match_date": "07/06/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 55th minute of this game, the above-named "
            "player, Marco DiSilva (shirt no. 10, Guiseley AFC), who had already been "
            "cautioned in the 31st minute for unsporting behaviour (C1), received a "
            "second caution for simulation (C1) and was consequently dismissed from "
            "the field of play. DiSilva had fallen inside the penalty area following "
            "minimal contact from away defender Rob Cross (shirt no. 4); in my opinion "
            "the contact was not sufficient to cause a fall and I considered this to be "
            "an attempt to deceive me into awarding a penalty kick. I was approximately "
            "8 metres from the incident and had a clear and unobstructed view. I showed "
            "DiSilva the yellow card for the second cautionable offence and immediately "
            "showed the red card, making clear he was dismissed under Law 12 (S7). "
            "DiSilva stated 'you have got to be kidding me, referee, that is two "
            "shocking decisions' before leaving the field without further incident. "
            "I restarted play with a direct free kick to Brighouse Town FC from the "
            "point of the simulation. Final score: Guiseley AFC 0-1 Brighouse Town FC."
        ),
        "referee":          "Olusegun Adeyemi",
        "ref_u18":          "No",
        "submission_date":  "08/06/2026",
        "submitted_by":     "Olusegun Adeyemi",
    },

    # ── 18 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Hanley Town FC vs Stone Old Alleynians FC",
        "competition":"North West Counties League Division One North",
        "match_date": "13/06/2026",
        "abandoned":  "No",
        "club":       "Home Team",
        "report_details": (
            "I have to report that in the 44th minute of this game, as the ball was "
            "out of play for a goal kick, my fourth official Mr Wayne Lowe drew my "
            "attention to home player Bradley Lawton (shirt no. 4, Hanley Town FC), "
            "who had turned away from the play and, without provocation, struck away "
            "player Jack Millward (shirt no. 7) on the right side of the face with "
            "his closed right fist. The incident occurred approximately 25 metres "
            "from my position; I did not personally witness the strike. Mr Lowe "
            "confirmed he had a clear and uninterrupted view from approximately "
            "4 metres. Millward required treatment for approximately five minutes and "
            "was subsequently able to continue. Acting on Mr Lowe's report, I dismissed "
            "Lawton from the field of play for violent conduct under Law 12 (S2) and "
            "showed him the red card. Lawton accepted the dismissal without protest. "
            "Mr Lowe has submitted a separate written report to the Staffordshire "
            "County FA confirming his account of the incident. I restarted play with "
            "the goal kick. Final score: Hanley Town FC 1-1 Stone Old Alleynians FC."
        ),
        "referee":          "Rob Milligan",
        "ref_u18":          "No",
        "submission_date":  "14/06/2026",
        "submitted_by":     "Rob Milligan",
    },

    # ── 19 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Loughborough Dynamo FC vs Hucknall Town FC",
        "competition":"Midland League Division One",
        "match_date": "15/06/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 90th minute of this game, the above-named "
            "player, Dean Morrison (shirt no. 14, Hucknall Town FC), deliberately "
            "handled the ball on the goal line, preventing a certain goal from home "
            "striker Curtis Flynn (shirt no. 9) whose shot was clearly goal-bound. "
            "I was positioned approximately 12 metres from the goal line and had a "
            "clear and uninterrupted view of Morrison extending his right arm to "
            "deflect the ball over the crossbar. There was no other defending player "
            "between Flynn and the goalkeeper at the time of the strike. I immediately "
            "awarded a penalty kick to Loughborough Dynamo FC and dismissed Morrison "
            "from the field of play under Law 12 (S4) for denying an obvious "
            "goalscoring opportunity by deliberately handling the ball, showing him "
            "the red card. Morrison accepted the decision without protest and left the "
            "field. The penalty kick was taken by Flynn but struck the crossbar and "
            "did not enter the goal. Play was restarted with a goal kick. The match "
            "concluded immediately following this incident. Final score: "
            "Loughborough Dynamo FC 2-2 Hucknall Town FC."
        ),
        "referee":          "Simone Carter",
        "ref_u18":          "No",
        "submission_date":  "16/06/2026",
        "submitted_by":     "Simone Carter",
    },

    # ── 20 ────────────────────────────────────────────────────────────────────
    {
        "fixture":    "Ramsgate FC vs Hythe Town FC",
        "competition":"Southern Counties East League Premier Division",
        "match_date": "17/06/2026",
        "abandoned":  "No",
        "club":       "Away Team",
        "report_details": (
            "I have to report that in the 61st minute of this game, the above-named "
            "player, Dean Parsons (shirt no. 6, Hythe Town FC), deliberately held "
            "back home forward Liam Oates (shirt no. 11) who had a clear and "
            "uninterrupted run through on goal, by grasping Oates by the left arm "
            "from behind and pulling him to the ground. The incident took place "
            "approximately 22 metres from the Hythe Town FC goal, outside the penalty "
            "area. I was approximately 10 metres from the incident and had a clear "
            "and uninterrupted view. At the time of the offence, Oates had beaten the "
            "last defender and in my opinion had an obvious goalscoring opportunity. "
            "There were no other outfield players between Oates and the opposing "
            "goalkeeper. I awarded a direct free kick to Ramsgate FC, dismissed "
            "Parsons from the field of play under Law 12 (S5) for denying an obvious "
            "goalscoring opportunity by an offence punishable by a free kick, and "
            "showed him the red card. Parsons accepted the decision without protest "
            "and left the field. The free kick was taken without further incident. "
            "The match concluded without further extraordinary incident. Final score: "
            "Ramsgate FC 1-0 Hythe Town FC."
        ),
        "referee":          "Gary Holt",
        "ref_u18":          "No",
        "submission_date":  "18/06/2026",
        "submitted_by":     "Gary Holt",
    },
]


def build_report_dataset() -> list[dict]:
    """Create 50 synthetic FA reports with repeated referees, clubs and varied incidents."""
    fixture_templates = [
        ("Riverside Athletic FC", "Northbridge United FC", "FA Cup Preliminary Round", "01/05/2026"),
        ("Oakridge Town FC", "Westfield Rovers FC", "FA Vase", "03/05/2026"),
        ("Bramley AFC", "Kingsford Town FC", "Isle of Man Senior Cup", "05/05/2026"),
        ("Marlowe FC", "Seabrook United FC", "Southern League Cup", "07/05/2026"),
        ("Harlow Athletic FC", "Dunston Rangers FC", "FA Trophy", "10/05/2026"),
        ("Northend United FC", "Riverside Athletic FC", "County Senior League", "12/05/2026"),
        ("Westfield Rovers FC", "Oakridge Town FC", "FA Vase", "14/05/2026"),
        ("Kingsford Town FC", "Bramley AFC", "League Cup", "16/05/2026"),
        ("Seabrook United FC", "Harlow Athletic FC", "FA Cup Extra Preliminary Round", "18/05/2026"),
        ("Dunston Rangers FC", "Marlowe FC", "Northern Premier League East", "20/05/2026"),
    ]
    fixture_dates = [
        "01/05/2026", "03/05/2026", "05/05/2026", "07/05/2026", "10/05/2026",
        "12/05/2026", "14/05/2026", "16/05/2026", "18/05/2026", "20/05/2026",
        "22/05/2026", "24/05/2026", "26/05/2026", "28/05/2026", "30/05/2026",
    ]
    referees = ["Sarah Jennings", "Mark Thompson", "David Osei", "Claire Hutchins", "Paul Nicholson"]
    repeated_clubs = [
        "Riverside Athletic FC",
        "Oakridge Town FC",
        "Northbridge United FC",
        "Westfield Rovers FC",
        "Bramley AFC",
    ]

    def build_details(index: int, club: str, home: str, away: str) -> str:
        minute = [12, 24, 37, 49, 61, 73, 81, 88, 90, 54][index % 10]
        player_one = ["Daniel Hartley", "Luke Pemberton", "Ryan Sutcliffe", "Jermaine Campbell", "Owen Price"][index % 5]
        player_two = ["Marcus Webb", "Nathan Cole", "Callum Reid", "Kyle Marsh", "Ben Hargreaves"][index % 5]
        templates = [
            (
                f"I have to report that in the {minute} minute of this game, following a dispute over a free kick, "
                f"{player_one} (shirt no. {7 + index % 5}, {home}) deliberately struck {player_two} (shirt no. {8 + index % 4}, {away}) "
                f"on the side of the face with an open hand. I was approximately 8 metres away and had a clear and unobstructed view. "
                f"{player_two} fell immediately and required treatment for several minutes before continuing. I asked {player_one} for his name, "
                f"informed him he was being dismissed for violent conduct under Law 12 (S2) and showed him the red card. "
                f"The match continued after a brief delay and I restarted play with the original free kick."
            ),
            (
                f"I have to report that in the {minute} minute, {player_one} (shirt no. {9 + index % 4}, {club}) made a reckless challenge "
                f"on {player_two} (shirt no. {11 + index % 3}, {away}) while contesting a loose ball. The challenge was late, with both feet off the ground, "
                f"and in my opinion endangered the safety of an opponent. I was approximately 12 metres from the incident and had a clear and uninterrupted view. "
                f"{player_two} received treatment on the floor and was replaced after the stoppage. I dismissed {player_one} for serious foul play under Law 12 (S1) "
                f"and awarded a direct free kick to {away}."
            ),
            (
                f"I have to report that in the {minute} minute a group of approximately 10 supporters attempted to enter the playing surface near the home technical area. "
                f"I immediately halted play and instructed both sets of players to retreat to the centre circle. I was positioned near the halfway line and had a clear view of the encroachment. "
                f"The stewards and the fourth official assisted in containing the issue, but the delay lasted approximately 14 minutes. "
                f"Because player safety could not be guaranteed, I took the decision to abandon the match in accordance with Law 5."
            ),
            (
                f"I have to report that in the {minute} minute, a spectator in the away enclosure directed a racially abusive remark towards {player_one} "
                f"(shirt no. {10 + index % 2}, {club}) as he was preparing to take a throw-in. I halted play immediately and spoke to both captains. "
                f"I then requested the individual be identified and removed by the home club officials. A tannoy warning was issued and the person was removed. "
                f"{player_one} confirmed he was willing to continue and play resumed after a delay of around nine minutes. "
                f"I later submitted a full written report to the County Football Association."
            ),
            (
                f"I have to report that in the {minute} minute, {player_one} (shirt no. {3 + index % 5}, {home}) and {player_two} (shirt no. {4 + index % 4}, {away}) became involved in a heated confrontation "
                f"after a robust challenge. {player_one} then pushed {player_two} forcefully in the chest, causing him to fall to the ground. I was approximately 6 metres away and had a clear and unobstructed view. "
                f"I addressed both captains and warned the players to disperse. I cautioned both sides for failing to retreat when instructed and dismissed {player_one} for violent conduct under Law 12 (S2)."
            ),
            (
                f"I have to report that in the {minute} minute, {player_one} (shirt no. {15 + index % 3}, {club}) deliberately handled the ball inside the penalty area and denied an obvious goal-scoring opportunity. "
                f"I was approximately 10 metres from the incident and had a clear view. I awarded a penalty to {away} and showed {player_one} a yellow card for the handball. "
                f"The offender accepted the decision without protest and the game resumed after a short delay."
            ),
            (
                f"I have to report that in the {minute} minute, following a collision between {player_one} (shirt no. {6 + index % 4}, {home}) and {player_two} (shirt no. {8 + index % 3}, {away}), "
                f"{player_two} remained on the ground and required treatment from the visiting physio for approximately six minutes. I was approximately 7 metres away and had a clear view of the incident. "
                f"I spoke to both players and, after reviewing the challenge, I cautioned {player_one} for reckless play and restarted play with an indirect free kick."
            ),
            (
                f"I have to report that in the {minute} minute, {player_one} (shirt no. {12 + index % 2}, {away}) challenged for a high ball, lost balance and made contact with {player_two} (shirt no. {14 + index % 3}, {home}) "
                f"with excessive force. The incident was seen by the fourth official and by the assistant referee. I was approximately 9 metres from the incident and had a clear and uninterrupted view. "
                f"I issued a yellow card for unsporting behaviour and restarted play with a dropped ball after a short stoppage."
            ),
            (
                f"I have to report that in the {minute} minute, {player_one} (shirt no. {5 + index % 4}, {club}) used abusive and offensive language towards an opposing player after a throw-in. "
                f"I stopped play immediately, spoke to both captains and warned the player about his conduct. I was approximately 5 metres away and had a clear and unobstructed view. "
                f"I then cautioned {player_one} for dissent and restarted play with a free kick to {away}."
            ),
            (
                f"I have to report that in the {minute} minute, after a challenge by {player_one} (shirt no. {13 + index % 4}, {home}) on {player_two} (shirt no. {16 + index % 4}, {away}), "
                f"a number of players from both sides gathered around the incident and delayed the restart. I was approximately 6 metres away and had a clear view. "
                f"I spoke to both captains, instructed the players to disperse and cautioned two players for failing to retreat. The game resumed after a brief delay."
            ),
        ]
        return templates[index % len(templates)]

    reports = []
    for i in range(1, 51):
        fixture = fixture_templates[(i - 1) % len(fixture_templates)]
        home, away, competition, match_date = fixture
        if i <= 10:
            club = repeated_clubs[(i - 1) % len(repeated_clubs)]
        elif i <= 20:
            club = repeated_clubs[(i - 11) % len(repeated_clubs)]
        elif i <= 30:
            club = repeated_clubs[(i - 21) % len(repeated_clubs)]
        elif i <= 40:
            club = repeated_clubs[(i - 31) % len(repeated_clubs)]
        else:
            club = repeated_clubs[(i - 41) % len(repeated_clubs)]

        report_date = fixture_dates[(i - 1) % len(fixture_dates)]
        referee = referees[(i - 1) % len(referees)]
        abandoned = "Yes" if i % 6 == 0 else "No"
        report = {
            "fixture": f"{home} vs {away}",
            "competition": competition,
            "match_date": report_date,
            "abandoned": abandoned,
            "club": club,
            "report_details": build_details(i, club, home, away),
            "referee": referee,
            "ref_u18": "No",
            "submission_date": fixture_dates[(i - 1) % len(fixture_dates)],
            "submitted_by": referee,
        }
        reports.append(report)

    return reports


REPORTS = build_report_dataset()

# ── PDF builder ───────────────────────────────────────────────────────────────

def build_pdf(data: dict, index: int, output_dir: str) -> str:
    """Render one FA Extraordinary Incident Report PDF and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"EI_Report_{(index + 21):02d}.pdf")

    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    W = A4[0] - 44 * mm   # usable width
    COL_LABEL = 52 * mm
    COL_VALUE = W - COL_LABEL

    # ── Paragraph styles ──────────────────────────────────────────────────────
    def ps(name, **kw):
        defaults = dict(fontName="Helvetica", fontSize=9,
                        leading=13, textColor=FA_DARK)
        defaults.update(kw)
        return ParagraphStyle(name, **defaults)

    s_title   = ps("title",   fontName="Helvetica-Bold", fontSize=16, leading=20)
    s_sub     = ps("sub",     fontSize=10, leading=13, textColor=MID_GREY)
    s_section = ps("section", fontName="Helvetica-Bold", fontSize=10,
                   leading=14, spaceBefore=10, spaceAfter=2)
    s_label   = ps("label",   fontName="Helvetica-Bold")
    s_value   = ps("value")
    s_body    = ps("body",    leading=14)

    # ── Helper: labelled two-column row ───────────────────────────────────────
    def field_row(label: str, value: str, body: bool = False) -> Table:
        t = Table(
            [[Paragraph(label, s_label),
              Paragraph(value, s_body if body else s_value)]],
            colWidths=[COL_LABEL, COL_VALUE],
        )
        t.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING",   (0, 0), (-1, -1), 0),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
            ("TOPPADDING",    (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        return t

    def hr(thick=0.5, colour=LT_GREY, before=2, after=4):
        return HRFlowable(width="100%", thickness=thick,
                          color=colour, spaceBefore=before, spaceAfter=after)

    # ── Build story ───────────────────────────────────────────────────────────
    story = []

    story.append(Paragraph("The Football Association", s_title))
    story.append(Paragraph("Extraordinary Incident Report", s_sub))
    story.append(Spacer(1, 4))
    story.append(hr(thick=1.2, colour=FA_RED, before=0, after=10))

    story.append(Paragraph("Fixture Details", s_section))
    story.append(hr())
    story.append(field_row("Fixture:",            data["fixture"]))
    story.append(field_row("Competition:",        data["competition"]))
    story.append(field_row("Match Date:",         data["match_date"]))
    story.append(field_row("Is Match Abandoned:", data["abandoned"]))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Report Details", s_section))
    story.append(hr())
    story.append(field_row("Club:",           data["club"]))
    story.append(field_row("Report Details:", data["report_details"], body=True))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Match Official Details", s_section))
    story.append(hr())
    story.append(field_row("Referee Name:",        data["referee"]))
    story.append(field_row("Is Referee U18?:",     data["ref_u18"]))
    story.append(field_row("Submission Date:",     data["submission_date"]))
    story.append(field_row("Report Submitted By:", data["submitted_by"]))

    doc.build(story)
    return filepath


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Generating {len(REPORTS)} FA Extraordinary Incident Reports ...\n")
    generated = []
    for i, report in enumerate(REPORTS, start=1):
        path = build_pdf(report, i, OUTPUT_DIR)
        generated.append(path)
        print(f"  [{i:02d}] {os.path.basename(path)}")

    print(f"\nDone — {len(generated)} PDFs written to:\n  {OUTPUT_DIR}")
    print("\n── How to add more reports ───────────────────────────────────────")
    print("Append a dict to the REPORTS list with these keys:")
    print("  fixture, competition, match_date, abandoned, club,")
    print("  report_details, referee, ref_u18, submission_date, submitted_by")
    print("\nWrite report_details as a referee would:")
    print("  - First person ('I have to report that...')")
    print("  - Include shirt numbers, player names, minute of incident")
    print("  - State your distance and confirm clear/unobstructed view")
    print("  - Quote exact words spoken (using single quotes)")
    print("  - Cite the Law 12 section (S1-S7) for dismissals")
    print("  - End with restart method and final score")


"""
Factual lookup

“Which match involved a red card for violent conduct?”
“What happened in report 05?”
“Which report mentions a spectator breach of the pitch?”
Entity-based questions

“Which players were named across these reports?”
“Which referee submitted the most reports?”
“Which clubs appear most often?”
Incident classification

“Show me all reports involving abusive language.”
“Which reports mention player injuries or treatment on the pitch?”
“Find all cases of abandonment.”
Rule and disciplinary questions

“Which reports mention Law 12?”
“Which incidents led to dismissal from the field of play?”
“Which matches resulted in a direct free kick or red card?”
Outcome and follow-up questions

“Which reports were submitted to the County FA?”
“Which incidents involved a delay longer than 10 minutes?”
“Which matches were abandoned due to safety concerns?”
Summarization and comparison

“Summarize the common patterns across these reports.”
“Compare violent conduct cases with spectator misconduct cases.”
“What are the most common types of extraordinary incidents in this set?”
Natural-language search

“Find reports about racial abuse.”
“Find matches where the referee had to stop play because of crowd trouble.”
“Show me reports where the player was dismissed and the match continued.”"""