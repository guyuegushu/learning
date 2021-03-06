import random

"""
1. 采用坐标方式,随机取出行\段,得出字符
2. 添加其他字段选择方式, 浊音, 半浊音, 全选等
3. 将平片假名合在一起, 加个按钮
4. 添加重点词汇标记
whole_word =[
            ({"a":"あ"},{"a":"ア"}),
            ({"i":"い"},{"i":"イ"}),
            ({"u":"う"},{"u":"ウ"}),
            ({"e":"え"},{"e":"エ"}),
            ({"o":"お"},{"o":"を"}, {"o":"オ"}, {"o":"ヲ"}),
            ({"ka":"か"},{"ka":"カ"}),
            ({"ki":"き"},{"ki":"キ"}),
            ({"ku":"く"},{"ku":"ク"}),
            ({"ke":"け"},{"ke":"ケ"}),
            ({"ko":"こ"},{"ko":"コ"}),
            ({"sa":"さ"},{"sa":"サ"}),
            ({"shi":"し"},{"shi":"シ"}),
            ({"su":"す"},{"su":"ス"}),
            ({"se":"せ"},{"se":"セ"}),
            ({"so":"ソ"},{"so":"そ"}),
            ({"ta":"タ"},{"ta":"た"}),
            ({"chi":"チ"},{"chi":"ち"}),
            ({"tsu":"つ"},{"tsu":"ツ"}),
            ({"te":"て"},{"te":"テ"}),
            ({"to":"と"},{"to":"ト"}),
            ({"na":"な"},{"na":"ナ"}),
            ({"ni":"に"},{"ni":"ニ"}),
            ({"nu":"ぬ"},{"nu":"ヌ"}),
            ({"ne":"ね"},{"ne":"ネ"}),
            ({"no":"の"},{"no":"ノ"}),
            ({"ha":"は"},{"ha":"ハ"}),
            ({"hi":"ひ"},{"hi":"ヒ"}),
            ({"fu":"ふ"},{"fu":"フ"}),
            ({"he":"ヘ"},{"he":"へ"}),
            ({"ho":"ほ"},{"ho":"ホ"}),
            ({"ma":"ま"},{"ma":"マ"}),
            ({"mi":"み"},{"mi":"ミ"}),
            ({"mu":"む"},{"mu":"ム"}),
            ({"me":"め"},{"me":"メ"}),
            ({"mo":"も"},{"mo":"モ"}),
            ({"ya":"や"},{"ya":"ヤ"}),
            ({"yu":"ゆ"},{"yu":"ユ"}),
            ({"yo":"よ"},{"yo":"ヨ"}),
            ({"ra":"ら"},{"ra":"ラ"}),
            ({"ri":"り"},{"ri":"リ"}),
            ({"ru":"る"},{"ru":"ル"}),
            ({"re":"れ"},{"re":"レ"}),
            ({"ro":"ろ"},{"ro":"ロ"}),
            ({"wa":"わ"},{"wa":"ワ"}),
            ({"wo":"を"},{"wo":"ヲ"}),
            ({"n":"ん"},{"n":"ン"}),
            ({"ga":"が"},{"ga":"ガ"}),
            ({"gi":"ぎ"},{"gi":"ギ"}),
            ({"gu":"ぐ"},{"gu":"グ"}),
            ({"ge":"げ"},{"ge":"ゲ"}),
            ({"go":"ご"},{"go":"ゴ"}),
            ({"za":"ざ"},{"za":"ザ"}),
            ({"zi":"じ"},{"zi":"ジ"}),
            ({"zu":"ず"},{"zu":"ズ"}),
            ({"ze":"ぜ"},{"ze":"ゼ"}),
            ({"zo":"ぞ"},{"zo":"ゾ"}),
            ({"da":"だ"},{"da":"ダ"}),
            ({"di":"ぢ"},{"di":"ヂ"}),
            ({"du":"づ"},{"du":"ヅ"}),
            ({"de":"で"},{"de":"デ"}),
            ({"do":"ど"},{"do":"ド"}),
            ({"ba":"ば"},{"ba":"バ"}),
            ({"bi":"び"},{"bi":"ビ"}),
            ({"bu":"ぶ"},{"bu":"ブ"}),
            ({"be":"べ"},{"be":"ベ"}),
            ({"bo":"ぼ"},{"bo":"ボ"}),
            ({"pa":"ぱ"},{"pa":"パ"}),
            ({"pi":"ぴ"},{"pi":"ピ"}),
            ({"pu":"ぷ"},{"pu":"プ"}),
            ({"pe":"ぺ"},{"pe":"ペ"}),
            ({"po":"ぽ"},{"po":"ポ"}),
            ({"kya":"きゃ"},{"kya":"キャ"}),
            ({"kyu":"きゅ"},{"kyu":"キュ"}),
            ({"kyo":"きょ"},{"kyo":"キョ"}),
            ({"sha":"しゃ"},{"sha":"シャ"}),
            ({"shu":"しゅ"},{"shu":"シュ"}),
            ({"sho":"しょ"},{"sho":"ショ"}),
            ({"cha":"ちゃ"},{"cha":"チャ"}),
            ({"chu":"ちゅ"},{"chu":"チュ"}),
            ({"cho":"ちょ"},{"cho":"チョ"}),
            ({"nya":"にゃ"},{"nya":"ニャ"}),
            ({"nyu":"にゅ"},{"nyu":"ニュ"}),
            ({"nyo":"にょ"},{"nyo":"ニョ"}),
            ({"hya":"ひゃ"},{"hya":"ヒャ"}),
            ({"hyu":"ひゅ"},{"hyu":"ヒュ"}),
            ({"hyo":"ひょ"},{"hyo":"ヒョ"}),
            ({"mya":"みゃ"},{"mya":"ミャ"}),
            ({"myu":"みゅ"},{"myu":"ミュ"}),
            ({"myo":"みょ"},),
            ({"myo":"ミョ"},),
            ({"rya":"りゃ"},{"rya":"リャ"}),
            ({"ryu":"りゅ"},{"ryu":"リュ"}),
            ({"ryo":"りょ"},{"ryo":"リョ"}),
            ({"gya":"ぎゃ"},{"gya":"ギャ"}),
            ({"gyu":"ぎゅ"},),
            ({"gyu":"ギュ"},),
            ({"gyo":"ぎょ"},{"gyo":"ギョ"}),
            ({"zya":"じゃ"},{"zya":"ジャ"}),
            ({"zyu":"じゅ"},{"zyu":"ジュ"}),
            ({"zyo":"じょ"},{"zyo":"ジョ"}),
            ({"bya":"びゃ"},{"bya":"ビャ"}),
            ({"byu":"びゅ"},{"byu":"ビュ"}),
            ({"byo":"びょ"},{"byo":"ビョ"}),
            ({"pya":"ぴゃ"},{"pya":"ピャ"}),
            ({"pyu":"ぴゅ"},{"pyu":"ピュ"}),
            ({"pyo":"ぴょ"},{"pyo":"ピョ"})
]
"""
a = [({"a": "あ"}, {"a": "ア"}),
     ({"i": "い"}, {"i": "イ"}),
     ({"u": "う"}, {"u": "ウ"}),
     ({"e": "え"}, {"e": "エ"}),
     ({"o": "お"}, {"o": "オ"})]

