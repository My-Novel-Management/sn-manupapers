# -*- coding: utf-8 -*-
"""Chapter: story 2: 「絵」
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
def sc_sisletter(w: World):
    mika, ane = W(w.mika), W(w.ane)
    return w.scene("姉の手紙",
            mika.be(),
            mika.explain("派手な幾何学模様じみた絵葉書は、最近絵画教室に通い始めたという彼女の姉が描いたものだった。人生に悩んでいた姉は随分《ずいぶん》と元気になったようだ。その教室の先生が若くてかっこいいらしい。元気のもとは、それだろうか、と、絵葉書を見つめながら妹は思っていた"),
            camera=w.mika,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_artclass(w: World):
    mika, ane = W(w.mika), W(w.ane)
    kiri = W(w.kiri)
    return w.scene("絵画教室",
            ane.come(),
            kiri.be(),
            ane.talk("ここですか？"),
            ane.do("通っている絵画教室の先生に連れられて彼女がやってきたのは、ある美術館だった。そこは以前あった洋館を復元する形で造られていて、現代社会から隔離されたような雰囲気を感じさせられた"),
            ane.do("中に入ると、至る場所に絵画が飾られている。あらゆる部屋、廊下の壁、階段の踊り場、更には天井にまで、大小様々な額が並んでいる。その絵はどれも人物画ばかりだったが、とても繊細に描き込まれ、じっと見つめていると、まるで今にも喋り出しそうに思えた"),
            ane.talk("あれって……"),
            ane.do("その中の一つに、彼女は足を止める"),
            ane.do("突き当たりの小さな部屋に飾られていたのは、単なる額と真っ白のキャンバスだけだ"),
            kiri.talk("ああ、それはね……君にはまだ見えないよ"),
            kiri.do("先生はその『絵』をじっと見つめながら、彼女に言った"),
            ane.talk("どうすれば、私にも？"),
            kiri.talk("そうだね。君なら、教室に通い続けていればいずれ見えるようになるよ。君にその素質はあるからね"),
            ane.do("素質がある"),
            ane.do("彼女は自分が先生にそんな風に思われていると知って、血圧が上昇するのを感じた"),
            w.br(),
            ane.do("翌日から、彼女は今まで以上に熱心に絵画教室に通った"),
            ane.do("絵は苦手な方だったけれど、先生の丁寧な指導もあって、徐々に形になってゆく。筆で一つずつ色を置く。それは描くというよりも、そこに何かを塗り込めるような作業だった"),
            kiri.talk("絵筆で自分自身を、そこに移してゆくのです"),
            kiri.do("先生はそう説明してくれた"),
            ane.do("彼女は自分の中で、何かが変わってゆくのを感じていた"),
            w.br(),
            ane.do("彼女の作品が完成に近づいていたある日の午後、窓から差し込む夕陽の先にある筈の自分の影に、目が留まった"),
            ane.do("薄い"),
            ane.do("今にも消えてしまいそうだ"),
            ane.do("消しゴムでも消せるかも知れない"),
            ane.do("そう考えると、何故か彼女はとても気分が良かった"),
            camera=w.ane,
            )

def sc_vanish(w: World):
    mika, ane = W(w.mika), W(w.ane)
    kiri = W(w.kiri)
    return w.scene("姉が消えた",
            mika.come(),
            mika.do("一カ月も音信不通が続き、流石に心配になった妹は彼女のマンションを訪ねた"),
            mika.do("呼鈴が何度も空しく響き、妹は仕方なく合鍵で玄関のドアを開け、中に入る"),
            mika.do("部屋はとても綺麗に片づいていた"),
            mika.do("誰もいない"),
            mika.do("ただ、部屋の中央には一枚の大きな絵がイーゼルに立てかけられていた"),
            mika.do("それは何かを見て微笑んでいる、姉の姿だった"),
            w.symbol("（了）"),
            camera=w.mika,
            )

## episode
def ep_mysis(w: World):
    return w.episode("絵画教室に通う姉",
            sc_sisletter(w),
            sc_artclass(w),
            sc_vanish(w),
            )

## chapter
def ch002_drawing(w: World):
    return w.chapter("２．絵画教室に通う姉",
            ep_mysis(w),
            )
