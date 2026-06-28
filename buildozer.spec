[app]
# (str) Title of your application
title = LotteryApp
# (str) Package name
package.name = lotteryapp
# (str) Package domain
package.domain = org.test.lottery
# (str) Source code where the main.py live
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.ndk = 25b
android.minapi = 21

[buildozer]
log_level = 2
