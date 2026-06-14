# Genes.py

Reproduction of GENES - Virtual Life with mutate evolution - with Python, adding original functions

これは、トラ技ジュニア2019年春号に掲載された「GENES」を、プログラムの動作を観察して1からPythonで再現したものです。

C#で実装されたオリジナルのGENESと比較して、当たり判定やマップサイズ、初期状態や移動方向が異なります。
さらに、状態のセーブ・ロード機能を追加して、独自フォーマット(中2のときはそういうのがカッコいいと思っていました)で読み書きが可能です。
また、オリジナルではバグとして存在していた、「IDが被ることによるエサの消失(置き換え)」が、「エサが最大数に達すると既存のエサを移動」として実装されています。

## Requirements

- Python 3
- Tkinter

## How to run

```py
python3 Genes.py
```

# Credits

オリジナルのGENESは[株式会社ラジアン](https://radiun.co.jp/)の著作物です。