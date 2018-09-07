#!/usr/local/pyenv/shims/python
# coding:utf-8

import flickrapi
import pprint
import AppConf

# 検索キーワード
# keyword = "海岸"
num = 1

def getFlickrImage(keyword, num = 1):
    resultStr = ""

    flickr = flickrapi.FlickrAPI(AppConf.api_key, AppConf.secret, format='parsed-json')
    
    # 画像サイズurl
    # s	75x75 サイズの小さな四角形
    # q	150x150 サイズの大きな四角形
    # t	最大100の幅を持つサムネイル
    # m	小型サイズ。最も大きい辺のサイズが 240
    # n	小型サイズ。最も大きい辺のサイズが 320
    # -	中型サイズ。最も大きい辺のサイズが 500
    # z	640の中型サイズ。最も大きい辺のサイズが 640
    # c	800の中型サイズ。最も大きい辺のサイズが 800†
    # b	大型サイズ。最も大きい辺のサイズが1024*
    # h	1600の大型サイズ。最も大きい辺のサイズが1600†
    # k	2048の大型サイズ。最も大きい辺のサイズが2048†
    # o	オリジナルの画像。画像形式については元の画像形式に依存する
    urlKind = "url_z"
    
    res = flickr.photos.search(
        text = keyword,
        per_page = num,
        media = 'photos',
        # sort = 'date-posted-desc',
        sort = 'relevance',
        safe_search = 1,
        extras = urlKind + ', licences'
    )

    if not res["photos"]["photo"]:
        resultStr = u"こめんなさい。:woman-facepalming:画像の取得に失敗しちゃいました。\n何度か試してみてください。:wink:"
    else:
        resultStr = u"こちらの画像で、いかがかしら:wink:\n" + res["photos"]["photo"][0][urlKind]

    # print(resultStr)

    return resultStr
