from typing import List

from ansiblelint.errors import MatchError
from ansiblelint.file_utils import TargetFile
from ansiblelint.rules import AnsibleLintRule


class EMatcherRule(AnsibleLintRule):
    id = 'TEST0001'
    description = 'This is a test rule that looks for lines ' + \
                  'containing the letter e'
    shortdesc = 'The letter "e" is present'
    tags = ['fake', 'dummy', 'test1']

    def match(self, file: TargetFile, line: str = "") -> List[MatchError]:
        if "e" in line:
            return [self.create_matcherror()]
        return []
