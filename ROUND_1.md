# Tempo V2 implementation round 1

## Qualified baseline

All nine local checkouts started clean on `feat/readable-modules`. The
implementation branches descend from these commits.

| Repository | Baseline | Accepted implementation |
| --- | --- | --- |
| `.planning` | `4e67368788b0a0d6505b03a4971eb3f63c730b25` | This ledger |
| `tempo` | `acedf953499bfd93c781cdcd29fc494dc33612c0` | `f25553ec9d8ff922888096a8f34b6c7c0bb4630f` |
| `tempo-chess` | `3de2b3a6341443ce8d151e4748617fbe94d8105b` | `46e611146dbbc8aa7b7e83cbd56c96b13761c4a9` |
| `tempo-core-components` | `3c05ab709ef426c422b3453d8965665e6704f6b8` | Baseline |
| `tempo-learning` | `a84a4c83bfe164fd1a3117d733621f63323e125b` | Baseline |
| `tempo-queue` | `866ba060d7e6f78293a34eeea0498c0cf806826c` | Baseline |
| `tempo-store` | `6457059e2312d2a2d15d9ab3f41a40ea17932da5` | `2bf63905ba5b475f652868b82ec8f4884f511977` |
| `tempo-study` | `4bfe734dd564965d370ae5c60c9a02e49ebfc095` | Baseline |
| `tempo-types` | `8662444cfb1ed1d2710c2bd95c4939473d6c0307` | Baseline |

Baseline checks passed with Rust 1.85.0 and the local workspace. Chess and Store
passed 49 unit tests and five doctests, Tempo passed 15 application contracts,
and the architecture gate and four self-tests passed.

## Interface decision

Real PGN needs the learner's color to distinguish exercises from context.
`ImportRequest::learner_color` is an approved optional Rust field with
`White` and `Black` choices. Real repertoire imports require an explicit choice.
Older JSON without the field decodes to `None` and fixture callers use `None`.
The Store trait, Tempo dependency directions, and version 1 Study wire contract
remain the integration baseline.

## Qualification

The two subprocesses used the same temporary SQLite file. The first imported a
White repertoire, issued a question, and committed an incorrect answer. The
second reopened the file and resumed the same attempt. Exact replay returned
the saved result without changing the snapshot. Reusing the ID with a changed
answer conflicted. Correction retained the original Again assessment, and the
next exercise received a distinct attempt ID.

| Check | Result on Rust 1.85.0 |
| --- | --- |
| `cargo test -p tempo-chess` | 43 unit tests and 3 doctests passed |
| `cargo test -p tempo-store` | 22 unit tests and 3 doctests passed. Six tests use real SQLite files, including simultaneous writers and rollback after a late SQL failure. |
| `cargo test -p tempo` | 33 unit tests, 16 application contracts, and 1 doctest passed |
| `cargo build -p tempo` and `node --test tempo/tests/ui_boundary.mjs` | Build and all 3 stdio/UI scenarios passed |
| `cargo fmt -p tempo-chess -p tempo-store -p tempo -- --check` | Passed |
| `cargo clippy -p tempo-chess -p tempo-store -p tempo --all-targets -- -D warnings` | Passed |
| `cargo doc --no-deps -p tempo-chess -p tempo-store -p tempo` with warnings denied | Passed |
| `python3 .planning/scripts/check_architecture.py .` and changed source diff whitespace checks | Passed |

An independent reviewer approved all three exact implementation heads above.
Review found that the chess library accepted incomplete FEN boards, invalid
empty-square encodings, and adjacent kings. The final Chess head rejects those
cases with regression coverage. Chess checks, architecture, and the assembled
restart journey passed again after the repair.

## Remaining scope

Round 1 qualifies orthodox repertoire mainlines and the two-process
import, study, restart, and replay journey against a temporary database.
Tactic and variation import, real game comparison, and production runtime
composition remain follow-up work.
SQLite evidence covers schema version 1, transaction rollback, and restart.
Schema upgrades, power-loss recovery, and larger-dataset performance remain
unqualified.