k = [({"ka": "か"}, {"ka": "カ"}),
     ({"ki": "き"}, {"ki": "キ"}),
     ({"ku": "く"}, {"ku": "ク"}),
     ({"ke": "け"}, {"ke": "ケ"}),
     ({"ko": "こ"}, {"ko": "コ"})]

s = [({"sa": "さ"}, {"sa": "サ"}),
     ({"shi": "し"}, {"shi": "シ"}),
     ({"su": "す"}, {"su": "ス"}),
     ({"se": "せ"}, {"se": "セ"}),
     ({"so": "そ"}, {"so": "ソ"})]

t = [({"ta": "た"}, {"ta": "タ"}),
     ({"chi": "ち"}, {"chi": "チ"}),
     ({"tsu": "つ"}, {"tsu": "ツ"}),
     ({"te": "て"}, {"te": "テ"}),
     ({"to": "と"}, {"to": "ト"})]

n = [({"na": "な"}, {"na": "ナ"}),
     ({"ni": "に"}, {"ni": "ニ"}),
     ({"nu": "ぬ"}, {"nu": "ヌ"}),
     ({"ne": "ね"}, {"ne": "ネ"}),
     ({"no": "の"}, {"no": "ノ"})]

h = [({"ha": "は"}, {"ha": "ハ"}),
     ({"hi": "ひ"}, {"hi": "ヒ"}),
     ({"fu": "ふ"}, {"fu": "フ"}),
     ({"he": "ヘ"}, {"he": "へ"}),
     ({"ho": "ほ"}, {"ho": "ホ"})]

m = [({"ma": "ま"}, {"ma": "マ"}),
     ({"mi": "み"}, {"mi": "ミ"}),
     ({"mu": "む"}, {"mu": "ム"}),
     ({"me": "め"}, {"me": "メ"}),
     ({"mo": "も"}, {"mo": "モ"})]

y = [({"ya": "や"}, {"ya": "ヤ"}),
     ({"yu": "ゆ"}, {"yu": "ユ"}),
     ({"yo": "よ"}, {"yo": "ヨ"})]

r = [({"ra": "ら"}, {"ra": "ラ"}),
     ({"ri": "り"}, {"ri": "リ"}),
     ({"ru": "る"}, {"ru": "ル"}),
     ({"re": "れ"}, {"re": "レ"}),
     ({"ro": "ろ"}, {"ro": "ロ"})]

w = [({"wa": "わ"}, {"wa": "ワ"}),
     ({"wo": "を"}, {"wo": "ヲ"})]

N = [({"n": "ん"}, {"n": "ン"})]

