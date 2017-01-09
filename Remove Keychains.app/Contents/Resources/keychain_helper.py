#!/usr/bin/python
# encoding: utf-8
"""
Keychain helper to move current keychain folder if your login.keychain is
locked. We then force a restart immediately.

http://apple.stackexchange.com/a/103633
"""

import sys
import os
import shutil
import time
import subprocess
import keychainlib as kc

# Per SecKeychain.h
kSecPreferencesDomainUser = 0
kSecPreferencesDomainSystem = 1

# Get our login keychain path and the lock/unlock status of that keychain
login_kc_path = kc.list_our_keychains(kSecPreferencesDomainUser)[0]
status = kc.keychain_unlocked(login_kc_path)

# If our login keychain is not unlocked let's assume the AD password
# is out of sync and we need to recreate the keychain. Make a backup first.
# Then lets start deleting.
if status is False:
    home = os.path.expanduser("~")
    time = time.time()
    source_dir = os.path.join(home, 'Library/Keychains')
    bkup_dir = os.path.join(home, 'Library/Keychain_bkups')
    if not os.path.exists(bkup_dir):
        os.makedirs(bkup_dir)
    dest_dir = os.path.join(bkup_dir, str(time).split('.', 1)[0])
    shutil.copytree(source_dir, dest_dir)
    # This will only delete the login.keychain which isn't enough
    kc.delete_keychain(login_kc_path)
    # This will remove the entire Keychain directory
    shutil.rmtree(source_dir)

    # Force a restart thanks to 10.9 and the Local keychain
    cmd = ['/usr/bin/osascript', '-e', 'tell app "System Events" to restart']
    result = subprocess.check_output(cmd)
