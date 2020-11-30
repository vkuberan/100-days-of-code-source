# Refer https://realpython.com/python-lambda/
# Python lambdas are little, anonymous functions, subject to a more restrictive
# but more concise syntax than regular Python functions.

# Identity Function


def identity(x):
    return x


# same can be written in lambda function
identityLambda = (lambda x: x)

# Both print 10
print(identityLambda(10))
print(identity(10))

# Lambda's can take multiple arguments
fullName = (lambda title, fname,
            lname: f'{title.title()}. {fname.title()} {lname.title()}')

print(fullName('Mr', 'Velmurugan', 'Kuberan'))
