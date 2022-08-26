def linerSearch(num):
    global lists
    i = 0
    for val in lists:
        if val == num:
            return i
        i += 1
    return

lists = list(map(int, input('リストを入力してください: ').split()))
n = int(input('検索したい数値を入力してください: '))
index = linerSearch(n)
if index is not None:
    print('検索した値は' + str(index + 1) + '番目です')
else:
    print('一致するものはありませんでした')
