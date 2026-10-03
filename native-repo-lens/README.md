# Repo Lens — native Android and Linux

These are native clients, not a WebView or a website shortcut. Android uses
platform Activity/widgets, Java HTTPS and a launcher entry. Linux uses native
Tk widgets and a standalone packaged Python executable. Both reuse the existing
GitHub Actions/Jetson provider backend without cloning repositories.

The user installs only an APK or executable. Source builds run on ephemeral
GitHub builders, not the laptop. No external drive or local Android SDK is
needed to use the resulting programs. Linux release target: x86_64, Ubuntu
22.04 or newer (including the Dell's Ubuntu). Android minimum: Android 8.

## Use

1. Select a repository, AI slots and a question.
2. Choose **Reference and prepare**. Fresh default-branch heads, complete
   manifests and canonical root instructions are read in memory. Truncation,
   submodules or drift stop preparation.
3. Choose **Submit prepared question on GitHub**. Your normal browser opens the
   prefilled GitHub commit screen. Sign in there and commit to start the run.
   No terminal commands or copy/paste are needed. Until a secure native write
   connection is provisioned, the final GitHub commit is a user action.
4. Choose **Read current result once**. This is a single request, never timed
   polling. The result shows real slot states, answers, pieces read and source
   evidence. Source/metadata view contains unchanged receipts and manifests.

Questions/results are public in Builds. Model credentials stay at the backend.
Claude's invocation disables tools; neither native client exposes a local shell
or repository download operation. No cloning, archives, worktrees, scheduled
retries or timer-driven model cycles. Desktop settings are a small JSON file;
Android settings use app preferences. A bootstrap manifest is explicitly not a
claim that all contents have been read: the backend enforces full source reading.

Native installation does not fix blocked providers. GPT/Gemini peer exchange
was verified earlier; DeepSeek full-cycle validation, Claude sign-in and Grok
authentication are separate backend boundaries. The clients show HOLD honestly.

## Building

Workflow `.github/workflows/repo-lens-native.yml` builds the Android APK and
Linux executable, checks Android lint and native contract tests, and starts the
frozen Linux UI under Xvfb. APK uses the normal debug signature for sideloading;
production distribution needs a durable private signing key. Nothing is
published to Google Play or installed on a user device automatically.

Android: JDK 17, Gradle 8.9, Android plugin 8.7.3, API 35.
Linux: Python/Tk, PyInstaller. Linux GUI smoke is not a hardware installation
test. Android compile/lint is not a phone launch test; launch on a phone remains
an explicit verification boundary.
