# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    x = set(input("Введите первое предложение: "))
    y = set(input("Введите второе предложение: "))
    common_letters = x.intersection(y)
    print(', '.join(common_letters))
