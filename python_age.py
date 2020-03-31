text = input('年齢は？')
if text.isdigit():
    age = int(text)
    if age < 20:
        if 6 <= age and age <= 15:
            print('未成年(義務教育)')
        else:
            print('未成年')
    elif age < 65:
        print('成人')
    else:
        print('高齢者')
else:
    print('数字を入れろよデコスケ野郎')
