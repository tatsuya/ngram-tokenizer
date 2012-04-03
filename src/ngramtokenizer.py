# -*- coding: utf-8 -*-

class NgramTokenizer(object):

    def tokenize(self, text, n=1):
        results = []
        for chunk in text.split(' '):
            if len(chunk) >= n:
                for i in xrange(len(chunk) - n + 1):
                    results.append(chunk[i:i + n])
            else:
                results.append(chunk)

        return results

if __name__ == '__main__':
    nt = NgramTokenizer()
    results = nt.tokenize('This is a pen.', 2)
    for chunk in results:
        print chunk + ' |',
