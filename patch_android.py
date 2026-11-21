# Aplica: ecrã horizontal, ecrã inteiro e suporte a notch no projeto Android gerado.
import re, pathlib
m = pathlib.Path("android/app/src/main/AndroidManifest.xml")
t = m.read_text()
if "screenOrientation" not in t:
    t = t.replace("<activity", '<activity\n            android:screenOrientation="sensorLandscape"', 1)
m.write_text(t)
s = pathlib.Path("android/app/src/main/res/values/styles.xml")
t = s.read_text()
if "windowFullscreen" not in t:
    t = re.sub(r'(<style name="AppTheme\.NoActionBar"[^>]*>)',
               r'\1\n        <item name="android:windowFullscreen">true</item>\n        <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>', t, 1)
s.write_text(t)
print("patch ok")
