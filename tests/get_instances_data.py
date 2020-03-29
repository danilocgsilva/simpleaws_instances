# Just for update the aws return or check members from response

import sys
from tests_src import \
    argument_1_has_been_provided, \
    argument_2_has_been_provided, \
    not_all_argument_provided, \
    get_instances_data


if argument_1_has_been_provided() and argument_2_has_been_provided():
    get_instances_data(sys.argv[1], sys.argv[2])
else:
    not_all_argument_provided(argument_1_has_been_provided(), argument_2_has_been_provided())

