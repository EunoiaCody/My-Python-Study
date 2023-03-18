menber = [
    '小红','小明','小聪','小杰','小光','小坤','小东',
    '小智','小琪','小可','小艺','小菜','小美','小帅',
    '小卡拉米','丧彪','佛波勒','李白','鲁迅','唐三',
    '小舞','小黑','梁志超','特朗普','拜登','鸣人',
    '佐助','刻晴','钟离','魈','一斗','心海','哈利波特'
    ,'伏地魔','jojo','波奇酱','伊蕾娜','绫华','派蒙'
    ,'琪亚娜'
]
results_chinese = [
    46,99,32,47,18,92,85,70,87,50,42,39,63,75,50,
    53,5,57,4,42,19,34,84,28,17,41,4,98,65,52,35,
    16,89,30,57,85,16,59,24,42
]
results_math = [
    98,3,28,73,17,34,91,66,65,85,62,47,75,44,45,
    65,82,44,28,97,68,85,97,45,49,98,91,92,41,1,
    42,75,92,88,69,71,27,87,28,66
]
results_english = [
    26,67,72,67,80,75,94,3,6,76,75,9,7,2,23,97,
    75,15,13,87,17,72,35,19,1,27,10,3,66,1,50,
    16,31,79,86,73,77,21,70,21
]
menber_results = dict()
for i in range (len(menber)):
    results = {
        '语文':results_chinese[i],
        '数学':results_math[i],
        '英语':results_english[i]
    }
    menber_results[menber[i]] = results
kind = int(input('查询学生成绩，查询科目成绩，（1，2）'))
if kind == 1:
    results_name = input('输入你想查询的学生')
    search_results = menber_results.get(results_name,'未查询到该学生')
    print('TA的成绩是',search_results)
    print('TA的总分是',{search_results['语文']+search_results['数学']+search_results['英语']})
elif kind == 2:
    kind_subject_type = int(input('查询科目总分，最高分，最低分，平均分（1，2，3，4）'))
    if kind_subject_type == 1:
        all_score = 0
        kind_subject = int(input('语文数学还是英语（1，2，3）'))
        if kind_subject == 1:
            for i in range(len(results_chinese)):
                all_score = all_score + results_chinese[i]
            print('语文的总分是',all_score)
        elif kind_subject == 2:
            for i in range(len(results_math)):
                all_score = all_score + results_math[i]
            print('数学的总分是',all_score)
        elif kind_subject == 3:
            for i in range(len(results_english)):
                all_score = all_score + results_english[i]
            print('英语的总分是',all_score)
    elif kind_subject_type == 2:
        highest_score = 0
        kind_subject = int(input('语文数学还是英语（1，2，3）'))
        if kind_subject == 1:
            for i in range(len(results_chinese)):
                i = results_chinese[i]
                if highest_score > i:
                    highest_score = highest_score
                elif highest_score == i:
                    highest_score = highest_score
                elif highest_score < i:
                    highest_score = i
            print('语文的最高分是',highest_score)
        elif kind_subject == 2:
            for i in range(len(results_math)):
                i = results_math[i]
                if highest_score > i:
                    highest_score = highest_score
                elif highest_score == i:
                    highest_score = highest_score
                elif highest_score < i:
                    highest_score = i
            print('数学的最高分是',highest_score)
        elif kind_subject == 3:
            for i in range(len(results_english)):
                i = results_english[i]
                if highest_score > i:
                    highest_score = highest_score
                elif highest_score == i:
                    highest_score = highest_score
                elif highest_score < i:
                    highest_score = i
            print('英语的最高分是',highest_score)
    elif kind_subject_type == 3:
        i = results_chinese[0]
        lowest_score = results_chinese[0]
        kind_subject = int(input('语文数学还是英语（1，2，3）'))
        if kind_subject == 1:
            for i in range(len(results_chinese)):
                i = results_chinese[i]
                if lowest_score < i:
                    lowest_score = lowest_score
                elif lowest_score == i:
                    lowest_score = lowest_score
                elif lowest_score > i:
                    lowest_score = i
            print('语文的最低分是',lowest_score)
        elif kind_subject == 2:
            for i in range(len(results_math)):
                i = results_math[i]
                if lowest_score < i:
                    lowest_score = lowest_score
                elif lowest_score == i:
                    lowest_score = lowest_score
                elif lowest_score > i:
                    lowest_score = i
            print('数学的最低分是',lowest_score)
        elif kind_subject == 3:
            for i in range(len(results_english)):
                i = results_english[i]
                if lowest_score < i:
                    lowest_score = lowest_score
                elif lowest_score == i:
                    lowest_score = lowest_score
                elif lowest_score > i:
                    lowest_score = i
            print('英语的最低分是',lowest_score)
    elif kind_subject_type == 4:
        kind_subject = int(input('语文数学还是英语（1，2，3）'))
        all_score = 0
        if kind_subject == 1:
            for i in range(len(results_chinese)):
                all_score += results_chinese[i]
            final = round(all_score/(len(results_chinese)),2)
            print(f'语文平均分是{final}')
        elif kind_subject == 2:
            for i in range(len(results_math)):
                all_score += results_math[i]
            final = round(all_score/(len(results_math)),2)
            print(f'数学平均分是{final}')
        elif kind_subject == 3:
            for i in range(len(results_english)):
                all_score += results_english[i]
            final = round(all_score/(len(results_english)),2)
            print(f'英语平均分是{final}')
