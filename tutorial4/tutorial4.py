# 4. その他の制御フローツール

# --- if文 ---
x = int(input("数字を入力してください: "))
if x < 0:
    x = 0
    print("負の数は0に変換されました")
elif x == 0:
    print("0です")
elif x == 1:
    print("1です")
else:
    print("1より大きい数です")

# --- for文 ---
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# コレクション作成
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 方針:  コピーを反復
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# 方針:  新コレクション作成
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# --- range() 関数 ---
# range(start, stop, step)
# start … 開始の数字（含む）
# stop  … 終了の数字（含まない）
# step  … 増分（省略時は1）
for i in range(5):
    print(i)
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# --- break 文と continue 文 ---
for n in range(1, 6):
    if n >= 3:
        print(f"{n} になったのでループを終了！")
        break  # ここでループ終了
    print(f"{n} はまだ続行中")

for n in range(1, 6):
    if n % 2 == 0:
        print(f"{n} は偶数なのでスキップ！")
        continue  # 次のループへ飛ぶ
    print(f"{n} は奇数なので表示")

# --- pass 文 ---
def initlog(*args):
    pass   # ここを忘れずに実装すること

# --- match 文 ---
fruit = "apple"

match fruit:
    case "apple" | "pear":
        print("リンゴかナシだよ")
    case "banana":
        print("バナナだよ")
    case _:
        print("その他のフルーツ")

# --- 関数を定義する ---
def greet(name):
    """名前を渡すと挨拶を返す関数"""
    return f"こんにちは、{name}さん！"

# 関数の呼び出し
message = greet("はるや")
print(message)
