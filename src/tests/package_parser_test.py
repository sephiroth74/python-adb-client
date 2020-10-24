#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python3 -m tests.package_parser_test
"""

import unittest

from pythonadb.packageparser import PackageParser


class PackageParserTest(unittest.TestCase):
    def runTest(self):
        self.test_001_parse()

    def test_001_parse(self):
        parser = PackageParser(DUMMY_PACKAGE_DATA)
        self.assertIsNotNone(parser)

        self.assertIsNotNone(parser['DUMP OF SERVICE package:'])

        child = parser['DUMP OF SERVICE package:']['Service Resolver Table:']
        self.assertIsNotNone(child)
        self.assertTrue(isinstance(child, dict))


DUMMY_PACKAGE_DATA = """
DUMP OF SERVICE package:
  Receiver Resolver Table:
    Schemes:
        package:
          cb99a50 com.swisscom.android.tv.library/.internal.receivers.PackageInstalledReceiver filter 951564d
            Action: "android.intent.action.ACTION_PACKAGE_ADDED"
            Category: "android.intent.category.DEFAULT"
            Scheme: "package"
            mPriority=900, mHasPartialTypes=false

    Non-Data Actions:
        com.netflix.ninja.intent.action.TOKEN_REQUEST:
          1eb4449 com.swisscom.android.tv.library/.internal.receivers.NetflixTokenRequestReceiver filter adcce13
            Action: "com.netflix.ninja.intent.action.TOKEN_REQUEST"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        swisscom.android.tv.action.LANGUAGE_CHANGED:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        swisscom.android.tv.action.CLIENT_AUTHENTICATED:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        swisscom.android.tv.action.AUTHENTICATED_ON_INIT:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        com.netflix.ninja.intent.action.DET_RESPONSE:
          ca1026f com.swisscom.android.tv.library/.internal.receivers.NetflixDetReceiver filter c7fb850
            Action: "com.netflix.ninja.intent.action.DET_RESPONSE"
            Action: "com.netflix.ninja.intent.action.DET_TOKEN"
            Action: "com.netflix.ninja.intent.action.USER_SIGNIN"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        com.netflix.ninja.intent.action.DET_TOKEN:
          ca1026f com.swisscom.android.tv.library/.internal.receivers.NetflixDetReceiver filter c7fb850
            Action: "com.netflix.ninja.intent.action.DET_RESPONSE"
            Action: "com.netflix.ninja.intent.action.DET_TOKEN"
            Action: "com.netflix.ninja.intent.action.USER_SIGNIN"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        swisscom.android.tv.action.SETTINGS_SYNCED:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        android.intent.action.TIME_SET:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        android.intent.action.BOOT_COMPLETED:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        com.netflix.ninja.intent.action.USER_SIGNIN:
          ca1026f com.swisscom.android.tv.library/.internal.receivers.NetflixDetReceiver filter c7fb850
            Action: "com.netflix.ninja.intent.action.DET_RESPONSE"
            Action: "com.netflix.ninja.intent.action.DET_TOKEN"
            Action: "com.netflix.ninja.intent.action.USER_SIGNIN"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false
        android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED:
          970814e com.swisscom.android.tv.library/.internal.receivers.LibraryReceiver filter c7b6502
            Action: "android.intent.action.BOOT_COMPLETED"
            Action: "android.bluetooth.adapter.action.CONNECTION_STATE_CHANGED"
            Action: "android.intent.action.TIME_SET"
            Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
            Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
            Action: "swisscom.android.tv.action.SETTINGS_SYNCED"
            Action: "swisscom.android.tv.action.AUTHENTICATED_ON_INIT"
            Category: "android.intent.category.DEFAULT"
            mPriority=900, mHasPartialTypes=false

  Service Resolver Table:
    Non-Data Actions:
        swisscom.android.tv.action.CLEAR_CACHE:
          260b7c com.swisscom.android.tv.library/.internal.services.SettingsSyncService filter 884bbdd
            Action: "swisscom.android.tv.action.SETTINGS_SYNC"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Category: "android.intent.category.DEFAULT"
          59adc05 com.swisscom.android.tv.library/.internal.services.EPGService filter 72a1623
            Action: "swisscom.android.tv.action.INIT_EPG_CACHE"
            Action: "swisscom.android.tv.action.FILL_EPG_CACHE"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_REPLAY_GENRES"
            Category: "android.intent.category.DEFAULT"
          2d7645a com.swisscom.android.tv.library/.internal.services.DiscoveryService filter d9638d9
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.AUTHENTICATE:
          de5568b com.swisscom.android.tv.library/.internal.services.UserService filter 9fea3b4
            Action: "swisscom.android.tv.action.AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_LOGOUT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.LOG_CAPTURE_STOP:
          5866368 com.swisscom.android.tv.library/.internal.services.LogService filter c0a269b
            Action: "swisscom.android.tv.action.LOG_CAPTURE_STOP"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START_REQUESTED"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_VOD_MOVIES_CACHE:
          6f23381 com.swisscom.android.tv.library/.internal.services.VODService filter f1e829e
            Action: "swisscom.android.tv.action.REFRESH_VOD_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_VOD_MOVIES_CACHE"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.START_SCHEDULES:
          7976c26 com.swisscom.android.tv.library/.internal.services.ScheduleService filter 5eeb54c
            Action: "swisscom.android.tv.action.START_SCHEDULES"
            Action: "swisscom.android.tv.action.NEXT_IS_NOW"
            Action: "swisscom.android.tv.action.CHECK_FOR_CONNECTIVITY"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.OTT_AUTHENTICATE:
          de5568b com.swisscom.android.tv.library/.internal.services.UserService filter 9fea3b4
            Action: "swisscom.android.tv.action.AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_LOGOUT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.CHECK_FOR_CONNECTIVITY:
          7976c26 com.swisscom.android.tv.library/.internal.services.ScheduleService filter 5eeb54c
            Action: "swisscom.android.tv.action.START_SCHEDULES"
            Action: "swisscom.android.tv.action.NEXT_IS_NOW"
            Action: "swisscom.android.tv.action.CHECK_FOR_CONNECTIVITY"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.INIT_EPG_CACHE:
          59adc05 com.swisscom.android.tv.library/.internal.services.EPGService filter 72a1623
            Action: "swisscom.android.tv.action.INIT_EPG_CACHE"
            Action: "swisscom.android.tv.action.FILL_EPG_CACHE"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_REPLAY_GENRES"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_REPLAY_GENRES:
          59adc05 com.swisscom.android.tv.library/.internal.services.EPGService filter 72a1623
            Action: "swisscom.android.tv.action.INIT_EPG_CACHE"
            Action: "swisscom.android.tv.action.FILL_EPG_CACHE"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_REPLAY_GENRES"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.COMPANION_NOTIFY:
          9d0d067 com.swisscom.android.tv.library/.internal.services.CompanionService filter 83a4776
            Action: "swisscom.android.tv.action.COMPANION_NOTIFY_ERROR"
            Action: "swisscom.android.tv.action.COMPANION_NOTIFY"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_VOD_CACHE:
          6f23381 com.swisscom.android.tv.library/.internal.services.VODService filter f1e829e
            Action: "swisscom.android.tv.action.REFRESH_VOD_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_VOD_MOVIES_CACHE"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.CHECK_NETWORK_STATUS:
          4124e14 com.swisscom.android.tv.library/.internal.services.SystemService filter dec2aaa
            Action: "swisscom.android.tv.action.CHECK_NETWORK_STATUS"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.COUNTER_LOG_EVENT:
          70d86bd com.swisscom.android.tv.library/.internal.services.CountersSaveService filter ef7da38
            Action: "swisscom.android.tv.action.COUNTER_LOG_EVENT"
            Action: "swisscom.android.tv.action.COUNTER_LOG_CHANNEL_TUNE"
            Action: "swisscom.android.tv.action.CHECK_CRASH"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.SETTINGS_SYNC:
          260b7c com.swisscom.android.tv.library/.internal.services.SettingsSyncService filter 884bbdd
            Action: "swisscom.android.tv.action.SETTINGS_SYNC"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FILL_EPG_CACHE:
          59adc05 com.swisscom.android.tv.library/.internal.services.EPGService filter 72a1623
            Action: "swisscom.android.tv.action.INIT_EPG_CACHE"
            Action: "swisscom.android.tv.action.FILL_EPG_CACHE"
            Action: "swisscom.android.tv.action.CLEAR_CACHE"
            Action: "swisscom.android.tv.action.REFRESH_REPLAY_GENRES"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.INIT_RADIO_CACHE:
          2fe24b2 com.swisscom.android.tv.library/.internal.services.RadioService filter baf8352
            Action: "swisscom.android.tv.action.INIT_RADIO_CACHE"
        swisscom.android.tv.action.IMPRESSION_PRESENT:
          9100c03 com.swisscom.android.tv.library/.internal.services.NetflixService filter 76c61e4
            Action: "swisscom.android.tv.action.IMPRESSION_PRESENT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.NOTIFICATION_SEND_HEARTBEAT_MESSAGE:
          cd03780 com.swisscom.android.tv.library/.internal.services.NotificationService filter dda9177
            Action: "swisscom.android.tv.action.NOTIFICATION_INIT"
            Action: "swisscom.android.tv.action.NOTIFICATION_SEND_HEARTBEAT_MESSAGE"
            Action: "swisscom.android.tv.action.SEND_REPORT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK:
          290d1b9 com.swisscom.android.tv.library/.internal.services.FirmwareService filter 6a88995
            Action: "swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK"
            Action: "swisscom.android.tv.action.FIRMWARE_UPDATE"
            Action: "swisscom.android.tv.action.FIRMWARE_CONFIRMATION"
            Action: "swisscom.android.tv.action.FIRMWARE_POSTPONE"
            Action: "swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_SPORTS:
          5a5d9fe com.swisscom.android.tv.library/.internal.services.SportService filter ffdf17f
            Action: "swisscom.android.tv.action.REFRESH_SPORTS"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.COMPANION_NOTIFY_ERROR:
          9d0d067 com.swisscom.android.tv.library/.internal.services.CompanionService filter 83a4776
            Action: "swisscom.android.tv.action.COMPANION_NOTIFY_ERROR"
            Action: "swisscom.android.tv.action.COMPANION_NOTIFY"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.CHECK_CRASH:
          70d86bd com.swisscom.android.tv.library/.internal.services.CountersSaveService filter ef7da38
            Action: "swisscom.android.tv.action.COUNTER_LOG_EVENT"
            Action: "swisscom.android.tv.action.COUNTER_LOG_CHANNEL_TUNE"
            Action: "swisscom.android.tv.action.CHECK_CRASH"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.NOTIFICATION_INIT:
          cd03780 com.swisscom.android.tv.library/.internal.services.NotificationService filter dda9177
            Action: "swisscom.android.tv.action.NOTIFICATION_INIT"
            Action: "swisscom.android.tv.action.NOTIFICATION_SEND_HEARTBEAT_MESSAGE"
            Action: "swisscom.android.tv.action.SEND_REPORT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_RECORDINGS:
          87d655f com.swisscom.android.tv.library/.internal.services.PersonalDataService filter 1bc4720
            Action: "swisscom.android.tv.action.REFRESH_RECORDINGS"
            Action: "swisscom.android.tv.action.REFRESH_LINEUPS"
            Action: "swisscom.android.tv.action.REFRESH_RADIO_LINEUPS"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FIRMWARE_CONFIRMATION:
          290d1b9 com.swisscom.android.tv.library/.internal.services.FirmwareService filter 6a88995
            Action: "swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK"
            Action: "swisscom.android.tv.action.FIRMWARE_UPDATE"
            Action: "swisscom.android.tv.action.FIRMWARE_CONFIRMATION"
            Action: "swisscom.android.tv.action.FIRMWARE_POSTPONE"
            Action: "swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.SEND_REPORT:
          cd03780 com.swisscom.android.tv.library/.internal.services.NotificationService filter dda9177
            Action: "swisscom.android.tv.action.NOTIFICATION_INIT"
            Action: "swisscom.android.tv.action.NOTIFICATION_SEND_HEARTBEAT_MESSAGE"
            Action: "swisscom.android.tv.action.SEND_REPORT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.LOG_CAPTURE_START_REQUESTED:
          5866368 com.swisscom.android.tv.library/.internal.services.LogService filter c0a269b
            Action: "swisscom.android.tv.action.LOG_CAPTURE_STOP"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START_REQUESTED"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.LOG_CAPTURE_START:
          5866368 com.swisscom.android.tv.library/.internal.services.LogService filter c0a269b
            Action: "swisscom.android.tv.action.LOG_CAPTURE_STOP"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START"
            Action: "swisscom.android.tv.action.LOG_CAPTURE_START_REQUESTED"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FIRMWARE_UPDATE:
          290d1b9 com.swisscom.android.tv.library/.internal.services.FirmwareService filter 6a88995
            Action: "swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK"
            Action: "swisscom.android.tv.action.FIRMWARE_UPDATE"
            Action: "swisscom.android.tv.action.FIRMWARE_CONFIRMATION"
            Action: "swisscom.android.tv.action.FIRMWARE_POSTPONE"
            Action: "swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK:
          290d1b9 com.swisscom.android.tv.library/.internal.services.FirmwareService filter 6a88995
            Action: "swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK"
            Action: "swisscom.android.tv.action.FIRMWARE_UPDATE"
            Action: "swisscom.android.tv.action.FIRMWARE_CONFIRMATION"
            Action: "swisscom.android.tv.action.FIRMWARE_POSTPONE"
            Action: "swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.BIND_DEBUG_SERVICE:
          8c14bac com.swisscom.android.tv.library/.internal.services.bound.DebugService filter 3487887
            Action: "swisscom.android.tv.action.BIND_DEBUG_SERVICE"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_LINEUPS:
          87d655f com.swisscom.android.tv.library/.internal.services.PersonalDataService filter 1bc4720
            Action: "swisscom.android.tv.action.REFRESH_RECORDINGS"
            Action: "swisscom.android.tv.action.REFRESH_LINEUPS"
            Action: "swisscom.android.tv.action.REFRESH_RADIO_LINEUPS"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.COUNTER_LOG_CHANNEL_TUNE:
          70d86bd com.swisscom.android.tv.library/.internal.services.CountersSaveService filter ef7da38
            Action: "swisscom.android.tv.action.COUNTER_LOG_EVENT"
            Action: "swisscom.android.tv.action.COUNTER_LOG_CHANNEL_TUNE"
            Action: "swisscom.android.tv.action.CHECK_CRASH"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.OTT_LOGOUT:
          de5568b com.swisscom.android.tv.library/.internal.services.UserService filter 9fea3b4
            Action: "swisscom.android.tv.action.AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_AUTHENTICATE"
            Action: "swisscom.android.tv.action.OTT_LOGOUT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.SEND_USAGE_REPORT:
          263d075 com.swisscom.android.tv.library/.internal.services.CountersSendService filter 3552a11
            Action: "swisscom.android.tv.action.SEND_USAGE_REPORT"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.FIRMWARE_POSTPONE:
          290d1b9 com.swisscom.android.tv.library/.internal.services.FirmwareService filter 6a88995
            Action: "swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK"
            Action: "swisscom.android.tv.action.FIRMWARE_UPDATE"
            Action: "swisscom.android.tv.action.FIRMWARE_CONFIRMATION"
            Action: "swisscom.android.tv.action.FIRMWARE_POSTPONE"
            Action: "swisscom.android.tv.action.FIRMWARE_ACTIVE_CHECK"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.REFRESH_RADIO_LINEUPS:
          87d655f com.swisscom.android.tv.library/.internal.services.PersonalDataService filter 1bc4720
            Action: "swisscom.android.tv.action.REFRESH_RECORDINGS"
            Action: "swisscom.android.tv.action.REFRESH_LINEUPS"
            Action: "swisscom.android.tv.action.REFRESH_RADIO_LINEUPS"
            Category: "android.intent.category.DEFAULT"
        swisscom.android.tv.action.NEXT_IS_NOW:
          7976c26 com.swisscom.android.tv.library/.internal.services.ScheduleService filter 5eeb54c
            Action: "swisscom.android.tv.action.START_SCHEDULES"
            Action: "swisscom.android.tv.action.NEXT_IS_NOW"
            Action: "swisscom.android.tv.action.CHECK_FOR_CONNECTIVITY"
            Category: "android.intent.category.DEFAULT"

  Permissions:
    Permission [swisscom.android.tv.permission.APPS_API_SERVICE] (d81980a):
      sourcePackage=com.swisscom.android.tv.library
      uid=1000 gids=null type=0 prot=normal
      perm=Permission{e3cf87b swisscom.android.tv.permission.APPS_API_SERVICE}
      packageSetting=PackageSetting{e96e295 com.swisscom.android.tv.library/1000}
    Permission [swisscom.android.tv.permission.WRITE_CONTENT] (dcd7698):
      sourcePackage=com.swisscom.android.tv.library
      uid=1000 gids=null type=0 prot=normal
      perm=Permission{c2dfef1 swisscom.android.tv.permission.WRITE_CONTENT}
      packageSetting=PackageSetting{e96e295 com.swisscom.android.tv.library/1000}
    Permission [swisscom.android.tv.permission.READ_CONTENT] (2a92ad6):
      sourcePackage=com.swisscom.android.tv.library
      uid=1000 gids=null type=0 prot=normal
      perm=Permission{498a157 swisscom.android.tv.permission.READ_CONTENT}
      packageSetting=PackageSetting{e96e295 com.swisscom.android.tv.library/1000}
    Permission [swisscom.android.tv.permission.LIBRARY_SERVICE] (66f6444):
      sourcePackage=com.swisscom.android.tv.library
      uid=1000 gids=null type=0 prot=normal
      perm=Permission{e92992d swisscom.android.tv.permission.LIBRARY_SERVICE}
      packageSetting=PackageSetting{e96e295 com.swisscom.android.tv.library/1000}
    Permission [swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT] (4e51e62):
      sourcePackage=com.swisscom.android.tv.library
      uid=1000 gids=null type=0 prot=signature
      perm=Permission{69bfbf3 swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT}
      packageSetting=PackageSetting{e96e295 com.swisscom.android.tv.library/1000}

  Registered ContentProviders:
    com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider:
      Provider{82080b0 com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider}
    com.swisscom.android.tv.library/.internal.providers.LibraryProvider:
      Provider{52c9b29 com.swisscom.android.tv.library/.internal.providers.LibraryProvider}
    com.swisscom.android.tv.library/.internal.providers.ConfigProvider:
      Provider{5fabeae com.swisscom.android.tv.library/.internal.providers.ConfigProvider}
    com.swisscom.android.tv.library/.internal.providers.SettingsProvider:
      Provider{a70644f com.swisscom.android.tv.library/.internal.providers.SettingsProvider}
    com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider:
      Provider{484f7dc com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider}
    com.swisscom.android.tv.library/.internal.providers.AppsProvider:
      Provider{4ac0e5 com.swisscom.android.tv.library/.internal.providers.AppsProvider}
    com.swisscom.android.tv.library/.internal.providers.CountersProvider:
      Provider{cb817ba com.swisscom.android.tv.library/.internal.providers.CountersProvider}

  ContentProvider Authorities:
    [com.swisscom.android.tv.apps]:
      Provider{4ac0e5 com.swisscom.android.tv.library/.internal.providers.AppsProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.android.tv.config]:
      Provider{5fabeae com.swisscom.android.tv.library/.internal.providers.ConfigProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.android.tv.discovery]:
      Provider{82080b0 com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.android.counters]:
      Provider{cb817ba com.swisscom.android.tv.library/.internal.providers.CountersProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.android.tv.settings]:
      Provider{a70644f com.swisscom.android.tv.library/.internal.providers.SettingsProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.tvlib.lifecycle]:
      Provider{484f7dc com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
    [com.swisscom.android.tv.epg]:
      Provider{52c9b29 com.swisscom.android.tv.library/.internal.providers.LibraryProvider}
        applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}

  Key Set Manager:
    [com.swisscom.android.tv.library]
        Signing KeySets: 1

  Packages:
    Package [com.swisscom.android.tv.library] (e96e295):
      userId=1000
      sharedUser=SharedUserSetting{157b5c8 android.uid.system/1000}
      pkg=Package{c6b8661 com.swisscom.android.tv.library}
      codePath=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      resourcePath=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      legacyNativeLibraryDir=/system/lib/swisscom-tv-library-IP2000-O-10.2.0-release
      primaryCpuAbi=null
      secondaryCpuAbi=null
      versionCode=9 minSdk=24 targetSdk=24
      versionName=10.2.0
      splits=[base]
      apkSigningVersion=2
      applicationInfo=ApplicationInfo{578f66b com.swisscom.android.tv.library}
      flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
      privateFlags=[ PRIVILEGED PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ]
      dataDir=/data/user/0/com.swisscom.android.tv.library
      supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
      usesLibraries:
        android.test.runner
      usesLibraryFiles:
        /system/framework/android.test.runner.jar
      timeStamp=2020-10-02 11:23:24
      firstInstallTime=2020-10-02 11:23:24
      lastUpdateTime=2020-10-02 11:23:24
      signatures=PackageSignatures{cbff586 [f70e61e8]}
      installPermissionsFixed=true installStatus=1
      pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ]
      declared permissions:
        swisscom.android.tv.permission.LIBRARY_SERVICE: prot=normal, INSTALLED
        swisscom.android.tv.permission.READ_CONTENT: prot=normal, INSTALLED
        swisscom.android.tv.permission.WRITE_CONTENT: prot=normal, INSTALLED
        swisscom.android.tv.permission.APPS_API_SERVICE: prot=normal, INSTALLED
        swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT: prot=signature, INSTALLED
      requested permissions:
        android.permission.BLUETOOTH
        android.permission.INTERNET
        android.permission.ACCESS_NETWORK_STATE
        android.permission.ACCESS_WIFI_STATE
        android.permission.LOCAL_MAC_ADDRESS
        android.permission.RECEIVE_BOOT_COMPLETED
        android.permission.SET_TIME_ZONE
        android.permission.READ_LOGS
        android.permission.REBOOT
        android.permission.DEVICE_POWER
        android.permission.WAKE_LOCK
        android.permission.KILL_BACKGROUND_PROCESSES
        android.permission.INJECT_EVENTS
        android.permission.WRITE_SETTINGS
        android.permission.WRITE_EXTERNAL_STORAGE
        android.permission.READ_EXTERNAL_STORAGE
        android.permission.INSTALL_PACKAGES
        android.permission.INTERACT_ACROSS_USERS_FULL
        android.permission.REAL_GET_TASKS
        android.permission.GRANT_REVOKE_PERMISSIONS
        swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT
        com.netflix.ninja.permission.ESN
        com.netflix.ninja.permission.TOKEN
        com.netflix.ninja.permission.DET
        android.permission.BLUETOOTH_ADMIN
      install permissions:
        android.permission.REAL_GET_TASKS: granted=true
        android.permission.WRITE_SETTINGS: granted=true
        android.permission.CONFIGURE_WIFI_DISPLAY: granted=true
        android.permission.CONFIGURE_DISPLAY_COLOR_MODE: granted=true
        android.permission.ACCESS_WIMAX_STATE: granted=true
        com.netflix.ninja.permission.TOKEN: granted=true
        com.marvell.tv.permission.WRITE_AVSETTINGS: granted=true
        android.permission.USE_CREDENTIALS: granted=true
        android.permission.MODIFY_AUDIO_SETTINGS: granted=true
        android.permission.ACCESS_CHECKIN_PROPERTIES: granted=true
        android.permission.INSTALL_LOCATION_PROVIDER: granted=true
        android.permission.CLEAR_APP_USER_DATA: granted=true
        android.permission.INSTALL_PACKAGES: granted=true
        android.permission.NFC: granted=true
        android.permission.MASTER_CLEAR: granted=true
        android.permission.WRITE_SYNC_SETTINGS: granted=true
        android.permission.RECEIVE_BOOT_COMPLETED: granted=true
        android.permission.PEERS_MAC_ADDRESS: granted=true
        android.permission.DEVICE_POWER: granted=true
        android.permission.SET_TIME_ZONE: granted=true
        android.permission.MANAGE_PROFILE_AND_DEVICE_OWNERS: granted=true
        android.permission.READ_PROFILE: granted=true
        android.permission.BLUETOOTH: granted=true
        android.permission.WRITE_MEDIA_STORAGE: granted=true
        android.permission.GET_TASKS: granted=true
        android.permission.INTERNET: granted=true
        android.permission.BLUETOOTH_ADMIN: granted=true
        android.permission.CONTROL_VPN: granted=true
        android.permission.MANAGE_FINGERPRINT: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=true
        android.permission.MANAGE_USB: granted=true
        android.permission.INTERACT_ACROSS_USERS_FULL: granted=true
        android.permission.BATTERY_STATS: granted=true
        android.permission.PACKAGE_USAGE_STATS: granted=true
        android.permission.MOUNT_UNMOUNT_FILESYSTEMS: granted=true
        android.permission.TETHER_PRIVILEGED: granted=true
        android.permission.WRITE_SECURE_SETTINGS: granted=true
        android.permission.MOVE_PACKAGE: granted=true
        com.marvell.tv.permission.READ_AVSETTINGS: granted=true
        android.permission.READ_SEARCH_INDEXABLES: granted=true
        android.permission.ACCESS_DOWNLOAD_MANAGER: granted=true
        android.permission.BLUETOOTH_PRIVILEGED: granted=true
        android.permission.HARDWARE_TEST: granted=true
        android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE: granted=true
        android.permission.BIND_JOB_SERVICE: granted=true
        android.permission.CONFIRM_FULL_BACKUP: granted=true
        android.permission.SET_TIME: granted=true
        android.permission.WRITE_APN_SETTINGS: granted=true
        android.permission.CHANGE_WIFI_STATE: granted=true
        android.permission.MANAGE_USERS: granted=true
        android.permission.ACCESS_NETWORK_STATE: granted=true
        android.permission.BACKUP: granted=true
        android.permission.CHANGE_CONFIGURATION: granted=true
        android.permission.USER_ACTIVITY: granted=true
        android.permission.LOCAL_MAC_ADDRESS: granted=true
        android.permission.READ_LOGS: granted=true
        android.permission.COPY_PROTECTED_DATA: granted=true
        android.permission.INTERACT_ACROSS_USERS: granted=true
        com.netflix.ninja.permission.DET: granted=true
        com.netflix.ninja.permission.ESN: granted=true
        android.permission.SET_KEYBOARD_LAYOUT: granted=true
        com.netflix.ninja.permission.NETFLIX_KEY: granted=true
        android.permission.MANAGE_APP_OPS_RESTRICTIONS: granted=true
        android.permission.KILL_BACKGROUND_PROCESSES: granted=true
        android.permission.USE_FINGERPRINT: granted=true
        android.permission.REQUEST_NETWORK_SCORES: granted=true
        android.permission.WRITE_USER_DICTIONARY: granted=true
        android.permission.READ_SYNC_STATS: granted=true
        android.permission.REBOOT: granted=true
        android.permission.MOUNT_FORMAT_FILESYSTEMS: granted=true
        android.permission.OEM_UNLOCK_STATE: granted=true
        android.permission.MANAGE_DEVICE_ADMINS: granted=true
        android.permission.CHANGE_APP_IDLE_STATE: granted=true
        android.permission.SET_POINTER_SPEED: granted=true
        android.permission.MANAGE_NOTIFICATIONS: granted=true
        android.permission.READ_SYNC_SETTINGS: granted=true
        android.permission.OVERRIDE_WIFI_CONFIG: granted=true
        android.permission.FORCE_STOP_PACKAGES: granted=true
        android.permission.HIDE_NON_SYSTEM_OVERLAY_WINDOWS: granted=true
        android.permission.ACCESS_NOTIFICATIONS: granted=true
        android.permission.WRITE_EXTERNAL_STORAGE: granted=true
        android.permission.VIBRATE: granted=true
        com.android.certinstaller.INSTALL_AS_USER: granted=true
        android.permission.READ_USER_DICTIONARY: granted=true
        android.permission.ACCESS_WIFI_STATE: granted=true
        android.permission.CHANGE_WIMAX_STATE: granted=true
        android.permission.MODIFY_PHONE_STATE: granted=true
        android.permission.STATUS_BAR: granted=true
        android.permission.LOCATION_HARDWARE: granted=true
        android.permission.WAKE_LOCK: granted=true
        android.permission.INJECT_EVENTS: granted=true
        android.permission.BIND_NETWORK_RECOMMENDATION_SERVICE: granted=true
        swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT: granted=true
        android.permission.DELETE_PACKAGES: granted=true
      User 0: ceDataInode=-4294885081 installed=true hidden=false suspended=false stopped=false notLaunched=false enabled=0 instant=false
      overlay paths:
        /vendor/overlay/framework-resOverlay.apk

  Shared users:
    SharedUser [android.uid.system] (157b5c8):
      userId=1000
      install permissions:
        android.permission.REAL_GET_TASKS: granted=true
        android.permission.WRITE_SETTINGS: granted=true
        android.permission.CONFIGURE_WIFI_DISPLAY: granted=true
        android.permission.CONFIGURE_DISPLAY_COLOR_MODE: granted=true
        android.permission.ACCESS_WIMAX_STATE: granted=true
        com.netflix.ninja.permission.TOKEN: granted=true
        com.marvell.tv.permission.WRITE_AVSETTINGS: granted=true
        android.permission.USE_CREDENTIALS: granted=true
        android.permission.MODIFY_AUDIO_SETTINGS: granted=true
        android.permission.ACCESS_CHECKIN_PROPERTIES: granted=true
        android.permission.INSTALL_LOCATION_PROVIDER: granted=true
        android.permission.CLEAR_APP_USER_DATA: granted=true
        android.permission.INSTALL_PACKAGES: granted=true
        android.permission.NFC: granted=true
        android.permission.MASTER_CLEAR: granted=true
        android.permission.WRITE_SYNC_SETTINGS: granted=true
        android.permission.RECEIVE_BOOT_COMPLETED: granted=true
        android.permission.PEERS_MAC_ADDRESS: granted=true
        android.permission.DEVICE_POWER: granted=true
        android.permission.SET_TIME_ZONE: granted=true
        android.permission.MANAGE_PROFILE_AND_DEVICE_OWNERS: granted=true
        android.permission.READ_PROFILE: granted=true
        android.permission.BLUETOOTH: granted=true
        android.permission.WRITE_MEDIA_STORAGE: granted=true
        android.permission.GET_TASKS: granted=true
        android.permission.INTERNET: granted=true
        android.permission.BLUETOOTH_ADMIN: granted=true
        android.permission.CONTROL_VPN: granted=true
        android.permission.MANAGE_FINGERPRINT: granted=true
        android.permission.READ_EXTERNAL_STORAGE: granted=true
        android.permission.MANAGE_USB: granted=true
        android.permission.INTERACT_ACROSS_USERS_FULL: granted=true
        android.permission.BATTERY_STATS: granted=true
        android.permission.PACKAGE_USAGE_STATS: granted=true
        android.permission.MOUNT_UNMOUNT_FILESYSTEMS: granted=true
        android.permission.TETHER_PRIVILEGED: granted=true
        android.permission.WRITE_SECURE_SETTINGS: granted=true
        android.permission.MOVE_PACKAGE: granted=true
        com.marvell.tv.permission.READ_AVSETTINGS: granted=true
        android.permission.READ_SEARCH_INDEXABLES: granted=true
        android.permission.ACCESS_DOWNLOAD_MANAGER: granted=true
        android.permission.BLUETOOTH_PRIVILEGED: granted=true
        android.permission.HARDWARE_TEST: granted=true
        android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE: granted=true
        android.permission.BIND_JOB_SERVICE: granted=true
        android.permission.CONFIRM_FULL_BACKUP: granted=true
        android.permission.SET_TIME: granted=true
        android.permission.WRITE_APN_SETTINGS: granted=true
        android.permission.CHANGE_WIFI_STATE: granted=true
        android.permission.MANAGE_USERS: granted=true
        android.permission.ACCESS_NETWORK_STATE: granted=true
        android.permission.BACKUP: granted=true
        android.permission.CHANGE_CONFIGURATION: granted=true
        android.permission.USER_ACTIVITY: granted=true
        android.permission.LOCAL_MAC_ADDRESS: granted=true
        android.permission.READ_LOGS: granted=true
        android.permission.COPY_PROTECTED_DATA: granted=true
        android.permission.INTERACT_ACROSS_USERS: granted=true
        com.netflix.ninja.permission.DET: granted=true
        com.netflix.ninja.permission.ESN: granted=true
        android.permission.SET_KEYBOARD_LAYOUT: granted=true
        com.netflix.ninja.permission.NETFLIX_KEY: granted=true
        android.permission.MANAGE_APP_OPS_RESTRICTIONS: granted=true
        android.permission.KILL_BACKGROUND_PROCESSES: granted=true
        android.permission.USE_FINGERPRINT: granted=true
        android.permission.REQUEST_NETWORK_SCORES: granted=true
        android.permission.WRITE_USER_DICTIONARY: granted=true
        android.permission.READ_SYNC_STATS: granted=true
        android.permission.REBOOT: granted=true
        android.permission.MOUNT_FORMAT_FILESYSTEMS: granted=true
        android.permission.OEM_UNLOCK_STATE: granted=true
        android.permission.MANAGE_DEVICE_ADMINS: granted=true
        android.permission.CHANGE_APP_IDLE_STATE: granted=true
        android.permission.SET_POINTER_SPEED: granted=true
        android.permission.MANAGE_NOTIFICATIONS: granted=true
        android.permission.READ_SYNC_SETTINGS: granted=true
        android.permission.OVERRIDE_WIFI_CONFIG: granted=true
        android.permission.FORCE_STOP_PACKAGES: granted=true
        android.permission.HIDE_NON_SYSTEM_OVERLAY_WINDOWS: granted=true
        android.permission.ACCESS_NOTIFICATIONS: granted=true
        android.permission.WRITE_EXTERNAL_STORAGE: granted=true
        android.permission.VIBRATE: granted=true
        com.android.certinstaller.INSTALL_AS_USER: granted=true
        android.permission.READ_USER_DICTIONARY: granted=true
        android.permission.ACCESS_WIFI_STATE: granted=true
        android.permission.CHANGE_WIMAX_STATE: granted=true
        android.permission.MODIFY_PHONE_STATE: granted=true
        android.permission.STATUS_BAR: granted=true
        android.permission.LOCATION_HARDWARE: granted=true
        android.permission.WAKE_LOCK: granted=true
        android.permission.INJECT_EVENTS: granted=true
        android.permission.BIND_NETWORK_RECOMMENDATION_SERVICE: granted=true
        swisscom.android.tv.permission.INTERNAL_WRITE_CONTENT: granted=true
        android.permission.DELETE_PACKAGES: granted=true
      User 0: 
        gids=[3002, 1023, 1015, 3003, 3001, 1007]
        runtime permissions:
          android.permission.ACCESS_FINE_LOCATION: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.ACCESS_COARSE_LOCATION: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.READ_PHONE_STATE: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.CALL_PHONE: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.WRITE_CONTACTS: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.GET_ACCOUNTS: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.RECORD_AUDIO: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]
          android.permission.READ_CONTACTS: granted=true, flags=[ SYSTEM_FIXED GRANTED_BY_DEFAULT ]

  Package Changes:
    Sequence number=2
    User 0:
      seq=1, package=com.swisscom.swisscomTv


  Dexopt state:
    [com.swisscom.android.tv.library]
      Instruction Set: arm
        path: /system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
        status: /data/dalvik-cache/arm/system@priv-app@swisscom-tv-library-IP2000-O-10.2.0-release.apk@classes.dex[status=
        kOatUpToDate, compilation_filter=verify]


  Compiler stats:
    [com.swisscom.android.tv.library]
       swisscom-tv-library-IP2000-O-10.2.0-release.apk - 1754

