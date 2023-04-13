


login_valid = [
    'rtkid_1673385238518'
]

login_invalid = [
    'rtkid_167328',
    'фвфв_1673287626894',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    '我不会说汉语请做不辣的怎么样你会说英语',
    ''
]


email_valid = [
    'testolola@yandex.ru'
]

email_invalid = [
    'a b c @xyz.com',
    'asd@z s v.com',
    'asd@asd. s g h',
    '@asd.asd',
    'asd@asd',
    'asd@asd,asd',
    'ads@asd@asd.asd',
    'asd@asd.a@asd',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    '我不会说汉语请做不辣的怎么样你会说英语',
    '',
    'FALSE',
    'true',
    'None'
]

phone_taken = [
    '79374466300'
]


phone_valid = [
    '+79374466300',
    '79374466300',
    '89374466300',
    '9374466300',
    '+7 937 44 66 300',
    '+375123456789'
]

phone_invalid = [
    '712345678900',
    '7_1234567890',
    '123456789',
    '11-22-33',
    '8 (123) 4567890',
    '-7123456789',
    '`~!@"#№;$%^:',
    'abcdйцукен',
    '',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    '我不会说汉语请做不辣的怎么样你会说英语',
    'FALSE',
    'true',
    'None'
]


personal_account_valid = [
    '358010484269'
]

personal_account_invalid = [
    '1',
    '123456789123456789123456789',
    'FALSE',
    'true',
    'None',
    '712345678900',
    '7_1234567890',
    '123456789',
    '11-22-33',
    '8 (123) 4567890',
    '-7123456789',
    '`~!@"#№;$%^:',
    'abcdйцукен',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '我不会说汉语请做不辣的怎么样你会说英语',
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    ''
]


# должен содержать не менее 8 символов, хотя бы одну заглавную и прописную букву,
# только латинский алфавит, -!- для восстановления - не совпадать с предыдущим, для регистрации
# совпадать с предыдущим-!-  ??? и не быть слишком простым
password_valid = [
    'Qq123456789Qq1'
]

password_invalid = [
    '1',
    '123456789123456789123456789',
    'FALSE',
    'true',
    'None',
    '`~!@"#№;$%^:',
    'abcdйцукен',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '我不会说汉语请做不辣的怎么样你会说英语',
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    ''
]


# должно быть не короче двух символов кириллицы, может содержать - (тире)
first_name_valid = [
    'Ан-на'
]

first_name_invalid = [
    '1',
    '123456789123123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789456789123456789',
    'FALSE',
    'true',
    'None',
    '`~!@"#№;$%^:',
    'abcdйцукен',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '我不会说汉语请做不辣的怎么样你会说英语',
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    ''
]


# должно быть не короче двух символов кириллицы, может содержать - (тире)
last_name_valid = [
    'Ивано-ва'
]

last_name_invalid = [
    '1',
    'asdasdaasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdadasdasdadasdasasdaddasdasasdad',
    'FALSE',
    'true',
    'None',
    '`~!@"#№;$%^:',
    'abcdйцукен',
    "nice site,  i think i'll take it. <script>alert('executing js')</script>",
    "robert'); drop table students;--",
    '我不会说汉语请做不辣的怎么样你会说英语',
    '<i><b>bold</i></b>',
    "'-prompt()-'",
    ''
]

