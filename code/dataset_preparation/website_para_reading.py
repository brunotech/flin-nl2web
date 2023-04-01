import numpy as np
import random

np.random.seed(1234)
random.seed(1234)


def read_annotated_para_file(trace_id, args, ext_KB):
    para_file = open(args['data_path'] + str(trace_id) + '_datafiles/' + str(trace_id) + '_para.csv', "r")

    p_DB = {}
    j = 0
    max_no_para_phrases = 0

    for line2 in para_file:
        j += 1

        data_fields = line2.strip().split(',')

        act_name = data_fields[0].strip()
        para_name = data_fields[1].lower().strip()
        para_val_fixed = data_fields[2].lower().strip()
        para_type = data_fields[3].lower().strip()

        para_type = 0 if para_type in ['open', 'text'] else 1
        if act_name == '' or para_val_fixed == '':
            print(line2, ' ...... parse error!')
            print(data_fields)
            input()
            continue

        if para_name == '-':
            para_name = act_name.split("#")[1].lower().strip()

        if para_name.strip() in {'reservation date', 'date', 'check out', 'check in',
                                 'check out date', 'check in date',
                                 'check-out', 'check-in'}:
            ext_para_list = [
                (para_val_ext, paraphrase_set, 1)
                for para_val_ext, paraphrase_set in ext_KB['date'].items()
            ]
            if act_name in p_DB:
               if para_name not in p_DB[act_name]:
                   p_DB[act_name][para_name] = ext_para_list
            else:
               p_DB[act_name] = {para_name: ext_para_list}
            print(f'{para_name}.....date data added')
        elif act_name in p_DB:
            if para_name in p_DB[act_name]:
                para_list = p_DB[act_name][para_name]
                para_list.append((para_val_fixed, para_type))
                p_DB[act_name][para_name] = para_list
            else:
                p_DB[act_name][para_name] = [(para_val_fixed, para_type)]
        else:
            p_DB[act_name] = {para_name: [(para_val_fixed, para_type)]}

        if j % 100 == 0:
            print(j)

    print('max # para phrases', max_no_para_phrases)
    return p_DB
