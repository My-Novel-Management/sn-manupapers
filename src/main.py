#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## assets
from storybuilder.assets import basic, accessory
## local files
from src.story_1to10.story001 import ch001_doller
from src.story_1to10.story002 import ch002_drawing
from src.story_1to10.story003 import ch003_getback


## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1.人形師の女
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("原稿用紙の為の作品集１")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2020)
    w.setBaseArea("Tokyo")
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("原稿用紙３枚程度の作品集")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch001_doller(w),
            ch002_drawing(w),
            ch003_getback(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

