# -*- coding: utf-8 -*-
"""Chapter: story 3: 「君を取り戻しに行こうか」
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_main(w: World):
    yui, gekko = W(w.yui), W(w.gekko)
    return w.scene("main",
            yui.do("また鐘の音だ。頭に響く度に、結衣は手術前のあのカリフォルニアの空の青さを思い出す。心臓すらも金で買えばいい。そんな父親の言葉を聞いて以来、自分が今ここで息をしていることすら鬱陶しかった",
                "結衣は右手のレバーで車椅子を操縦し、鏡台の前に移動した。何故か三十代くらいに老けた自分が映り込んでいる。酷い顔"),
            gekko.talk("この頃は可愛かったのにな"),
            yui.talk("誰？"),
            yui.do("振り返るといつの間に部屋に入ってきたのか、ジーンズにシャツといったラフな服装の男が壁に掛かった結衣のセーラー服姿の写真を見ていた"),
            yui.talk("人を呼ぶわよ"),
            gekko.talk("誰も来ないよ、日景結衣さん"),
            yui.talk("どうして"),
            gekko.talk("俺はそうだな、ゲッコウとでも呼んでもらおうか"),
            yui.talk("わたしの質問に答えなさい"),
            gekko.talk("どうして歩かないんだ？"),
            yui.talk("歩けないのよ"),
            gekko.talk("貰った心臓が悪いからか？"),
            yui.do("ゲッコウと名乗った男はからかいの嘲笑を洩らす"),
            yui.talk("あなたには関係ない"),
            gekko.talk("新しいのを貰えばいい"),
            yui.talk("何を"),
            gekko.talk("取ってきてやるよ"),
            yui.talk("やめて"),
            yui.do("そう言うなりゲッコウは窓を開けて外へと出て行った"),
            yui.talk("何なのよ"),
            w.br(),
            yui.do("その男は翌日も結衣の部屋にやってきた。眠っていた結衣の枕元で彼は、"),
            gekko.talk("右足はどうだ？"),
            yui.do("いきなりそんなことを訊ねる。「挨拶くらいすれば？」"),
            gekko.talk("おはようございます、マダム"),
            yui.talk("わたしは結婚なんてしてないし、そんな年齢でも"),
            yui.do("目覚めた結衣は右足の違和感に気づいて言葉を止めた。動く。動くのだ"),
            yui.talk("ちょっと、これ"),
            gekko.talk("取り戻してきてやったんだ"),
            yui.do("そう笑った彼は、けれど、自身の右足を引き摺っていた"),
            w.br(),
            yui.do("それから毎日のようにゲッコウは現れた。彼がやってくる度に結衣の体は治り、一週間もすれば車椅子も松葉杖もなしに生活出来るくらいになった。だが"),
            yui.talk("いる？"),
            yui.do("振り返ればそこに、彼がいた。ゲッコウは松葉杖を突き、今にも倒れてしまいそうな真っ青な顔をして、それでも結衣に笑いかけている"),
            gekko.talk("後は……心臓だけだな"),
            yui.talk("要らない"),
            gekko.talk("それで、終わりだ"),
            yui.talk("要らないから、そんなもの。だからもうやめて。お願い"),
            yui.do("鏡には相変わらず三十七歳の自分が映っている"),
            yui.talk("分かった。もう分かったから。わたしは……"),
            yui.do("十七歳のあの日からずっと、結衣の時間は止まったままなのだ"),
            gekko.talk("どこに行くつもりだ？"),
            yui.do("結衣はドアノブに手を掛け、それを回す"),
            gekko.talk("そうか"),
            yui.do("結衣が答えると、安心したように彼はふっと微笑み、そして闇に溶けるように消えてしまった"),
            yui.talk("ええ、行くわ"),
            w.br(),
            yui.do("わたしを、取り戻しに"),
            )

## episode
def ep_getbackman(w: World):
    return w.episode("君を取り戻す男",
            ## NOTE
            )

## chapter
def ch003_getback(w: World):
    return w.chapter("３．君を取り戻す影",
            ep_getbackman(w),
            )
