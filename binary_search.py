# キーではなく条件式を入れる方式。
# arrayを使う方式
# 注意！返り値のleftはlen(array)-2の値より大きくならないので、使う前にarrayの両端の条件が違うことをきちんと確認する。
# もしくは右端に絶対左端と異なるような要素をpaddingする。
# 状況に応じて探索の範囲を絞れるようにleftとrightを引数として設定可能なようにした。

def binary_search(func, array, left=0, right=-1):
    if right==-1:right=len(array)-1
    y_left, y_right = func(array[left]), func(array[right])
    while True:
        middle = (left+right)//2
        y_middle = func(array[middle])
        if y_left==y_middle: left=middle
        else: right=middle
        if right-left==1:break

    return left
