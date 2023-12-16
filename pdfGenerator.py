from fpdf import FPDF
import pandas


# Orientation = P/L = Portrait/Landscape
# unit = size = mm = millimeter
# format = paper size = A4 paper
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


df = pandas.read_csv('topics.csv')
# print(df)

cnt = 0
for idx, data in df.iterrows():
    # print(f'idx:{idx}    Topic:{data["Topic"]}   Pages:{data["Pages"]}')

    for x in range(data['Pages']):
        if x == 0:
            pdf.add_page()
            cnt+=1
            pdf.set_text_color(0, 0, 0)
            pdf.set_font(family='Times', style='B', size=24)    #this will applied to everthing below, until a new set_font
            pdf.cell(w=0, h=15, txt=data["Topic"], align='L', ln=1, border=0) #w-width 0:full page width, x>0, will be mm length, h-height, align-Left side, Right side, border-1-shows/0-empty, ln-breakline, number of returns
            pdf.line(10, 25, 200, 25)

            line = 25 #start from line 25mm (contains a header)
            for p in range(24):
                line += 10 #add 100mm
                pdf.line(10, line, 200, line) #generate a new line
            
            pdf.ln(246) #mv cursor to the footer

        else:
            pdf.add_page()
            cnt+=1
            
            line = 5    #start from line 5mm
            for p in range(26):
                line += 10  # add 10mm
                pdf.line(10, line, 200, line)   #generate a new line
            
            pdf.ln(260) #mv cursor to the footer
        
        # on every page, go to the footer and include the Topic
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family='Times', style='I', size=8)    #this will applied to everthing below, until a new set_font
        pdf.cell(w=0, h=8, txt=f"{data['Topic']}", align='R', ln=1, border=0) #w-width 0:full page width, x>0, will be mm length, h-height, align-Left side, Right side, border-1-shows/0-empty, ln-breakline, number of returns
        pdf.cell(w=0, h=8, txt=f"{cnt}", align='R', ln=1, border=0) #w-width 0:full page width, x>0, will be mm length, h-height, align-Left side, Right side, border-1-shows/0-empty, ln-breakline, number of returns

pdf.output('output.pdf')