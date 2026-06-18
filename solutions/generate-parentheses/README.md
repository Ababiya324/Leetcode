The rule is: take each string from the previous round and drop a fresh `()` into every gap, including the very start and very end.

For `()` (1 pair), the gaps are marked `_`:

```
_ ( _ ) _
```

Insert `()` at each:

- before everything: `()` + `()` → `()()`
- after the `(`: `(` + `()` + `)` → `(())`
- after the `)`: `()` + `()` → `()()` (duplicate, the set drops it)

So from `()` you get `()()` and `(())`, the two valid 2-pair strings.

Why every gap and not just some: every valid n-pair string has at least one `()` inside it. Delete that `()` and you get a valid (n−1)-pair string. Running this backward, every n-pair answer must come from inserting `()` somewhere into an (n−1)-pair answer, and that "somewhere" can be any gap, so you try them all and let the set kill repeats.
