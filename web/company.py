from bs4 import BeautifulSoup

html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
    <tr>
        <th>대표</th>
        <td>김길동</td>
        <td>홍길동</td>
        <td>박길동</td>
    </tr>
</table>
'''

companies = {}
data = {}
soup = BeautifulSoup(html, 'html.parser')
trs = soup.select('tr')

for i, tr in enumerate(trs):
    # print(i, tr)
    if i == 0:
        for j, th in enumerate(tr.select('th')):
            if j == 0: continue
            companies[th.text] = j - 1
        
    else:
        item = tr.select_one('th').text
        l = []
        for td in tr.select('td'):
            l.append(td.text)

        data[item] = l

print(companies)
print(data)

while True:
    inputValue = input("회사와 항목을 입력하세요(끝:q)> ")
    if inputValue == 'q':
        break

    inputValues = inputValue.split(' ')
    company = inputValues[0]
    itemName = inputValues[1]

    idx = companies[company]
    print("결과는", data[itemName][idx])

데이터 아이템네임의 idx의 첫번째값