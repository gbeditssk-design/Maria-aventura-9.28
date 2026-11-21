# MARIO ADVENTURE 100 — projeto Capacitor (Android)

Estrutura: www/index.html (o jogo, tudo offline), assets/ (ícone), capacitor.config.json,
patch_android.py (ecrã horizontal + ecrã inteiro), .github/workflows/android.yml (gera o APK online).

## Caminho A — sem instalar nada (só com conta GitHub, funciona no telemóvel)
1. Cria um repositório novo no GitHub e envia todo o conteúdo desta pasta (incluindo a pasta .github).
2. Separador Actions -> "Gerar APK" -> Run workflow.
3. Quando terminar (~5-8 min), abre a execução -> Artifacts -> MARIO-ADVENTURE-100-apk -> descarrega.
   Dentro do ZIP está o app-debug.apk (assinado com chave de debug, instala normalmente).

## Caminho B — no PC
Requisitos: Node 18+, Java 17, Android Studio/SDK. Corre ./build.sh
O APK fica em android/app/build/outputs/apk/debug/app-debug.apk

## Instalar no Galaxy A06
Copia o APK, abre-o e permite "instalar apps desconhecidas" quando pedido.
O Play Protect pode avisar porque o APK não vem da Play Store; escolhe "Instalar mesmo assim".

## MediaFire
Faz upload do app-debug.apk (renomeia para MARIO-ADVENTURE-100.apk) e partilha o link.
Para a Google Play é preciso um AAB assinado com a tua chave (./gradlew bundleRelease).
