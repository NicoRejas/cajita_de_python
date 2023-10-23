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
div_01_00 = ET.SubElement(td_05, 'div', {'class': 'movableContent', 
                                         'style': 'border: 0px; padding-top: 0px; position: relative;'})
table_05 = ET.SubElement(div_01_00, 'table', {'width': '100%', 
                                          'border': '0', 
                                          'cellspacing': '0', 
                                          'cellpadding': '0'})
tbody_05 = ET.SubElement(table_05, 'tbody')
tr_05_1 = ET.SubElement(tbody_05, 'tr')
td_06 = ET.SubElement(tr_05_1,'td', height="35")

tr_05_2 = ET.SubElement(tbody_05, 'tr')
td_07 = ET.SubElement(tr_05_2,'td')
table_06 = ET.SubElement(td_07, 'table', {'width': '100%', 
                                          'border': '0', 
                                          'cellspacing': '0', 
                                          'cellpadding': '0'})
tbody_06 = ET.SubElement(table_06, 'tbody')
tr_08 = ET.SubElement(tbody_06, 'tr')
td_08_00 = ET.SubElement(tr_08, 'td', {'valign': 'top', 'align': 'center', 'class': 'specbundle'})
div_02 = ET.SubElement(td_08_00, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_03 = ET.SubElement(div_02, 'div', {'class': 'contentEditable'})
p_01 = ET.SubElement(div_03, 'p', {'style': 'text-align:center;margin:0;font-family:Georgia,Time,sans-serif;font-size:26px;color:#222222;'})
span_01 = ET.SubElement(p_01, 'span', {'class': 'specbundle2'})
span_02 = ET.SubElement(span_01, 'span', {'class': 'font1'})
span_02.text = 'Zonda Alert Email' ############# ACA SE EDITA!!!!!

td_08_01 = ET.SubElement(tr_08, 'td', {'valign': 'top', 'class': 'specbundle'})
div_04 = ET.SubElement(td_08_01, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_05 = ET.SubElement(div_04, 'div', {'class': 'contentEditable'})
p_02 = ET.SubElement(div_05, 'p', {'style': 'text-align:center;margin:0;font-family:Georgia,Time,sans-serif;font-size:26px;color:#DC2828;'})
span_03 = ET.SubElement(p_02, 'span', {'class': 'font'})
span_03.text = 'Data Engineering Team' ############# ACA SE EDITA!!!!!

div_01_01 = ET.SubElement(td_05, 'div', {'class': 'movableContent', 
                                         'style': 'border: 0px; padding-top: 0px; position: relative;'})
table_07 = ET.SubElement(div_01_01, 'table', {'width': '100%', 
                                          'border': '0', 
                                          'cellspacing': '0', 
                                          'cellpadding': '0'})
tr_09 = ET.SubElement(table_07, 'tr')
td_08 = ET.SubElement(tr_09, 'td', {'valign': 'top', 'align': 'center'})
div_06 = ET.SubElement(td_08, 'div', {'class': 'contentEditableContainer contentImageEditable'})

div_07 = ET.SubElement(div_06,'div', {'class': 'contentEditable'})
comment_1 = ET.Comment(" <img th:src=\"@{images/test.png}\"/>")
div_07.append(comment_1)
hr_01 = ET.Element('hr', {'size': '3', 'color': '#DC2828'})
div_07.append(hr_01)
comment_2 = ET.Comment(" <img src=\"ATT00001.png\" th:src=\"|cid:${logo}|\"/>")
div_07.append(comment_2)
comment_3 = ET.Comment(" <img src=\"ATT00001\" th:src=\"|cid:${logo}|\"/>")
div_07.append(comment_3)
comment_4 = ET.Comment(" <img th:src=\"|cid:${logo}|\"/>")
div_07.append(comment_4)
comment_5 = ET.Comment(" <img src=\"ATT00001.png\" width='251' height='43' alt='' data-default=\"placeholder\" data-max-width=\"560\">")
div_07.append(comment_5)
comment_6 = ET.Comment(" <img src=\"images/line.png\" width='251' height='43' alt='' data-default=\"placeholder\" data-max-width=\"560\">")
div_07.append(comment_6)
hr_02 = ET.Element('hr', {'size': '3', 'color': '#DC2828'})
div_07.append(hr_02)
comment_7 = ET.Comment(" <img th:src=\"|cid:${logo}|\"/>")
div_07.append(comment_7)

div_01_02 = ET.SubElement(td_05, 'div', {'class': 'movableContent', 
                                         'style': 'border: 0px; padding-top: 0px; position: relative;'})
table_08 = ET.SubElement(div_01_02, 'table', {'width': '100%', 
                                              'border': '0', 
                                              'cellspacing': '0', 
                                              'cellpadding': '0',
                                              'align': 'center'})
tr_10_00 = ET.SubElement(table_08, 'tr')
td_09 = ET.SubElement(tr_10_00, 'td', height="1")
tr_10_01 = ET.SubElement(table_08, 'tr')
td_10 = ET.SubElement(tr_10_01, 'td', align='left')
div_08 = ET.SubElement(td_10, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_09 = ET.SubElement(div_08, 'div', {'class': 'contentEditable', 'align': 'center'})
h2_01 = ET.SubElement(div_09, 'h2', {'th:text': '${title}'})
tr_10_02 = ET.SubElement(table_08, 'tr')
td_10 = ET.SubElement(tr_10_02, 'td', height="2")
tr_10_03 = ET.SubElement(table_08, 'tr', {'th:if': '${message}'})
td_11 = ET.SubElement(tr_10_03, 'td', align='left')
div_10 = ET.SubElement(td_11, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_11 = ET.SubElement(div_10, 'div', {'class': 'contentEditable', 'align': 'center'})
p_03 = ET.SubElement(div_11, 'p', {'th:utext': "${#strings.replace( #strings.escapeXml( message ),T(java.lang.System).getProperty('line.separator'),'&lt;br /&gt;')}"})

tr_10_04 = ET.SubElement(table_08, 'tr')
td_12 = ET.SubElement(tr_10_04, 'td', height='25')

tr_10_05 = ET.SubElement(table_08, 'tr')
td_13 = ET.SubElement(tr_10_05, 'td', style='border-bottom:1px solid #DDDDDD;')

tr_10_06 = ET.SubElement(table_08, 'tr')
td_14 = ET.SubElement(tr_10_06, 'td', height='25')

tr_10_07 = ET.SubElement(table_08, 'tr')
td_15 = ET.SubElement(tr_10_07, 'td', align='left')
div_12 = ET.SubElement(td_15, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_13 = ET.SubElement(div_12, 'div', {'class': 'contentEditable', 'align': 'center'})
p_text_01_div_13 = ET.SubElement(div_13, 'text')
p_text_01_div_13.text = "Have questions? Get in touch with us via Slack or email. Please don't hesitate to reach us. Meanwhile, you can check out our " #### ACA SE EDITA
a_div_13 = ET.SubElement(p_text_01_div_13, 'a', {'target': 'https://xxxxxxxxxxxxxxxx', 'href': 'https://xxxxxxxxxxxxxxxx', 'class': 'link1'}) #### ACA SE EDITA
a_div_13.text = 'Confluence Page'
br_element1 = ET.SubElement(p_text_01_div_13, 'br')
br_element2 = ET.SubElement(p_text_01_div_13, 'br')
p_text_02_div_13 = ET.SubElement(p_text_01_div_13, 'text')
p_text_02_div_13.text = "Cheers,"
br_element3 = ET.SubElement(p_text_01_div_13, 'br')
span_04 = ET.SubElement(p_text_01_div_13, 'span', {'style': 'color:#222222;'})
span_04.text = 'DE Team'

div_01_03 = ET.SubElement(td_05, 'div', {'class': 'movableContent', 
                                         'style': 'border: 0px; padding-top: 0px; position: relative;'})
table_09 = ET.SubElement(div_01_03, 'table', width="100%", border="0", cellspacing="0", cellpadding="0")
tbody_07 = ET.SubElement(table_09, 'tbody')
tr_11_0 = ET.SubElement(tbody_07,'tr')
td_16 = ET.SubElement(tr_11_0, 'td', height='25')

tr_11_1 = ET.SubElement(tbody_07,'tr')
td_17 = ET.SubElement(tr_11_1, 'td', style='border-bottom:1px solid #DDDDDD;')

tr_11_2 = ET.SubElement(tbody_07,'tr')
td_18 = ET.SubElement(tr_11_2, 'td', height='25')

tr_11_3 = ET.SubElement(tbody_07,'tr')
td_19 = ET.SubElement(tr_11_3, 'td')
table_10 = ET.SubElement(td_19, 'table', {'width': '100%', 'border': '0', 'cellspacing': '0', 'cellpadding': '0'})
tbody_08 = ET.SubElement(table_10, 'tbody')
tr_12 = ET.SubElement(tbody_08, 'tr')

td_20_0 = ET.SubElement(tr_12, 'td', {'valign': 'top', 'class':'specbundle'})
div_14 = ET.SubElement(td_20_0, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_15 = ET.SubElement(div_14, 'div', {'class': 'contentEditable', 'align': 'center'})
p_text_01_div_15 = ET.SubElement(div_15,'p', {'style': 'text-align:left;color:#CCCCCC;font-size:12px;font-weight:normal;line-height:20px;'})
span_05 = ET.SubElement(p_text_01_div_15, 'span', {'style': 'font-weight:bold;'})
span_05.text = '[XXXXXXXX]'
br_element4 = ET.SubElement(p_text_01_div_15, 'br')
data_text = ET.Element('text')
data_text.text = '[DATA]'
p_text_01_div_15.append(data_text)
br_element5 = ET.SubElement(p_text_01_div_15, 'br')
a_div_15 = ET.SubElement(p_text_01_div_15, 'a', {'target': '_blank', 'class': 'link1', 'href': 'mailto:xxxxxxxxxxx@xxxxxxxxx.com'})
a_div_15.text = 'dxxxxxxxxg@xxxxxxxxx.com.ar'

td_20_1 = ET.SubElement(tr_12, 'td', {'valign': 'top', 'width': '30', 'class': 'specbundle'})
td_20_1.text = "&nbsp;"

td_20_2 = ET.SubElement(tr_12, 'td', {'valign': 'top', 'class': 'specbundle'})
table_11 = ET.SubElement(td_20_2, 'table', width="100%", border="0", cellspacing="0", cellpadding="0")
tbody_09 = ET.SubElement(table_11, 'tbody')
tr_13 = ET.SubElement(tbody_09, 'tr')

td_21_0 = ET.SubElement(tr_13, 'td', valign='top', width='52') #Linea 225
div_16 = ET.SubElement(td_21_0, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_17 = ET.SubElement(div_14, 'div', {'class': 'contentEditable', 'align': 'center'})
td_21_1 = ET.SubElement(tr_13, 'td', valign='top', width='16')
td_21_1.text = "&nbsp;"
td_21_2 = ET.SubElement(tr_13, 'td', valign='top', width='52')
div_18 = ET.SubElement(td_21_2, 'div', {'class': 'contentEditableContainer contentTextEditable'})
div_19 = ET.SubElement(div_18, 'div', {'class': 'contentEditable', 'align': 'center'})

tr_11_4 = ET.SubElement(tbody_07,'tr')
td_22 = ET.SubElement(tr_11_4,'td', height='88')
comment_footer = ET.Comment(" =============================== Footer ====================================== ")
div_01_03.append(comment_footer)

mensaje = ET.SubElement(tbody_04, 'p')
mensaje.text = 'Este es un mensaje de ejemplo en tbody_04'

td_03_1 = ET.SubElement(tr_03, 'td', {'valign': 'top', 'width': '40'})
td_03_1.text = "&nbsp;"

# Crear el árbol ElementTree
tree = ET.ElementTree(html)

# Guardar el archivo HTML
with open('mail.html', 'wb') as file:
    tree.write(file , encoding='utf-8', xml_declaration=True)
