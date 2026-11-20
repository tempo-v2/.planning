# First visit, existing experience

One agent used a fresh Chrome context, receiving the goals and fixture only. Findings describe this attempt, without human usability validation. The missing engines and token reflect the supplied environment.

| Goal | Action and observation | Confidence |
|---|---|---|
| 1. Import and find the opening decision | Games → Source → PGN file accepted Andy and recent.pgn. One new game, no learner deviations. Matched the new row by its counts because all four were called “PGN file game · andy”. Analyze this game opened an unconfigured detector. Compatibility identified an Italian gap at half-move 6. I inferred Nd4 by comparing the gap list before and after import. Fix response confirmed 3…Nd4. | High on import, moderate on identification |
| 2. Navigate and explore | The imported game row offered no move list. From the separate Nd4 gap I followed Fix response → Analyze lines. Clicked d3, Nf6, O-O from the move table and used Back one move. In the correction for a different game I could step backward and forward in its replay. I could explore from a gap, but could not select an arbitrary position of the imported game. | Partial |
| 3. Compare against intended repertoire | “Italian repertoire” and “Similar repertoire positions” provided d3 from two examples. The analysis table distinguished nearby examples, but I could not establish that a suggested nearby move was the saved answer at this position before saving. | Partial |
| 4. Save selected continuation | At d3 Nf6 O-O, Mark line → Preview changes showed that line, two new positions and zero changed answers. Save repertoire displayed “Repertoire saved.” The Nd4 gap disappeared on return. | High |
| 5. Recognize transposition | Checked another game’s compatibility disclosure. It said “Authored line ended on half-move 10” and counted matches. I could not identify which board position matched by another move order or its saved response from this game. | Unresolved |
| 6. Understand conflict | Returned three plies from the saved branch, explored c3 and previewed it. The preview showed d3 → c3 and named the O-O descendant that would retire. I left the preview without saving. | High |
| 7. Review a prepared answer played differently | Study immediately displayed the Italian correction, preceding moves, played Bb5, prepared Bc4. Replay game let me step through to Bb5. The Games row separately described the learner deviation by half-move and said the repair was ready in Study. | High |
| 8. Resume later | Reload landed in Study. Returned to Games and saw Nf6 still needs a response. Nd4 was gone from the gap list while the game still said “Recorded only” and counted one opponent deviation. Without remembering the prior gap, I could not identify finished analysis from this screen. | Partial |
| Empty case | Followed Games in a separate empty instance. “Save a repertoire before comparing games” linked to Repertoires. Game evidence said “No games recorded yet”. Date/account forms, historical backfill, modeled reach counters and gap analysis were all displayed before the first game. | High |

Screenshots 01–06 capture initial Study, import, marked-line preview, conflict preview, returning Games and empty Games respectively.

## Screenshots

[Initial Study](01-study.png) · [Import](02-import.png) · [Marked-line preview](03-preview.png) · [Conflict](04-conflict.png) · [Return to Games](05-return.png) · [Empty Games](06-empty.png)
