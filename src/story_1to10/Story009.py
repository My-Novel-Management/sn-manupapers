# -*- cofing: utf-8 -*-
'''
Story: 009
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# Chapter
def ch_story009(w: World):
    return w.chapter("ただ会いたくて",
            ep_main(w),
            )


# Episode
def ep_main(w: World):
    return w.episode("main",
            w.symbol("（了）"),
            )


## scenes

