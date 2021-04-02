import yaml
import re

ps = ['Manas,Mishra,22', 'Divya,Tyagi,22']

def courses_text_from_tt(filename='tt.txt'):
    text = open(filename).read()
    regex = r'\d\d\d\d\n[A-Z][A-Z]'
    matches = list(re.finditer(regex, text))
    m_len = len(matches)
    for i in range(m_len):
        i1 = matches[i].span()[0]
        if i == m_len-1:
            i2 = len(text)
        else:
            i2 = matches[i+1].span()[0]
        yield text[i1:i2]


def course_txt2dict(course):
    data = {
        'code': 'N/A',
        'ic': 'N/A',
        'title': 'N/A',
        'units': 0,
        'compre': 'N/A',
    }
    lines = course.split('\n')
    data['code'] = lines[1].strip()
    data['title'] = lines[2].strip()
    data['units'] = int(lines[5].strip())
    for line in lines[6:]:
        if line.upper() == line and line.replace(' ', '').isalpha():
            data['ic'] = line.strip()
            break
    for line in lines[6:]:
        compre_match = re.search(r'\d\d/\d\d [F,A]N', line)
        if compre_match:
            data['compre'] = compre_match.string
            break
    final_data = dict()
    final_data[data['title']] = {
        'code': data['code'],
        'ic': data['ic'],
        'compre': data['compre'],
        'units': data['units'],
    }
    return final_data

def dict2yaml_append(data, filename):
    with open(filename, 'a') as file:
        yaml.dump(data, file)

def textbooks_text_from_tt(filename='textbooks2.txt'):
    text = open(filename).read()
    regex = r'\n\d\d'
    matches = list(re.finditer(regex, text))
    m_len = len(matches)
    for i in range(m_len):
        i1 = matches[i].span()[0]
        if i == m_len-1:
            i2 = len(text)
        else:
            i2 = matches[i+1].span()[0]
        yield text[i1:i2]

if __name__ == '__main__':
    output_yaml_file = 'courses_.yaml'
    open(output_yaml_file, 'w').close()
    for course_txt in courses_text_from_tt():
        course = course_txt2dict(course_txt)
        dict2yaml_append(course, output_yaml_file)
    # for textbook in textbooks_text_from_tt():
    #     open('tbs.txt', 'a').write('\n#######################################################################'+textbook)

    

