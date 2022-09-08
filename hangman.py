def guess_next_letter(pattern, used_letters=[], word_list=['about', 'cboud', 'anoad']):
    l = len(pattern)
    patternIndex = [] #记录下线先索引
    latterIndex = {} #记录字母索引
    possibleAlphabet = {} #可能的出现的下一个字母列表 ，key字母，值为出现次数

    for index in range(l):
        if pattern[index] == "_":
            patternIndex.append(index)
        else:
            latterIndex[index] = pattern[index]

    for word in word_list:
        if len(word) != l:
            continue
        else:
            flag = True
            #匹配非下滑线位置，如果不批配跳过
            for index in latterIndex:
                if word[index] != latterIndex[index]:
                    flag = False
                    break

            if flag:
                #保存可能出现的字符列表，并记录出现次数
                for index in patternIndex:
                    if word[index] in possibleAlphabet:
                        possibleAlphabet[word[index]] += 1
                    else:
                        possibleAlphabet[word[index]] = 1

    maxNum = ""
    #找出出现次数最多字母
    for index in possibleAlphabet:
        if maxNum == "":
            maxNum = index
        if possibleAlphabet[index] > possibleAlphabet[maxNum]:
            maxNum = index

    return maxNum


def test_function_should_return_something():
    pattern = "____d"
    used_letters = list("abcde")
    word_list = ['about', 'fboud', 'cnoad']
    x = guess_next_letter(pattern, used_letters, word_list)
    print(x)


test_function_should_return_something()
