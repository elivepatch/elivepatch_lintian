import whatthepatch



class checks(object):
    
    def __init__(self, patch_file='/tmp/temporary.patch'):
        self.patch_file = patch_file

    def parse(self):
        with open(self.patch_file) as f:
            text = f.read()
        for diff in whatthepatch.parse_patch(text):
            for i in diff[1]:
                self.check_for__init(i)

    def check_for__init(self, diff_line):
        if "__init" in diff_line[2]:
            print("Patch inside __init functions may require a load hook")
            print(diff_line[2])

    def check_test(self):
        pass
    
    

checks()
