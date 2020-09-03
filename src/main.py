#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: The Stories for manuscript-papers.
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from story_1to10 import Story008
from story_1to10 import Story009


################################################################
#
#   1.人形師の女
#   2.絵画教室に通う姉
#   3.君を取り戻す男
#   4.電子蝶は夢を飛ぶ
#   5.悲しみは雨に似ている
#   6.涙の大河
#   7.風とシャボン玉
#   8.十年後の世界の君に
#   9.ただ会いたくて　＞AMGコン
#
################################################################


# Constant
TITLE = "原稿用紙の為の作品集"
MAJOR, MINOR, MICRO = 8, 0, 0
COPY = "原稿用紙は、物語をいつも待っている"
ONELINE = "原稿用紙三枚（約1200字程度）の掌編集。ジャンルも作風もバラバラです"
OUTLINE = "凪司工房が昔書いた掌編集から選んだ作品をリメイクし、約一冊分になるように作品を集めたものです"
THEME = "バラエティ"
GENRE = "各作品による"
TARGET = "20-50台（男女）"
SIZE = "〜1.2K"
CONTEST_INFO = ""
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (4, 15, 2020)



def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            Story008.ch_story008(w).omit(),
            Story009.ch_story009(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

