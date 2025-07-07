alist = ['사과', '바나나', '딸기']
blist = ['Apple', 'Banana', 'Strawberry']

print('test')

[print(idx, (v0, v1)) for idx, (v0, v1) in enumerate([*zip(alist, blist)])]
# 동작을 하고 끝나기 때문에, [None, None, None]은 코랩의 코드셀에서만 보여줄 뿐 의미가 없다.
