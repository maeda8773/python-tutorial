# 6. モジュール

# Pythonでは、モジュールを使用してコードを整理し、再利用可能にすることができます。
# モジュールは、関数、クラス、変数などを含むPythonファイルです。

import fibo
print(fibo.fib(1000))  # fiboモジュールのfib関数を使用してフィボナッチ数列を計算
print(fibo.fib2(100))  # fiboモジュールのfib2関数を使用してフィボナッチ数列をリストとして取得
fib = fibo.fib  # fib関数をローカルにインポート
fib(500)  # ローカルにインポートしたfib関数を使用

# --- モジュールについてもうすこし ---
# モジュールには、関数定義に加えて実行文を入れることができる
# 実行文は、インポート文の中で 最初に モジュール名が見つかったときにだけ実行
# 各々のモジュールは、プライベートな名前空間を持っていて、モジュールで定義されている関数はこのテーブルをグローバルな名前空間として使用

# --- モジュールをスクリプトとして実行する ---
# モジュール(.pyファイル)を読み込む時に内部で__name_という特別な変数が設定される
# もしモジュールがスクリプトとして実行された場合、__name__は"__main__"に設定される
# もしモジュールがインポートされた場合、__name__はモジュールの名前に設定される

# これを利用して、モジュールがスクリプトとして実行された場合にだけ実行されるコードを書くことができる
if __name__ == "__main__":
    import fibo
    fibo.fib(1000)  # fiboモジュールのfib関数を使用してフィボナッチ数列を計算

# --- モジュール検索パス ---
# Pythonが import 文でモジュールを読み込むときの探索順序
# 1. 組み込みモジュール (sys.builtin_module_names)
# 2. スクリプトのあるディレクトリ
# 3. PYTHONPATH 環境変数で指定されたディレクトリ
# 4. 標準ライブラリ / site-packages

# --- "コンパイル" された Python ファイル ---
# Pythonはモジュールを読み込む際、読み込み高速化のために
# コンパイル済みファイル(.pyc)を __pycache__ ディレクトリに保存する

# 例:
#   spam.py  →  __pycache__/spam.cpython-3X.pyc
#     - 3X は Python バージョン (例: 38 → Python 3.8)

# 特徴:
# - ソースの更新日時を自動で確認し、必要なら再コンパイル
# - .pyc は読み込みだけ高速化。実行速度は変わらない
# - コマンド直実行やソースなしの場合はキャッシュされない
# - -O / -OO スイッチで最適化可能
#     - -O: assert ステートメント削除
#     - -OO: assert と __doc__ 削除 → ファイルサイズ小さくなる
# - compileall モジュールでディレクトリ丸ごと .pyc 作成可能

# --- dir() 関数 ---
import fibo, sys
print(dir(fibo))  # ['__name__', 'fib', 'fib2']
print(dir(sys))   # sys モジュールの属性全部のリスト
print(dir())     # 現在のスコープの名前のリスト

import builtins
print(dir(builtins))  # 組み込み関数や例外のリスト

# --- パッケージ ---

# パッケージ = モジュールをまとめて階層的に管理する仕組み
# ディレクトリに __init__.py があればパッケージとして認識される

# 例: sound パッケージ
# sound/
#   __init__.py
#   formats/    ← サブパッケージ
#       wavread.py
#   effects/
#       echo.py

# import の方法
import sound.effects.echo             # 完全なパスで指定
from sound.effects import echo        # パッケージ名なしで使える
from sound.effects.echo import echofilter  # 関数だけ直接 import

# from package import * の場合
# __all__ リストにある名前だけ import される
# 例: __all__ = ["echo", "surround"]

# パッケージ内での相対 import
from . import echo       # 同じパッケージ内
from .. import formats   # 一つ上のパッケージ
