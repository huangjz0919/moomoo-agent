# Prompt Sections For topic-review

This skill comes from:

- `<QUALITY_CHECKLIST>`
- `<CAUSALITY_RULE>`
- `<CAUSALITY_SEPARATION_RULE>`
- `<NEUTRALITY>`
- `<TICKER_FORMAT>`

Key inherited checks:

- Stop with `<ERROR>Insufficient source material</ERROR>` when source content is empty, unreadable, link-only, or irrelevant.
- Every factual claim must be supported.
- Do not treat source links as factual content by themselves.
- Avoid unsupported causal wording.
- Do not merge separate facts into unsupported causal statements.
- If causality is missing, state observable facts only.
- Omit missing details instead of guessing.
- Title uses Title Case and stays within 95 characters, including spaces, punctuation, and digits.
- Summary is within 70 words and uses a standalone bold discussion question as the second paragraph.
- Poll is neutral and discussion-oriented.
- Tickers are formatted correctly.
- Content uses ASCII punctuation and an official tone.
