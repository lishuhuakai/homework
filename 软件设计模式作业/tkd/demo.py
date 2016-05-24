import functools


def log(arg1):
    def wrapper1(arg2):
        def wrapper2(arg3):
            def wrapper3(*args, **kw):
                print("in wrapper:", arg1, arg2, arg3.__name__)
                return arg3(*args, **kw)
        return wrapper2
    return wrapper1

@log("1")
@log("2")
def callback(event, self):
    print(event, "--", self)

if __name__ == "__main__":
    callback(1, 2)
