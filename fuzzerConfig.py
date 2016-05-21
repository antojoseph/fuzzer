import os
USR_HOME_DIR = os.path.expanduser('~')

#tools and symbols for the fuzzer
ndkstack = USR_HOME_DIR+"/Documents/android-ndk/ndk-stack"
addr2line = USR_HOME_DIR+"/Documents/android-ndk/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin/arm-linux-androideabi-addr2line"
symbols = USR_HOME_DIR+"/Desktop/new_new/android-tombstones/out/symbols"

#folders for the fuzzer
path_for_confirmed_samples = USR_HOME_DIR+"/myfuzzer/fuzzer/confirmed_crashes/"
path_for_crash_samples = USR_HOME_DIR+"/myfuzzer/fuzzer/crashes/"
path_to_generated_samples = USR_HOME_DIR+"/myfuzzer/fuzzer/generated_samples_folder/"
path_to_save_logcat= USR_HOME_DIR+"/myfuzzer/fuzzer/logcat.txt"
path_to_dex_fixer = USR_HOME_DIR+"/myfuzzer/fuzzer/bin/dexRepair"
path_to_mutated_dex = USR_HOME_DIR+"/myfuzzer/fuzzer/generated_samples_folder/"

#android binary which needs to be fuzzed
target_android_executable = "/system/xbin/dexdump"