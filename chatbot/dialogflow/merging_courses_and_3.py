import yaml

courses3 = yaml.full_load(open('courses3.yaml'))
courses = yaml.full_load(open('courses_.yaml'))

for _,course3 in courses3.items():
    course3['compre'] = 'N/A'
    for _,course in courses.items():
        if course['code'] in course3['code']:
            course3['units'] = course['units']
            course3['compre'] = course['compre']

yaml.dump(courses3, open('courseses3.yaml', 'a'))