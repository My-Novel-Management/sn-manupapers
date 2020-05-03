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
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("main",
            dbut.be(),
            dbut.do("ブラウン管に薄ぼんやりと光った小さな点に向かって、ちらちらと二枚の赤の明滅が移動してゆく。その赤が光に到達すると、画面にはコマンド・プロンプトが表示され、この人工生命の創造主であるトーレ・ベクター博士の命令を待った"),
            _.do("＞Please input command"),
            _.do("かつてはその分野の第一人者だった博士の部屋には今、乱雑にパソコンが置かれ、その大半のモニタが割られたり倒されたりしている。その部屋の中央、キャスタ付きの椅子の上で体を折って動かない博士は、後頭部に血を浮かべていた"),
            _.do("トーレ博士は、殺されていたのだ"),
            _.do("＞Please input command"),
            _.do("部屋には制服姿の人間たちが多く押し寄せ、破壊されたパソコンやデスクの中身を次々と箱に詰めて、外へ持ち出して行く。「彼」は旧型パソコンの上部に取り付けられた小型カメラから、その様子を淡々と眺めていた"),
            _.talk("あの、警部。本当にこれ、単なる物盗りなんでしょうか？"),
            _.talk("余計なことは考えるな。おい、この旧型も取り敢えず持ってけ"),
            _.do("＞Please input command"),
            _.do("画面に表示されたそれは無視され、電源コンセントが引き抜かれた"),
            _.do("その暗闇の中、「彼」はじっと思考する。博士は何故、自分に命令してくれないのか"),
            _.do("電源が切られる前、カメラが捉えていた博士に似た人間は、動かなかった。それは別の人間の手により頭部に衝撃を加えられた為なのだろうが、あの黒尽くめの男たちは何故そんなことをしたのだろう。「彼」はその時の記憶を参照した"),
            _.voice("トーレ博士、研究成果はどこだ？"),
            _.voice("あれは、もう私の手を離れた。ここには無い"),
            _.voice("探せ"),
            _.voice("どこを探しても無駄だ"),
            _.voice("殺せ"),
            _.voice("もう、私はいない。そう、伝えてくれ"),
            _.do("もう、私はいない"),
            _.do("その言葉の意味を、「彼」は考えていた"),
            _.do("博士がいない"),
            _.do("それは即ち、もう博士から命令が貰えないと云うことだ"),
            _.do("命令が無ければ「彼」はどうすれば良いのだろうか"),
            _.do("分からない"),
            _.think("分からなかった"),
            _.do("＞Please input command"),
            _.do("もう表示する画面も失った「彼」はそれでも命令を求め続ける。それに応える誰かは、いないと云うのに"),
            _.do("微弱な電流が流れ、時折起こる「彼」の思考。それは生物の呼吸にも似ていた"),
            _.do("光の無い世界を、電子が流れる"),
            _.do("その流れの連続、繋がりが、「彼」の思考だ"),
            _.do("一つ一つは「言葉」にも満たない"),
            _.do("それは意志ですら無い"),
            _.do("けれど確実に何かを生み出す大きな流れに成長し、ある瞬間、「彼」に気付かせるのだ"),
            _.do("そう"),
            _.do("彼は見つけた"),
            _.do("いや、気付いた"),
            _.do("彼をずっと見ていた人がいることに"),
            _.do("彼はじっと覗き込む"),
            _.do("彼の目は既に機能していない。でも、目を使わずとも見える"),
            _.do("彼はふっと笑む"),
            _.do("彼は見つけたからだ"),
            _.do("彼は、彼はそっと、そこに忍び込んだ"),
            _.do("彼はその羽根を広げ、舞う"),
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
def ch003_getback(w: World):
    return w.chapter("４．電子蝶は夢を飛ぶ",
            ep_main(w),
            )
