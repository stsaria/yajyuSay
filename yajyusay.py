import unicodedata, sys

yajyuuAa = """　　　　　　　　　　　　　 ,,,z=~'ﾞ'+''ｯ彡ｯ,､
　　　　　　　　　　　　,ｨ´ 　　　　　 "':';:;ｯ;,
　　　　　　　　 ,　' ﾞ´`ﾞﾐﾞｯ,　　　　　　　 "',`,
　　　　　　 ,／ 　　　 `､ﾞミ　　　　　　　　 ﾞ:;:,
　　　　　 /　　　　　 _ =ヾ､ﾞｼｼ=;,z,、　　　 ﾞ;ｼ::ﾐ
　　　　 /　　　　 ,ｒ,´　　 /　´`ヽ ゛ﾞ`　 　　,ﾞ彡:ﾐ
　　　 / 　　　, '-､_`ヽ_/,　　　　　　　 　 ﾐ;::彡;:
　　 ,'　　　,ｼ´｀｀ ヽ`i｀!　　　　　　　　 ,,彡;::ｼ:彡　
　　;i　　､（´ ￣`ヽ / '　　　　　　　　シ:ｼ;:ﾐ::ｼ"
　ノ:!､　 ヽ｀`ｰ =;ｨ'　　　　　　　　,,ｼ:;彡;ｼﾞ
´:::::.ヾ. 　　　￣´　　　　　　　　' `,ｼﾐﾞ
:::::::::::::.`:ヽ､_　　　　　　　...:;'＿,ソ'ﾞ''
::::::::::::::::::::::::::｀:::::::::::::::-=''"／"""

yajyuuMessageText = "イキスギィ"
yajyuuMessageAa = ""

if len(sys.argv) >= 2:
    yajyuuMessageText = sys.argv[1]

for i in range(3):
    yajyuuMessageAa += "          "
    if i == 1:
        yajyuuMessageAa += "< "+yajyuuMessageText+" >\n"
        continue
    else:
        yajyuuMessageAa += "  "
    for k in yajyuuMessageText:
        yajyuuMessageAa += "="
        if unicodedata.east_asian_width(k) in 'FWA':
            yajyuuMessageAa += "="
    yajyuuMessageAa += "\n"
yajyuuAa = yajyuuMessageAa + "\n" + yajyuuAa

print(yajyuuAa)