g = [({"ga": "が"}, {"ga": "ガ"}),
     ({"gi": "ぎ"}, {"gi": "ギ"}),
     ({"gu": "ぐ"}, {"gu": "グ"}),
     ({"ge": "げ"}, {"ge": "ゲ"}),
     ({"go": "ご"}, {"go": "ゴ"})]

z = [({"za": "ざ"}, {"za": "ザ"}),
     ({"zi": "じ"}, {"zi": "ジ"}),
     ({"zu": "ず"}, {"zu": "ズ"}),
     ({"ze": "ぜ"}, {"ze": "ゼ"}),
     ({"zo": "ぞ"}, {"zo": "ゾ"})]

d = [({"da": "だ"}, {"da": "ダ"}),
     ({"di": "ぢ"}, {"di": "ヂ"}),
     ({"du": "づ"}, {"du": "ヅ"}),
     ({"de": "で"}, {"de": "デ"}),
     ({"do": "ど"}, {"do": "ド"})]

b = [({"ba": "ば"}, {"ba": "バ"}),
     ({"bi": "び"}, {"bi": "ビ"}),
     ({"bu": "ぶ"}, {"bu": "ブ"}),
     ({"be": "べ"}, {"be": "ベ"}),
     ({"bo": "ぼ"}, {"bo": "ボ"})]

p = [({"pa": "ぱ"}, {"pa": "パ"}),
     ({"pi": "ぴ"}, {"pi": "ピ"}),
     ({"pu": "ぷ"}, {"pu": "プ"}),
     ({"pe": "ぺ"}, {"pe": "ペ"}),
     ({"po": "ぽ"}, {"po": "ポ"})]

xxx = [({"kya": "きゃ"}, {"kya": "キャ"}),
       ({"kyu": "きゅ"}, {"kyu": "キュ"}),
       ({"kyo": "きょ"}, {"kyo": "キョ"}),
       ({"sha": "しゃ"}, {"sha": "シャ"}),
       ({"shu": "しゅ"}, {"shu": "シュ"}),
       ({"sho": "しょ"}, {"sho": "ショ"}),
       ({"cha": "ちゃ"}, {"cha": "チャ"}),
       ({"chu": "ちゅ"}, {"chu": "チュ"}),
       ({"cho": "ちょ"}, {"cho": "チョ"}),
       ({"nya": "にゃ"}, {"nya": "ニャ"}),
       ({"nyu": "にゅ"}, {"nyu": "ニュ"}),
       ({"nyo": "にょ"}, {"nyo": "ニョ"}),
       ({"hya": "ひゃ"}, {"hya": "ヒャ"}),
       ({"hyu": "ひゅ"}, {"hyu": "ヒュ"}),
       ({"hyo": "ひょ"}, {"hyo": "ヒョ"}),
       ({"mya": "みゃ"}, {"mya": "ミャ"}),
       ({"myu": "みゅ"}, {"myu": "ミュ"}),
       ({"myo": "みょ"},),
       ({"myo": "ミョ"},),
       ({"rya": "りゃ"}, {"rya": "リャ"}),
       ({"ryu": "りゅ"}, {"ryu": "リュ"}),
       ({"ryo": "りょ"}, {"ryo": "リョ"}),
       ({"gya": "ぎゃ"}, {"gya": "ギャ"}),
       ({"gyu": "ぎゅ"},),
       ({"gyu": "ギュ"},),
       ({"gyo": "ぎょ"}, {"gyo": "ギョ"}),
       ({"zya": "じゃ"}, {"zya": "ジャ"}),
       ({"zyu": "じゅ"}, {"zyu": "ジュ"}),
       ({"zyo": "じょ"}, {"zyo": "ジョ"}),
       ({"bya": "びゃ"}, {"bya": "ビャ"}),
       ({"byu": "びゅ"}, {"byu": "ビュ"}),
       ({"byo": "びょ"}, {"byo": "ビョ"}),
       ({"pya": "ぴゃ"}, {"pya": "ピャ"}),
       ({"pyu": "ぴゅ"}, {"pyu": "ピュ"}),
       ({"pyo": "ぴょ"}, {"pyo": "ピョ"})]

whole_word = (
    a,
    k,
    s,
    t,
    n,
    h,
    m,
    y,
    r,
    w,
    N,
    g,
    z,
    d,
    b,
    p,
    xxx
)


def random_select_group(selected_row):
    row_list_tmp = []
    for list_tmp in selected_row:
        row_list_tmp[len(row_list_tmp):len(row_list_tmp)] = list_tmp
    list_len = len(row_list_tmp)
    index = random.randint(0, list_len - 1)
    selected_group = row_list_tmp[index]
    return selected_group


def random_select_signal(selected_group):
    selected_dict = selected_group[0]
    signal = ''
    for key, value in selected_dict.items():
        signal = key
    return signal


def random_select_pin(selected_group):
    selected_dict = selected_group[0]
    word = ''
    for key, value in selected_dict.items():
        word = value
    return word


def random_select_pian(selected_group):
    selected_dict = selected_group[1]
    word = ''
    for key, value in selected_dict.items():
        word = value
    return word
