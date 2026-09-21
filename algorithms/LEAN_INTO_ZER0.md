# Zer0 and the lean — not memory

Memory is not a receipt. Memory is not a row. Memory is the lean still in the path after the signal has passed.

Zer0 does not store memory. Zer0 may only:

- notice a lean (READ / COMPARE)
- propose a next lean (use)
- refuse to treat that proposal as real until T6 RESOLVE → REBASE

After T6, the *hardware* holds the lean. The number in `lean_weight.py` is a pointer for the lock rule in a sandbox. If the pair is powered down long enough for the magnetic / analog state to fade, that number is a lie. The body forgot. The file did not remember for it.

## Map (talk, not storage)

| In the body | In Zer0 talk |
| --- | --- |
| floating VGND | next center after T6 |
| direction / magnitude / hardness | PLUS/MINUS, how far, how stiff |
| HOLD | live balance, current still flowing |
| use | propose |
| T6 | allowed to treat the proposal as the new lean *if the body still has it* |
| disuse | body fades; software must not pretend it didn't |

## Rule

Do not update a software `q` and call it memory.
Do not keep `q` after the bench state is gone.
The only memory interface is use and time on the cell.
