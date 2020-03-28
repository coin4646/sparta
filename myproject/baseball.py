#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
	## 여기에 코딩을 해주세요
    dict = {}
    for i in a_list:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] = dict[i] + 1
    return dict

#결과값
print(count_list(a))

#아래와 같이 출력됩니다
{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}