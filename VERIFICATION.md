# Readability refactor verification

Prepared and checked 2026-11-17. This report describes the source change and the
checks actually run, not a release installed on Andy's machine.

## Verified GitHub starting state

All nine repositories contain the pushed `feat/interface-scaffold` branch. The
latest Types, Study, and application view splits are present on that branch and
were used as the base for this work. The older `main` scaffold was not used as the
refactor baseline. These feature heads were checked again before delivery:

| Repository | Exact `feat/interface-scaffold` base |
| --- | --- |
| `.planning` | `321a73039c5feb411590ae210a508e80a9f918f6` |
| `tempo-types` | `ad09bbe7d70e7737b1140d3f0f3f7a4746c237b2` |
| `tempo-study` | `4a9773fcb4959b41a55f50ed4cba79c21a428806` |
| `tempo-queue` | `248c8dbc0aeeddac99abc5178f0664bc425af678` |
| `tempo-learning` | `efa6214085db05d9069f4097c91ceef0f0de275f` |
| `tempo-chess` | `c080da41aba4b2d17c0359179c6bf137e4c1ced3` |
| `tempo-store` | `cd001152df8ef40976074ea90c0d3d20227bc802` |
| `tempo` | `e29f0a4ae5085a2dcf711cd91fa98b3ef19e4b0a` |
| `tempo-core-components` | `8123bb74d7b834a7f7ce2bd22a9d70574fee5890` |

The new local branch is `feat/readable-modules` in each source tree. No source
checkout from earlier work was reset or overwritten. No local `AGENTS.md` files
were present in these nine checked-out trees.

## What changed

- Concrete shared IDs and counters have named files, explicit definitions, and
  usage contexts. Existing grouping and root paths remain.
- Domain records, traits, operations, and replaceable adapters are separated into
  named modules. Each component README maps concept → source → scenario.
- Rust usage scenarios live in the module they explain. Shared helpers construct
  fixtures; the scenario's action and assertion remain near its owner.
- The app's integration target remains `contracts`; its fifteen existing journeys
  are now grouped by subject in named files. The UI keeps the existing public
  barrel and test entry point, with adjacent scenario files for its modules.
- [READING_GUIDE.md](READING_GUIDE.md) provides a cross-component map and explains
  identity/version distinctions and runtime calls versus dependency direction.
- Qualification now builds rustdoc with warnings denied, in addition to running
  compile examples. Documentation links are part of the checked reading surface.

The initial feature head did not compile across components: shared `Grade` and
several Study root exports were missing after an unfinished split, and moved app
views needed imports/re-exports. Those connections are repaired. There is one
canonical `tempo_types::Grade`, re-exported through `tempo_study::grader::Grade`,
so Learning does not acquire a dependency on Study. The incomplete Progress test
and placeholder documentation example are replaced with real scenarios.

## Executed evidence

Toolchain: Rust/Cargo 1.85.0, Node 24.22.1, Python 3.12.14. The complete
`scripts/qualify_scaffold.py` run passed after all source changes.

| Check | Result |
| --- | --- |
| Types | 11 same-module tests + 1 compile-fail documentation example |
| Study | 27 same-module tests, including a complete non-chess grader |
| Queue | 24 same-module tests + 1 compiling documentation example |
| Learning | 19 same-module tests + 1 compiling documentation example |
| Chess | 33 same-module tests + 3 compiling documentation examples |
| Store | 16 same-module tests + 2 compiling documentation examples |
| App | 33 same-module tests + 15 retained integration journeys + 1 compiling documentation example |
| UI component/controller | All 10 retained scenarios passed |
| Actual Rust process ↔ UI controller | All 3 retained boundary tests passed |
| Architecture negative checks | 4 tests passed |
| Workspace setup/migration | 4 tests passed |
| Resolved dependency/source boundary gate | Passed: the same seven package identities and allowed import directions |
| Rust formatting, strict Clippy, and app build | Passed across the workspace/all targets |
| Rust documentation | Built with warnings denied; compile examples pass |
| README/guide source links and whitespace | Relative source paths resolve; `git diff --check` passes |

That is **178 Rust unit/integration tests, 9 documentation compile checks, 13 Node
tests, and 8 Python checks: 208 checks with test results**, plus the dependency
gate, build, formatting, Clippy, and documentation build. This count describes
scope; it is not a claim that test count proves compatibility.

## Independent review

A second reader reviewed each implementation area. Public struct/enum/trait
layouts, serde attributes, root exports, and production algorithm bodies were
compared against the feature baseline. Aside from the required connection repairs,
changes are organization, explicit definitions replacing small type macros,
documentation, usage scenarios, formatting, and private helper names/visibility.
No Cargo/npm dependency or public serialized field/variant was changed.

Review specifically checked sticky terminal outcomes, immediate first-miss
recording, stale positive suppression, ordering/group validation, receipt replay
before currency checks, atomic staging/publication, restore identity, and unchanged
UI command construction/retry. Small documentation corrections clarify that Queue
and Study do not receive scheduler memory, only fresh same-day repeats bypass the
scheduler, and Store validates the resulting learning state.

## Delivery and limits

The connected GitHub integration again rejected creation of `feat/readable-modules`
with HTTP 403, `Resource not accessible by integration`. No remote branch or commit
was created by this refactor. The update bundle contains a per-repository patch,
exact base commit, final per-path hashes, source snapshot, and apply instructions.
Its helper uses a new feature branch and refuses mismatched/modified baselines;
commit/push are explicit options using the user's normal Git configuration. It
never merges `main`. Bundle-specific application checks are recorded with the
bundle, separately from the source qualification above.

This refactor does not implement real PGN/canonicalization/comparison algorithms,
FSRS, random/repeat-spacing policy, SQLite durability/migrations, a graphical board,
browser event binding, or production transport. Existing fixtures remain explicit.
Study is generic; App/Store/UI remain concrete chess models. Whole-dataset snapshots
and future installed-release compatibility still have their previous limits.

For historical context, the initial interface-scaffold qualification had 48 Rust,
13 Node, and 8 Python tests (69 total). Those component behaviors remain exercised;
the new scenarios explain their individual values and boundaries more directly.
