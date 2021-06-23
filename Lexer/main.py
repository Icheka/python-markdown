characters = {
    '*': 'BOLD',
    '\n': 'NEWLINE'
}



class Lexer:
    def __init__(self, code):
        self.input = code
        self.pointer = 0
        self.tokens = []
        self.ast = []
    
    def tokenize(self):
        while (self.pointer < len(self.input)):
            char = self.input[self.pointer]
            if char in characters:
                self.tokens.append({ 'type': characters[char], 'value': char })
            else:
                self.tokens.append({ 'type': 'LITERAL', 'value': char })
            self.pointer += 1

    
    def peek(self, at = 1):
        return self.input[at]

    def seek(self, start = 0):
        index = start 
        foundSymbol = False
        str = ''

        # while foundSymbol == False:
        for c in self.tokens[start:]:
            # print(c['type'])
            if c['type'] == 'LITERAL':
                str += c['value']
                index += 1
                continue
            elif c['type'] == 'NEWLINE':
                str += c['value']
                index += 1
                continue
            else:
                # foundSymbol = True
                break
        return [str, index]

    def toAST(self, index):
        if (index == (len(self.tokens) - 1)):
            return
        for i in range(index, len(self.tokens)):
            # print(self.tokens[i]['type'])
            if self.tokens[i]['type'] == 'LITERAL':
                matches = self.seek(i)
                self.ast.append([matches[0]])
                self.ast.append([
                    self.tokens[matches[1]]['value']
                ])
                return self.toAST(matches[1])
            elif self.tokens[i]['type'] == 'NEWLINE':
                self.ast.append(['NEWLINE'])
                # print(matches)



code = '''
Icheka is a human *being*
*Yes, he is!*
*No, he isn't!*
'''
lex = Lexer(code)
lex.tokenize()
# print(lex.tokens)
lex.toAST(0)
print(lex.ast)