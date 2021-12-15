# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    u = set("aelouy")
    x = input("Введите слово: ")
    count = 0
    for letter in x:
        if letter in u:
            count += 1
    print(f"Количество гласных равно: {count}")
