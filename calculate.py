from flask import Flask, render_template, request, redirect

version = "1.1.1"


def calculate(gold, iron, coal, copper):
    goldOutput = gold*2275
    ironOutput = iron*2275
    coalOutput = coal*2275
    copperOutput = copper*2275

    total=goldOutput+ironOutput+coalOutput+copperOutput
    return total
