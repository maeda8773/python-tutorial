# 3. 形式ばらない Python の紹介

# --- コメント ---
print(2 + 2)  # 4


# --- 数値演算 ---
print(17 / 3)     # 5.666666666666667
print(17 // 3)    # 5
print(17 % 3)     # 2


# --- 変数 ---
width = 20
height = 5 * 9
print(width)
print(height)


# --- 文字列 ---
print('doesn\'t')

s = 'First line.\nSecond line.'
print(s)


# --- 複数行文字列 ---
print("""\
Usage: thingy [OPTIONS]
  -h
  -H hostname
""")


# --- 文字列操作 ---
word = 'Python'
print(word[0])    # P
print(word[0:2])  # Py
print(len('supercalifragilisticexpialidocious'))


# --- リスト ---
squares = [1, 4, 9, 16, 25]
print(squares)

cubes = [1, 8, 27, 64, 125]
cubes.append(216)
print(cubes)

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # True

# --- 全てのスライス操作は、指定された要素を含む新しいリストを返します ---
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)  # ['Red', 'Green', 'Alpha']
print(rgba)         # ['Red', 'Green', 'Blue']
print(id(rgb) == id(correct_rgba))  # False
