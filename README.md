# Zotero Android Nightly Build

![Official Repo GitHub Tag](https://img.shields.io/github/v/tag/zotero/zotero-android?label=Version%20from%20Offical%20Repo)
![GitHub last commit](https://img.shields.io/github/last-commit/zotero/zotero-android)
[![Zotero Android CI](https://github.com/zotero/zotero-android/actions/workflows/android.yml/badge.svg)](https://github.com/zotero/zotero-android/actions/workflows/android.yml)

![GitHub Release](https://img.shields.io/github/v/release/northword/zotero-android-nightly-build?label=Version%20from%20This%20Repo)
![GitHub Release Date](https://img.shields.io/github/release-date/northword/zotero-android-nightly-build)
[![Daily Build Zotero Android](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml/badge.svg)](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/northword/zotero-android-nightly-build/total)

This repository pulls the latest code from the [zotero/zotero-android](https://github.com/zotero/zotero-android) repository daily and executes a debug build, the generated build output is published in the [Artifacts of the current workflow run](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml) and [GitHub Release](https://github.com/northword/zotero-android-nightly-build/releases).

## Get Apks

Each release may contain multiple assets corresponding to all commits after each tag push in the zotero-android repository, with the file name `app-dev-debug-${versionName}-${commitHash}.xpi`.

<details>
<summary>From Artifacts</summary>

In the zip file, `app-dev-debug.xpi` is the installation package: 

```plain
app-outputs.zip
|-- apk
|   `-- dev
|       `-- debug
|           |-- app-dev-debug.apk
|           `-- output-metadata.json
`-- logs
    `-- manifest-merger-dev-debug-report.txt
```
    
</details>

## Sync with upstream build workflow

The build steps of this repo's `ci.yml` mirror the upstream [`zotero/zotero-android` `android.yml`](https://github.com/zotero/zotero-android/blob/master/.github/workflows/android.yml). The auto-synced region covers the environment setup steps (`set up JDK`, `set up Python`, etc.) and the bundle scripts, so upstream's Java/Python/action-version bumps are picked up automatically. Steps that need upstream secrets (PSPDFKit key, keystore, google-services decrypt) and the Google Play deploy step are intentionally excluded.

The [`Sync Upstream` workflow](.github/workflows/upstream-watch.yml) runs twice a day and:

1. Fetches the latest upstream `android.yml` and compares it with the committed reference [`.github/upstream-android.yml`](.github/upstream-android.yml).
2. When the upstream workflow changes, it runs [`scripts/sync_ci.py`](scripts/sync_ci.py) to update the build steps in `ci.yml`, then opens a pull request (labeled `upstream`) containing the change and the full diff. The reference file is updated so the same change is only reported once.

You can also run it manually via **Actions → Sync Upstream → Run workflow**, or run the script locally:

```bash
python3 scripts/sync_ci.py .github/workflows/ci.yml .github/upstream-android.yml
```

## Disclaimer

> [!IMPORTANT]
> 
> This build is not a release version tested by Zotero and is extremely unstable, it is for trial use only and should not be used for production purposes.
> 
> I am not responsible for any consequences caused by APPs downloaded from this repository!
