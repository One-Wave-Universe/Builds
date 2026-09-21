# Hex seats (clockwise)

Point-up. Ports at **edge centers**, not corners.

Clockwise from top-right-ish starting at A+:

```
              A+
         /           \
      F /             \ B+
       |               |
    C- |      +        | B+
       |    CENTER     |
      E \             / C+
         \           /
              A-
```

That sketch is messy if sides don’t match. Use the **side index** instead:

```
Side 0  A+
Side 1  B+
Side 2  C+
Side 3  A-
Side 4  B-
Side 5  C-
```

Walk clockwise: `A+ → B+ → C+ → A- → B- → C- → A+`

```
                    side 0
                     A+
                 _________
                /         \
      side 5   /           \   side 1
         C-   /             \   B+
             |               |
             |     CENTER    |
             |               |
      side 4  \             /   side 2
         B-    \           /    C+
                \_________/
                    A-
                   side 3
```

Mirrors (opposite sides = three hops):

- A+ ↔ A-   (side 0 ↔ side 3)
- B+ ↔ B-   (side 1 ↔ side 4)
- C+ ↔ C-   (side 2 ↔ side 5)

That is one differential per letter. Six seats, three D’s.

Core of axis A lives at A+ (side 0). A- (side 3) is the other end of that core.
