import whatthepatch



class checks(object):
    
    def __init__(self, patch_file='/tmp/temporary.patch'):
        self.patch_file = patch_file

    def parse(self):
        _error = 0
        with open(self.patch_file) as f:
            text = f.read()
        for diff in whatthepatch.parse_patch(text):
            for diff_line in diff[1]:
                _error = self.check_for__init(diff_line)
        if _error == 0:
            print('no problem found!')

    def check_for__init(self, diff_line):
        if "__init" in diff_line[2]:
            print("Patch inside __init functions may require a load hook. (https://github.com/dynup/kpatch/blob/master/doc/patch-author-guide.md#init-code-changes)")
            print("'"+diff_line[2]+"'")
            return 1

    def check_test(self):
        pass
