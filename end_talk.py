import hgtk
def 두음(a):
    if a[0] == 'ㄹ'or a[0] =='ㄴ':
        if a[1] in ('ㅏ', 'ㅑ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅖ', 'ㅟ', 'ㅐ'):
            if a[0] == 'ㄹ':
                if a[1] in ('ㅏ','ㅐ','ㅗ','ㅜ','ㅡ'):
                    return 'ㄴ'
                if a[1] in ('ㅑ','ㅕ','ㅛ','ㅠ','ㅣ'):
                    return 'ㅇ'
            if a[0] == 'ㄴ':
                if a[1] in ('ㅕ','ㅛ','ㅠ','ㅣ'):
                    return 'o'
    return a[0]
        
        
def word_linkgame(a, b, c):
    msgs=[]
    word=''
    player=[a, b]
    print("처음 단어를 적어주세요.\n")
    msgs.append(input())
    player.reverse()
    while 1:
        if c==True:
            n=list(두음(list(hgtk.letter.decompose(msgs[len(msgs)-1][-1]))))
            word=list(hgtk.letter.decompose(msgs[len(msgs)-1][-1]))
            word[0]=n[0]
            print(word)
            word=hgtk.letter.compose(tuple(word))
            if n == True:
                print("두음 법칙이 적용됬습니다.")
            print("\n{0}님은 {1}로 시작하는 단어를 적어주세요.\n".format(player[0], word))
            x=input()
        else:
            print("\n{0}님은 {1}로 시작하는 단어를 적어주세요.\n".format(player[0], msgs[len(msgs)-1][-1]))
            x=input()
        if x in msgs:
            print("\n이미 말한 단어 입니다.\n")
            break
        if x[0] != msgs[len(msgs)-1][-1] or x[0] != word:
            print("\n끝말을 잇지 못했습니다.\n")
            break
        print("\n{0}님이 적으신 단어는 {1}입니다.\n".format(player[0], x))
        msgs.append(x)
        player.reverse()
    print("{0}님이 끝말잇기를 승리하셨습니다.\n".format(player[0]))
    return
while 1:
    wordof=False
    if "끝말잇기 시작"==input():
        x=input("두음 법칙을 적용하실려면 적용 아니라면 아니요를 적어주세요: \n")
        if "적용"==x:
            print("두음 법칙 적용이 됩니다.\n")
            wordok=True
        elif "아니요"==x:
            print("두음 법칙 적용이 안됩니다.\n")
            wordok=False
        else:
            print("적용확인이 실패하였습니다.\n")
        c=word_linkgame(input("1번째로 플레이 하실분 이름을 적어주세요: "),input("2번째로 플레이 하실분 이름을 적어주세요: "),wordok)
        print(c)
        break