# Multicode: Miscelleneous functions for handling unicode in transcriptions

[![Build Status](https://github.com/cldf/multicode/workflows/tests/badge.svg)](https://github.com/cldf/multicode/actions?query=workflow%3Atests)
[![PyPI](https://img.shields.io/pypi/v/multicode.svg)](https://pypi.org/project/multicode)


## General information

This repository provides code and data to normalize datasets, to avoid pitfalls of unicode when creating linguistic data, and to infer general information about digital data when dealing with it in linguistic contexts.

One major concern is the normalization of phonetic transcriptions. There are many lookalikes in unicode which linguists use without knowing that they are not what they initially want to write. Thus the character used to transcribe an alveolar voiceless fricative, for example, has three candidates in Unicode which look extremely similar: ```ʃ ∫ ꭍ```, although only the first one is the character that should be used when writing phonetic transcriptions. Our goal is to provide ways to detect and normalize those cases which result from the confusion of Unicode characters when transcribing languages phonetically.

Other cases include specific writing systems, like CJK systems, where we want to offer services to more quickly handle them. These cases include the possibility to detect the Unicode code points of very rare characters by naming only the parts, but also simple Python functions that allow to determine whether a given character is a Chinese character or not.


## CLI

Installing this package will also install the `multicode` command.


### Normalizing data

The main purpose of this package is data normalization, i.e. replacing lookalikes
in strings with the canonical characters. This can be done using the `recode`
subcommand, either passing a string as argument:
```shell
$ multicode recode "ʃ ∫ ꭍ"
ʃ ʃ ʃ
```
or using pipes, i.e. having `recode` read from stdin:
```shell
$ echo "ʃ ∫ ꭍ" | multicode recode 
ʃ ʃ ʃ
```


## Structure of the Repository

Our repository contains data and code. Data is represented in a custom CSV dialect, namely tab-separated, with `|` as optional secondary separator for field content. Unicode characters can be represented either as UTF-8 encoded strings, or using notation like `U+0020`.
