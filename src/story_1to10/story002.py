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
            mika.do("派手な幾何学模様じみた絵葉書は、$Sの姉からのものだった", "&"),
            mika.explain("最近通い始めたという彼女が描いたもので、",
                "何を考えて描いたのか相変わらず自分にはとても理解が及ばないと感じたが、",
                "人生に悩んであちこちの病院に通っていた頃に比べれば、文面からは随分元気になったように思う"),
            mika.do("その教室の先生が若くてかっこいい、というのが一番の要因だろうか",
                "絵葉書を見つめながら$me、まだこの時微笑ましく思っていたのだ"),
            camera=w.mika,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_artclass(w: World):
    mika, ane = W(w.mika), W(w.ane)
    kiri = W(w.kiri)
    return w.scene("絵画教室",
            w.symbol("　　　　◆"),
            ane.come(),
            kiri.be(),
            ane.talk("ここ、ですか？"),
            ane.do("通っている絵画教室の先生に連れられて$Sがやってきたのは、郊外の森に囲まれたある美術館だった",
                "そこは以前あった洋館を復元する形で造られており、現代社会から隔絶したような雰囲気を感じさせられた"),
            ane.do("中に入ると、至る場所に絵が飾られている",
                "あらゆる部屋、廊下の壁、階段の踊り場、更には天井にまで、大小様々な額が並び、そのどれに人物が描かれている",
                "タッチはとても繊細で、それらに描き込まれた瞳がともすれば動いて自分たちを追いかけているんじゃないかとすら思えて、",
                "彼女は先生のジャケットの背中に慌てて付いていった"),
            ane.talk("あれは……？"),
            ane.do("一番奥の部屋だった",
                "真っ白で天井の高いそこにはたった一つしか額がなく、それを見上げて彼女は動きを止める"),
            ane.talk("何も、描かれてない？"),
            ane.do("額には真っ白なキャンバスだけが飾られている"),
            kiri.talk("ああ、それはね……君にはまだ見えないよ"),
            kiri.do("先生はその『絵』をじっと見つめながら彼女に言った"),
            ane.talk("$meにも見えるようになりますか？"),
            kiri.talk("そうだね"),
            kiri.do("先生は薄い髭のある顎に手を当てながら落ち着いた声で言う"),
            kiri.talk("君なら教室に通い続けていればいずれ見えるようになる", "君にその素質はあるからね"),
            ane.do("――素質がある"),
            ane.do("$Sは自分が先生にそんな風に思われていると知り、血圧が上昇するのを感じた"),
            w.br(),
            ane.do("翌日から彼女は今まで以上に熱心に絵画教室に通った"),
            ane.do("絵は苦手な方だったけれど先生の丁寧な指導もあり、徐々に形になってゆく",
                "特別描きたいものがある訳ではなかった",
                "それでも筆で一つずつ色をキャンバスに置いていく",
                "描く、というよりそこに何かを塗り込めるような作業は、", "社会生活に疲れて毛羽立った$Sの心を滑らかにしてくれる気がした"),
            kiri.do("先生は言う"),
            kiri.talk("絵筆で自分自身を、そこに移してゆくのです"),
            ane.talk("はい"),
            ane.do("先生の声を背中で聞きながら、$Sは自分の中で確実に何かが変わっていくのを感じていた"),
            w.br(),
            ane.do("作品が完成に近づいていたある日の午後、窓から差し込む夕陽の先にある筈の自分の影に目を留めた"),
            ane.do("――薄い"),
            ane.do("それは今にも消えてしまいそうで、キャンバスとイーゼルの四角い影だけがくっきりと床に貼り付けられたみたいに黒い"),
            ane.do("――消しゴムでも消せるかも知れない"),
            ane.do("そう考えると彼女はとても気分が良くなり、久しぶりに笑い声を漏らした"),
            camera=w.ane,
            )

def sc_vanish(w: World):
    mika, ane = W(w.mika), W(w.ane)
    kiri = W(w.kiri)
    return w.scene("姉が消えた",
            w.symbol("　　　　◆"),
            mika.come(),# TODO
            mika.do("三ヶ月も音信不通が続き、流石に心配になった$meは姉のマンションを訪ねた"),
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
