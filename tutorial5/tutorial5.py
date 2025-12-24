# 5. データ構造

# --- リスト型についてもう少し ---
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('grape')          # 末尾に追加
print(fruits)

fruits.extend(['mango', 'melon'])  # 複数追加
print(fruits)

fruits.insert(2, 'watermelon')  # 指定位置に挿入
print(fruits)

fruits.remove('apple')          # 最初に見つかった要素を削除
print(fruits)

fruits.pop()                    # 末尾の要素を削除して返す
print(fruits)

print(fruits.index('banana'))          # 最初に見つかった要素のインデックスを返す

print(fruits.count('banana'))          # 指定した要素の出現回数を返す

fruits.sort()                    # 昇順にソート
print(fruits)

fruits.reverse()                 # 逆順に並び替え
print(fruits)

fruits_copy = fruits.copy()                    # リストのコピー
print(fruits_copy)

fruits_copy.clear()                   # リストの全要素を削除
print(fruits_copy)

# --- リストをスタックとして使う ---
# 最後に追加された要素が最初に取り出されます ("last-in, first-out")
# スタックの一番上に要素を追加するには append() を使用
# スタックの一番上から要素を取り出すには pop() をインデックスを指定せずに使用

stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print(stack)

print(stack.pop())
print(stack.pop())

# --- リストをキューとして使う ---
# 最初に追加した要素を最初に取り出します ("first-in, first-out")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry が到着
queue.append("Graham")          # Graham が到着
print(queue.popleft())                 # 最初に到着した人が去って行った
print(queue.popleft())                 # 2番目の人も去って行った
print(queue)                           # キューに残っているものは到着順

# --- リストの内包表記 ---
# リストを生成するための簡潔な方法
# [ 式  for 変数 in イテラブル  if 条件 ]

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# --- del 文 ---
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]          # インデックスで指定した要素を削除
print(a)

del a[2:4]       # スライスで指定した範囲の要素を削除
print(a)

del a[:]         # リストの全要素を削除
print(a)

# --- タプルとシーケンス ---
t = 12345, 54321, 'hello!'
print(t[0])            # インデックスでアクセス
print(t)

u = t, (1, 2, 3, 4, 5)            # タプルは入れ子にできる
print(u)

# t[0] = 88888            # タプルの要素は変更できない  # エラー発生

v = ([1, 2, 3], [3, 2, 1])    # タプルの要素がリストの場合、リストの内容は変更可能
print(v)
v[0][0] = 999
print(v)

empty = ()
print(len(empty))
print(empty)
singleton = 'hello',    # 末尾のカンマに注意
print(len(singleton))
print(singleton)

t = 1, 2, 3
x, y, z = t         # タプルのアンパック
print(x)
print(y)
print(z)

# --- 集合型 ---
# 集合とは、重複する要素をもたない、順序づけられていない要素の集まり
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                  # 重複する要素は表示されない
print('orange' in basket)    # メンバーシップのテスト
print('crabgrass' in basket)

{} # 空の辞書を作成 (空の集合ではないことに注意)
set() # 空の集合を作成

# --- 辞書型 (dictionary) ---
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

# --- ループのテクニック ---
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# --- 条件についてもう少し ---
# in や not in を使って、シーケンスや集合、辞書のメンバーシップをテストできます
a = ['apple', 'banana', 'pear']
print('banana' in a)
print('grape' not in a)

# is や is not を使って、オブジェクトの同一性をテストできます
a = ['apple', 'banana', 'pear']
b = a
c = list(a)
print(a is b)
print(a is c)
print(a == c)

# and or not 優先順位
# not が最も高く、次に and、最後に or
x = True
y = False
print(x or y and not x)
print((x or y) and (not x))

# and や or は短絡評価を行います
# A and B の場合、A が偽と評価された時点で B は評価されません
# A or B の場合、A が真と評価された時点で B は評価されません

# セイウチ演算子 (:=)
# 式の中で代入したいときだけ明示的に:=を使う
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if (n := len(items)) > 10:
    print(n)
