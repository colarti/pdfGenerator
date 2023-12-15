from fpdf import FPDF
import pandas

# Orientation = P/L = Portrait/Landscape
# unit = size = mm = millimeter
# format = paper size = A4 paper
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_font(family='Times', style='B', size=24)    #this will applied to everthing below, until a new set_font

df = pandas.read_csv('topics.csv')
# print(df)

for idx, data in df.iterrows():
    # print(f'idx:{idx}    Topic:{data["Topic"]}   Pages:{data["Pages"]}')

    for x in range(data['Pages']):
        if x == 0:
            pdf.add_page()
            pdf.cell(w=0, h=24, txt=data["Topic"], align='L', ln=1, border=0) #w-width 0:full page width, x>0, will be mm length, h-height, align-Left side, Right side, border-1-shows/0-empty, ln-breakline, number of returns
        else:
            pdf.add_page()





# pdf.set_font(family='Times', size=10)    #this will applied to everthing below, until a new set_font
# pdf.cell(w=0, h=12, txt='Hi There', align='R', ln=1, border=1)

pdf.output('output.pdf')