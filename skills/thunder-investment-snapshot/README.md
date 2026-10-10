# Thunder Investment Snapshot

Create dated, source-backed investment snapshots for Thunder Accounting from holdings context supplied by the user and authorized public price or NAV data.

## Use this skill when

- The user asks to value, update, or review their Thunder Accounting holdings.
- A position has a missing market value and its units, buy date, or dated cash flows can be verified.
- The user provides the app-generated `context.json` needed to prepare a scoped snapshot proposal.

## What it does

The agent checks each instrument against an appropriate public source, calculates values with the source's actual date, preserves quantity and cost meanings, accounts for confirmed cash flows, and groups products only when their shared underlying exposure is explicit. It then prepares one app proposal through the bundled helper when the host has the required local-file capability.

The helper stages a proposal in the app-managed inbox. The app remains responsible for validating the session, holdings baseline, and account-scoped auto-apply setting.

## Requirements

- A current `context.json` exported by Thunder Accounting and supplied by the user.
- Node.js 18 or newer to run `scripts/submit.mjs`.
- Public issuer, fund-manager, exchange, or reputable market-data pages for any valuation that needs a price or NAV lookup.

The helper uses only Node.js built-in modules and makes no network, database, cloud, broker, or confirmation calls.

## Example

Give the agent the requested holdings statement or the specific authorized holdings file and the current app context. The agent should report each valuation source/date and calculation, then stage one proposal only if it can meet the skill's data and app-context requirements. For example, a currency-amount fund position may be reconstructed from confirmed contributions and effective-date NAVs; any uncertain fee or flow treatment must be disclosed instead of guessed.

## Limits and safeguards

- This skill provides recordkeeping calculations, not investment recommendations or trading instructions.
- Public values are dated snapshots or clearly labeled estimates, not live or intraday prices.
- It never logs in to a broker, trades, changes the ledger directly, or treats a missing value as zero.
- If the user has not supplied a valid app context, the helper cannot create an app-scoped proposal.
- An estimate can differ from the final fund statement due to fees, rounding, settlement timing, or source publication delays; the source date and assumptions remain visible.

Read [SKILL.md](SKILL.md) for the complete workflow and [the proposal protocol](references/protocol/README.md) for the app data contract.
