# -*- coding: utf-8 -*-

# def get_letters(text):
#     letters = {}
#
#     for letter in text:
#
#         if letters.get(letter) == None:
#             letters[letter] = 0
#
#         letters[letter] += 1
#
#     sort_orders = sorted(letters.items(), key=lambda x: x[1], reverse=True)
#     return sort_orders
#
#
# def get_words(text: str):
#     words = {}
#
#     for row in text.split("\n"):
#         words_list = row.split(" ")
#
#         for word_item in words_list:
#             if words.get(word_item) == None:
#                 words[word_item] = 0
#             words[word_item] += 1
#
#     sort_orders = sorted(words.items(), key=lambda x: x[1], reverse=True)
#     return sort_orders

def unlock_password(password):
    password_dict = {
        "k": "a",
        "q": "n",
        "m": "t",
        "f": "h",
        "n": "e",
        "o": "i",
        "z": "o",
        "e": "s",
        "u": "w",
        "i": "u",
        "r": "d",
        "y": "g",
        "w": "l",
        "a": "f",
        "j": "r",
        "s": "c",
        "g": "k",
        "d": "p",
        "p": "b",
        "t": "y",
        "l": "m",
        "x": "x",
        "c": "v",
        "v": "q",
        "b": "j",
        "h": "h",
        ".": ".",
        ",": ",",
        "!": "!",
        ";": ";",
        "'": "'",
        "`": "`",
        ":": ":",
        "-": "-",
        "û": "û"

    }

    #ustekileri kendim doldurdum altdaki kodu çağıra çağıra [x] x harfı bilinmiyor anlamına geliyor.
    #haflerin kaçar tane olduğunu getiren get_letters()
    #kelimelerden kaçar tane olduğunu getiren get_words()
    #bu fonksiyonları kullanarak ilgili sayfayı dikkate alınarak harf karşılıkları bulundu
    unlocked_password = ""

    for letter in password:
        if password_dict.get(letter) == None:
            if letter.isalpha():
                unlocked_password += "[" + letter + "]"
            else:
                unlocked_password += letter
        else:
            unlocked_password += password_dict.get(letter)

    return unlocked_password


