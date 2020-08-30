class Solution(object):
    def evaluate(self, expression):
        def getval(lookup, x):
            return lookup.get(x, x)

        def evaluate(tokens, lookup):
            if tokens[0] in ('add', 'mult'):
                a, b = map(int, map(lambda x: getval(lookup, x), tokens[1:]))
                return str(a+b if tokens[0] == 'add' else a*b)
            for i in range(1, len(tokens)-1, 2):
                if tokens[i+1]:
                    lookup[tokens[i]] = getval(lookup, tokens[i+1])
            return getval(lookup, tokens[-1])

        tokens, lookup, stk = [''], {}, []
        for c in expression:
            if c == '(':
                if tokens[0] == 'let':
                    evaluate(tokens, lookup)
                stk.append((tokens, dict(lookup)))
                tokens =  ['']
            elif c == ' ':
                tokens.append('')
            elif c == ')':
                val = evaluate(tokens, lookup)
                tokens, lookup = stk.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c
        return int(tokens[0])
val=Solution()
m=input()
print(val.evaluate(m))
