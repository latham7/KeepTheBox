from flask import Flask, render_template, request, redirect

version = "1.1.1"


def calculate(gold, iron, coal, copper, payoutInt):
    goldOutput = gold*35.00*payoutInt
    ironOutput = iron*35.00*payoutInt
    coalOutput = coal*35.00*payoutInt
    copperOutput = copper*35.00*payoutInt

    total=goldOutput+ironOutput+coalOutput+copperOutput
    return total
