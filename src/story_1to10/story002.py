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
            w.comment("一人称で開始"),
            mika.be(),
            mika.do("派手な幾何学模様じみた絵葉書は、$meの姉からのものだった", "&"),
            mika.explain("最近通い始めた絵画教室で描いたもののようで何を表現しているのか相変わらず理解できないが、随分元気になったように思える", "&"),
            mika.do("その教室の先生が若くてかっこいい、というのが一番の要因だろう"),
            _.do("絵葉書を見つめながら$meはまだこの時、それを微笑ましいと思っていた"),
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
                "あらゆる部屋、廊下の壁、階段の踊り場、更には天井にまで、大小様々な額が並び、そのどれにも人物が描かれている",
                "タッチは繊細で、描き込まれた瞳がともすれば動いて自分たちを追いかけているんじゃないかとすら思えて、",
                "彼女は先生のジャケットの背中を慌てて追いかけた"),
            ane.talk("あれは……？"),
            ane.do("一番奥の部屋だった"),
            _.do("真っ白で天井の高いそこにはたった一つしか額がなく、それを見上げて$Sは動きを止める").omit(),
            ane.talk("何も、描かれてない？").omit(),
            ane.do("その額には真っ白なキャンバスだけが飾られている"),
            kiri.talk("ああ、それはね……君にはまだ見えないよ"),
            kiri.do("先生はその『絵』をじっと見つめながら彼女に言った"),
            ane.talk("$meにも見えるようになりますか？"),
            kiri.talk("そうだね"),
            kiri.do("先生は薄い髭のある顎に手を当てながら落ち着いた声で言う"),
            kiri.talk("教室に通い続けていれば君ならいずれ見えるようになるだろう", "君にはその素質があるからね"),
            ane.do("――素質がある"),
            ane.do("$Sは自分が先生にそんな風に思われていると知り、血圧が上昇するのを感じた"),
            w.br(),
            ane.do("翌日から今まで以上に熱心に絵画教室に通った"),
            ane.do("絵は苦手な方だったけれど先生の丁寧な指導もあり、徐々に形になっていく",
                "特別描きたいものがある訳ではなかった",
                "それでも筆で一つずつ色をキャンバスに置いていく",
                "描く、というよりそこに何かを塗り込めるような作業は、", "社会生活に疲れて毛羽立った$Sの心を滑らかにしてくれる気がした"),
            kiri.do("先生は言う").omit(),
            kiri.talk("絵筆で自分自身を、そこに移してゆくのです"),
            ane.think("はい――先生の声を背中で聞きながら、$Sは自分の中で確実に何かが変わっていくのを感じていた"),
            w.br(),
            ane.do("作品が完成に近づいていたある日の午後、窓から差し込む夕陽の先に伸びる自分の影に目を留めた"),
            ane.do("――薄い"),
            ane.do("それは今にも消えてしまいそうで、"),
            ane.do("――消しゴムでも消せるかも知れない"),
            ane.do("そう考えると気分が良くなり、彼女は久しぶりに笑い声を漏らした"),
            camera=w.ane,
            )

def sc_vanish(w: World):
    mika, ane = W(w.mika), W(w.ane)
    kiri = W(w.kiri)
    return w.scene("姉が消えた",
            w.symbol("　　　　◆"),
            mika.come(),
            mika.do("三ヶ月も音信不通が続き、流石に心配になった$meは姉のマンションを訪ねた"),
            mika.do("呼鈴が何度も空しく響くだけで応答はない",
                "$meは仕方なく合鍵で中に入った"),
            mika.do("部屋はとても綺麗に片づいている", "&"),
            mika.do("誰の姿もなく、それでいてコンロには湯気を昇らせる味噌汁の鍋があった"),
            mika.talk("おねえ、ちゃん？"),
            mika.do("寝室には一枚の大きな絵があった", "&"),
            mika.do("描かれていたのは姉自身の姿だ",
                "彼女はそこでとても幸せそうに微笑していた"),
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
