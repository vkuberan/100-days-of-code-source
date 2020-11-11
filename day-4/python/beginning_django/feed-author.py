import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginning_django.settings")
django.setup()

from bookstore.models import Author
from faker import Faker
import phonenumbers

cnt = 1

for i in range(1, 2750):
        
    fake    = Faker()
    profile = fake.profile()

    title       = 'Mr.'
    first_name  = profile['name'].split(' ')[0]
    last_name   = profile['name'].split(' ')[1]
    gender      = profile['sex']
    birth_date  = profile['birthdate']

    phone_number    = phonenumbers.format_number(
        phonenumbers.parse(fake.phone_number(), "US"), 
        phonenumbers.PhoneNumberFormat.INTERNATIONAL
    )
    email           = profile['mail']
    ssn             = profile['ssn']

    address         = None
    city            = None
    state           = None
    postal_code     = None
    country         = 'US'

    if gender == 'F':

        result = i % 3

        if result == 0: title = 'Mrs.'
        elif result == 1: title = 'Ms.'
        else: title = 'Miss'

    isClean = True

    try:

        tempAddress     = profile['address'].split("\n")
        address         = tempAddress[0]
        city            = tempAddress[1].split(",")[0]
        state           = tempAddress[1].split(",")[1].strip().split(" ")[0]
        postal_code     = tempAddress[1].split(",")[1].strip().split(" ")[1]

    except:

        isClean = False

    if isClean:

        print('Data is clean.')
        
        myprofile   = "{}\nName: {} {} {} \n".format(cnt, title, first_name, last_name)
        myprofile  += "Gender: {}\n".format(gender)
        myprofile  += "Birth Date: {}\n".format(birth_date)
        myprofile  += "Phone: {}\n".format(phone_number)
        myprofile  += "Email: {}\n".format(email)
        myprofile  += "SSN: {}\n".format(ssn)
        myprofile  += "Address: {}, {}, {}, {} {}\n".format(address, city, state, postal_code, country)

        author = Author()
        author.title = title
        author.first_name = first_name
        author.last_name = last_name
        author.gender = gender
        author.birth_date = birth_date
        author.phone_number = phone_number
        author.email = email
        author.ssn = ssn
        author.address = address
        author.city = city
        author.state = state
        author.postal_code = postal_code
        author.country = country
        author.save()

        print(myprofile)

    else: 
        print("Sorry Data is not clean.")

    cnt += 1