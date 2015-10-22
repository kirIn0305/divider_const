# divider_const

定数除算の定数乗算化をPyhtonで実装

## Description
整数変数Vを整数定数Cで割りたい場合があります。その時除算器を使わず、定数Cの逆数を変数Vに掛けたほうが、簡単かつ高速な回路になります。

Unsignedの場合の手順

1. 被除数がKビットとする
2. 定数除数の２進表現で、最初に出現する1から後のKビットを切り出す。
3. 切り出した定数除数のLSBに1を足す
4. 被除数に、その定数値の小数部を乗じる
5. 結果の上位Kビットが答え

**Signedの場合は絶対値上で計算**

## Requirement
- Python3
- icarus-verilog
- GTKwave

## Usage

```bash:terminal
# Makefileを編集
# 被除数 K 除数C
# DIVIDEND_WIDTH = K
# DIVISOR = C

$ make create_hdl 
$ make sim
```

## References

> [LSI/FPGAの回路アーキテクチャ設計法](http://shop.cqpub.co.jp/hanbai/books/31/31091.html)
