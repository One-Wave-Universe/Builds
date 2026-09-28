# Migration Map

## Destinations

| Class | Repo |
|---|---|
| Iron / architecture / CELL | `One-Wave-Universe/Builds` |
| Pipes / Jetson / AI relays | `One-Wave-Universe/Bridge-Comand` |
| Math / hypothesis | Science repos |
| Fiction | `Mythos-and-Stories` |

## Content-preserving routing

| Source material | Destination |
|---|---|
| Rabbit Hopping files | Builds `algorithms/` |
| `Hardware_Packets/` | Builds `Hardware_Packets/` |
| `Virtual_Breadboard/` | Builds `Virtual_Breadboard/` |
| `CELL_V1_*` | Builds `cell-v1/` |
| `VTC_BUILD_ARCHITECTURE.md` | Builds architecture |
| Hardware *measurement* notes from `One_Wave_Bench/` | Builds `cell-v1/` or `bench-notes/` |
| `One_Wave_Bench/hive-pipe` and relay scripts | **Bridge-Comand `hive-pipe/`** |
| `Workshop/` terminal / adapter | **Bridge-Comand** |
| Jetson command workflows | **Bridge-Comand `.github/workflows` + `scripts/`** |

## Handling rule

Documents can be split. A file that is half magnetics and half SSH goes: magnetics → Builds, SSH → Bridge.
This map is not evidence that hardware has been validated.
