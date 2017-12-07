import sys
import json

fonte = sys.argv[1]

with open('cores.json', 'r') as tema:
    cores = json.load(tema)

print('<meta charset="UTF-8">')
print('<div style="font-family:Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New, monospace;">') 

with open(fonte, 'r') as arquivo:
    for linha in arquivo:
        comment = ''
        label = ''
        mnemonic = ''
        arg = ''

        if ';' in linha:
            elems = linha.split(';')
            if len(elems) == 1:
                # A linha é só um comentário
                comment = elems[0]
            else:
                cmd, comment = elems
                cmd = cmd.split()
        else:
            cmd = linha.split()

        if len(cmd) > 0:
            arg = cmd[-1]
            mnemonic = cmd[-2]
        if len(cmd) > 2:
            label = cmd[0]

        if label:
            print('<span style="color:{}; ">{}</span>'.format(cores['label'], label), end='')
        if mnemonic:
            padding = '&nbsp;'*(12 - len(label))
            print(padding+'<span style="color:{}; ">{}</span> '.format(cores['mnemonic'], mnemonic), end='')
        if arg:
            print('<span style="color:{}; ">{}</span>'.format(cores['arg'], arg) if arg else '', end='')
        if comment:
            padding = '&nbsp'*(12-(len(arg)+len(mnemonic)))
            print(padding+'<span style="color:{}; ">;{}</span>'.format(cores['comment'], comment),end='')
        print('<br>')
print('</div>')
