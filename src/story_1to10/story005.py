# -*- coding: utf-8 -*-
"""Chapter: story 5: 「悲しみは雨に似ている」
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
    eiji, jun = W(w.eiji), W(w.junko)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("main",
            eiji.be(),
            eiji.do("鼓膜が裂けたのかと思った"),
            _.do("視界の全てがチョークを寝かせて描いたような雨に覆われ、一歩ごとに体温が奪われる",
                "それでも$full_eijiは歩いた",
                "傘など無い",
                "それはあの日と同じだ",
                "月も星も、",
                "電灯すら見当たらない",
                "鼓膜が震えても雨音しか分からず、ここが道路の上ということすら忘れてしまいそうだ"),
            w.br(),
            eiji.think("――もう、三年になるのか"),
            w.br(),
            eiji.do("$junkoは大きな口をいっぱいに開けてよく笑う女だった"),
            jun.talk("$eijiってほんとによく転ぶよね"),
            eiji.think("何もない場所で躓く彼を助け起こしては揶揄して笑った",
                "出会いのきっかけもそんな彼を見た彼女の笑い声だ",
                "大学のキャンパスで鞄の中身をひっくり返して何とも恥ずかしい思いだった彼の心に、", "すっと差し込む光のように入ってきた"),
            eiji.do("彼女は同級生なのにしっかりしていてどこか姉のようでもあり、それでいて雨の中にはしゃいで飛び出すような無邪気さも持っていた"),
            eiji.do("どんなに雨が降っても$junkoが居れば太陽がもう一つあるようなものだ", "そう思っていた").omit(),
            eiji.do("あの日、$Sは$junkoと二人で雨の中、大学前のバス停目掛けて走っていた",
                "講義が休講になったからと二人で歩いていたら暗くなって急にスコールになったのだ",
                "二人とも鞄を傘代わりに、それでも$junkoは楽しそうに笑っていた",
                "いつもならしっかり彼女の手を掴まえて歩いていたのに、どうしてあの日は手を離してしまっていたのだろう"),
            eiji.do("最初に気づいたのは彼女の視線だった",
                "それから強烈な光、続いてブレーキ音と耳障りなスリップ音が響いた"),
            eiji.do("振り向いた刹那、黒い物体が彼女を目の前から掻っ攫っていった"),
            eiji.do("酷い雨で、側溝に凄い勢いで雨水が流れ込んでいく音がやたらとうるさかったことを思い出す"),
            w.br(),
            eiji.think("――ああ、また雨が降っている"),
            w.br(),
            eiji.do("あの日から$Sは雨が降る度、その中に彼女の姿を探して歩くようになった"),
            eiji.talk("$junko！"),
            eiji.do("呼び掛ければいつか答えてくれるような気がした"),
            eiji.talk("居るんだろ？"),
            eiji.do("振り返ればそこで彼女が笑っているような気がした"),
            eiji.talk("$junko、あの頃みたいに$meを驚かそうとしてどこかに隠れているんだろう？　なあ！"),
            w.br(),
            eiji.do("$Sは思う",
                "悲しみは雨に似ている",
                "降っても降っても尽きることはない",
                "沢山のものを濡らして、大切なものを奪い、流しさってしまう",
                "その中ではただ、震えていることしかできない"),
            eiji.do("強烈な光だった",
                "続いて甲高いブレーキ音"),
            eiji.do("あの時と同じ",
                "そう、やっと巡り合えた",
                "$Sはずっとこの瞬間を探していたのだ",
                "あの瞬間、あそこに居たのが彼女でなく自分だったらと何度考えただろう",
                "これでもう終わる", "これで$junkoの許へ――"),
            eiji.talk("純子？"),
            eiji.do("彼女が居る", "笑っている"),
            eiji.talk("純子！"),
            eiji.do("$Sは駆け出そうと一歩、踏み出す", "その背中を突風が抜けた"),
            eiji.do("脇腹が捻れそうな不快な音を流して車は中央分離帯を抜け、",
                    "そのまま対抗車線の縁石に乗り上げて止まった"),
            eiji.do("視線を戻すとそこで彼女は微笑み、それから少し寂しそうに頷いた").omit(),
            eiji.talk("お前は、お前は俺に生きろと、そう言うのか？"),
            eiji.do("彼女はただ微笑し、そのまま雨に消える"),
            eiji.do("雨は$Sをどこまでも濡らしていたが、まるで彼女に抱きしめられているかのように温かかった"),
            w.symbol("（了）"),
            camera=w.digibutterfly,
            stage=w.on_vectorroom_int,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_main(w: World):
    return w.episode("雨",
            sc_main(w),
            ## NOTE
            )

## chapter
def ch005_rainy(w: World):
    return w.chapter("＃００５　【恋愛】　悲しみは雨に似ている",
            ep_main(w),
            )
