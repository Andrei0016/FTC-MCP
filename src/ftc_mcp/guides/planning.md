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
1. Draft a concrete plan (steps, files, the approach and one alternative).
2. Run **plan-pro-advocate** and **plan-critic** on that plan.
3. Reconcile: adjust the plan to neutralize the critic's critical concerns; keep the
   strengths the advocate identified. If a critical concern can't be resolved, surface
   it to the user before coding.
4. Implement.

Both agents keep project-scoped memory — they get sharper about this robot over time.
