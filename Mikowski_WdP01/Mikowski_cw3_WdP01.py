print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))


##################################
print("\n")


class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


print('%s %r' % (Data(), Data()))
print('{0!s} {0!r}'.format(Data()))

##################################
print("\n")

print('%10s' % ('test',))
print('{:>10}'.format('test'))


##################################
print("\n")

print('%-10s' % ('test',))
print('{:10}'.format('test'))


##################################
print("\n")

print('%.5s' % ('xylophone',))
print('{:.5}'.format('xylophone'))