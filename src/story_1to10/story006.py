# -*- coding: utf-8 -*-
"""Chapter: story 6: 「涙の大河」
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
    eika, cho = W(w.eika), W(w.chomei)
    inside, outside = W(w.inside), W(w.outside)
    woman = W(w.woman1)
    return w.scene("main",
            eika.be(),
            cho.be(),
            eika.do("ゆるりと立ち昇る靄を抜けると向こう岸が見えないほど広い川に出た",
                "そこでじっとたゆたう水面を見つめる女が一人、声もなく泣いていた",
                "あなたは問いかける"),
            eika.talk("何故、泣いているのですか？"),
            w.symbol("　　　　※"),
            eika.explain("まだ西暦が始まる前のこと。随分と湿気の多い空気の中、ひょろり伸びた豆を収穫していた王詠華は、服を泥だらけにした夫の長明がやってきたのに気づいて声をかけた"),
            eika.talk("あなた。もういい加減にして下さい"),
            _.talk("またあの川のところに行っていたのですか？").omit(),
            cho.do("悪いか、と低く答え、$Sは足元の籠を手に取る"),
            eika.talk("もうあの川をどうにかしようなどと考えないで下さい", "神様でもきっと無理なのですから"),
            cho.talk("神に無理だからと言って俺にも無理かどうかは分からない", "もう二度と洪水で悲しい思いをしたくはないのだ"),
            eika.do("詠華が嫁いできた淀里の住民はよくも悪くも、複雑な支流を持つ七龍川に影響されて暮らしていた",
                "雨季になる度に洪水で里を押し流すが、その川がもたらす養分により貧しい土地でも何とか作物を収穫することが出来た"),
            eika.do("薄木の板を張り合わせたぼろ屋に戻ると、詠華は覚悟を決め、桶の水を被っている長明に言った"),
            eika.talk("洪水は確かに困るけれど、それは淀里の歴史の一部なのでしょう。あれがあるから私たちは生きていられる"),
            cho.talk("それは最初から何も出来ないと考え何もしてこなかった、ただその放置の歴史の積み重ねではないのか"),
            eika.do("長明の両親は洪水で死んだ。それを聞かされた時、詠華は彼の気持ちを理解出来なかった訳では無い"),
            eika.do("それでも彼が幾度となく住民に迷惑を掛けていることを考えると、もういい加減に諦めてももらいたかった").omit(),
            eika.talk("けど、このままではいつかあなたまで犠牲に"),
            cho.talk("それでも構わない。神には自分を犠牲にする覚悟などないからな。それが人間との大きな違いだ"),
            eika.talk("私を一人残して、それでも構わないと？"),
            eika.do("だがそれには長明は答えなかった"),
            w.br(),
            eika.explain("今年の雨季は例年より早くにやってきた"),
            eika.do("既に里の住民は避難を始めていて、詠華も最低限の家財道具を持ち出そうとまとめていた"),
            woman.be(),
            woman.talk("詠華さん、早く避難を"),
            eika.talk("あの人が、まだ帰ってこないんです！"),
            woman.talk("長明も馬鹿ではない。もう避難しているさ。さあ、早く！"),
            eika.do("詠華は近所の者に言われるまま、里を見下ろす高台まで避難したが、そこに夫の姿は無かった"),
            w.br(),
            eika.explain("雨は三日三晩の間ずっと降り続いた"),
            eika.do("雨が上がると直ぐに詠華は里へと下りて行った"),
            eika.talk("一体、これは……"),
            eika.do("いつもなら増水してまだ里はとても歩ける状態ではないのに、何故か水は殆どなく、家々も流されてはいなかった"),
            eika.do("里の傍を流れる七龍川は、たっぷりの水量を湛えて流れていたが、その淵には石が埋め込まれ、よく見れば今までの倍の川幅となっていた。詠華はそれが夫の仕業なのだと悟った"),
            eika.talk("長明"),
            eika.do("夫の名はその川面を僅かに揺らしただけだった"),
            w.symbol("　　　　※"),
            eika.talk("前世なんてものを私は信じてやいません。それでも何故この川を見て涙が溢れるというのでしょう"),
            eika.do("彼女はそう口にして、目を閉じて手を合わせた",
                "目の前の川はどこまでも穏やかに流れ続けていた"),
            w.symbol("（了）"),
            camera=w.eika,
            stage=w.on_field,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_main(w: World):
    return w.episode("大河",
            sc_main(w),
            ## NOTE
            )

## chapter
def ch006_tearsriver(w: World):
    return w.chapter("＃００６　【歴史】　涙の大河",
            ep_main(w),
            )
