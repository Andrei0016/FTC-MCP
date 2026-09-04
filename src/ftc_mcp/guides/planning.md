# Planning workflow — two adversarial agents

At project setup, `create_ftc_project` installs two subagents in `.claude/agents/`:

- **plan-pro-advocate** — builds the strongest honest case *for* a proposed plan.
- **plan-critic** — adversarially attacks the plan for risks, blind spots, failure modes.

## When to use them
Before implementing anything non-trivial:
- a new subsystem or a control strategy (PID vs bang-bang, feedforward tables, …)
- a new autonomous routine or a change to path strategy
- a refactor that touches `Robot` or a base opmode
- a hardware/architecture decision

Trivial changes (rename, constant tweak, one-line fix) don't need them.

## The loop
1. **Ask the user** anything needed to understand the task before drafting — target
   hardware, constraints, which alliance/routine, acceptable tradeoffs. Don't guess at
   requirements that change the design.
2. **When you judge the task hits the trigger list above, ask the user first whether it
   needs a plan for this specific task** (e.g. "this looks like a design decision — want
   me to draft a plan and run it past the two planning agents before I implement?").
   Don't assume — some "serious-looking" changes are ones the user has already decided on
   and just wants built. If they say no, skip straight to implementing.
3. If they say yes: **ask the user to confirm the task is understood correctly and
   outline the intended approach *before* drafting the full plan and running the
   agents** — cheap to redirect early, expensive after two agents have argued over the
   wrong plan.
4. Draft a concrete plan (steps, files, the approach and one alternative).
5. Run **plan-pro-advocate** and **plan-critic** on that plan.
6. Reconcile: adjust the plan to neutralize the critic's critical concerns; keep the
   strengths the advocate identified.
7. **Present the reconciled plan to the user and get their go-ahead before implementing**
   — this is required for every serious task, not just when a critical concern remains
   unresolved.
8. Implement.

Trivial changes skip straight to implementing — no pre-check, no ask, no agents, no plan
presentation.

Both agents keep project-scoped memory — they get sharper about this robot over time.
