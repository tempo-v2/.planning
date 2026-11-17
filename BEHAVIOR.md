# Shared behavioral examples

These are acceptance expectations, **not executed tests or implementation evidence**. See [ARCHITECTURE.md](ARCHITECTURE.md) for ownership and dependencies.

**R — established requirement:** learning identity, one repertoire response, whole-puzzle assessment, separated eligibility/order, same-day repeat semantics, flexible grading, and content preservation.

**D — v0.1 working default:** an operational choice, including immediate failure persistence, replay, stale-attempt checks, introduction, and restart behavior. These defaults do not imply that Andy separately selected every detail.

## Fixture vocabulary

- `R1/P1`: repertoire R1, canonical position P1, prescribed response M1.
- `T1`: one tactic with two learner decisions and an automatic opponent reply; one puzzle schedule.
- An **exercise/attempt** assesses one target. A **queue block** orders exercises without combining learning identities.
- Use fixed instants on configured Study dates `2026-11-17` (`D`) and `2026-11-18` (`D+1`), with supplied clock/randomness.
- Unless stated otherwise: active valid content, unassisted attempts, credit-eligible targets. Attempts retain issued content versions and miss revisions.

## First implementation examples

| ID / basis | Given and action | Required observation | Primary owner / boundary |
| --- | --- | --- | --- |
| B01 — R | R1/P1 is due. A fresh attempt submits M1. | The grader reports one clean success. Learning applies the eligible success policy to R1/P1. No line occurrence receives a separate schedule. | Chess + Study; Learning |
| B02 — R | A fresh T1 attempt answers both learner decisions correctly. | The first answer advances presentation without a terminal assessment. The final answer completes one successful puzzle assessment. The opponent reply receives no learner grade. | Chess + Study |
| B03 — R/D | T1's first or second learner decision is wrong; the learner then corrects it and finishes. | The first accepted miss commits one terminal failure/Again immediately. Correction can continue presentation but cannot replace the failure, produce Good, or clear the repeat. Reload preserves that accepted failure. | Study + Learning; Tempo + Store |
| B04 — R | T1 was missed on D. A **new** attempt, opened after the latest miss, completes cleanly on D. | The outstanding repeat clears. T1 remains due on D+1; the repeat does not extend its interval. Correct continuation of B03's failed attempt cannot satisfy this example. | Learning; application integration |
| B05 — R | A tiny instructional fixture accepts choice B instead of a chess move. | The same Study protocol presents, accepts input, invokes its supplied grader, and completes without a chess type. This fixture proves the interface; no additional product feature is required. | Study |
| B06 — R | One fixed snapshot produces eligible targets {R1/P1, T1, N1}. Apply two ordering policies. | Both outputs contain the same selected targets and respect block order. Only presentation order differs. Neither policy changes due dates, introduction state, or repeat obligations. | Queue |
| B07 — R/D | An external source submits an identified Again for R1/P1 without a human attempt. | Ordinary learning policy records the miss and repeat obligation. Scheduling uses acceptance time; observation time remains provenance. Retrying follows B08. | Learning; Tempo + Store |
| B08 — D | A submission commits, but its response is lost. Retry that submission; also try another event ID for the same terminal human attempt. | The identical retry returns the original result without another learning effect. The second ID cannot create a second terminal grade. Reusing an ID with different meaning is a conflict. A failed transaction leaves no partial grade. | Tempo + real Store transaction |

## Shared content and lifecycle examples

| ID / basis | Given and action | Required observation | Primary owner / boundary |
| --- | --- | --- | --- |
| B09 — R | Two lines transpose to P1, or one line visits P1 twice. Import a competing response for R1/P1. | Occurrences retain their contexts but share one target and schedule. The conflicting response prevents that content change from activating. Another repertoire's response remains independent. Enforce this with actual unique/foreign-key constraints. | Chess + Store |
| B10 — R | Queue groups two eligible repertoire exercises with intervening context moves. | The exercises remain contiguous and individually assessed. Autoplayed context earns no credit. A tactic remains one queue exercise even when it contains several learner decisions. Grouping cannot make an ineligible target eligible. | Queue + Study |
| B11 — D | Attempt A opens; a newer miss occurs; a fresh repeat clears it; A later succeeds, even on D+1. | A cannot clear the newer miss or earn positive credit. Clearing a repeat does not erase the miss revision used to identify stale attempts. | Learning; Tempo + Store |
| B12 — R/D | Edit annotations, then replace M1 with M2 for R1/P1. Submit an uncommitted attempt issued for M1. | Metadata preserves progress. The changed answer versions and resets only affected learning while retaining history. All occurrences agree; other repertoires remain unchanged. The stale attempt is refused. An already committed old result remains replayable without changing M2's learning. | Chess + Learning; Tempo + Store |
| B13 — R/D | Import older enriched PGN into a live dataset; separately restore compatible content/current progress into an empty destination. | Ordinary import does not overwrite local progress. Restore uses a new dataset identity and preserves semantic content, target sharing, current learning facts, and policy settings. At the same fixed time, the same next grade produces the same schedule. Old pending commands cannot mutate the restored dataset. | Chess + Learning; Tempo + Store |
| B14 — R/D | No eligible targets remain; alternatively, one puzzle is invalid or the game provider is unavailable. | Empty is normal, distinct from operational failure. Isolate invalid content while valid targets remain usable. Study neither waits for game fetching nor spins on an empty queue. | Queue + Tempo; Store/content validation |
| B15 — R/D | Reimport an identical tactic; then import a distinct solution at that same canonical practice-start position. | Exact duplicate content adds provenance without resetting learning. Distinct unresolved candidates are quarantined together, preserving their content/history and unrelated usable puzzles until explicit resolution. | Chess + Store |

## Operational defaults used by these examples

New repertoire eligibility takes the first unintroduced learner target per active line, unioned and deduplicated. Introduce on accepted Good or Again, not display. Randomize eligible exercises; insert a distinct miss after 5–10 other exercises when available. A tactic counts once. Short decks use available alternatives; with none, allow a fresh immediate repeat. Reload may rebuild order while preserving learning obligations.

## Validation ownership

Run pure examples in their owning crates with independent expected results. Use production database constraints for atomicity, replay, content changes, and restore. Tempo owns the cross-component journey. Ordering-only changes require no browser/database suite; persistence changes prove their affected transactions. Record execution evidence separately.
