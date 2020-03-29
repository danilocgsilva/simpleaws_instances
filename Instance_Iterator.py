class Instance_Iterator:

    def __init__(self, instances_result):
        self.instances_result = instances_result


    def get_instances(self):
        if len(self.instances_result) is not 0:
            return self.instances_result
        return []
        