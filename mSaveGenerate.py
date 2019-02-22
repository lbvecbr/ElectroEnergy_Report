import re
from datetime import datetime
from docxtpl import DocxTemplate


def save_generate_(window):
    active_energy = re.compile(r'(38.\d\d\s[\w№]*)\s+.*[\n]?Обсяг споживання \* тариф\s*=\s*(-*\d+)')
    mon = re.compile(r'від (\d\d)\.(\d\d)\.(20\d\d)')

    date = datetime.now()
    months = ['', 'січень', 'лютий', 'березень', 'квітень', 'травень', 'червень',
              'липень', 'серпень', 'вересень', 'жовтень', 'листопад', 'грудень']

    months1 = ['', 'січня', 'лютого', 'березня', 'квітня', 'травня', 'червня',
               'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']

    text = window.textEdit.toPlainText()
    listOfStrigs = text.split('\n')
    dic = dict()
    rezult_dic = {}
    summa = 0
    for K in listOfStrigs:
        m = active_energy.match(K)
        month = mon.match(K)
        if month is not None:
            year = month.group(3)
            month = month.group(2)
            if month[0] == '0':
                month = month[1]
            month = months[int(month)]
            rezult_dic.update({'month': month})
            rezult_dic.update({'year': year})
        if m:
            key = m.group(1)
            value = m.group(2)
            if key not in dic.keys():
                dic.update({key: list()})
                dic[key].append(int(value))
            else:
                dic[key].append(int(value))

    for key, value in dic.items():
        print(key + ': ' + str(value) + '      ' + str(sum(value)))
        print(rezult_dic['month'])

    for key in dic.keys():
        summa += sum(dic[key])
    print(summa + 50)

    if sum(dic['38.04 Мехмайстерня']) > 1500:
        mtf = (sum(dic['38.04 Мехмайстерня']) + sum(dic['38.02 МТФ№1'])) - 1000
        mehmasterna = 600
        avtogarag = 400
    else:
        mtf = sum(dic['38.02 МТФ№1'])
        mehmasterna = int(sum(dic['38.04 Мехмайстерня']) / 100 * 60)
        avtogarag = sum(dic['38.04 Мехмайстерня']) - mehmasterna
    molodnak = int((mtf / 100) * 15)
    mtf -= molodnak
    komplex = int(sum(dic['38.01 Комплекс']) / 100 * 30)
    oil_sep = sum(dic['38.01 Комплекс']) - komplex
    sep_punkt = int(oil_sep / 100 * 70)
    oil = oil_sep - sep_punkt
    kladova = int(sum(dic['38.10 Зерносклад']) / 100 * 85)
    zernosklad_ternove = sum(dic['38.10 Зерносклад']) - kladova

    rezult_dic.update({
        'trbr1': sum(dic['38.05 Тракторна']),
        'trbr3': sum(dic['38.11 Гаражи']),
        'tik': sum(dic['38.03 Мехток']),
        'kompl': komplex,
        'mtf': mtf,
        'molodn': molodnak,
        'stf': sum(dic['38.09 СТФ']),
        'budceh': sum(dic['38.07 Будцех']),
        'separat': sep_punkt,
        'oil': oil,
        'mehm': mehmasterna,
        'garage': avtogarag,
        'zertern': zernosklad_ternove,
        'kladov': kladova,
        'kontora': sum(dic['38.15 виробничі']),
        'lotok': 50,
    })

    roslinnictvo = rezult_dic['trbr1'] + rezult_dic['trbr3'] + \
                   rezult_dic['tik'] + rezult_dic['kompl']
    tvarinnictvo = rezult_dic['mtf'] + rezult_dic['molodn'] + rezult_dic['stf']

    dopomijni = rezult_dic['budceh'] + rezult_dic['separat'] + rezult_dic['oil'] + \
                rezult_dic['mehm'] + rezult_dic['garage'] + rezult_dic['zertern'] + \
                rezult_dic['kladov'] + rezult_dic['kontora'] + rezult_dic['lotok']

    razom = roslinnictvo + tvarinnictvo + dopomijni

    temp_dic = {
        'rosl': roslinnictvo,
        'tvar': tvarinnictvo,
        'dopom': dopomijni,
        'razom': razom
    }

    rezult_dic.update(temp_dic)

    print(rezult_dic)

    doc = DocxTemplate('report_electro_template.docx')
    context = rezult_dic
    doc.render(context)
    doc.save('generated.docx')
