
from ..package_B.print_module import print_func as print_func_b
from ..package_C.print_module import print_func as print_func_c
def print_func() -> None:
    print("A")
    print_func_b()
    print_func_c()