teacher_given_sentence = """
`qzu azj mfn wkem jksn! ' ekor ykqrkwa. 'oa mfn eiq oe efoqoqy zimeorn un lkt emoww neskdn. kamnj ln! '
fn mijqnr wnam kqr ednr ksjzee mfn elzzmf awzzj za mfn fkww. mfn roemkqsn uke yjnkmnj mfkq om fkr wzzgnr. ke mfnt jkq mfnt fnkjr mfn pnkm kqr nsfz za 
lkqt fijjtoqy annm pnfoqr. k efjoww tnww unqm id: mfnt fkr pnnq ennq. mfnjn uke k joqy kqr swkef za emnnw. kq kjjzu ufoemwnr zcnj ajzrz'e fnkr.       
pzjzloj wkiyfnr. `mfnt ror qzm nxdnsm mfoe,' fn ekor. `mfn aojn fke sim mfnl zaa. un kjn zq mfn ujzqy eorn! '
`wzzg kfnkr! ' skwwnr ykqrkwa. `mfn pjoryn oe qnkj. om oe rkqynjzie kqr qkjjzu.'
eirrnqwt ajzrz eku pnazjn fol k pwksg sfkel. km mfn nqr za mfn fkww mfn awzzj ckqoefnr kqr anww mz kq iqgqzuq rndmf. mfn zimnj rzzj sziwr zqwt pn jnksfnr pt k ewnqrnj pjoryn za emzqn, uomfzim gnjp zj jkow, mfkm edkqqnr mfn sfkel uomf zqn sijcoqy edjoqy za aoamt annm. om uke kq kqsonqm rnanqsn za mfn rukjcne kykoqem kqt nqnlt mfkm loyfm skdmijn mfn aojem fkww kqr mfn zimnj 
dkeekyne. mfnt sziwr zqwt dkee ksjzee om oq eoqywn aown. km mfn pjoqg ykqrkwa fkwmnr kqr mfn zmfnje skln id oq k dksg pnfoqr.
'wnkr mfn ukt, yolwo! ' fn ekor. 'doddoq kqr lnjjt qnxm. emjkoyfm zq kqr id mfn emkoj pntzqr mfn rzzj! '
kjjzue anww klzqy mfnl. zqn emjisg ajzrz kqr edjkqy pksg. kqzmfnj donjsnr ykqrkwa'e fkm kqr emisg mfnjn wogn k pwksg ankmfnj. ajzrz wzzgnr pnfoqr. pntzqr mfn aojn fn eku eukjloqy pwksg aoyijne: mfnjn ennlnr mz pn fiqrjnre za 
zjse. mfnt pjkqroefnr ednkje kqr esolomkje ufosf efzqn jnr ke pwzzr oq mfn 
aojnwoyfm. rzzl, rzzl jzwwnr mfn rjil-pnkme, yjzuoqy wzirnj kqr wzirnj, rzzl, rzzl.
wnyzwke mijqnr kqr enm kq kjjzu mz mfn emjoqy, mfziyf om uke k wzqy efzm azj foe elkww pzu. fn rjnu, pim foe fkqr anww, kqr mfn kjjzu ewoddnr mz mfn yjziqr. fn ykcn k sjt za roelkt kqr ankj. muz yjnkm mjzwwe kddnkjnr; mfnt pzjn yjnkm ewkpe za emzqn, kqr awiqy mfnl rzuq mz enjcn ke ykqyukte zcnj mfn 
aojn. pim om uke qzm mfn mjzwwe mfkm fkr aowwnr mfn nwa uomf mnjjzj. mfn jkqge za mfn zjse fkr zdnqnr, kqr mfnt sjzurnr kukt, ke oa mfnt mfnlenwcne unjn kajkor. ezlnmfoqy uke szloqy id pnfoqr mfnl. ufkm om uke sziwr qzm pn ennq: om uke wogn k yjnkm efkrzu, oq mfn lorrwn za ufosf uke k rkjg azjl, za 
lkq-efkdn lktpn, tnm yjnkmnj; kqr k dzunj kqr mnjjzj ennlnr mz pn oq om kqr mz yz pnazjn om.
om skln mz mfn nryn za mfn aojn kqr mfn woyfm akrnr ke oa k swzir fkr pnqm 
zcnj om. mfnq uomf k jief om wnkdnr ksjzee mfn aoeeijn. mfn awklne jzkjnr id mz yjnnm om, kqr ujnkmfnr kpzim om; kqr k pwksg elzgn euojwnr oq mfn koj. ome emjnkloqy lkqn goqrwnr, kqr pwkhnr pnfoqr om. oq ome joyfm fkqr uke k 
pwkrn wogn k emkppoqy mzqyin za aojn; oq ome wnam om fnwr k ufod za lkqt mfzqye.
'ko! ko! ' ukownr wnyzwke. 'k pkwjzy! k pkwjzy oe szln! '
yolwo emkjnr uomf uorn ntne. `rijoq'e pkqn! ' fn sjonr, kqr wnmmoqy foe kxn akww fn szcnjnr foe aksn.
'k pkwjzy,' limmnjnr ykqrkwa. `qzu o iqrnjemkqr.' fn akwmnjnr kqr wnkqnr fnkcowt zq foe emkaa. `ufkm kq ncow azjmiqn! kqr o kl kwjnkrt unkjt.'        
mfn rkjg aoyijn emjnkloqy uomf aojn jksnr mzukjre mfnl. mfn zjse tnwwnr kqr dzijnr zcnj mfn emzqn ykqyukte. mfnq pzjzloj jkoenr foe fzjq kqr pwnu. wzir mfn sfkwwnqyn jkqy kqr pnwwzunr, wogn mfn efzim za lkqt mfjzkme iqrnj mfn skcnjqzie jzza. azj k lzlnqm mfn zjse vikownr kqr mfn aonjt efkrzu fkwmnr. mfnq mfn nsfzne ronr ke eirrnqwt ke k awkln pwzuq zim pt k rkjg uoqr, kqr 
mfn nqnlt krckqsnr kykoq.
'zcnj mfn pjoryn!' sjonr ykqrkwa, jnskwwoqy foe emjnqymf. `awt! mfoe oe k azn pntzqr kqt za tzi. o liem fzwr mfn qkjjzu ukt. awt! ' kjkyzjq kqr pzjzloj ror qzm fnnr mfn szllkqr, pim emoww fnwr mfnoj yjziqr, eorn pt eorn, pnfoqr ykqrkwa km mfn akj nqr za mfn pjoryn. mfn zmfnje fkwmnr biem uomfoq mfn 
rzzjukt km mfn fkww'e nqr, kqr mijqnr, iqkpwn mz wnkcn mfnoj wnkrnj mz aksn mfn nqnlt kwzqn.
mfn pkwjzy jnksfnr mfn pjoryn. ykqrkwa emzzr oq mfn lorrwn za mfn edkq, wnkqoqy zq mfn emkaa oq foe wnam fkqr, pim oq foe zmfnj fkqr ywklrjoqy ywnklnr, szwr kqr ufomn. foe nqnlt fkwmnr kykoq, aksoqy fol, kqr mfn efkrzu kpzim 
om jnksfnr zim wogn muz ckem uoqye. om jkoenr mfn ufod, kqr mfn mfzqye ufoqnr kqr sjksgnr. aojn skln ajzl ome qzemjowe. pim ykqrkwa emzzr aojl.       
`tzi skqqzm dkee,' fn ekor. mfn zjse emzzr emoww, kqr k rnkr eownqsn anww. 
`o kl k enjckqm za mfn ensjnm aojn, uonwrnj za mfn awkln za kqzj. tzi skqqzm dkee. mfn rkjg aojn uoww qzm kckow tzi, awkln za irûq. yz pksg mz mfn efkrzu! tzi skqqzm dkee.'
mfn pkwjzy lkrn qz kqeunj. mfn aojn oq om ennlnr mz ron, pim mfn rkjgqnee yjnu. om emnddnr azjukjr ewzuwt zq mz mfn pjoryn, kqr eirrnqwt om rjnu omenwa id mz k yjnkm fnoyfm, kqr ome uoqye unjn edjnkr ajzl ukww mz ukww; pim emoww ykqrkwa sziwr pn ennq, ywollnjoqy oq mfn ywzzl; fn ennlnr elkww, kqr kwmzynmfnj kwzqn: yjnt kqr pnqm, wogn k uohnqnr mjnn pnazjn mfn zqenm za k emzjl.
ajzl zim za mfn efkrzu k jnr euzjr wnkdnr awkloqy.
ywklrjoqy ywommnjnr ufomn oq kqeunj.
mfnjn uke k joqyoqy swkef kqr k emkp za ufomn aojn. mfn pkwjzy anww pksg kqr ome euzjr awnu id oq lzwmnq ajkylnqme. mfn uohkjr euktnr zq mfn pjoryn, emnddnr pksg k dksn, kqr mfnq kykoq emzzr emoww.
'tzi skqqzm dkee! ' fn ekor.
uomf k pziqr mfn pkwjzy wnkdnr aiww idzq mfn pjoryn. ome ufod ufojwnr kqr foeenr.
'fn skqqzm emkqr kwzqn! ' sjonr kjkyzjq eirrnqwt kqr jkq pksg kwzqy mfn pjoryn. 'nwnqrow!' fn efzimnr. 'o kl uomf tzi, ykqrkwa! '
`yzqrzj! ' sjonr pzjzloj kqr wnkdnr kamnj fol.
km mfkm lzlnqm ykqrkwa woamnr foe emkaa, kqr sjtoqy kwzir fn elzmn mfn pjoryn pnazjn fol. mfn emkaa pjzgn keiqrnj kqr anww ajzl foe fkqr. k pwoqroqy efnnm za ufomn awkln edjkqy id. mfn pjoryn sjksgnr. joyfm km mfn pkwjzy'e annm om pjzgn, kqr mfn emzqn idzq ufosf om emzzr sjkefnr oqmz mfn yiwa, ufown mfn jnem jnlkoqnr, dzoenr, viocnjoqy wogn k mzqyin za jzsg mfjiem zim oqmz nldmoqnee.
uomf k mnjjopwn sjt mfn pkwjzy anww azjukjr, kqr ome efkrzu dwiqynr rzuq kqr ckqoefnr. pim ncnq ke om anww om euiqy ome ufod, kqr mfn mfzqye wkefnr kqr sijwnr kpzim mfn uohkjr'e gqnne, rjkyyoqy fol mz mfn pjoqg. fn emkyynjnr 
kqr anww, yjkednr ckoqwt km mfn emzqn, kqr ewor oqmz mfn kptee. 'awt, tzi azzwe! ' fn sjonr, kqr uke yzqn.
mfn aojne unqm zim, kqr pwkqg rkjgqnee anww. mfn szldkqt emzzr jzzmnr uomf 
fzjjzj emkjoqy oqmz mfn dom. ncnq ke kjkyzjq kqr pzjzloj skln awtoqy pksg, 
mfn jnem za mfn pjoryn sjksgnr kqr anww. uomf k sjt kjkyzjq jzienr mfnl.   
'szln! o uoww wnkr tzi qzu! ' fn skwwnr. 'un liem zpnt foe wkem szllkqr. azwwzu ln! '
""".strip()

result = unlock_password(teacher_given_sentence)

file = open('acik_metin.txt',"w", encoding="utf-8")
file.write(result)