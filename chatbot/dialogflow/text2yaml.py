import yaml
from tqdm import tqdm
from glob import glob

is_course_code = lambda line: ('course number' in line or 'course no ' in line or 'course no.' in line or 'course no:' in line or 'course code' in line)
# is_instructor = lambda line: 'instructor' in line and 'in' in line and 'arge' in line and ':' in line
is_instructor = lambda line: 'instructor' in line
is_title = lambda line: ('course title' in line or 'course name' in line or 'name of the course' in line or 'title of the course' in line)

def txt2dict(filename):
    course = {
        'code': '',
        'ic': '',
        'title': ''
    }
    for line in open(filename).readlines():
        line = line.strip()
        if is_course_code(line.lower()) and not course['code']:
            if ':' in line:
                course['code'] = line.strip().split(':')[1].strip()
            elif '>' in line:
                course['code'] = line.strip().split('>')[1].strip()
            elif '-' in line:
                course['code'] = line.strip().split('-')[1].strip()
        elif is_title(line.lower()) and not course['title']:
            if ':' in line:
                course['title'] = line.strip().split(':')[1].strip()
            elif '>' in line:
                course['title'] = line.strip().split('>')[1].strip()
        elif is_instructor(line.lower()) and not course['ic']:
            if ':' in line:
                ic = line.strip().split(':')[1].strip()
            elif '>' in line:
                ic = line.strip().split('>')[1].strip()
            else:
                continue
            if 'pilani.bits-pilani.ac.in' in ic:
                if ',' in ic:
                    ic = ic.split(',')[0].strip()
                if '(' in ic:
                    ic = ic.split('(')[0].strip()
            course['ic'] = ic
    if not (course['title'] or course['ic'] or course['code']):
        # print('SKIPPING !!!')
        open('errors.log', 'a').write(f'Error in file {filename}: {course["title"]}, {course["code"]}, {course["ic"]}\n')
        return dict()
    final_course = dict()
    final_course[course['title'].title()] = {
        'code': course['code'],
        'ic': course['ic']
    }
    print(course)
    return final_course
    # return course


def dict2yaml_append(data, filename):
    with open(filename, 'a') as file:
        yaml.dump(data, file)

if __name__ == '__main__':
    codes = set()
    # for filename in tqdm(glob(f"{input('Enter directory of pdfs: ')}/*.txt"), desc='Loading...'):
    for filename in tqdm(glob(f"handout_texts/*.txt"), desc='Loading...'):
        data = txt2dict(filename)
        if str(data) not in codes:
            dict2yaml_append(data, 'courses3.yaml')
        codes.add(str(data))
