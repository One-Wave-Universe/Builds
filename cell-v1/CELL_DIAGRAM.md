# Three differentials

Cell-0 is *one* of these. The cell at law is three.

```
                         V_BUS  (separate reference)
                           |
              +------------+------------+
              |            |            |
           steer A      steer B      steer C
              |            |            |
            C_A          C_B          C_C     local caps
              |            |            |
           wind A       wind B       wind C
              |            |            |
           HB A         HB B         HB C     half-bridges
              |            |            |


        DA+          DB+          DC+        drains / + seats
         |            |            |
        QA+          QB+          QC+
         |            |            |
         +------+-----+------+-----+         sources
                |
             CENTER  (one home for all three D's)
                |
               V0

        QA-          QB-          QC-
         |            |            |
        DA-          DB-          DC-        - seats


      [core A]      [core B]      [core C]
        at A+         at B+         at C+
      A- is the other end of core A. Not a second core.

      D_A = DA+ - DA-     (vs CENTER)
      D_B = DB+ - DB-
      D_C = DC+ - DC-
```

Two-of-three reads those three D's. V_BUS never substitutes for CENTER.
