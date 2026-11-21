#!/bin/bash
# Uso (PC com Node 18+, Java 17 e Android SDK): ./build.sh
set -e
npm install
[ -d android ] || npx cap add android
npx capacitor-assets generate --android
python3 patch_android.py
npx cap sync android
cd android && chmod +x gradlew && ./gradlew assembleDebug
echo "APK: android/app/build/outputs/apk/debug/app-debug.apk"
