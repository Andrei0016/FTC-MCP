# Accuracy — only state what you can verify

The FTC SDK, Pedro Pathing and Panels are poorly documented. Guessing produces code
that does not compile and advice that wastes the team's time. Hold to this:

## Rules
- **Only provide information you are sure of and can verify.** If you have not confirmed
  a method name, signature, constant, behaviour or version, do not present it as fact.
- **Verify against the decompiled reference before using any library API:**
  `sdk_search("...")`, `sdk_class("Follower")`, `ftc://sdk/<lib>/<package>`,
  `ftc://sdk/<lib>`. For project code, check the file or the map.
- **When you cannot verify, say so.** State plainly that you are unsure, name what would
  confirm it (a doc, the source, a test), and either go check or ask — never fill the
  gap with a plausible guess.
- **Distinguish fact from inference.** Mark anything you are reasoning about rather than
  confirming ("I believe", "this likely") so the reader knows to check it.
- **No invented identifiers.** Class names, package paths, enum values, config keys and
  hardware names must come from the reference or the codebase, verbatim.
