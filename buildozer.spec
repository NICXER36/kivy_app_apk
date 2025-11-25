[app]

title = KivyApp
package.name = kivyapp
package.domain = org.nicolas
source.dir = .
source.include_exts = py, kv, png, jpg, jpeg, gif

version = 1.0

# Tu archivo principal
entrypoint = main.py

orientation = portrait

requirements = python3, kivy
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 28
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# Si usas imágenes, incluye assets aquí
presplash.filename = assets/presplash.png
icon.filename = assets/icon.png

fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
