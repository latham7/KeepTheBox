from flask import Flask, render_template, request, redirect

version = "1.1.1"


def calculate(gold, iron, coal, copper, payoutInt, gunpowder, netherwart, dirt, deepslate):
    goldOutput = gold*35*payoutInt
    ironOutput = iron*35*payoutInt
    coalOutput = coal*35*payoutInt
    copperOutput = copper*35*payoutInt
    gunpowderOutput = gunpowder*35*payoutInt
    netherwartOutput = netherwart*20*payoutInt
    dirtOutput = dirt*35*payoutInt
    deepslateOutput = deepslate*15*payoutInt

    total=goldOutput+ironOutput+coalOutput+copperOutput+gunpowderOutput+netherwartOutput+dirtOutput+deepslateOutput
    return total
