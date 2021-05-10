import pandas as pd

# sample.csvファイルを読み込む。
df = pd.read_csv('./sample.csv')

# お店の一覧を格納する変数を宣言する。
shopNameList = []

# 商品一覧を格納する変数を宣言する。
productList = []

# 2次元配列 → 1次元配列へ変換する。
# 2次元配列 → 1次元配列へ変換する際に、改行処理も施す。


def convertProductList(list):
    tmp = []
    for l in list:
        # joinについて : https://www.headboost.jp/python-strings-into-a-list/#1_join
        tmp.append("\n".join(l))
    return tmp


# csv情報を1行ずつ読み出す。
# iterrows参考 : https://note.nkmk.me/python-pandas-dataframe-for-iteration/
for index, row in df.iterrows():
    # A列に含まれるお店の名前を格納する。
    shopName = row[0]
    # B列に含まれる商品の名前を格納する。
    productName = row[1]

    # 既にお店一覧(shopNameList)内にお店が登録されているのか確認する。
    # 登録されている場合
    if shopName in shopNameList:
        # 既存で登録されているお店が格納される位置をindex関数を利用して探索する。
        # indexについて : https://www.javadrive.jp/python/list/index10.html
        # appendを活用して、商品の名前を末尾に格納する。
        productList[shopNameList.index(shopName)].append(productName)
    # 登録されていない場合
    else:
        # 新規の商品登録を行う。index位置は新規のお店と揃える。
        productList.append([productName])
        # 新規でお店を登録する。
        shopNameList.append(shopName)

# csvファイル名をoutput.csvとしてcsvを生成する。
# indexを付与しないように、index=Falseとする。
# to_csvについて : https://note.nkmk.me/python-pandas-to-csv/
# B列にて2次元配列のままだと、DataFrameが使えないので、convertProductList関数を呼び出し、1次元配列への変換を行う。
# 2次元配列 → 1次元配列へ変換する際に、改行処理も施す。
pd.DataFrame({
    'A': shopNameList,
    'B': convertProductList(productList)
}).to_csv('./output.csv', index=False)
