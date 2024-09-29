
def value():
    s=2
    while s<20:
        val=s*s
        yield val
        s+=3

a=value()
for k in a:
    print(k)


def func (x):
    x("safety to all")
func(print)
func(input)

