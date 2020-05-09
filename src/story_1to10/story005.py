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
    eiji = W(w.eiji)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("main",
            eiji.be(),
            eiji.do("鼓膜が裂けたのかと思った。視界の全てが止むことのない雨に覆われ、一歩ごとに体温が奪われる。それでも黒河英嗣は歩いていた。傘など無い。それはあの日と同じだ。月も星も無い。電灯すら殆ど見当たらない。いつしかここが道路の上ということすら忘れてしまうだろう"),
            w.br(),
            eiji.do("もう、三年になるのか"),
            w.br(),
            eiji.do("純子はよく笑う女だった。その大きな口で「英嗣ってほんとによく転ぶよね」何もない場所で躓く彼を揶揄して笑った。出会いのきっかけもそんな英嗣を見た彼女の笑い声だ"),
            eiji.do("同級生なのにしっかりしていて、どこか姉のようでもあり、それでいて、雨の中にはしゃいで飛び出すような無邪気さも持っていた。どんなに雨が降っても、彼女が居れば太陽がもう一つあるようなものだった"),
            eiji.do("その日、二人はバス停目指して走っていた。講義が休講になったからと二人で歩いていたら、暗くなって急に振り出した雨に遭遇したのだ。英嗣も純子も、それぞれ鞄を傘代わりにして走った。いつもならしっかり手を掴まえて歩いた英嗣だったが、どうしてあの日は手を離してしまっていたのだろう"),
            eiji.do("最初に気づいたのは彼女の視線だった。それから強烈な光。続くブレーキ音とスリップ音"),
            eiji.do("振り向いた時には黒い物体が、彼女を英嗣の目の前から掻っ攫っていった"),
            eiji.do("酷い雨だった"),
            w.br(),
            eiji.do("ああ、また雨が降っている"),
            w.br(),
            eiji.do("あの日から英嗣は雨が降る度に、その中に彼女の姿を探して歩いた"),
            eiji.talk("純子！"),
            eiji.do("呼び掛ければいつか、答えてくれるような気がした"),
            eiji.talk("居るんだろ"),
            eiji.do("振り返れば、そこで彼女が笑っているような気がした"),
            eiji.talk("なあ"),
            eiji.do("どこかで笑って見てくれているんだろ？"),
            w.br(),
            eiji.do("英嗣は思う。悲しみは雨に似ている。降っても降っても尽きることはない。沢山のものを濡らして、大切なものを奪い、流しさってしまう。その中でただ、英嗣は震えているだけだ"),
            eiji.do("強烈な光だった。続く甲高いブレーキ音"),
            eiji.do("あの時と同じ。やっと巡り合えた。英嗣はずっとこの瞬間を探していた。あの瞬間、あそこに居たのが彼女でなく自分だったらと、何度考えただろう。これでもう終わる。これで純子の許へ"),
            eiji.talk("純子？"),
            eiji.do("彼女が居る。笑っている"),
            eiji.talk("純子！"),
            eiji.do("英嗣は駆け出そうと、一歩、踏み出す。その背中を突風が抜けた"),
            eiji.do("脇腹が捻れそうな不快な音を流して、車は分離帯を抜けて対向車線へ。その縁石に乗り上げて止まった"),
            eiji.do("英嗣は視線を戻す。純子は微笑んで、それから少し寂しそうに頷いた"),
            eiji.talk("お前は、お前は俺に生きろと、そう言うのか？"),
            eiji.do("けれど彼女は答えず、止まない雨に掻き消された"),
            eiji.do("英嗣は思い切り声を上げた。あの日から一度として大声を張り上げたことが無かったというのに。雨はその全てを消してくれる。この悲しみまでも"),
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
