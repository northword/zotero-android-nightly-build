# Zotero Android Nightly Build

![GitHub last commit](https://img.shields.io/github/last-commit/zotero/zotero-android)
[![Zotero Android CI](https://github.com/zotero/zotero-android/actions/workflows/android.yml/badge.svg)](https://github.com/zotero/zotero-android/actions/workflows/android.yml)
[![Daily Build Zotero Android](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml/badge.svg)](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml)

This repository pulls the latest code from the [zotero/zotero-android](https://github.com/zotero/zotero-android) repository daily and executes a debug build, the generated build output is published in the [Artifacts of the current workflow run](https://github.com/northword/zotero-android-nightly-build/actions/workflows/ci.yml).

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

> [!IMPORTANT]
> 
> This build is not a release version tested by Zotero and is extremely unstable, it is for trial use only and should not be used for production purposes.
> 
> I am not responsible for any consequences caused by APPs downloaded from this repository!
