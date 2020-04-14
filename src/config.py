# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("taro", "太郎", "", 20,(1,1), "male", "主人公"),
        ("man1", "男", "", 30,(1,1), "male", "会社員"),
        ## 001
        ("yuki", "由岐", "", 30,(1,1), "female", "人形師", "me:私"),
        ("hiro", "浩史", "", 35,(1,1), "male", "投資家", "me:俺"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ## 001
        ("yakata", "人形の館", "Tokyo"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        ## 001
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

