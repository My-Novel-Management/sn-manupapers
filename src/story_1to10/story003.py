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
    dad = W(w.yuidad)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("main",
            yui.be(),
            yui.do("また鐘の音だ",
                "頭に響く度に、結衣は手術前のあのカリフォルニアの空の青さを思い出す"),
            dad.think("――心臓すらも金で買えばいい"),
            yui.think("そんな父の言葉を聞いて以来、自分が今ここで息をしていることすら鬱陶しい",
                "けれど耳を塞いでみても、", "ただ自分の心臓が苦しそうに助けを求めている不規則なリズムが聞こえてくるばかりで、",
                "情けなさだけが増していく", "この心臓の持ち主は一体どんな思いでドナーカードに書き込んだのだろうかと考えてしまう"),
            yui.do("$Sは右手のレバーで車椅子を操縦し、鏡台の前に移動した",
                "いつ見ても何故か三十代くらいと思える、張りのない、たるんだ目尻や痩せて痩けた頬の自分が映り込んでいる",
                "何とも酷い顔だと頭を振って、車椅子の向きを変える"),
            gekko.be(),
            gekko.talk("この頃は可愛かったのにな"),
            yui.talk("誰？"),
            yui.do("いつ部屋に入ってきたのだろう",
                "知らない全身黒のスーツ姿の男性がベッドサイドの棚の前で背を向けていた",
                "そこには$Sがまだ学校に通っていた頃の、小さな体をセーラー服に包んで笑っていた写真が飾られている",
                "写真立てを持ち上げて「そう思わないか？」と男は笑いかけた"),
            yui.talk("人を呼ぶわよ"),
            gekko.talk("誰も来ないよ、$full_yuiさん"),
            yui.talk("どうして？"),
            gekko.talk("$meはそうだな、$gekkoとでも呼んでもらおうか"),
            yui.talk("$meの質問に答えなさい"),
            gekko.talk("どうして歩かないんだ？"),
            yui.talk("歩けないのよ"),
            gekko.talk("貰った心臓が悪いからか？"),
            yui.do("$gekkoと名乗った男はからかいの嘲笑を洩らす"),
            yui.talk("あなたには関係ない"),
            gekko.talk("新しいのを貰えばいい"),
            yui.talk("何を"),
            gekko.talk("取ってきてやるよ"),
            yui.talk("やめて"),
            yui.do("そう言うなり$gekkoは窓を開けて外へと出て行った"),
            yui.talk("何なのよ"),
            yui.do("窓を閉めながら男の言葉がチクリ、と胸を刺した"),
            w.br(),
            yui.do("男は翌日も彼女の部屋にやってきた",
                "眠っていた$Sの枕元で彼は、"),
            gekko.talk("右足はどうだ？"),
            yui.do("いきなりそんなことを訊ねる"),
            yui.talk("挨拶くらいすれば？"),
            gekko.talk("おはようございます、マダム"),
            yui.talk("$meは結婚なんてしてないし、そんな年齢でも"),
            yui.do("目覚めた$Sは右足の違和感に気づいて言葉を止めた",
                "動く。動くのだ"),
            yui.talk("ちょっと、これ"),
            gekko.talk("取り戻してきてやったんだ"),
            yui.do("そう笑った彼は、けれど、自身の右足を引き摺っていた"),
            w.br(),
            yui.do("それから毎日のように$gekkoは現れた",
                "彼がやってくる度に$Sの体は治り、一週間もすれば車椅子も松葉杖もなしに生活出来るくらいになった", "だが、"),
            yui.talk("いる？"),
            yui.do("振り返ればそこに、彼がいた",
                    "$gekkoは松葉杖を突き、今にも倒れてしまいそうな真っ青な顔をして、それでも$Sに笑いかけている"),
            gekko.talk("後は……心臓だけだな"),
            yui.talk("要らない"),
            gekko.talk("それで、終わりだ"),
            yui.talk("要らないから、そんなもの！",
                    "だからもうやめて。お願い"),
            yui.talk("分かった。もう分かったから",
                    "$meは……"),
            yui.do("改めて自分の両足で鏡の前に立つ",
                    "そこに映っているのはあの日から二十年間ずっと、心の時間を止めたままの$Sだ"),
            gekko.talk("どこに行くつもりだ？"),
            yui.do("$Sはドアノブに手を掛け、それを回す"),
            gekko.talk("そうか"),
            yui.do("彼女は振り返り、彼に笑顔を向ける",
                    "それに$gekkoは安心したようにふっと微笑むと、足元の影に溶けるようにして姿を消した"),
            yui.talk("行くよ"),
            yui.do("――あなたと生きる為に"),
            camera=w.yui,
            stage=w.on_yakata_int,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_getbackman(w: World):
    return w.episode("君を取り戻す男",
            sc_main(w),
            ## NOTE
            )

## chapter
def ch003_getback(w: World):
    return w.chapter("３．君を取り戻す影",
            ep_getbackman(w),
            )
