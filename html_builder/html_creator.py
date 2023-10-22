from xml.etree import ElementTree as ET

# Crear el elemento raíz 'html'
html = ET.Element('html')
html.set('xmlns:th', 'http://www.thymeleaf.org')

# Crear el elemento 'head'
head = ET.SubElement(html, 'head')

# Crear el elemento 'meta' dentro de 'head'
meta = ET.SubElement(head, 'meta')
meta.set('http-equiv', 'Content-Type')
meta.set('content', 'text/html; charset=utf-8')

# Crear el elemento 'title' dentro de 'head'
title = ET.SubElement(head, 'title')
title.text = '[SUBJECT]'

# Crear el elemento 'style' dentro de 'head'
#style = ET.SubElement(head, 'style')
#style.set('type', 'text/css')

# Crear el elemento 'script' dentro de 'head'
script = ET.SubElement(head, 'script')
script.set('type', 'colorScheme')
script.set('class', 'swatch active')
script.text = '''{
    "name":"Default",
    "bgBody":"ffffff",
    "link":"382F2E",
    "color":"999999",
    "bgItem":"ffffff",
    "title":"222222"
}'''

# Crear el elemento 'body'

body = ET.SubElement(html, 'body', {
    'paddingwidth': '0',
    'paddingheight': '0',
    'style': 'padding-top: 0; padding-bottom: 0; padding-top: 0; padding-bottom: 0; background-repeat: repeat; width: 100% !important; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased;',
    'offset': '0',
    'toppadding': '0',
    'leftpadding': '0'
})

mensaje = ET.SubElement(body, 'p')
mensaje.text = 'Este es un mensaje de ejemplo en body.'

table_01 = ET.SubElement(body, 'table', {
                                'gcolor':'#ffffff',
                                'width':'100%',
                                'border':'0',
                                'cellspacing':'0',
                                'cellpadding':'0',
                                'class':'tableContent', 
                                'align':'center',
                                'style':'font-family:Helvetica, Arial,serif;'})
mensaje = ET.SubElement(table_01, 'p')
mensaje.text = 'Este es un mensaje de ejemplo en tabla_1.'

tbody_01 = ET.SubElement(table_01, 'tbody')
tr_01 = ET.SubElement(tbody_01, 'tr')
td_01 = ET.SubElement(tr_01, 'td')
table_02 = ET.SubElement(td_01, 'table', {'width': '600',
                                        'border': '0', 
                                        'cellspacing': '0', 
                                        'cellpadding': '0', 
                                        'align': 'center', 
                                        'bgcolor': '#ffffff',
                                    'class': 'MainContainer'})
tbody_02 = ET.SubElement(table_02, 'tbody')
tr_02 = ET.SubElement(tbody_02, 'tr')
td_02 = ET.SubElement(tr_02, 'td')

table_03 = ET.SubElement(td_02, 'table', {'width': '100%', 
                                          'border': '0', 
                                          'cellspacing': '0', 
                                          'cellpadding': '0'})
tbody_03 = ET.SubElement(table_03, 'tbody')
tr_03 = ET.SubElement(tbody_03, 'tr')
td_03 = ET.SubElement(tr_03, 'td', {'valign': 'top', 'width': '40'})
td_03.text = "&nbsp;"
td_04 = ET.SubElement(tr_03, 'td')
table_04 = ET.SubElement(td_04, 'table', {'width': '100%', 
                                          'border': '0', 
                                          'cellspacing': '0', 
                                          'cellpadding': '0'})
tbody_04 = ET.SubElement(table_04, 'tbody')
comment_header = ET.Comment(" =============================== Header ====================================== ")
tbody_04.append(comment_header)
tr_04_0 = ET.SubElement(table_04, 'tr')
td_05 = ET.SubElement(tr_04_0, 'td',{'height': '30', 'class': 'spechide'})
comment_body = ET.Comment(" =============================== Body ====================================== ")
td_05.append(comment_body)
tr_04_1 = ET.SubElement(table_04, 'tr')
td_05 = ET.SubElement(tr_04_1, 'td',{'class': 'movableContentContainer ', 'valign': 'top'})



mensaje = ET.SubElement(tbody_04, 'p')
mensaje.text = 'Este es un mensaje de ejemplo en tbody_04'

td_03_1 = ET.SubElement(tr_03, 'td', {'valign': 'top', 'width': '40'})
td_03_1.text = "&nbsp;"





# Crear el árbol ElementTree
tree = ET.ElementTree(html)

# Guardar el archivo HTML
with open('output.html', 'wb') as file:
    tree.write('mail.html', encoding='utf-8', xml_declaration=True)
