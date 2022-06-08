#!/usr/bin/python3
common_elements = __import__('3-common_elements')

set_1 = {"python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Per1"}
c_set = common_elements.common_elements(set_1, set_2)
print(sorted(list(c_set)))
