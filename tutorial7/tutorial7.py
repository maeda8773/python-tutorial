# 7. 入力と出力

# --- 出力を見やすくフォーマットする ---
# year = 2025
# event = "Tokyo Olympics"
# print(f"{year} will host the {event}.")  # f文字列を使用

# yes_votes = 42_572_654
# total_votes = 85_705_149
# percentage = yes_votes / total_votes * 100
# print('{:-9} 賛成票 {:2.2%}'.format(yes_votes, percentage))  # str.format() メソッド

# s = 'Hello, world.'
# print(str(s))          # 文字列として出力
# print(repr(s))        # 文字列の公式表現を出力

# # 文字列に repr() を使うとクォートとバックスラッシュが追加される:
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# # repr() の引数はどんな Python オブジェクトでも可:
# x = 10 * 3.25
# y = 200 * 200
# print(repr((x, y, ('spam', 'eggs'))))

# --- フォーマット済み文字列リテラル ---
# 文字列の頭に f か F を付け、式を {expression} と書くことで、 Python の式の値を文字列の中に入れ込める
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}') # ':10' はフィールド幅を指定

# animals = 'ウナギ'
# print(f'私のホバークラフトは {animals} でいっぱいです。')
# print(f'私のホバークラフトは {animals!r} でいっぱいです。') # !r は repr() を呼び出す

# bugs = 'roaches'
# count = 13
# area = 'living room'
# print(f'Debugging {bugs=} {count=} {area=}') # '=' は変数名と値を表示

# --- 文字列の format() メソッド ---
# print('We are the {} who say "{}!"'.format('knights', 'Ni')) # 波括弧 {} は引数で置換される

# # 引数の位置を指定可能
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# # キーワード引数も使用可能
# print('This {food} is {adjective}.'.format(
#       food='spam', adjective='absolutely horrible'))

# # 混在も可能
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# # 辞書の値を参照することも可能
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# --- 文字列の手作業でのフォーマット ---
# rjust(), ljust(), center() メソッドを使用して文字列を特定の幅に揃えることができる
# text = "Hello"
# print(text.ljust(10))     # 左揃え
# print(text.rjust(10))     # 右揃え
# print(text.center(20))    # 中央揃え

# --- ファイルを読み書きする ---
