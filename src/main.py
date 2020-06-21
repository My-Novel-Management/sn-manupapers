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
from src.config import PERSONS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS
from src.story_1to10.story007 import ch007_windandbubble


################################################################
#
#   1.人形師の女
#   2.絵画教室に通う姉
#   3.君を取り戻す男
#   4.電子蝶は夢を飛ぶ
#   5.悲しみは雨に似ている
#   6.涙の大河
#   7.風とシャボン玉
#
################################################################



def main(): # pragma: no cover
    w = World.create_world('原稿用紙の為の作品集１')
    w.config.set_outline('原稿用紙三枚程度の短編を収めたもの')
    w.db.build_db(PERSONS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS)
    return w.run(
            ch007_windandbubble(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

