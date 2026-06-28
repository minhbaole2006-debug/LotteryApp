[app]
title = LotteryApp
package.name = lotteryapp
package.domain = org.test.lottery
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.ndk = 25b
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
