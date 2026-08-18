### Upstream `android.yml` has changed

Diff against [zotero/zotero-android](https://github.com/zotero/zotero-android/blob/master/.github/workflows/android.yml):

```diff
--- .github/upstream-android.yml	2026-08-18 10:56:07.076344779 +0000
+++ upstream-android.yml	2026-08-18 10:56:07.311267437 +0000
@@ -15,18 +15,18 @@
     runs-on: ubuntu-latest
 
     steps:
-      - uses: actions/checkout@v4
+      - uses: actions/checkout@v6
         with:
           submodules: recursive
       - name: set up JDK
-        uses: actions/setup-java@v3
+        uses: actions/setup-java@v5
         with:
           java-version: '17'
           distribution: 'zulu'
           cache: gradle
 
       - name: set up Python
-        uses: actions/setup-python@v5
+        uses: actions/setup-python@v7
         with:
           python-version: '3.10'
 
```
