menber = []
results_chinese = []
results_math = []
results_english = []
menber_results = dict()
input_students_number = int(input('本程序未内置学生，需要手动添加学生和成绩，请输入学生的数量'))
for each in range(input_students_number):
    studen_name = str(input('输入学生名字'))
    menber.append(studen_name)
    studen_chinese_results = float(input('输入语文成绩'))
    results_chinese.append(studen_chinese_results)
    studen_math_results = float(input('输入数学成绩'))
    results_math.append(studen_math_results)
    studen_english_results = float(input('输入英语成绩'))
    results_english.append(studen_english_results)
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
