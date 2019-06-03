class add_post_func_delay(object):

    def __init__(self, seconds):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        # print("Inside __init__()")
        self.seconds = seconds

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        # print("Inside __call__()")

        def wrapped_f(*args, **kwargs):
            # print("Inside wrapped_f()")
            # print("Decorator arguments:", self.seconds)
            import time
            f(*args, **kwargs)
            time.sleep(self.seconds)
            # print("After f(*args, **kwargs)")
        return wrapped_f

