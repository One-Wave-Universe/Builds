# Native Repo Lens boundaries

Read the current GitHub reference before working. These clients are transport
and result viewers; software receipts are not physical-memory evidence.

Never clone, mirror, download a repository archive, create a worktree, or copy
repository contents onto the user's laptop, phone, Jetson or external drive.
Use GitHub HTTPS API and pinned raw files in memory. App settings and selected
result receipts are allowed; keep them small. Installing an APK or executable
does not require installing its source repository or build toolchain.

Claude must not run shell, filesystem or native MCP tools through this app.
The backend Claude invocation uses `--tools '' --no-session-persistence`.
Provider credentials stay at the existing backend; never embed them in either
binary or ask the user to paste them into app source or chat.

Model workers advance on completed responses, independently. Do not add timer
polling, scheduled retries, sleep loops or automatic repeated failed requests
to either native client. A user-initiated result read is one network operation.

Builds may check out this source on an ephemeral GitHub build runner. Do not
run builds or install a compiler/SDK on a user's device without task authority
and a verified storage check. Preserve working branches and build in a new one.
