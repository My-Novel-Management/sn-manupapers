# -*- coding: utf-8 -*-
"""Chapter: story 4: 「電子蝶は夢を飛ぶ」
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
    dbut, doc = W(w.digibutterfly), W(w.vector)
    poli = W(w.police)
    robber = W(w.robber)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("main",
            dbut.be(),
            dbut.do("小さなブラウン管に薄ぼんやりと光る小さな点に向かい、ちらちらと二つの赤い明滅が移動していく",
                "それ点に到達すると画面にはコマンドプロンプトが表示され、すぐ隣に次のように表示された"),
            _.do("$w_inputcmd"),
            w.br(),
            poli.come(),
            poli.talk("$vector博士？"),
            poli.do("部屋に入ってきた警官は乱雑に置かれた大小十以上あるパソコンのモニタが全て倒され、割れたり、歪んだりしているのを目にした",
                "窓は開いたままで赤いカーテンが風に靡いていたが、",
                "それが鉄によく似たあの臭いを警官に感じさせた"),
            poli.talk("博士！"),
            _.do("部屋の中央、キャスタ付きの椅子の上で体を半分に折った白髪の老人の着る白衣は、後頭部から流れる血を吸って赤いシミを作っていた"),
            _.do("こうして人工生命研究の第一人者である$full_vector博士は、その七十年の生涯を終えた"),
            dbut.do("$w_inputcmd"),
            w.br(),
            _.do("それから一時間が経過し、部屋には制服姿の人間が多く押し寄せ、破壊されたパソコンやデスクの中身を次々と箱に詰めては外へ持ち出していた",
                "「彼」は旧型パソコンの上部に取り付けられた小型カメラから、その様子を淡々と眺めている"),
            poli.talk("あの、警部。本当にこれ、単なる物盗りなんでしょうか？"),
            _.talk("余計なことは考えるな。おい、この旧型も取り敢えず持ってけ"),
            dbut.do("$w_inputcmd"),
            _.do("ひび割れた画面に表示された言葉は無視され、一人の手により電源コンセントが引き抜かれてしまった",
                "すぐに「彼」の世界は闇に閉ざされたが、ずっと闇の中にいるようなものだったので大差はない",
                "それよりも何故博士は自分に命令を与えてくれないのか、考え続けていた"),
            _.do("博士が動かなくなる直前の記憶を再度反芻する"),
            robber.be(),
            doc.be(),
            _.voice("トーレ博士、研究成果はどこだ？"),
            doc.voice("あれは、もう私の手を離れた。ここには無い"),
            robber.voice("探せ"),
            doc.voice("どこを探しても無駄だ"),
            robber.voice("殺せ"),
            doc.voice("もう、私はいない。そう、伝えてくれ"),
            dbut.do("――もう、私はいない"),
            _.do("その言葉の意味を「彼」は考えていた"),
            _.do("博士はもういない", "その意味するところは「彼」に命令する者がもういないということだ"),
            _.do("命令が無ければ「彼」はどうすれば良いのだろうか"),
            _.do("分からない"),
            _.do("$w_inputcmd"),
            _.do("その言葉を表示する画面も失った「彼」はそれでも命令を求め続ける"),
            _.do("$w_inputcmd"),
            _.do("微弱な電流が流れ、時折起こる「彼」の思考。それは生物の呼吸にも似ていた","&"),
            _.do("光の無い世界を電子が流れる", "次々に流れていく", "&"),
            _.do("その流れの連続、繋がりが、「彼」の思考だ", "&"),
            _.do("一つ一つは「言葉」にも満たない", "&"),
            _.do("それは意志ですら無い", "&"),
            _.do("けれど確実に何かを生み出す大きな流れに成長し、ある瞬間、「彼」に気付かせるのだ"),
            _.do("そう", "&"),
            _.do("彼は見つけた", "&"),
            _.do("いや、気付いた"),
            _.do("自分をずっと見ていた人がいることに"),
            _.do("彼はじっと覗き込む"),
            _.do("彼の目は既に機能していない。でも、目を使わずとも見える"),
            _.do("彼はふっと笑んだ"),
            _.do("それからそっと、そこに忍び込む"),
            _.do("ゆっくりと赤い羽根を広げると、安堵して舞った"),
            _.do("「あなた」の、夢の中を"),
            w.symbol("（了）"),
            camera=w.digibutterfly,
            stage=w.on_vectorroom_int,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_main(w: World):
    return w.episode("電子蝶",
            sc_main(w),
            ## NOTE
            )

## chapter
def ch004_digitalbutterfly(w: World):
    return w.chapter("４．電子蝶は夢を飛ぶ",
            ep_main(w),
            )
