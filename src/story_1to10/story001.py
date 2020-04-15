# -*- coding: utf-8 -*-
"""Chapter: story 1 to 10
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
def sc_visit(w: World):
    hiro, yuki = W(w.hiro), W(w.yuki)
    return w.scene("人形師の館",
            yuki.do("約束してね――と、女は言った"),
            w.br(),
            yuki.do("外灯一つで照らす薄暗い裏庭で、スコップが土を掘り返す音だけが響いている",
                "上着の袖を捲り上げた女の腕は白く細いが、逞しい",
                "その女の足元には随分と大きな風呂敷包があった",
                "中身はよく分からない",
                "雑然と置かれているから女にとってそれほど大切なものでは無いのだろう"),
            yuki.do("女は一度顔を上げ、額を拭った",
                "それから小さく唇を歪める",
                "紅は引いていないがその唇は随分と血色が良い",
                "笑みを浮かべながら昨日の出来事を思い出した"),
            camera=w.yuki,
            stage=w.on_yakata,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_memmory(w: World):
    hiro, yuki = W(w.hiro), W(w.yuki)
    return w.scene("昨日の記憶",
            w.br(),
            hiro.talk("たった一度のことだろう？"),
            yuki.do("天井の高い部屋で大きな窓を背にし、頬に傷のある男は女の言った事がまるで理解不能だというように眉を顰めた", "&"),
            hiro.do("側のガラスケースには彼と寸分違わぬ大きさの蝋細工の人形が、優しげに微笑しながら収まっている"),
            hiro.talk("$meは君に謝った", "もう二度とはしないと、", "そう約束しただろう？", "それなのに君は").omit(),
            yuki.talk("たった一度"),
            yuki.do("女は男の言葉を遮って口を開く",
                "きりっとした薄化粧の顔を苦い表情の男に向けた"),
            yuki.talk("その一度で充分だと私は思うのです"),
            yuki.do("涼しげな声だったが女の表情は真剣そのものだ",
                "眉を立てることも寝かすこともせず、ただ真っ直ぐに向けられたその視線に男はたじろぐ"),
            yuki.talk("白い布を汚すには一滴の墨汁があれば良い、そう思いませんか？"),
            hiro.do("男は何か言おうとしたが言葉を見つけられなかったのか、口を噤んだまま茶のカップを手にし、",
                "溜息を飲み込むようにそれを口にした"),
            )

def sc_digging(w: World):
    hiro, yuki = W(w.hiro), W(w.yuki)
    return w.scene("掘る女",
            w.br(),
            yuki.do("自分一人が入れるくらいの穴を掘り終えた女は、",
                "足元にあった風呂敷包を開けた",
                "中からは人間の腕や足と思しき物体が山となって現れ、ばらばらとその山が崩れた"),
            yuki.do("女はその中から右腕を手に取り、愛おしそうに握り締めて頬ずりをする",
                "それから暫くじっとりと見つめていたが、",
                "急に歯を食いしばったかと思うとその腕を穴に向かって無造作に放り入れた",
                "続いて、足、胴体、右耳、左の薬指。唇に、目玉……",
                "全てを穴に入れ終えると上から土を被せる"),
            yuki.do("女は額の汗を拭い、満足そうにすっかり埋まった穴を見下ろすと、",
                "ぽつり、とこう呟いた"),
            yuki.talk("さようなら"),
            )

def sc_newman(w: World):
    hiro, yuki = W(w.hiro), W(w.yuki)
    man = W(w.man1)
    return w.scene("新しい男",
            w.br(),
            yuki.do("外では今朝から雨が降り続いていた"),
            yuki.do("女は一瞬窓の外を気にしたが、すぐに男に向き直る",
                "男は初めて来た彼女の館の天井の高さに驚いているようだ"),
            man.talk("人形を作っているっていうから、もっと和風の家を想像していたよ"),
            yuki.talk("明かりが蝋燭だけしかないような？"),
            yuki.do("そう答えて、女は微笑む"),
            yuki.talk("ここが、寝室兼仕事場"),
            yuki.do("ドアを開けながら女は男を中へと招き入れた"),
            man.talk("それは、何？"),
            man.do("男が見つけたのは、部屋の片側に飾られていた高さ二メートルほどの透明な箱だ",
                "中には何も入っていない", "男が触れようとすると女は注意して小さく首を振った"),
            yuki.talk("新作用よ"),
            yuki.do("女はそう言って、用意しておいた紅茶をカップに注ぐ"),
            yuki.do("男は気づかなかったようだが、その箱の脇に小さな棒状ものが転がっていた",
                "小指の先の部分だ",
                "微かに血が付いている"),
            yuki.talk("一つ、約束して欲しいの"),
            yuki.do("紅茶を男に勧めながら女は言った"),
            yuki.talk("浮気はしない、と"),
            w.symbol("（了）"),
            )

## episode
def ep_doller(w: World):
    return w.episode("人形師の女",
            sc_visit(w),
            sc_memmory(w),
            sc_digging(w),
            sc_newman(w),
            )

## chapter
def ch001_doller(w: World):
    return w.chapter("１．人形師の女",
            ep_doller(w),
            )