DUMP OF SERVICE activity:
  ACTIVITY MANAGER SETTINGS (dumpsys activity settings) activity_manager_constants:
    max_cached_processes=32
    background_settle_time=60000
    fgservice_min_shown_time=2000
    fgservice_min_report_time=3000
    fgservice_screen_on_before_time=1000
    fgservice_screen_on_after_time=5000
    content_provider_retain_time=20000
    gc_timeout=5000
    gc_min_interval=60000
    full_pss_min_interval=600000
    full_pss_lowered_interval=120000
    power_check_delay=900000
    wake_lock_min_check_duration=300000
    cpu_min_check_duration=300000
    service_usage_interaction_time=1800000
    usage_stats_interaction_interval=86400000
    service_restart_duration=1000
    service_reset_run_duration=60000
    service_restart_duration_factor=4
    service_min_restart_time_between=10000
    service_max_inactivity=1800000
    service_bg_start_timeout=15000

    CUR_MAX_CACHED_PROCESSES=32
    CUR_MAX_EMPTY_PROCESSES=16
    CUR_TRIM_EMPTY_PROCESSES=8
    CUR_TRIM_CACHED_PROCESSES=5

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER PENDING INTENTS (dumpsys activity intents)
    * com.swisscom.android.tv.library: 24 items
      #0: PendingIntentRecord{62e8e47 com.swisscom.android.tv.library broadcastIntent}
        uid=1000 packageName=com.swisscom.android.tv.library type=broadcastIntent flags=0x0
        requestIntent=act=swisscom.android.tv.action.ALU_READ_EVALUATE
      #1: PendingIntentRecord{3166674 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.CALCULATE_ROUNDTRIP_TIME cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #2: PendingIntentRecord{579279d com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.COUNTER_LOG_CHANNEL_TUNE (has extras)
        sent=true canceled=false
      #3: PendingIntentRecord{f15e412 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.INIT_EPG_VERSION flg=0x4 cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #4: PendingIntentRecord{fbbc7e3 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_APPS_CACHE cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #5: PendingIntentRecord{66d75e0 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_RECOMMENDATIONS cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #6: PendingIntentRecord{1c5a099 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_SPORTS_FALLBACK cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #7: PendingIntentRecord{76a2f5e com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.LOG_CAPTURE_START cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #8: PendingIntentRecord{358ff3f com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.CHECK_CRASH flg=0x4 cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #9: PendingIntentRecord{464100c com.swisscom.android.tv.library broadcastIntent}
        uid=1000 packageName=com.swisscom.android.tv.library type=broadcastIntent flags=0x0
        requestIntent=act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT
      #10: PendingIntentRecord{c6ad55 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.UPLOAD_CRASH_LOGS cmp=com.swisscom.android.tv.library/.internal.services.CountersSendService
      #11: PendingIntentRecord{225e36a com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_PBA_FORMULA cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #12: PendingIntentRecord{368505b com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.SEND_TECHNICAL_COUNTERS cmp=com.swisscom.android.tv.library/.internal.services.CountersSendService
      #13: PendingIntentRecord{d4820f8 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_HOME_SCREEN_BANNERS cmp=com.swisscom.android.tv.library/.internal.services.EPGService
      #14: PendingIntentRecord{991c9d1 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.FIRMWARE_PASSIVE_CHECK cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #15: PendingIntentRecord{736cc36 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.SEND_ALU_COUNTERS cmp=com.swisscom.android.tv.library/.internal.services.CountersSendService
      #16: PendingIntentRecord{c519737 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.CHECK_THE_SPORT_VERSION cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #17: PendingIntentRecord{65a54a4 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.INIT_EPG_CACHE cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #18: PendingIntentRecord{518320d com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.AUTHENTICATE cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #19: PendingIntentRecord{d9b75c2 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.REFRESH_VOD_CACHE cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #20: PendingIntentRecord{f1e6fd3 com.swisscom.android.tv.library broadcastIntent}
        uid=1000 packageName=com.swisscom.android.tv.library type=broadcastIntent flags=0x0
        requestIntent=act=swisscom.android.tv.action.REPORT_CHANNEL_TUNE (has extras)
      #21: PendingIntentRecord{63a1710 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.STB_ON flg=0x4 cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #22: PendingIntentRecord{22e209 com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.SEND_HEARTBEAT flg=0x4 cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)
      #23: PendingIntentRecord{baf2c0e com.swisscom.android.tv.library startService}
        uid=1000 packageName=com.swisscom.android.tv.library type=startService flags=0x0
        requestIntent=act=swisscom.android.tv.action.NEXT_IS_NOW flg=0x4 cmp=com.swisscom.android.tv.library/.internal.services.AlarmService (has extras)

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER BROADCAST STATE (dumpsys activity broadcasts)
    Registered Receivers:
    * ReceiverList{412fa82 1385 com.swisscom.android.tv.library/1000/u0 remote:7dbd1cd}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{6f47593}
        Action: "android.intent.action.SCREEN_OFF"
        Action: "android.intent.action.SCREEN_ON"
    * ReceiverList{4f43618 1385 com.swisscom.android.tv.library/1000/u0 remote:5d105fb}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{3068871}
        Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
    * ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{3528792}
        Action: "swisscom.android.tv.action.WIFI_QUALITY_START_SLOT"
    * ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{eeb63eb}
        Action: "com.swisscom.dialserver.action.STAT_APP_ENABLED"
        Action: "com.swisscom.dialserver.action.STAT_APP_STARTED"
        Action: "com.swisscom.dialserver.action.LAUNCH_APP"
        Action: "com.swisscom.dialserver.action.HIDE_APP"
        Action: "com.swisscom.dialserver.action.STOP_APP"
        Action: "com.swisscom.swisscomTv.action.DLNA_START"
        Action: "swisscom.android.tv.action.NAVIGATION_START"
        Action: "swisscom.android.tv.action.HDMI_HOTPLUG_CONCLUDED"
        mPriority=1000, mHasPartialTypes=false
    * ReceiverList{2030832 1385 com.swisscom.android.tv.library/1000/u0 remote:851c83d}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{75e983}
        Action: "swisscom.android.tv.action.BANDWIDTH_RESERVATION_RENEW"
    * ReceiverList{415da66 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:4872c1}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{6bd41a7}
        Action: "android.intent.action.PACKAGE_ADDED"
        Scheme: "package"
    * ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{c1a53c7}
        Action: "swisscom.android.tv.action.REPORT_CHANNEL_TUNE"
        Action: "swisscom.android.tv.action.REPORT_WATCH_REPLAY_START"
        Action: "swisscom.android.tv.action.REPORT_WATCH_RECORDING_START"
        Action: "swisscom.android.tv.action.REPORT_WATCH_VOD_START"
        Action: "swisscom.android.tv.action.REPORT_RADIO_TUNE"
    * ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{207f942}
        Action: "android.intent.action.TIME_SET"
        Action: "android.net.conn.CONNECTIVITY_CHANGE"
        mPriority=999, mHasPartialTypes=false
      Filter #1: BroadcastFilter{f5b2a51}
        Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATED"
        Action: "swisscom.android.tv.action.CLIENT_AUTHENTICATION_FAILED"
        Action: "swisscom.android.tv.action.MASTER_LINEUP_REFRESHED"
        Action: "swisscom.android.tv.action.FIRMWARE_CHECKED"
        Action: "swisscom.android.tv.action.LOGOS_DOWNLOADED"
        Action: "swisscom.android.tv.action.GET_ACTUAL_STATE"
        Action: "swisscom.android.tv.action.CLEAR_SESSION"
        Action: "swisscom.android.tv.action.CLEAR_EPG"
        mPriority=999, mHasPartialTypes=false
    * ReceiverList{cbec1f5 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fd3132c}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{4cf6b8a}
        Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"
    * ReceiverList{3111ddb 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:5e376ea}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{7c4a078}
        Action: "swisscom.android.tv.action.DISPATCH_ERROR"
    * ReceiverList{7fa17b6 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c6d1351}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{579bcb7}
        Action: "swisscom.android.tv.action.DISPATCH_SUCCESS"
    * ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{e373a19}
        Action: "android.intent.action.SCREEN_OFF"
        Action: "android.intent.action.SCREEN_ON"
        Action: "swisscom.android.tv.action.ALU_READ_EVALUATE"
    * ReceiverList{9e0bdc9 1385 com.swisscom.android.tv.library/1000/u0 remote:49b09d0}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{fa3cce}
        Action: "android.net.conn.CONNECTIVITY_CHANGE"
    * ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}
      app=1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000 user=0
      Filter #0: BroadcastFilter{8785ed5}
        Action: "swisscom.android.tv.action.DISPATCH_ERROR"
        Action: "swisscom.android.tv.action.DISPATCH_PENDING_FIRMWARE"
        Action: "swisscom.android.tv.action.DISPATCH_SUCCESS"
        mPriority=999, mHasPartialTypes=false
    * ReceiverList{96ef2fc 1385 com.swisscom.android.tv.library/1000/u0 remote:e66d7ef}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{d2e6d85}
        Action: "android.intent.action.SCREEN_OFF"
        Action: "android.intent.action.SCREEN_ON"
    * ReceiverList{51ec0f7 1385 com.swisscom.android.tv.library/1000/u0 remote:13b84f6}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{2ed9b64}
        Action: "android.media.action.HDMI_AUDIO_PLUG"
    * ReceiverList{1f3040b 1385 com.swisscom.android.tv.library/1000/u0 remote:c0157da}
      app=1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000 user=0
      Filter #0: BroadcastFilter{b3642e8}
        Action: "swisscom.android.voice.action.VOICE_EVENT"
    * ReceiverList{6029bc4 1443 com.swisscom.android.tv.library:IntentService/1000/u0 remote:92006d7}
      app=1443:com.swisscom.android.tv.library:IntentService/1000 pid=1443 uid=1000 user=0
      Filter #0: BroadcastFilter{82a3aad}
        Action: "swisscom.android.tv.action.LANGUAGE_CHANGED"

    Receiver Resolver Table:
      Schemes:
          package:
            BroadcastFilter{6bd41a7 u0 ReceiverList{415da66 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:4872c1}}

      Non-Data Actions:
          android.intent.action.SCREEN_OFF:
            BroadcastFilter{6f47593 u0 ReceiverList{412fa82 1385 com.swisscom.android.tv.library/1000/u0 remote:7dbd1cd}}
            BroadcastFilter{d2e6d85 u0 ReceiverList{96ef2fc 1385 com.swisscom.android.tv.library/1000/u0 remote:e66d7ef}}
            BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
          swisscom.android.tv.action.HDMI_HOTPLUG_CONCLUDED:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          swisscom.android.voice.action.VOICE_EVENT:
            BroadcastFilter{b3642e8 u0 ReceiverList{1f3040b 1385 com.swisscom.android.tv.library/1000/u0 remote:c0157da}}
          swisscom.android.tv.action.CLEAR_EPG:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.REPORT_CHANNEL_TUNE:
            BroadcastFilter{c1a53c7 u0 ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}}
          com.swisscom.dialserver.action.HIDE_APP:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          com.swisscom.swisscomTv.action.DLNA_START:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          android.intent.action.SCREEN_ON:
            BroadcastFilter{6f47593 u0 ReceiverList{412fa82 1385 com.swisscom.android.tv.library/1000/u0 remote:7dbd1cd}}
            BroadcastFilter{d2e6d85 u0 ReceiverList{96ef2fc 1385 com.swisscom.android.tv.library/1000/u0 remote:e66d7ef}}
            BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
          swisscom.android.tv.action.NAVIGATION_START:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          swisscom.android.tv.action.DISPATCH_ERROR:
            BroadcastFilter{8785ed5 u0 ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}}
            BroadcastFilter{7c4a078 u0 ReceiverList{3111ddb 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:5e376ea}}
          swisscom.android.tv.action.REPORT_WATCH_VOD_START:
            BroadcastFilter{c1a53c7 u0 ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}}
          swisscom.android.tv.action.CLIENT_AUTHENTICATION_FAILED:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          android.net.conn.CONNECTIVITY_CHANGE:
            BroadcastFilter{fa3cce u0 ReceiverList{9e0bdc9 1385 com.swisscom.android.tv.library/1000/u0 remote:49b09d0}}
            BroadcastFilter{207f942 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.LANGUAGE_CHANGED:
            BroadcastFilter{4cf6b8a u0 ReceiverList{cbec1f5 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fd3132c}}
            BroadcastFilter{3068871 u0 ReceiverList{4f43618 1385 com.swisscom.android.tv.library/1000/u0 remote:5d105fb}}
            BroadcastFilter{82a3aad u0 ReceiverList{6029bc4 1443 com.swisscom.android.tv.library:IntentService/1000/u0 remote:92006d7}}
          swisscom.android.tv.action.CLIENT_AUTHENTICATED:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.CLEAR_SESSION:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          android.media.action.HDMI_AUDIO_PLUG:
            BroadcastFilter{2ed9b64 u0 ReceiverList{51ec0f7 1385 com.swisscom.android.tv.library/1000/u0 remote:13b84f6}}
          swisscom.android.tv.action.FIRMWARE_CHECKED:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.ALU_READ_EVALUATE:
            BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
          swisscom.android.tv.action.DISPATCH_SUCCESS:
            BroadcastFilter{8785ed5 u0 ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}}
            BroadcastFilter{579bcb7 u0 ReceiverList{7fa17b6 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c6d1351}}
          com.swisscom.dialserver.action.LAUNCH_APP:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          android.intent.action.TIME_SET:
            BroadcastFilter{207f942 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.REPORT_RADIO_TUNE:
            BroadcastFilter{c1a53c7 u0 ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}}
          swisscom.android.tv.action.REPORT_WATCH_REPLAY_START:
            BroadcastFilter{c1a53c7 u0 ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}}
          com.swisscom.dialserver.action.STAT_APP_STARTED:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          swisscom.android.tv.action.DISPATCH_PENDING_FIRMWARE:
            BroadcastFilter{8785ed5 u0 ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}}
          swisscom.android.tv.action.WIFI_QUALITY_START_SLOT:
            BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
          com.swisscom.dialserver.action.STAT_APP_ENABLED:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          swisscom.android.tv.action.LOGOS_DOWNLOADED:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          com.swisscom.dialserver.action.STOP_APP:
            BroadcastFilter{eeb63eb u0 ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}}
          swisscom.android.tv.action.MASTER_LINEUP_REFRESHED:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
          swisscom.android.tv.action.BANDWIDTH_RESERVATION_RENEW:
            BroadcastFilter{75e983 u0 ReceiverList{2030832 1385 com.swisscom.android.tv.library/1000/u0 remote:851c83d}}
          swisscom.android.tv.action.REPORT_WATCH_RECORDING_START:
            BroadcastFilter{c1a53c7 u0 ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}}
          swisscom.android.tv.action.GET_ACTUAL_STATE:
            BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}

    Historical broadcasts [background]:
    Historical Broadcast background #0:
      BroadcastRecord{438e395 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:54:59 dispatchClockTime=2020-10-07 13:54:59
      dispatchTime=-1m34s156ms (0 since enq) finishTime=-1m34s153ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #1:
      BroadcastRecord{2a9e5b4 u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:53:49 dispatchClockTime=2020-10-07 13:53:49
      dispatchTime=-2m44s537ms (0 since enq) finishTime=-2m44s405ms (+132ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #2:
      BroadcastRecord{771cac0 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:49:59 dispatchClockTime=2020-10-07 13:49:59
      dispatchTime=-6m34s158ms (0 since enq) finishTime=-6m34s155ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #3:
      BroadcastRecord{28666cb u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:48:49 dispatchClockTime=2020-10-07 13:48:49
      dispatchTime=-7m44s538ms (0 since enq) finishTime=-7m44s396ms (+142ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #8:
      BroadcastRecord{9d6362f u0 swisscom.android.tv.action.STATE_UPDATE} to user 0
      Intent { act=swisscom.android.tv.action.STATE_UPDATE flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=96]
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:45:00 dispatchClockTime=2020-10-07 13:45:00
      dispatchTime=-11m33s218ms (0 since enq) finishTime=-11m33s217ms (+1ms since disp)
      Deliver #0: BroadcastFilter{409435c u0 ReceiverList{a70adcf 5238 com.swisscom.swisscomTv/10048/u0 remote:7103e2e}}
    Historical Broadcast background #16:
      BroadcastRecord{74f6074 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:44:59 dispatchClockTime=2020-10-07 13:44:59
      dispatchTime=-11m34s159ms (0 since enq) finishTime=-11m34s155ms (+4ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #18:
      BroadcastRecord{c11943c u0 swisscom.android.tv.action.STATE_UPDATE} to user 0
      Intent { act=swisscom.android.tv.action.STATE_UPDATE flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=96]
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:44:46 dispatchClockTime=2020-10-07 13:44:46
      dispatchTime=-11m47s678ms (0 since enq) finishTime=-11m47s678ms (0 since disp)
      Deliver #0: BroadcastFilter{2c0be5 u0 ReceiverList{b408edc 4985 com.swisscom.swisscomTv/10048/u0 remote:50ff74f}}
    Historical Broadcast background #21:
      BroadcastRecord{adbcba1 u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:43:49 dispatchClockTime=2020-10-07 13:43:49
      dispatchTime=-12m44s540ms (0 since enq) finishTime=-12m44s407ms (+133ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #22:
      BroadcastRecord{12b31c0 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:39:59 dispatchClockTime=2020-10-07 13:39:59
      dispatchTime=-16m34s161ms (0 since enq) finishTime=-16m34s158ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #23:
      BroadcastRecord{51fd98d u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:38:49 dispatchClockTime=2020-10-07 13:38:49
      dispatchTime=-17m44s542ms (+1ms since enq) finishTime=-17m44s407ms (+135ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #24:
      BroadcastRecord{62e84ea u0 swisscom.android.tv.action.MASTER_LINEUP_REFRESHED} to user 0
      Intent { act=swisscom.android.tv.action.MASTER_LINEUP_REFRESHED flg=0x10 }
      caller=com.swisscom.android.tv.library 1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000
      enqueueClockTime=2020-10-07 13:37:58 dispatchClockTime=2020-10-07 13:37:58
      dispatchTime=-18m35s496ms (0 since enq) finishTime=-18m35s493ms (+3ms since disp)
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
    Historical Broadcast background #25:
      BroadcastRecord{10e95c5 u0 swisscom.android.tv.action.BACKGROUND_WORK_END} to user 0
      Intent { act=swisscom.android.tv.action.BACKGROUND_WORK_END flg=0x10 }
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:37:58 dispatchClockTime=2020-10-07 13:37:58
      dispatchTime=-18m35s493ms (0 since enq) finishTime=-18m35s493ms (0 since disp)
      Deliver #0: BroadcastFilter{8eaedb8 u0 ReceiverList{357581b 3225 com.swisscom.swisscomTv/10048/u0 remote:151322a}}
    Historical Broadcast background #26:
      BroadcastRecord{35fb1a u0 swisscom.android.tv.action.STATE_EVENT} to user 0
      Intent { act=swisscom.android.tv.action.STATE_EVENT flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=316]
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:37:58 dispatchClockTime=2020-10-07 13:37:58
      dispatchTime=-18m35s494ms (0 since enq) finishTime=-18m35s494ms (0 since disp)
      Deliver #0: BroadcastFilter{a283ca4 u0 ReceiverList{8861f37 3225 com.swisscom.swisscomTv/10048/u0 remote:8c87436}}
    Historical Broadcast background #27:
      BroadcastRecord{9eee4d5 u0 swisscom.android.tv.action.LOGOS_DOWNLOADED} to user 0
      Intent { act=swisscom.android.tv.action.LOGOS_DOWNLOADED flg=0x10 }
      caller=com.swisscom.android.tv.library 1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000
      enqueueClockTime=2020-10-07 13:37:57 dispatchClockTime=2020-10-07 13:37:57
      dispatchTime=-18m36s979ms (+1ms since enq) finishTime=-18m36s973ms (+6ms since disp)
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{f5b2a51 u0 ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}}
    Historical Broadcast background #28:
      BroadcastRecord{99a064b u0 swisscom.android.tv.action.BACKGROUND_WORK_END} to user 0
      Intent { act=swisscom.android.tv.action.BACKGROUND_WORK_END flg=0x10 }
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:37:57 dispatchClockTime=2020-10-07 13:37:57
      dispatchTime=-18m36s974ms (0 since enq) finishTime=-18m36s974ms (0 since disp)
      Deliver #0: BroadcastFilter{8eaedb8 u0 ReceiverList{357581b 3225 com.swisscom.swisscomTv/10048/u0 remote:151322a}}
    Historical Broadcast background #29:
      BroadcastRecord{d81b828 u0 swisscom.android.tv.action.STATE_EVENT} to user 0
      Intent { act=swisscom.android.tv.action.STATE_EVENT flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=316]
      caller=com.swisscom.android.tv.library 1352:com.swisscom.android.tv.library:BoundService/1000 pid=1352 uid=1000
      enqueueClockTime=2020-10-07 13:37:57 dispatchClockTime=2020-10-07 13:37:57
      dispatchTime=-18m36s977ms (+1ms since enq) finishTime=-18m36s977ms (0 since disp)
      Deliver #0: BroadcastFilter{a283ca4 u0 ReceiverList{8861f37 3225 com.swisscom.swisscomTv/10048/u0 remote:8c87436}}
    Historical Broadcast background #30:
      BroadcastRecord{7b4758c u0 swisscom.android.tv.action.SETTINGS_SYNCED} to user 0
      Intent { act=swisscom.android.tv.action.SETTINGS_SYNCED flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=88]
      caller=com.swisscom.android.tv.library 1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000
      enqueueClockTime=2020-10-07 13:37:56 dispatchClockTime=2020-10-07 13:37:56
      dispatchTime=-18m38s19ms (0 since enq) finishTime=-18m37s809ms (+210ms since disp)
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=30 receiver=null
      Deliver #0: (manifest)
        priority=900 preferredOrder=0 match=0x108000 specificIndex=-1 isDefault=true
        labelRes=0x0 nonLocalizedLabel=BROADCASTS icon=0x0
        ActivityInfo:
          name=com.swisscom.android.tv.library.internal.receivers.LibraryReceiver
          packageName=com.swisscom.android.tv.library
          enabled=true exported=true directBootAware=false
          resizeMode=RESIZE_MODE_RESIZEABLE
      Deliver #1: BroadcastFilter{745abf5 u0 ReceiverList{9db652c 3225 com.swisscom.swisscomTv/10048/u0 remote:ab1f4df}}
      Deliver #2: BroadcastFilter{c2fa818 u0 ReceiverList{3eafffb 3225 com.swisscom.swisscomTv/10048/u0 remote:78d0d8a}}
      Deliver #3: BroadcastFilter{7dfa0d7 u0 ReceiverList{db67856 3225 com.swisscom.swisscomTv/10048/u0 remote:121271}}
      Deliver #4: BroadcastFilter{b39c3e2 u0 ReceiverList{b6464ad 3225 com.swisscom.swisscomTv/10048/u0 remote:a832dc4}}
      Deliver #5: BroadcastFilter{80f9ea9 u0 ReceiverList{7676230 3225 com.swisscom.swisscomTv/10048/u0 remote:4137373}}
      Deliver #6: BroadcastFilter{b18715c u0 ReceiverList{a7d3cf 3225 com.swisscom.swisscomTv/10048/u0 remote:b43c2e}}
      Deliver #7: BroadcastFilter{c77ddeb u0 ReceiverList{94bed3a 3225 com.swisscom.swisscomTv/10048/u0 remote:51a7c65}}
      Deliver #8: BroadcastFilter{49ee992 u0 ReceiverList{614d31d 3225 com.swisscom.swisscomTv/10048/u0 remote:66f8ff4}}
      Deliver #9: BroadcastFilter{40b4ebf u0 ReceiverList{3e0cde 3225 com.swisscom.swisscomTv/10048/u0 remote:b308419}}
      Deliver #10: BroadcastFilter{41a18ea u0 ReceiverList{cbc48d5 3225 com.swisscom.swisscomTv/10048/u0 remote:188e98c}}
      Deliver #11: BroadcastFilter{ff8d9b6 u0 ReceiverList{2059d51 3225 com.swisscom.swisscomTv/10048/u0 remote:da11278}}
      Deliver #12: BroadcastFilter{fb5bd8d u0 ReceiverList{510de24 3225 com.swisscom.swisscomTv/10048/u0 remote:80e56b7}}
      Deliver #13: BroadcastFilter{78fb890 u0 ReceiverList{6a7a753 3225 com.swisscom.swisscomTv/10048/u0 remote:830db42}}
      Deliver #14: BroadcastFilter{97b65af u0 ReceiverList{df5698e 3225 com.swisscom.swisscomTv/10048/u0 remote:1cda589}}
      Deliver #15: BroadcastFilter{62909a u0 ReceiverList{9621145 3225 com.swisscom.swisscomTv/10048/u0 remote:6dfcdbc}}
      Deliver #16: BroadcastFilter{a177cc1 u0 ReceiverList{cba09a8 3225 com.swisscom.swisscomTv/10048/u0 remote:322adcb}}
      Deliver #17: BroadcastFilter{37a1854 u0 ReceiverList{cac5ba7 3225 com.swisscom.swisscomTv/10048/u0 remote:2491c66}}
      Deliver #18: BroadcastFilter{7390b43 u0 ReceiverList{ba98f2 3225 com.swisscom.swisscomTv/10048/u0 remote:35e23fd}}
      Deliver #19: BroadcastFilter{655523e u0 ReceiverList{16e02f9 3225 com.swisscom.swisscomTv/10048/u0 remote:d8a65c0}}
      Deliver #20: BroadcastFilter{202d5b5 u0 ReceiverList{7901dec 3225 com.swisscom.swisscomTv/10048/u0 remote:b57189f}}
      Deliver #21: BroadcastFilter{1572cd8 u0 ReceiverList{21e9fbb 3225 com.swisscom.swisscomTv/10048/u0 remote:750544a}}
      Deliver #22: BroadcastFilter{40d7c97 u0 ReceiverList{2476b16 3225 com.swisscom.swisscomTv/10048/u0 remote:8d81831}}
      Deliver #23: BroadcastFilter{1c722a2 u0 ReceiverList{fe5066d 3225 com.swisscom.swisscomTv/10048/u0 remote:97e3e84}}
      Deliver #24: BroadcastFilter{f589c69 u0 ReceiverList{7e2bef0 3225 com.swisscom.swisscomTv/10048/u0 remote:9a34b33}}
      Deliver #25: BroadcastFilter{2ccda1c u0 ReceiverList{9bd678f 3225 com.swisscom.swisscomTv/10048/u0 remote:a98c6ee}}
      Deliver #26: BroadcastFilter{1b2edab u0 ReceiverList{2ce63fa 3225 com.swisscom.swisscomTv/10048/u0 remote:9559625}}
      Deliver #27: BroadcastFilter{d8ec5c6 u0 ReceiverList{56e6fa1 3225 com.swisscom.swisscomTv/10048/u0 remote:adb7c08}}
      Deliver #28: BroadcastFilter{7e164dd u0 ReceiverList{9b050b4 3225 com.swisscom.swisscomTv/10048/u0 remote:330b987}}
      Deliver #29: BroadcastFilter{965d96f u0 ReceiverList{376544e 3225 com.swisscom.swisscomTv/10048/u0 remote:9e88349}}
    Historical Broadcast background #31:
      BroadcastRecord{d47c941 u0 swisscom.android.tv.action.DISPATCH_SUCCESS} to user 0
      Intent { act=swisscom.android.tv.action.DISPATCH_SUCCESS flg=0x10 (has extras) }
        extras: Bundle[mParcelledData.dataSize=96]
      caller=com.swisscom.android.tv.library 1385:com.swisscom.android.tv.library/1000 pid=1385 uid=1000
      enqueueClockTime=2020-10-07 13:37:56 dispatchClockTime=2020-10-07 13:37:56
      dispatchTime=-18m38s22ms (0 since enq) finishTime=-18m38s22ms (0 since disp)
      Deliver #0: BroadcastFilter{8785ed5 u0 ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}}
      Deliver #1: BroadcastFilter{579bcb7 u0 ReceiverList{7fa17b6 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c6d1351}}
    Historical Broadcast background #32:
      BroadcastRecord{71f418 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:34:59 dispatchClockTime=2020-10-07 13:34:59
      dispatchTime=-21m34s163ms (0 since enq) finishTime=-21m34s161ms (+2ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #33:
      BroadcastRecord{1cb1f83 u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:33:49 dispatchClockTime=2020-10-07 13:33:49
      dispatchTime=-22m44s544ms (0 since enq) finishTime=-22m44s409ms (+135ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #36:
      BroadcastRecord{76946ff u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:29:59 dispatchClockTime=2020-10-07 13:29:59
      dispatchTime=-26m34s164ms (0 since enq) finishTime=-26m34s161ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #37:
      BroadcastRecord{a1b1e88 u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:28:49 dispatchClockTime=2020-10-07 13:28:49
      dispatchTime=-27m44s545ms (0 since enq) finishTime=-27m44s416ms (+129ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #38:
      BroadcastRecord{f7677c3 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:24:59 dispatchClockTime=2020-10-07 13:24:59
      dispatchTime=-31m34s165ms (0 since enq) finishTime=-31m34s162ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #39:
      BroadcastRecord{8068f1a u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:23:49 dispatchClockTime=2020-10-07 13:23:49
      dispatchTime=-32m44s546ms (0 since enq) finishTime=-32m44s410ms (+136ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #40:
      BroadcastRecord{f385a74 u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:19:59 dispatchClockTime=2020-10-07 13:19:59
      dispatchTime=-36m34s166ms (0 since enq) finishTime=-36m34s163ms (+3ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #41:
      BroadcastRecord{83a2f1 u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:18:49 dispatchClockTime=2020-10-07 13:18:49
      dispatchTime=-37m44s548ms (0 since enq) finishTime=-37m44s414ms (+134ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}
    Historical Broadcast background #42:
      BroadcastRecord{49cd44d u0 swisscom.android.tv.action.WIFI_QUALITY_START_SLOT} to user 0
      Intent { act=swisscom.android.tv.action.WIFI_QUALITY_START_SLOT flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:14:59 dispatchClockTime=2020-10-07 13:14:59
      dispatchTime=-41m34s167ms (0 since enq) finishTime=-41m34s165ms (+2ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{3528792 u0 ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}}
    Historical Broadcast background #43:
      BroadcastRecord{cd8ab4c u0 swisscom.android.tv.action.ALU_READ_EVALUATE} to user 0
      Intent { act=swisscom.android.tv.action.ALU_READ_EVALUATE flg=0x14 (has extras) }
        extras: Bundle[{android.intent.extra.ALARM_COUNT=1}]
      caller=com.swisscom.android.tv.library null pid=-1 uid=1000
      enqueueClockTime=2020-10-07 13:13:49 dispatchClockTime=2020-10-07 13:13:49
      dispatchTime=-42m44s549ms (0 since enq) finishTime=-42m44s410ms (+139ms since disp)
      resultTo=null resultCode=0 resultData=null
      resultAbort=false ordered=true sticky=false initialSticky=false
      nextReceiver=1 receiver=null
      Deliver #0: BroadcastFilter{e373a19 u0 ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}}

    mBroadcastsScheduled [foreground]=false
    mBroadcastsScheduled [background]=false
    mHandler:
      Handler (com.android.server.am.ActivityManagerService$MainHandler) {28aee6} @ 5895294
        Looper (ActivityManager, tid 18) {280bc27}
          Message 0: { when=+7m9s658ms what=27 target=com.android.server.am.ActivityManagerService$MainHandler }
          Message 1: { when=+11m21s979ms callback=com.android.server.AppOpsService$1 target=com.android.server.am.ActivityManagerService$MainHandler }
          (Total messages: 2, polling=true, quitting=false)

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER BROADCAST STATS STATE (dumpsys activity broadcast-stats)
    Current stats (from -1h37m56s348ms to now, +1h37m56s348ms uptime):
      swisscom.android.tv.action.ALU_READ_EVALUATE:
        Number received: 0, skipped: 0
        Total dispatch time: +2s565ms, max: +142ms
        Package com.swisscom.android.tv.library: 19 times
      swisscom.android.tv.action.SETTINGS_SYNCED:
        Number received: 2, skipped: 0
        Total dispatch time: +300ms, max: +210ms
        Package com.swisscom.android.tv.library: 2 times
      swisscom.android.tv.action.WIFI_QUALITY_START_SLOT:
        Number received: 0, skipped: 0
        Total dispatch time: +57ms, max: +4ms
        Package com.swisscom.android.tv.library: 19 times
      swisscom.android.tv.action.CLIENT_AUTHENTICATED:
        Number received: 1, skipped: 0
        Total dispatch time: +31ms, max: +31ms
        Package com.swisscom.android.tv.library: 1 times
      swisscom.android.tv.action.HDMI_HOTPLUG_CONCLUDED:
        Number received: 4, skipped: 0
        Total dispatch time: +11ms, max: +7ms
        Package com.swisscom.android.tv.library: 2 times
        Bg Check Violation com.swisscom.swisscomTv: 2 times
      swisscom.android.tv.action.MASTER_LINEUP_REFRESHED:
        Number received: 0, skipped: 0
        Total dispatch time: +9ms, max: +6ms
        Package com.swisscom.android.tv.library: 2 times
      swisscom.android.tv.action.LOGOS_DOWNLOADED:
        Number received: 0, skipped: 0
        Total dispatch time: +8ms, max: +6ms
        Package com.swisscom.android.tv.library: 2 times
      swisscom.android.tv.action.BOOT_COMPLETED:
        Number received: 2, skipped: 0
        Total dispatch time: +6ms, max: +5ms
        Package com.swisscom.android.tv.library: 2 times
        Bg Check Violation com.swisscom.dlnagui: 1 times
      swisscom.android.tv.action.FIRMWARE_CHECKED:
        Number received: 0, skipped: 0
        Total dispatch time: +4ms, max: +4ms
        Package com.swisscom.android.tv.library: 1 times
      swisscom.android.tv.action.EPG_CACHE_LOADED:
        Number received: 1, skipped: 0
        Total dispatch time: +3ms, max: +3ms
        Package com.swisscom.android.tv.library: 1 times
      swisscom.android.tv.action.HDMI_HOTPLUG_DETECTED:
        Number received: 2, skipped: 0
        Total dispatch time: +3ms, max: +2ms
        Package com.swisscom.android.tv.library: 2 times
        Bg Check Violation com.swisscom.swisscomTv: 2 times
      swisscom.android.tv.action.DEBUG_SERVICE_LOG_EVENT:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 15 times
      swisscom.android.tv.action.STAT_APP_REFRESH:
        Number received: 1, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 1 times
        Bg Check Violation com.swisscom.dialserver: 1 times
      swisscom.android.tv.action.HDMI_HOTPLUG_DISCONNECTED:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 1 times
      swisscom.android.tv.action.STATE_UPDATE:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 4 times
      swisscom.android.tv.action.BACKGROUND_WORK_END:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 3 times
      swisscom.android.tv.action.DISPATCH_SUCCESS:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 4 times
      swisscom.android.tv.action.STATE_EVENT:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 10 times
      swisscom.android.tv.action.LIB_SUCCESS:
        Number received: 0, skipped: 0
        Total dispatch time: 0, max: 0
        Package com.swisscom.android.tv.library: 4 times

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER CONTENT PROVIDERS (dumpsys activity providers)
    Published user 0 content providers (by class):
    * ContentProviderRecord{74e2ed4 u0 com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@a86b87d
      authority=com.swisscom.tvlib.lifecycle
      isSyncable=false multiprocess=false initOrder=9
    * ContentProviderRecord{540d372 u0 com.swisscom.android.tv.library/.internal.providers.AppsProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@932f3c3
      authority=com.swisscom.android.tv.apps
      isSyncable=false multiprocess=false initOrder=1
      Connections:
        -> 1352:com.swisscom.android.tv.library:BoundService/1000 s0/0 u1/1 +1h37m47s67ms
    * ContentProviderRecord{cc96440 u0 com.swisscom.android.tv.library/.internal.providers.CountersProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@7cb5f79
      authority=com.swisscom.android.counters
      isSyncable=false multiprocess=false initOrder=1
      Connections:
        -> 1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m40s79ms
        -> 1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h32m44s548ms
    * ContentProviderRecord{944b4be u0 com.swisscom.android.tv.library/.internal.providers.SettingsProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      launchingApp=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@a47091f
      authority=com.swisscom.android.tv.settings
      isSyncable=false multiprocess=false initOrder=8
      Connections:
        -> 1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h37m49s159ms
        -> 1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m46s714ms
        -> 5238:com.swisscom.swisscomTv/u0a48 s0/0 u2/2 +11m33s153ms
    * ContentProviderRecord{200846c u0 com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@a197a35
      authority=com.swisscom.android.tv.discovery
      isSyncable=false multiprocess=false initOrder=1
      Connections:
        -> 1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m37s896ms
        -> 5238:com.swisscom.swisscomTv/u0a48 s0/0 u1/1 +11m29s404ms
    * ContentProviderRecord{a135eca u0 com.swisscom.android.tv.library/.internal.providers.LibraryProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@b5d183b
      authority=com.swisscom.android.tv.epg
      isSyncable=false multiprocess=false initOrder=2
      Connections:
        -> 1352:com.swisscom.android.tv.library:BoundService/1000 s0/0 u1/1 +1h37m47s306ms
        -> 1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m39s348ms
        -> 5238:com.swisscom.swisscomTv/u0a48 s0/0 u1/1 +11m32s632ms
    * ContentProviderRecord{ca77b58 u0 com.swisscom.android.tv.library/.internal.providers.ConfigProvider}
      package=com.swisscom.android.tv.library process=com.swisscom.android.tv.library
      proc=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      launchingApp=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      uid=1000 provider=android.content.ContentProviderProxy@8f484b1
      authority=com.swisscom.android.tv.config
      isSyncable=false multiprocess=false initOrder=10
      Connections:
        -> 1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h37m49s686ms
        -> 1443:com.swisscom.android.tv.library:IntentService/1000 s1/1 u0/0 +1h37m49s437ms
        -> 5238:com.swisscom.swisscomTv/u0a48 s0/0 u1/1 +11m33s203ms

    User 0 authority to provider mappings:
    com.swisscom.android.tv.apps: 540d372/com.swisscom.android.tv.library/.internal.providers.AppsProvider
    com.swisscom.android.tv.config: ca77b58/com.swisscom.android.tv.library/.internal.providers.ConfigProvider
    com.swisscom.android.tv.epg: a135eca/com.swisscom.android.tv.library/.internal.providers.LibraryProvider
    com.swisscom.android.tv.settings: 944b4be/com.swisscom.android.tv.library/.internal.providers.SettingsProvider
    com.swisscom.android.counters: cc96440/com.swisscom.android.tv.library/.internal.providers.CountersProvider
    com.swisscom.tvlib.lifecycle: 74e2ed4/com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider
    com.swisscom.android.tv.discovery: 200846c/com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER URI PERMISSIONS (dumpsys activity permissions)
    (nothing)

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER SERVICES (dumpsys activity services)
    User 0 active services:
    * ServiceRecord{4204c23 u0 com.swisscom.android.tv.library/.internal.services.LogService}
      intent={act=swisscom.android.tv.action.LOG_CAPTURE_START cmp=com.swisscom.android.tv.library/.internal.services.LogService}
      packageName=com.swisscom.android.tv.library
      processName=com.swisscom.android.tv.library:IntentService
      permission=swisscom.android.tv.permission.LIBRARY_SERVICE
      baseDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      dataDir=/data/user/0/com.swisscom.android.tv.library
      app=ProcessRecord{e6d205a 1443:com.swisscom.android.tv.library:IntentService/1000}
      createTime=-1h37m46s720ms startingBgTimeout=--
      lastActivity=-1h37m45s432ms restartTime=-1h37m46s720ms createdFromFg=true
      startRequested=true delayedStop=false stopIfKilled=true callStart=true lastStartId=2

    * ServiceRecord{f649758 u0 com.swisscom.android.tv.library/.internal.services.RadioService}
      intent={act=swisscom.android.tv.action.BARRIER_BLOCKERS_SET cmp=com.swisscom.android.tv.library/.internal.services.RadioService}
      packageName=com.swisscom.android.tv.library
      processName=com.swisscom.android.tv.library
      baseDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      dataDir=/data/user/0/com.swisscom.android.tv.library
      app=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      createTime=-1h37m45s449ms startingBgTimeout=--
      lastActivity=-18m37s998ms restartTime=-1h37m45s449ms createdFromFg=true
      startRequested=true delayedStop=false stopIfKilled=false callStart=true lastStartId=5

    * ServiceRecord{f37d104 u0 com.swisscom.android.tv.library/.internal.services.NotificationService}
      intent={act=swisscom.android.tv.action.NOTIFICATION_INIT cmp=com.swisscom.android.tv.library/.internal.services.NotificationService}
      packageName=com.swisscom.android.tv.library
      processName=com.swisscom.android.tv.library:IntentService
      baseDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      dataDir=/data/user/0/com.swisscom.android.tv.library
      app=ProcessRecord{e6d205a 1443:com.swisscom.android.tv.library:IntentService/1000}
      createTime=-1h37m45s440ms startingBgTimeout=--
      lastActivity=-50m11s584ms restartTime=-1h37m45s440ms createdFromFg=true
      startRequested=true delayedStop=false stopIfKilled=true callStart=true lastStartId=3

    * ServiceRecord{8fd260f u0 com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
      intent={act=swisscom.android.tv.action.BIND_LIBRARY cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
      packageName=com.swisscom.android.tv.library
      processName=com.swisscom.android.tv.library:BoundService
      permission=swisscom.android.tv.permission.LIBRARY_SERVICE
      baseDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      dataDir=/data/user/0/com.swisscom.android.tv.library
      app=ProcessRecord{d20b24a 1352:com.swisscom.android.tv.library:BoundService/1000}
      createTime=-1h37m49s853ms startingBgTimeout=--
      lastActivity=-11m32s658ms restartTime=-1h37m49s794ms createdFromFg=true
      startRequested=true delayedStop=false stopIfKilled=false callStart=true lastStartId=1
      Bindings:
      * IntentBindRecord{2709d96 CREATE}:
        intent={act=swisscom.android.tv.action.BIND_LIBRARY cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@1fafd17
        requested=true received=true hasBound=false doRebind=false
        * Client AppBindRecord{7c4f504 ProcessRecord{15c3a56 5238:com.swisscom.swisscomTv/u0a48}}
          Per-process Connections:
            ConnectionRecord{7032d5 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@9523b8c}
            ConnectionRecord{433bfc4 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@28f3ad7}
      * IntentBindRecord{69bbaed CREATE}:
        intent={act=swisscom.android.tv.action.BIND_AUDIO cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@390fd22
        requested=true received=true hasBound=false doRebind=false
        * Client AppBindRecord{c2853b3 ProcessRecord{d20b24a 1352:com.swisscom.android.tv.library:BoundService/1000}}
          Per-process Connections:
            ConnectionRecord{27b8055 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@96c4f0c}
      * IntentBindRecord{61e5d70}:
        intent={act=swisscom.android.tv.action.BIND_HBBTV cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@618e9
        requested=true received=true hasBound=false doRebind=false
      * IntentBindRecord{b65c96e}:
        intent={act=swisscom.android.tv.action.BIND_POWER cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@6ca780f
        requested=true received=true hasBound=false doRebind=false
      * IntentBindRecord{f63e09c CREATE}:
        intent={act=swisscom.android.tv.action.BIND_PLAYBACK cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@9e5aa5
        requested=true received=true hasBound=false doRebind=false
        * Client AppBindRecord{3a90e7a ProcessRecord{15c3a56 5238:com.swisscom.swisscomTv/u0a48}}
          Per-process Connections:
            ConnectionRecord{79a5e2 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@40e8ead}
      * IntentBindRecord{dc0862b}:
        intent={act=swisscom.android.tv.action.BIND_SYSTEM_INFO cmp=com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
        binder=android.os.BinderProxy@41c6a88
        requested=true received=true hasBound=false doRebind=false
      All Connections:
        ConnectionRecord{433bfc4 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@28f3ad7}
        ConnectionRecord{79a5e2 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@40e8ead}
        ConnectionRecord{7032d5 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@9523b8c}
        ConnectionRecord{27b8055 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@96c4f0c}

    * ServiceRecord{4ad243b u0 com.swisscom.android.tv.library/.internal.services.EPGService}
      intent={act=swisscom.android.tv.action.BARRIER_BLOCKERS_SET cmp=com.swisscom.android.tv.library/.internal.services.EPGService}
      packageName=com.swisscom.android.tv.library
      processName=com.swisscom.android.tv.library
      baseDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk
      dataDir=/data/user/0/com.swisscom.android.tv.library
      app=ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      createTime=-1h37m45s451ms startingBgTimeout=--
      lastActivity=-4m4s137ms restartTime=-1h37m45s451ms createdFromFg=true
      startRequested=true delayedStop=false stopIfKilled=false callStart=true lastStartId=11

    Connection bindings to services:
    * ConnectionRecord{27b8055 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@96c4f0c}
      binding=AppBindRecord{c2853b3 com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:com.swisscom.android.tv.library:BoundService}
      conn=android.os.BinderProxy@96c4f0c flags=0x1

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER RECENT TASKS (dumpsys activity recents)
    (nothing)

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER ACTIVITIES (dumpsys activity lastanr)
    <no ANR has occurred since boot>

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER ACTIVITIES (dumpsys activity starter)
  ActivityStarter:
    mCurrentUser=0
    mLastStartReason=startActivityAsUser
    mLastStartActivityTimeMs=07 ott 2020 13:47:11
    mLastStartActivityResult=2
    mLastStartActivityRecord:
     packageName=com.swisscom.swisscomTv processName=com.swisscom.swisscomTv
     launchedFromUid=0 launchedFromPackage=null userId=0
     app=ProcessRecord{15c3a56 5238:com.swisscom.swisscomTv/u0a48}
     Intent { act=android.intent.action.MAIN cat=[android.intent.category.HOME] flg=0x10000100 cmp=com.swisscom.swisscomTv/.ActivityMain }
     frontOfTask=true task=TaskRecord{5befc21 #112 A=com.swisscom.swisscomTv U=0 StackId=0 sz=1}
     taskAffinity=com.swisscom.swisscomTv
     realActivity=com.swisscom.swisscomTv/.ActivityMain
     baseDir=/data/app/com.swisscom.swisscomTv-hhNWSdpv7VCQ-8_eqfdroQ==/base.apk
     dataDir=/data/user/0/com.swisscom.swisscomTv
     stateNotNeeded=false componentSpecified=false mActivityType=1
     compat={320dpi always-compat} labelRes=0x7f110073 icon=0x7f080170 theme=0x7f120008
     mLastReportedConfigurations:
      mGlobalConfig={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
      mOverrideConfig={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
     CurrentConfiguration={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
     taskDescription: iconFilename=null label="null" primaryColor=ffba86fc
      backgroundColor=ff121212
      statusBarColor=ff000000
      navigationBarColor=ff000000
     launchFailed=false launchCount=1 lastLaunchTime=-11m33s420ms
     haveState=false icicle=null
     state=RESUMED stopped=false delayedResume=false finishing=false
     keysPaused=false inHistory=true visible=true sleeping=false idle=true mStartingWindowState=STARTING_WINDOW_SHOWN
     fullscreen=true noDisplay=false immersive=false launchMode=3
     frozenBeforeDestroy=false forceNewConfig=false
     mActivityType=HOME_ACTIVITY_TYPE
     waitingVisible=false nowVisible=true lastVisibleTime=-11m31s154ms
     connections=[ConnectionRecord{2386938 u0 CR com.swisscom.swisscomTv/.v2.app.services.notification.FloatingNotificationService:@ec7919b}, ConnectionRecord{7032d5 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@9523b8c}]
     resizeMode=RESIZE_MODE_UNRESIZEABLE
     mLastReportedMultiWindowMode=false mLastReportedPictureInPictureMode=false
    mLastHomeActivityStartResult=0
    mLastHomeActivityStartRecord:
     packageName=com.swisscom.swisscomTv processName=com.swisscom.swisscomTv
     launchedFromUid=0 launchedFromPackage=null userId=0
     app=ProcessRecord{15c3a56 5238:com.swisscom.swisscomTv/u0a48}
     Intent { act=android.intent.action.MAIN cat=[android.intent.category.HOME] flg=0x10000100 cmp=com.swisscom.swisscomTv/.ActivityMain }
     frontOfTask=true task=TaskRecord{5befc21 #112 A=com.swisscom.swisscomTv U=0 StackId=0 sz=1}
     taskAffinity=com.swisscom.swisscomTv
     realActivity=com.swisscom.swisscomTv/.ActivityMain
     baseDir=/data/app/com.swisscom.swisscomTv-hhNWSdpv7VCQ-8_eqfdroQ==/base.apk
     dataDir=/data/user/0/com.swisscom.swisscomTv
     stateNotNeeded=false componentSpecified=false mActivityType=1
     compat={320dpi always-compat} labelRes=0x7f110073 icon=0x7f080170 theme=0x7f120008
     mLastReportedConfigurations:
      mGlobalConfig={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
      mOverrideConfig={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
     CurrentConfiguration={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
     taskDescription: iconFilename=null label="null" primaryColor=ffba86fc
      backgroundColor=ff121212
      statusBarColor=ff000000
      navigationBarColor=ff000000
     launchFailed=false launchCount=1 lastLaunchTime=-11m33s422ms
     haveState=false icicle=null
     state=RESUMED stopped=false delayedResume=false finishing=false
     keysPaused=false inHistory=true visible=true sleeping=false idle=true mStartingWindowState=STARTING_WINDOW_SHOWN
     fullscreen=true noDisplay=false immersive=false launchMode=3
     frozenBeforeDestroy=false forceNewConfig=false
     mActivityType=HOME_ACTIVITY_TYPE
     waitingVisible=false nowVisible=true lastVisibleTime=-11m31s156ms
     connections=[ConnectionRecord{2386938 u0 CR com.swisscom.swisscomTv/.v2.app.services.notification.FloatingNotificationService:@ec7919b}, ConnectionRecord{7032d5 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@9523b8c}]
     resizeMode=RESIZE_MODE_UNRESIZEABLE
     mLastReportedMultiWindowMode=false mLastReportedPictureInPictureMode=false
    mStartActivity:
     packageName=com.swisscom.swisscomTv processName=com.swisscom.swisscomTv
     launchedFromUid=10048 launchedFromPackage=com.swisscom.swisscomTv userId=0
     app=null
     Intent { flg=0x10000000 cmp=com.swisscom.swisscomTv/.ActivityMain (has extras) }
     frontOfTask=false task=TaskRecord{5befc21 #112 A=com.swisscom.swisscomTv U=0 StackId=0 sz=1}
     taskAffinity=com.swisscom.swisscomTv
     realActivity=com.swisscom.swisscomTv/.ActivityMain
     baseDir=/data/app/com.swisscom.swisscomTv-hhNWSdpv7VCQ-8_eqfdroQ==/base.apk
     dataDir=/data/user/0/com.swisscom.swisscomTv
     stateNotNeeded=false componentSpecified=true mActivityType=0
     compat=null labelRes=0x7f110073 icon=0x7f080170 theme=0x7f120008
     mLastReportedConfigurations:
      mGlobalConfig={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
      mOverrideConfig={0.0 ?mcc?mnc ?localeList ?layoutDir ?swdp ?wdp ?hdp ?density ?lsize ?long ?ldr ?wideColorGamut ?orien ?uimode ?night ?touch ?keyb/?/? ?nav/?}
     CurrentConfiguration={1.0 ?mcc?mnc [it] ldltr sw540dp w960dp h540dp 320dpi lrg long hdr land television -touch -keyb/v/h dpad/v appBounds=Rect(0, 0 - 1920, 1080) s.6}
     launchFailed=false launchCount=0 lastLaunchTime=0
     haveState=true icicle=null
     state=INITIALIZING stopped=false delayedResume=false finishing=false
     keysPaused=false inHistory=false visible=false sleeping=false idle=false mStartingWindowState=STARTING_WINDOW_NOT_SHOWN
     fullscreen=true noDisplay=false immersive=false launchMode=3
     frozenBeforeDestroy=false forceNewConfig=false
     mActivityType=APPLICATION_ACTIVITY_TYPE
     resizeMode=RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION
     mLastReportedMultiWindowMode=false mLastReportedPictureInPictureMode=false
    mIntent=Intent { flg=0x10000000 cmp=com.swisscom.swisscomTv/.ActivityMain (has extras) }
    mLaunchSingleTop=false mLaunchSingleInstance=true mLaunchSingleTask=false mLaunchFlags=0x10000000 mDoResume=true mAddingToTask=false

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER ACTIVITIES (dumpsys activity activities)
  Display #0 (activities from top to bottom):

    Stack #0:
    mFullscreen=true
    mBounds=null
    (nothing)

  -------------------------------------------------------------------------------
  ACTIVITY MANAGER RUNNING PROCESSES (dumpsys activity processes)
    All known processes:
    *APP* UID 1000 ProcessRecord{d20b24a 1352:com.swisscom.android.tv.library:BoundService/1000}
      user #0 uid=1000 gids={41000, 11000, 9997, 3002, 1023, 1015, 3003, 3001, 1007}
      requiredAbi=armeabi-v7a instructionSet=null
      class=com.swisscom.android.tv.library.internal.LibApplication
      dir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk publicDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk data=/data/user/0/com.swisscom.android.tv.library
      packageList={com.swisscom.android.tv.library}
      compat={320dpi always-compat}
      thread=android.app.IApplicationThread$Stub$Proxy@5a99846
      pid=1352 starting=false
      lastActivityTime=-11m32s662ms lastPssTime=-11m3s391ms nextPssTime=+3m56s532ms
      adjSeq=6956 lruSeq=0 lastPss=32MB lastSwapPss=0,00 lastCachedPss=0,00 lastCachedSwapPss=0,00
      cached=false empty=true
      oom: max=1001 curRaw=100 setRaw=100 cur=100 set=100
      curSchedGroup=1 setSchedGroup=1 systemNoUi=false trimMemoryLevel=0
      curProcState=3 repProcState=3 pssProcState=3 setProcState=3 lastStateTime=-11m33s267ms
      reportedInteraction=true time=-11m33s268ms
      hasClientActivities=true foregroundActivities=false (rep=false)
      hasStartedServices=true
      lastRequestedGc=-1h37m49s798ms lastLowMemory=-1h37m49s798ms reportLowMemory=false
      Services:
        - ServiceRecord{8fd260f u0 com.swisscom.android.tv.library/.internal.services.bound.ServiceManager}
      Connections:
        - ConnectionRecord{27b8055 u0 CR com.swisscom.android.tv.library/.internal.services.bound.ServiceManager:@96c4f0c}
      Connected Providers:
        - ca77b58/com.swisscom.android.tv.library/.internal.providers.ConfigProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h37m49s692ms
        - 944b4be/com.swisscom.android.tv.library/.internal.providers.SettingsProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h37m49s165ms
        - a135eca/com.swisscom.android.tv.library/.internal.providers.LibraryProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s0/0 u1/1 +1h37m47s312ms
        - 540d372/com.swisscom.android.tv.library/.internal.providers.AppsProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s0/0 u1/1 +1h37m47s73ms
        - 1bf5a07/com.android.providers.settings/.SettingsProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h37m44s769ms
        - cc96440/com.swisscom.android.tv.library/.internal.providers.CountersProvider->1352:com.swisscom.android.tv.library:BoundService/1000 s1/1 u0/0 +1h32m44s555ms
      Receivers:
        - ReceiverList{ef978c 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:98d8ade}
        - ReceiverList{2e1cb3a 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:e051265}
        - ReceiverList{2fc291d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fa67df4}
        - ReceiverList{3111ddb 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:5e376ea}
        - ReceiverList{415da66 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:4872c1}
        - ReceiverList{4a78560 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c5e6563}
        - ReceiverList{7fa17b6 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:c6d1351}
        - ReceiverList{81e938d 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:8df4c24}
        - ReceiverList{a916106 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:d396fe1}
        - ReceiverList{cbec1f5 1352 com.swisscom.android.tv.library:BoundService/1000/u0 remote:fd3132c}
    *APP* UID 1000 ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      user #0 uid=1000 gids={41000, 11000, 9997, 3002, 1023, 1015, 3003, 3001, 1007}
      requiredAbi=armeabi-v7a instructionSet=null
      class=com.swisscom.android.tv.library.internal.LibApplication
      dir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk publicDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk data=/data/user/0/com.swisscom.android.tv.library
      packageList={com.swisscom.android.tv.library}
      compat={320dpi always-compat}
      thread=android.app.IApplicationThread$Stub$Proxy@451a734
      pid=1385 starting=false
      lastActivityTime=-34s78ms lastPssTime=-11m3s343ms nextPssTime=+3m56s530ms
      adjSeq=6956 lruSeq=0 lastPss=29MB lastSwapPss=0,00 lastCachedPss=0,00 lastCachedSwapPss=0,00
      cached=false empty=true
      oom: max=1001 curRaw=0 setRaw=0 cur=0 set=0
      curSchedGroup=1 setSchedGroup=1 systemNoUi=false trimMemoryLevel=0
      curProcState=3 repProcState=3 pssProcState=3 setProcState=3 lastStateTime=-11m33s210ms
      reportedInteraction=true time=-11m33s210ms
      hasStartedServices=true
      lastRequestedGc=-1h37m49s627ms lastLowMemory=-1h37m49s627ms reportLowMemory=false
      Services:
        - ServiceRecord{4ad243b u0 com.swisscom.android.tv.library/.internal.services.EPGService}
        - ServiceRecord{f649758 u0 com.swisscom.android.tv.library/.internal.services.RadioService}
      Published Providers:
        - com.swisscom.android.tv.library.internal.providers.ConfigProvider
          -> ContentProviderRecord{ca77b58 u0 com.swisscom.android.tv.library/.internal.providers.ConfigProvider}
        - com.swisscom.android.tv.library.internal.providers.SettingsProvider
          -> ContentProviderRecord{944b4be u0 com.swisscom.android.tv.library/.internal.providers.SettingsProvider}
        - com.swisscom.tvlib.app.generic.service.LifecycleProvider
          -> ContentProviderRecord{74e2ed4 u0 com.swisscom.android.tv.library/com.swisscom.tvlib.app.generic.service.LifecycleProvider}
        - com.swisscom.android.tv.library.internal.providers.AppsProvider
          -> ContentProviderRecord{540d372 u0 com.swisscom.android.tv.library/.internal.providers.AppsProvider}
        - com.swisscom.android.tv.library.internal.providers.CountersProvider
          -> ContentProviderRecord{cc96440 u0 com.swisscom.android.tv.library/.internal.providers.CountersProvider}
        - com.swisscom.android.tv.library.internal.providers.DiscoveryProvider
          -> ContentProviderRecord{200846c u0 com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider}
        - com.swisscom.android.tv.library.internal.providers.LibraryProvider
          -> ContentProviderRecord{a135eca u0 com.swisscom.android.tv.library/.internal.providers.LibraryProvider}
      Connected Providers:
        - 1bf5a07/com.android.providers.settings/.SettingsProvider->1385:com.swisscom.android.tv.library/1000 s1/1 u0/0 +1h37m45s793ms
        - dee395d/com.swisscom.voiceservice/.app.generic.service.VoiceSettingsProvider->1385:com.swisscom.android.tv.library/1000 s0/0 u1/1 +1h37m44s721ms
      Receivers:
        - ReceiverList{1f3040b 1385 com.swisscom.android.tv.library/1000/u0 remote:c0157da}
        - ReceiverList{2030832 1385 com.swisscom.android.tv.library/1000/u0 remote:851c83d}
        - ReceiverList{412fa82 1385 com.swisscom.android.tv.library/1000/u0 remote:7dbd1cd}
        - ReceiverList{4f43618 1385 com.swisscom.android.tv.library/1000/u0 remote:5d105fb}
        - ReceiverList{51ec0f7 1385 com.swisscom.android.tv.library/1000/u0 remote:13b84f6}
        - ReceiverList{96ef2fc 1385 com.swisscom.android.tv.library/1000/u0 remote:e66d7ef}
        - ReceiverList{9e0bdc9 1385 com.swisscom.android.tv.library/1000/u0 remote:49b09d0}
    *APP* UID 1000 ProcessRecord{e6d205a 1443:com.swisscom.android.tv.library:IntentService/1000}
      user #0 uid=1000 gids={41000, 11000, 9997, 3002, 1023, 1015, 3003, 3001, 1007}
      requiredAbi=armeabi-v7a instructionSet=null
      class=com.swisscom.android.tv.library.internal.LibApplication
      dir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk publicDir=/system/priv-app/swisscom-tv-library-IP2000-O-10.2.0-release.apk data=/data/user/0/com.swisscom.android.tv.library
      packageList={com.swisscom.android.tv.library}
      compat={320dpi always-compat}
      thread=android.app.IApplicationThread$Stub$Proxy@ed6f2d2
      pid=1443 starting=false
      lastActivityTime=-34s143ms lastPssTime=-16m45s38ms nextPssTime=+3m14s857ms
      adjSeq=6956 lruSeq=0 lastPss=8,4MB lastSwapPss=0,00 lastCachedPss=0,00 lastCachedSwapPss=0,00
      cached=true empty=true
      oom: max=1001 curRaw=1001 setRaw=900 cur=1001 set=900
      curSchedGroup=0 setSchedGroup=0 systemNoUi=false trimMemoryLevel=0
      curProcState=11 repProcState=11 pssProcState=11 setProcState=11 lastStateTime=-1h37m49s483ms
      hasStartedServices=true
      lastWakeTime=0 timeUsed=0
      lastCpuTime=0 timeUsed=0
      lastRequestedGc=-1h37m49s484ms lastLowMemory=-1h37m49s484ms reportLowMemory=false
      Services:
        - ServiceRecord{4204c23 u0 com.swisscom.android.tv.library/.internal.services.LogService}
        - ServiceRecord{f37d104 u0 com.swisscom.android.tv.library/.internal.services.NotificationService}
      Connected Providers:
        - ca77b58/com.swisscom.android.tv.library/.internal.providers.ConfigProvider->1443:com.swisscom.android.tv.library:IntentService/1000 s1/1 u0/0 +1h37m49s444ms
        - 944b4be/com.swisscom.android.tv.library/.internal.providers.SettingsProvider->1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m46s721ms
        - cc96440/com.swisscom.android.tv.library/.internal.providers.CountersProvider->1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m40s86ms
        - a135eca/com.swisscom.android.tv.library/.internal.providers.LibraryProvider->1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m39s355ms
        - 200846c/com.swisscom.android.tv.library/.internal.providers.DiscoveryProvider->1443:com.swisscom.android.tv.library:IntentService/1000 s0/0 u1/1 +1h37m37s903ms
      Receivers:
        - ReceiverList{6029bc4 1443 com.swisscom.android.tv.library:IntentService/1000/u0 remote:92006d7}

    UID states:
      UID 1000: UidRecord{fed8fa3 1000 PER  fgServices procs:17 seq(0,0,0)}

    UID validation:
      UID 1000: UidRecord{4fc02a0 1000 PER  idle procs:0 seq(0,0,0)}

    Process LRU list (sorted by oom_adj, 33 total, non-act at 2, non-svc at 2):
      Proc # 2: fore  F/ /BFGS trm: 0 1385:com.swisscom.android.tv.library/1000 (provider-top)
          com.swisscom.android.tv.library/.internal.providers.ConfigProvider<=Proc{5238:com.swisscom.swisscomTv/u0a48}
      Proc # 0: vis   F/ /BFGS trm: 0 1352:com.swisscom.android.tv.library:BoundService/1000 (service)
          com.swisscom.android.tv.library/.internal.services.bound.ServiceManager<=Proc{5238:com.swisscom.swisscomTv/u0a48}
      Proc # 3: cch   B/ /SVC  trm: 0 1443:com.swisscom.android.tv.library:IntentService/1000 (cch-started-services)

    PID mappings:
      PID #1352: ProcessRecord{d20b24a 1352:com.swisscom.android.tv.library:BoundService/1000}
      PID #1385: ProcessRecord{82d17a6 1385:com.swisscom.android.tv.library/1000}
      PID #1443: ProcessRecord{e6d205a 1443:com.swisscom.android.tv.library:IntentService/1000}
    mPreviousProcessVisibleTime: 0
    mConfigWillChange: false
    mDeviceIdleWhitelist=[2000, 10003, 10041]
    mDeviceIdleTempWhitelist=[]
    mVrController=[VrState=0x0,VrRenderThreadTid=0]

DUMP OF SERVICE meminfo:
  Applications Memory Usage (in Kilobytes):
  Uptime: 5895322 Realtime: 5895322

  ** MEMINFO in pid 1443 [com.swisscom.android.tv.library:IntentService] **
                     Pss  Private  Private  SwapPss     Heap     Heap     Heap
                   Total    Dirty    Clean    Dirty     Size    Alloc     Free
                  ------   ------   ------   ------   ------   ------   ------
    Native Heap     1943     1792        0        0        0        0        0
    Dalvik Heap      682      664        0        0        0        0        0
   Dalvik Other      512      512        0        0                           
          Stack       28       28        0        0                           
      Other dev        8        0        8        0                           
       .so mmap      508       76        0        0                           
      .apk mmap       42        0        0        0                           
      .dex mmap     2594        8        0        0                           
      .oat mmap     1161        0       60        0                           
      .art mmap      690      456        0        0                           
     Other mmap       59        4        0        0                           
        Unknown      386      368        0        0                           
          TOTAL     8613     3908       68        0        0        0        0
   
   App Summary
                         Pss(KB)
                          ------
             Java Heap:     1120
           Native Heap:     1792
                  Code:      144
                 Stack:       28
              Graphics:        0
         Private Other:      892
                System:     4637
   
                 TOTAL:     8613       TOTAL SWAP PSS:        0

  ** MEMINFO in pid 1385 [com.swisscom.android.tv.library] **
                     Pss  Private  Private  SwapPss     Heap     Heap     Heap
                   Total    Dirty    Clean    Dirty     Size    Alloc     Free
                  ------   ------   ------   ------   ------   ------   ------
    Native Heap    16082    15936        0        0        0        0        0
    Dalvik Heap     2830     2812        0        0        0        0        0
   Dalvik Other     2384     2384        0        0                           
          Stack       28       28        0        0                           
         Ashmem        0        0        0        0                           
      Other dev      116        0      116        0                           
       .so mmap      600       88        0        0                           
      .apk mmap       61        0        0        0                           
      .dex mmap     3011        8       44        0                           
      .oat mmap     1552        0        0        0                           
      .art mmap      787      556        0        0                           
     Other mmap       88        4        0        0                           
        Unknown      845      828        0        0                           
          TOTAL    28384    22644      160        0        0        0        0
   
   App Summary
                         Pss(KB)
                          ------
             Java Heap:     3368
           Native Heap:    15936
                  Code:      140
                 Stack:       28
              Graphics:        0
         Private Other:     3332
                System:     5580
   
                 TOTAL:    28384       TOTAL SWAP PSS:        0

  ** MEMINFO in pid 1352 [com.swisscom.android.tv.library:BoundService] **
                     Pss  Private  Private  SwapPss     Heap     Heap     Heap
                   Total    Dirty    Clean    Dirty     Size    Alloc     Free
                  ------   ------   ------   ------   ------   ------   ------
    Native Heap    11627    11408        0        0        0        0        0
    Dalvik Heap     1063     1044        0        0        0        0        0
   Dalvik Other     1144     1144        0        0                           
          Stack       28       28        0        0                           
         Ashmem        0        0        0        0                           
      Other dev      234        0      116        0                           
       .so mmap    11720      764     9936        0                           
      .apk mmap       42        0        0        0                           
      .dex mmap     2508        8        4        0                           
      .oat mmap      930        0       60        0                           
      .art mmap      631      396        0        0                           
     Other mmap       53        4        0        0                           
        Unknown     1056     1048        0        0                           
          TOTAL    31036    15844    10116        0        0        0        0
   
   App Summary
                         Pss(KB)
                          ------
             Java Heap:     1440
           Native Heap:    11408
                  Code:    10772
                 Stack:       28
              Graphics:        0
         Private Other:     2312
                System:     5076
   
                 TOTAL:    31036       TOTAL SWAP PSS:        0

DUMP OF SERVICE procstats:
  CURRENT STATS:
  System memory usage:
    SOn /Norm: 1 samples:
      Cached: 239MB min, 239MB avg, 239MB max
      Free: 228MB min, 228MB avg, 228MB max
      ZRam: 12KB min, 12KB avg, 12KB max
      Kernel: 125MB min, 125MB avg, 125MB max
      Native: 201MB min, 201MB avg, 201MB max

  Per-Package Stats:
    * com.swisscom.android.tv.library / 1000 / v9:
        * com.swisscom.android.tv.library:IntentService / 1000 / v9:
                 TOTAL: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
               Service: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
        * com.swisscom.android.tv.library / 1000 / v9:
                 TOTAL: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
                Imp Fg: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
               Service: 0,04%
        * com.swisscom.android.tv.library:BoundService / 1000 / v9:
                 TOTAL: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
                Imp Fg: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
               Service: 0,03%
        * com.swisscom.android.tv.library.internal.services.NotificationService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 3 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.FirmwareService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.NetflixService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,01%
              Started count 1 / time 0,01%
              Executing count 3 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.bound.ServiceManager:
          Process: com.swisscom.android.tv.library:BoundService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Bound count 1 / time 100%
              Executing count 9 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.AppsService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,06%
              Started count 1 / time 0,06%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.EPGService:
          Process: com.swisscom.android.tv.library
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 10 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSendService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 40 / time 0,10%
              Started count 20 / time 0,10%
              Executing count 40 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SystemService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 12 / time 0,06%
              Started count 6 / time 0,06%
              Executing count 14 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.PersonalDataService:
          Process: com.swisscom.android.tv.library
              Running count 226 / time 0,06%
              Started count 113 / time 0,06%
              Executing count 227 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.CompanionService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.AlarmService:
          Process: com.swisscom.android.tv.library
              Running count 400 / time 0,04%
              Started count 201 / time 0,04%
              Executing count 400 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.ScheduleService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 192 / time 0,04%
              Started count 99 / time 0,03%
              Executing count 192 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.SportService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,04%
              Started count 1 / time 0,04%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSaveService:
          Process: com.swisscom.android.tv.library
              Running count 58 / time 0,18%
              Started count 29 / time 0,18%
              Executing count 59 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.VODService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,13%
              Started count 1 / time 0,13%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.BootService:
          Process: com.swisscom.android.tv.library
              Running count 6 / time 0,02%
              Started count 3 / time 0,02%
              Executing count 6 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.DiscoveryService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.LogService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SettingsSyncService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,02%
              Started count 2 / time 0,02%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.RadioService:
          Process: com.swisscom.android.tv.library
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 5 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.UserService:
          Process: com.swisscom.android.tv.library
              Running count 198 / time 0,06%
              Started count 99 / time 0,06%
              Executing count 199 / time 0,01%

  Summary:
    * com.swisscom.android.tv.library:BoundService / 1000 / v9:
             TOTAL: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
            Imp Fg: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
           Service: 0,03%
    * com.swisscom.android.tv.library / 1000 / v9:
             TOTAL: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
            Imp Fg: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
           Service: 0,04%
    * com.swisscom.android.tv.library:IntentService / 1000 / v9:
             TOTAL: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
           Service: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)

  Run time Stats:
    SOn /Norm: +1h38m7s520ms (running)
        TOTAL: +1h38m7s520ms

  Memory usage:
    Kernel : 125MB (8 samples)
    Native : 201MB (8 samples)
    Persist: 107MB (49 samples)
    Top    : 181MB (53 samples)
    ImpFg  : 155MB (94 samples)
    ImpBg  : 11MB (35 samples)
    Service: 24MB (111 samples)
    Receivr: 2,9KB (100 samples)
    LastAct: 84KB (5 samples)
    CchEmty: 70MB (71 samples)
    Cached : 239MB (8 samples)
    Free   : 228MB (8 samples)
    Z-Ram  : 12KB (8 samples)
    TOTAL  : 1,3GB
    ServRst: 9,9KB (72 samples)

            Start time: 2009-02-14 00:31:37
    Total elapsed time: +1h38m8s722ms (partial) (swapped-out-pss) libart.so

  Available pages by page size:
  Zone   0       Unmovable      3     3     0     1     0     0     1     0     7     3     0
  Zone   0         Movable      0     1     0     1     1     1     1     0     0     0   136
  Zone   0     Reclaimable      1     1     1     1     0     0     0     1     0     1     0
  Zone   0      HighAtomic      0     0     0     0     0     0     0     0     0     0     0

  AGGREGATED OVER LAST 24 HOURS:
  System memory usage:
    SOn /Norm: 2 samples:
      Cached: 233MB min, 236MB avg, 239MB max
      Free: 228MB min, 230MB avg, 232MB max
      ZRam: 12KB min, 12KB avg, 12KB max
      Kernel: 125MB min, 126MB avg, 126MB max
      Native: 200MB min, 200MB avg, 201MB max

  Per-Package Stats:
    * com.swisscom.android.tv.library / 1000 / v9:
        * com.swisscom.android.tv.library:IntentService / 1000 / v9:
                 TOTAL: 100% (7,8MB-8,4MB-8,7MB/3,5MB-4,1MB-4,9MB over 9)
               Service: 100% (7,8MB-8,4MB-8,7MB/3,5MB-4,1MB-4,9MB over 9)
        * com.swisscom.android.tv.library / 1000 / v9:
                 TOTAL: 100% (24MB-27MB-30MB/19MB-23MB-25MB over 17)
                Imp Fg: 100% (24MB-27MB-30MB/19MB-23MB-25MB over 17)
               Service: 0,08%
        * com.swisscom.android.tv.library:BoundService / 1000 / v9:
                 TOTAL: 100% (14MB-23MB-32MB/11MB-18MB-27MB over 22)
                   Top: 9,4% (27MB-28MB-29MB/21MB-22MB-23MB over 6)
                Imp Fg: 90% (14MB-22MB-32MB/11MB-17MB-27MB over 16)
               Service: 0,07%
        * com.swisscom.android.tv.library.internal.services.NotificationService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 4 / time 99%
              Started count 3 / time 99%
              Executing count 15 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.FirmwareService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 4 / time 0,00%
              Started count 2 / time 0,00%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.NetflixService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 4 / time 0,01%
              Started count 2 / time 0,01%
              Executing count 5 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.bound.ServiceManager:
          Process: com.swisscom.android.tv.library:BoundService
              Running count 18 / time 99%
              Started count 7 / time 90%
              Bound count 6 / time 99%
              Executing count 35 / time 0,05%
        * com.swisscom.android.tv.library.internal.services.AppsService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,09%
              Started count 2 / time 0,09%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.EPGService:
          Process: com.swisscom.android.tv.library
              Running count 3 / time 99%
              Started count 3 / time 99%
              Executing count 22 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSendService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 62 / time 0,13%
              Started count 31 / time 0,13%
              Executing count 62 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SystemService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 55 / time 0,11%
              Started count 28 / time 0,11%
              Executing count 59 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.PersonalDataService:
          Process: com.swisscom.android.tv.library
              Running count 244 / time 0,06%
              Started count 122 / time 0,06%
              Executing count 245 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.CompanionService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.AlarmService:
          Process: com.swisscom.android.tv.library
              Running count 560 / time 0,04%
              Started count 281 / time 0,03%
              Executing count 560 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.ScheduleService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 274 / time 0,04%
              Started count 140 / time 0,04%
              Executing count 274 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.SportService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,05%
              Started count 2 / time 0,05%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSaveService:
          Process: com.swisscom.android.tv.library
              Running count 104 / time 0,26%
              Started count 52 / time 0,26%
              Executing count 106 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.VODService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,18%
              Started count 2 / time 0,18%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.BootService:
          Process: com.swisscom.android.tv.library
              Running count 26 / time 0,03%
              Started count 13 / time 0,03%
              Executing count 26 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.DiscoveryService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,00%
              Started count 2 / time 0,00%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.LogService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 3 / time 100%
              Started count 3 / time 100%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SettingsSyncService:
          Process: com.swisscom.android.tv.library
              Running count 6 / time 0,03%
              Started count 3 / time 0,03%
              Executing count 6 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.RadioService:
          Process: com.swisscom.android.tv.library
              Running count 3 / time 99%
              Started count 3 / time 99%
              Executing count 9 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.UserService:
          Process: com.swisscom.android.tv.library
              Running count 280 / time 0,07%
              Started count 140 / time 0,07%
              Executing count 282 / time 0,01%

  Summary:
    * com.swisscom.android.tv.library / 1000 / v9:
             TOTAL: 100% (24MB-27MB-30MB/19MB-23MB-25MB over 17)
            Imp Fg: 100% (24MB-27MB-30MB/19MB-23MB-25MB over 17)
           Service: 0,08%
    * com.swisscom.android.tv.library:BoundService / 1000 / v9:
             TOTAL: 100% (14MB-23MB-32MB/11MB-18MB-27MB over 22)
               Top: 9,4% (27MB-28MB-29MB/21MB-22MB-23MB over 6)
            Imp Fg: 90% (14MB-22MB-32MB/11MB-17MB-27MB over 16)
           Service: 0,07%
    * com.swisscom.android.tv.library:IntentService / 1000 / v9:
             TOTAL: 100% (7,8MB-8,4MB-8,7MB/3,5MB-4,1MB-4,9MB over 9)
           Service: 100% (7,8MB-8,4MB-8,7MB/3,5MB-4,1MB-4,9MB over 9)

  Run time Stats:
    SOn /Norm: +1h48m26s176ms
         Mod : +30m0s117ms
        TOTAL: +2h18m26s293ms

  Memory usage:
    Kernel : 126MB (16 samples)
    Native : 200MB (16 samples)
    Persist: 106MB (70 samples)
    Top    : 181MB (95 samples)
    ImpFg  : 142MB (156 samples)
    ImpBg  : 10MB (95 samples)
    Service: 23MB (269 samples)
    Receivr: 4,2KB (153 samples)
    LastAct: 117KB (8 samples)
    CchEmty: 67MB (127 samples)
    Cached : 236MB (16 samples)
    Free   : 230MB (16 samples)
    Z-Ram  : 12KB (16 samples)
    TOTAL  : 1,3GB
    ServRst: 34KB (135 samples)

            Start time: 2009-02-14 00:31:36
    Total elapsed time: +2h18m28s673ms (partial) (swapped-out-pss) libart.so

  Available pages by page size:
  Zone   0       Unmovable      3     3     0     1     0     0     1     0     7     3     0
  Zone   0         Movable      0     1     0     1     1     1     1     0     0     0   136
  Zone   0     Reclaimable      1     1     1     1     0     0     0     1     0     1     0
  Zone   0      HighAtomic      0     0     0     0     0     0     0     0     0     0     0

  AGGREGATED OVER LAST 3 HOURS:
  System memory usage:
    SOn /Norm: 1 samples:
      Cached: 239MB min, 239MB avg, 239MB max
      Free: 228MB min, 228MB avg, 228MB max
      ZRam: 12KB min, 12KB avg, 12KB max
      Kernel: 125MB min, 125MB avg, 125MB max
      Native: 201MB min, 201MB avg, 201MB max

  Per-Package Stats:
    * com.swisscom.android.tv.library / 1000 / v9:
        * com.swisscom.android.tv.library:IntentService / 1000 / v9:
                 TOTAL: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
               Service: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
        * com.swisscom.android.tv.library / 1000 / v9:
                 TOTAL: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
                Imp Fg: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
               Service: 0,04%
        * com.swisscom.android.tv.library:BoundService / 1000 / v9:
                 TOTAL: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
                Imp Fg: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
               Service: 0,03%
        * com.swisscom.android.tv.library.internal.services.NotificationService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 3 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.FirmwareService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.NetflixService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,01%
              Started count 1 / time 0,01%
              Executing count 3 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.bound.ServiceManager:
          Process: com.swisscom.android.tv.library:BoundService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Bound count 1 / time 100%
              Executing count 9 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.AppsService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,06%
              Started count 1 / time 0,06%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.EPGService:
          Process: com.swisscom.android.tv.library
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 10 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSendService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 40 / time 0,10%
              Started count 20 / time 0,10%
              Executing count 40 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SystemService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 12 / time 0,06%
              Started count 6 / time 0,06%
              Executing count 14 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.PersonalDataService:
          Process: com.swisscom.android.tv.library
              Running count 226 / time 0,06%
              Started count 113 / time 0,06%
              Executing count 227 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.CompanionService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.AlarmService:
          Process: com.swisscom.android.tv.library
              Running count 400 / time 0,04%
              Started count 201 / time 0,04%
              Executing count 400 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.ScheduleService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 192 / time 0,04%
              Started count 99 / time 0,03%
              Executing count 192 / time 0,02%
        * com.swisscom.android.tv.library.internal.services.SportService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,04%
              Started count 1 / time 0,04%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.CountersSaveService:
          Process: com.swisscom.android.tv.library
              Running count 58 / time 0,18%
              Started count 29 / time 0,18%
              Executing count 59 / time 0,01%
        * com.swisscom.android.tv.library.internal.services.VODService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,13%
              Started count 1 / time 0,13%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.BootService:
          Process: com.swisscom.android.tv.library
              Running count 6 / time 0,02%
              Started count 3 / time 0,02%
              Executing count 6 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.DiscoveryService:
          Process: com.swisscom.android.tv.library
              Running count 2 / time 0,00%
              Started count 1 / time 0,00%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.LogService:
          Process: com.swisscom.android.tv.library:IntentService
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 2 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.SettingsSyncService:
          Process: com.swisscom.android.tv.library
              Running count 4 / time 0,02%
              Started count 2 / time 0,02%
              Executing count 4 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.RadioService:
          Process: com.swisscom.android.tv.library
              Running count 1 / time 100%
              Started count 1 / time 100%
              Executing count 5 / time 0,00%
        * com.swisscom.android.tv.library.internal.services.UserService:
          Process: com.swisscom.android.tv.library
              Running count 198 / time 0,06%
              Started count 99 / time 0,06%
              Executing count 199 / time 0,01%

  Summary:
    * com.swisscom.android.tv.library:BoundService / 1000 / v9:
             TOTAL: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
            Imp Fg: 100% (21MB-27MB-32MB/17MB-22MB-27MB over 9)
           Service: 0,03%
    * com.swisscom.android.tv.library / 1000 / v9:
             TOTAL: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
            Imp Fg: 100% (24MB-27MB-29MB/19MB-21MB-23MB over 9)
           Service: 0,04%
    * com.swisscom.android.tv.library:IntentService / 1000 / v9:
             TOTAL: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)
           Service: 100% (7,8MB-8,3MB-8,7MB/3,5MB-3,8MB-4,2MB over 6)

  Run time Stats:
    SOn /Norm: +1h38m7s566ms
        TOTAL: +1h38m7s566ms

  Memory usage:
    Kernel : 125MB (8 samples)
    Native : 201MB (8 samples)
    Persist: 107MB (49 samples)
    Top    : 181MB (53 samples)
    ImpFg  : 155MB (94 samples)
    ImpBg  : 11MB (35 samples)
    Service: 24MB (111 samples)
    Receivr: 2,9KB (100 samples)
    LastAct: 84KB (5 samples)
    CchEmty: 70MB (71 samples)
    Cached : 239MB (8 samples)
    Free   : 228MB (8 samples)
    Z-Ram  : 12KB (8 samples)
    TOTAL  : 1,3GB
    ServRst: 9,9KB (72 samples)

            Start time: 2009-02-14 00:31:37
    Total elapsed time: +1h38m8s759ms (partial) (swapped-out-pss) libart.so

  Available pages by page size:
  Zone   0       Unmovable      3     3     0     1     0     0     1     0     7     3     0
  Zone   0         Movable      0     1     0     1     1     1     1     0     0     0   136
  Zone   0     Reclaimable      1     1     1     1     0     0     0     1     0     1     0
  Zone   0      HighAtomic      0     0     0     0     0     0     0     0     0     0     0

DUMP OF SERVICE usagestats:
  user=0 
    In-memory daily stats
    timeRange="7/10/2020, 12:18–13:45" 
      packages
        package=com.synaptics.hdrhandler totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.calendar totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.providers.media totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.power.shutdownreceiver totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.downloads totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.voiceservice totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.defcontainer totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.keychain totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.tv.netflix totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=android.ext.services totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.swisscom.panelcontroller totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.swisscomTv totalTime="1:26:15" lastTime="7/10/2020, 13:45" 
        package=com.swisscom.android.tv.library totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.settings totalTime="00:05" lastTime="7/10/2020, 13:45" 
        package=com.marvell.audio.loopback totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.userdictionary totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.systemui totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.bluetooth totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.contacts totalTime="00:00" lastTime="24/8/1981, 12:46" 
      
      ChooserCounts
        package=com.synaptics.hdrhandler 
        package=com.android.providers.calendar 
        package=com.android.providers.media 
        package=com.marvell.power.shutdownreceiver 
        package=com.android.providers.downloads 
        package=com.swisscom.voiceservice 
        package=com.android.defcontainer 
        package=com.android.keychain 
        package=com.marvell.tv.netflix 
        package=android.ext.services 
        package=com.swisscom.panelcontroller 
        package=com.swisscom.swisscomTv 
        package=com.swisscom.android.tv.library 
        package=com.android.settings 
        package=com.marvell.audio.loopback 
        package=com.android.providers.userdictionary 
        package=com.android.systemui 
        package=com.android.bluetooth 
        package=com.android.providers.contacts 
      configurations
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:20" lastTime="7/10/2020, 12:18" count=3 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
      events
        time="7/10/2020, 12:18" type=CONFIGURATION_CHANGE package=android config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 flags=0x0 
        time="7/10/2020, 12:18" type=CONFIGURATION_CHANGE package=android config=television-notnight-v26 flags=0x0 
        time="7/10/2020, 12:18" type=CONFIGURATION_CHANGE package=android config=v26 flags=0x0 
        time="7/10/2020, 12:18" type=CONFIGURATION_CHANGE package=android config=v26 flags=0x0 
        time="7/10/2020, 12:18" type=MOVE_TO_FOREGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 12:18" type=MOVE_TO_BACKGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 12:18" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 12:18" type=CONFIGURATION_CHANGE package=android config=v26 flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_BACKGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_BACKGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_FOREGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_BACKGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:05" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:44" type=MOVE_TO_BACKGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:44" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:45" type=MOVE_TO_BACKGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:45" type=MOVE_TO_FOREGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 13:45" type=MOVE_TO_BACKGROUND package=com.android.settings class=com.android.settings.FallbackHome flags=0x0 
        time="7/10/2020, 13:45" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
        time="7/10/2020, 13:45" type=MOVE_TO_FOREGROUND package=com.swisscom.swisscomTv class=com.swisscom.swisscomTv.ActivityMain flags=0x0 
    In-memory weekly stats
    timeRange="7/10/2020, 12:18–13:45" 
      packages
        package=com.synaptics.hdrhandler totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.calendar totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.providers.media totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.power.shutdownreceiver totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.downloads totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.voiceservice totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.defcontainer totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.keychain totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.tv.netflix totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=android.ext.services totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.swisscom.panelcontroller totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.swisscomTv totalTime="1:26:15" lastTime="7/10/2020, 13:45" 
        package=com.swisscom.android.tv.library totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.settings totalTime="00:05" lastTime="7/10/2020, 13:45" 
        package=com.marvell.audio.loopback totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.userdictionary totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.systemui totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.bluetooth totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.contacts totalTime="00:00" lastTime="24/8/1981, 12:46" 
      
      ChooserCounts
        package=com.synaptics.hdrhandler 
        package=com.android.providers.calendar 
        package=com.android.providers.media 
        package=com.marvell.power.shutdownreceiver 
        package=com.android.providers.downloads 
        package=com.swisscom.voiceservice 
        package=com.android.defcontainer 
        package=com.android.keychain 
        package=com.marvell.tv.netflix 
        package=android.ext.services 
        package=com.swisscom.panelcontroller 
        package=com.swisscom.swisscomTv 
        package=com.swisscom.android.tv.library 
        package=com.android.settings 
        package=com.marvell.audio.loopback 
        package=com.android.providers.userdictionary 
        package=com.android.systemui 
        package=com.android.bluetooth 
        package=com.android.providers.contacts 
      configurations
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:20" lastTime="7/10/2020, 12:18" count=3 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
      events
    In-memory monthly stats
    timeRange="7/10/2020, 12:18–13:45" 
      packages
        package=com.synaptics.hdrhandler totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.calendar totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.providers.media totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.power.shutdownreceiver totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.downloads totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.voiceservice totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.defcontainer totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.keychain totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.tv.netflix totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=android.ext.services totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.swisscom.panelcontroller totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.swisscomTv totalTime="1:26:15" lastTime="7/10/2020, 13:45" 
        package=com.swisscom.android.tv.library totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.settings totalTime="00:05" lastTime="7/10/2020, 13:45" 
        package=com.marvell.audio.loopback totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.userdictionary totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.systemui totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.bluetooth totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.contacts totalTime="00:00" lastTime="24/8/1981, 12:46" 
      
      ChooserCounts
        package=com.synaptics.hdrhandler 
        package=com.android.providers.calendar 
        package=com.android.providers.media 
        package=com.marvell.power.shutdownreceiver 
        package=com.android.providers.downloads 
        package=com.swisscom.voiceservice 
        package=com.android.defcontainer 
        package=com.android.keychain 
        package=com.marvell.tv.netflix 
        package=android.ext.services 
        package=com.swisscom.panelcontroller 
        package=com.swisscom.swisscomTv 
        package=com.swisscom.android.tv.library 
        package=com.android.settings 
        package=com.marvell.audio.loopback 
        package=com.android.providers.userdictionary 
        package=com.android.systemui 
        package=com.android.bluetooth 
        package=com.android.providers.contacts 
      configurations
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:20" lastTime="7/10/2020, 12:18" count=3 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
      events
    In-memory yearly stats
    timeRange="7/10/2020, 12:18–13:45" 
      packages
        package=com.synaptics.hdrhandler totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.calendar totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.providers.media totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.power.shutdownreceiver totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.downloads totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.voiceservice totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.defcontainer totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.android.keychain totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.marvell.tv.netflix totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=android.ext.services totalTime="00:00" lastTime="1/1/1970, 01:00" 
        package=com.swisscom.panelcontroller totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.swisscom.swisscomTv totalTime="1:26:15" lastTime="7/10/2020, 13:45" 
        package=com.swisscom.android.tv.library totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.settings totalTime="00:05" lastTime="7/10/2020, 13:45" 
        package=com.marvell.audio.loopback totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.userdictionary totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.systemui totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.bluetooth totalTime="00:00" lastTime="24/8/1981, 12:46" 
        package=com.android.providers.contacts totalTime="00:00" lastTime="24/8/1981, 12:46" 
      
      ChooserCounts
        package=com.synaptics.hdrhandler 
        package=com.android.providers.calendar 
        package=com.android.providers.media 
        package=com.marvell.power.shutdownreceiver 
        package=com.android.providers.downloads 
        package=com.swisscom.voiceservice 
        package=com.android.defcontainer 
        package=com.android.keychain 
        package=com.marvell.tv.netflix 
        package=android.ext.services 
        package=com.swisscom.panelcontroller 
        package=com.swisscom.swisscomTv 
        package=com.swisscom.android.tv.library 
        package=com.android.settings 
        package=com.marvell.audio.loopback 
        package=com.android.providers.userdictionary 
        package=com.android.systemui 
        package=com.android.bluetooth 
        package=com.android.providers.contacts 
      configurations
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:20" lastTime="7/10/2020, 12:18" count=3 
        config=it-ldltr-sw540dp-w960dp-h540dp-large-long-notround-highdr-nowidecg-land-television-notnight-xhdpi-notouch-keysexposed-nokeys-navexposed-dpad-v26 totalTime="00:00" lastTime="7/10/2020, 12:18" count=1 
      events
    
    Package idle stats:
      package=com.synaptics.hdrhandler lastUsedElapsed=+1h37m50s829ms lastUsedScreenOn=+1h37m50s829ms idle=n
      package=com.android.providers.calendar lastUsedElapsed=+1h37m47s852ms lastUsedScreenOn=+1h37m47s852ms idle=n
      package=com.android.providers.media lastUsedElapsed=+1h37m49s776ms lastUsedScreenOn=+1h37m49s776ms idle=n
      package=com.marvell.power.shutdownreceiver lastUsedElapsed=+1h37m50s845ms lastUsedScreenOn=+1h37m50s845ms idle=n
      package=com.android.providers.downloads lastUsedElapsed=+1h37m49s775ms lastUsedScreenOn=+1h37m49s775ms idle=n
      package=com.swisscom.voiceservice lastUsedElapsed=+11m33s738ms lastUsedScreenOn=+11m33s738ms idle=n
      package=com.android.defcontainer lastUsedElapsed=+11m44s818ms lastUsedScreenOn=+11m44s818ms idle=n
      package=android lastUsedElapsed=+12h9m7s406ms lastUsedScreenOn=+2h36m23s11ms idle=n
      package=com.android.keychain lastUsedElapsed=+1h37m50s730ms lastUsedScreenOn=+1h37m50s730ms idle=n
      package=com.marvell.tv.netflix lastUsedElapsed=+1h37m50s839ms lastUsedScreenOn=+1h37m50s839ms idle=n
      package=android.ext.services lastUsedElapsed=+1h37m36s569ms lastUsedScreenOn=+1h37m36s569ms idle=n
      package=com.swisscom.panelcontroller lastUsedElapsed=+1h37m50s834ms lastUsedScreenOn=+1h37m50s834ms idle=n
      package=com.swisscom.swisscomTv lastUsedElapsed=+11m33s957ms lastUsedScreenOn=+11m33s957ms idle=n
      package=com.swisscom.android.tv.library lastUsedElapsed=+11m33s789ms lastUsedScreenOn=+11m33s789ms idle=n
      package=com.android.settings lastUsedElapsed=+11m34s355ms lastUsedScreenOn=+11m34s355ms idle=n
      package=com.marvell.audio.loopback lastUsedElapsed=+1h37m50s731ms lastUsedScreenOn=+1h37m50s731ms idle=n
      package=com.android.providers.userdictionary lastUsedElapsed=+1h37m49s57ms lastUsedScreenOn=+1h37m49s57ms idle=n
      package=com.android.systemui lastUsedElapsed=+1h37m56s845ms lastUsedScreenOn=+1h37m56s845ms idle=n
      package=com.netflix.ninja lastUsedElapsed=+6h52m37s523ms lastUsedScreenOn=+1h35m45s79ms idle=n
      package=com.android.bluetooth lastUsedElapsed=+1h37m56s952ms lastUsedScreenOn=+1h37m56s952ms idle=n
      package=com.android.providers.contacts lastUsedElapsed=+1h37m49s57ms lastUsedScreenOn=+1h37m49s57ms idle=n
      
      totalElapsedTime=+12h9m8s417ms
      totalScreenOnTime=+2h36m23s11ms

  Carrier privileged apps (have=false): null

  Settings:
    mAppIdleDurationMillis=+12h0m0s0ms
    mAppIdleWallclockThresholdMillis=+2d0h0m0s0ms
    mCheckIdleIntervalMillis=+3h0m0s0ms
    mAppIdleParoleIntervalMillis=+1d0h0m0s0ms
    mAppIdleParoleDurationMillis=+10m0s0ms

  mAppIdleEnabled=false mAppIdleTempParoled=false mCharging=true mLastAppIdleParoledTime=0

DUMP OF SERVICE batterystats:
  Daily stats:
    Current start time: 2009-02-14-00-31-37
    Next min deadline: 2009-02-15-01-00-00
    Next max deadline: 2009-02-15-03-00-00
    Current daily steps:
    Daily from 2020-10-06-16-07-22 to 2009-02-14-00-31-37:
    Daily from 2009-02-14-00-31-37 to 2020-10-06-16-07-22:

  Statistics since last charge:
    System starts: 13, currently on battery: false
    Estimated battery capacity: 1000 mAh
    Time on battery: 0ms (0,0%) realtime, 0ms (0,0%) uptime
    Time on battery screen off: 0ms (0,0%) realtime, 0ms (0,0%) uptime
    Total run time: 12h 6m 29s 211ms realtime, 12h 6m 29s 211ms uptime
    Discharge: 0 mAh
    Screen off discharge: 0 mAh
    Screen on discharge: 0 mAh
    Start clock time: 2020-10-06-10-16-00
    Screen on: 0ms (--%) 0x, Interactive: 0ms (--%)
    Screen brightnesses: (no activity)
    Connectivity changes: 10
    Mobile total received: 0B, sent: 0B (packets received 0, sent 0)
    Phone signal levels: (no activity)
    Signal scanning time: 0ms
    Radio types: (no activity)
    Mobile radio active time: 0ms (--%) 0x
    Radio Idle time:   0ms (--%)
    Radio Rx time:     0ms (--%)
    Radio Tx time:     0ms (--%)
      [0] 0ms (--%)
      [1] 0ms (--%)
      [2] 0ms (--%)
      [3] 0ms (--%)
      [4] 0ms (--%)
    Radio Power drain: 0mAh
    Wi-Fi total received: 0B, sent: 0B (packets received 0, sent 0)
    Wifi on: 0ms (--%), Wifi running: 0ms (--%)
    Wifi states: (no activity)
    Wifi supplicant states: (no activity)
    Wifi signal levels: (no activity)
    WiFi Idle time:   0ms (--%)
    WiFi Rx time:     0ms (--%)
    WiFi Tx time:     0ms (--%)
    WiFi Power drain: 0mAh
    Bluetooth total received: 0B, sent: 0B
    Bluetooth scan time: 0ms 
    Bluetooth Idle time:   0ms (--%)
    Bluetooth Rx time:     0ms (--%)
    Bluetooth Tx time:     0ms (--%)
    Bluetooth Power drain: 0mAh

    Device battery use since last full charge
      Amount discharged (lower bound): 0
      Amount discharged (upper bound): 0
      Amount discharged while screen on: 0
      Amount discharged while screen off: 0

  Memory Stats
    1000:
      Wake lock ActivityManager-Sleep realtime
      Wake lock *dexopt* realtime
      Wake lock WiredAccessoryManager realtime
      Wake lock *alarm* realtime
      Wake lock PhoneWindowManager.mPowerKeyWakeLock realtime
      Wake lock AudioMix realtime
      Wake lock AudioIn realtime
      Wake lock *launch* realtime
      Wake lock NetworkStats realtime
      Wake lock WindowManager realtime
      Wake lock handleAudioEvent realtime
      Wake lock ShutdownThread-cpu realtime
      Wake lock *job*/android/com.android.server.pm.BackgroundDexOptService realtime
      Wake lock SyncLoopWakeLock realtime
      Wake lock SCREEN_FROZEN realtime
      Job android/com.android.server.pm.BackgroundDexOptService: (not used)
      Apk com.android.location.fused:
        Service com.android.location.fused.FusedLocationService:
          Created for: 0ms uptime
          Starts: 0, launches: 10
      Apk com.iwedia.stbmonitor:
        Service com.iwedia.stbmonitor.STBMonitorSetTimeService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.iwedia.stbmonitor.STBMonitorService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.marvell.onetouchplay:
        Service com.marvell.onetouchplay.OneTouchPlayService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.swisscom.android.tv.library:
        Service com.swisscom.android.tv.library.internal.services.RadioService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.swisscom.android.tv.library.internal.services.LogService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.swisscom.android.tv.library.internal.services.SystemService:
          Created for: 0ms uptime
          Starts: 4, launches: 4
        Service com.swisscom.android.tv.library.internal.services.EPGService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.swisscom.android.tv.library.internal.services.bound.ServiceManager:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.swisscom.android.tv.library.internal.services.NotificationService:
          Created for: 0ms uptime
          Starts: 6, launches: 6
      Apk com.swisscom.panelcontroller:
        Service com.swisscom.panelcontroller.PanelService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.swisscom.matchcontentservice:
        Service com.swisscom.matchcontentservice.MatchContentService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.marvell.wol:
        Service com.marvell.wol.WOLService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.marvell.tv.netflix:
        Service com.marvell.tv.netflix.PowerOnService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.marvell.tv.netflix.audiocapsignal.AudioCapabilitySignalService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.android.keychain:
        (nothing executed)
      Apk com.swisscom.dialserver:
        Service com.swisscom.dialserver.DIALServerService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.swisscom.hotwordservice:
        Service com.swisscom.hotwordservice.HotwordService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk android:
        Service android.hardware.location.GeofenceHardwareService:
          Created for: 0ms uptime
          Starts: 0, launches: 10
        Service com.android.server.content.SyncJobService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
        Service com.android.internal.backup.LocalTransportService:
          Created for: 0ms uptime
          Starts: 0, launches: 10
      Apk com.swisscom.voiceservice:
        Service com.swisscom.voiceservice.app.generic.service.VoiceService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
      Apk com.synaptics.hdrhandler:
        Service com.synaptics.hdrhandler.HDRHandlerService:
          Created for: 0ms uptime
          Starts: 10, launches: 10
"""

if __name__ == "__main__":
    unittest.main()
