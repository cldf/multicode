# Multicode: Miscelleneous functions for handling unicode in transcriptions

[![Build Status](https://travis-ci.org/clpn/multicode.svg?branch=master)](https://travis-ci.org/clpn/multicode)
[![codecov](https://codecov.io/gh/clpn/multicode/branch/master/graph/badge.svg)](https://codecov.io/gh/clpn/multicode)
[![PyPI](https://img.shields.io/pypi/v/multicode.svg)](https://pypi.python.org/pypi/multicode)


## General information

This repository provides code and data to normalize datasets, to avoid pitfalls of unicode when creating linguistic data, and to infer general information about digital data when dealing with it in linguistic contexts.

One major concern is the normalization of phonetic transcriptions. There are many lookalikes in unicode which linguists use without knowing that they are not what they initially want to write. Thus the character used to transcribe an alveolar voiceless fricative, for example, has three candidates in Unicode which look extremely similar: ```ʃ ∫ ꭍ```, although only the first one is the character that should be used when writing phonetic transcriptions. Our goal is to provide ways to detect and normalize those cases which result from the confusion of Unicode characters when transcribing languages phonetically.

Other cases include specific writing systems, like CJK systems, where we want to offer services to more quickly handle with them. These cases include the possibility to detect the Unicodes of very rare characters by naming only there parts, but also simple Python functions that allow to determine whether a given character is a Chinese character or not.

## Structure of the Repository

Our repository contains data and code. Data is represented in a custom CSV dialect, namely tab-separated, with `|` as optional secondary separator for field content. Unicode characters can be represented either as UTF-8 encoded strings, or using notation like `U+0020`.
