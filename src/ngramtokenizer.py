# -*- coding: utf-8 -*-

'''
Created on 2012/03/23

@author: tatsuya.oiwa
'''

from optparse import OptionParser

def tokenize(text, n):
    '''Tokenize a text.
    
    Args:
      text:
        The text for tokenize.
      n:
        The number of N-gram.
    '''
    for chunk in text.split(' '):
        if len(chunk) > n:
            for i in xrange(len(chunk) - n + 1):
                print chunk[i:i + n] + '|',
        else:
            print chunk

if __name__ == '__main__':
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage)
    
    parser.add_option('-t', '--text', action='store', type='string',
                      metavar='<text>', default='Hello world!',
                      dest='text', help='')
    
    parser.add_option('-n', action='store', type='int',
                      metavar='<number of ngram>', default='3',
                      dest='n', help='')
    
    args = parser.parse_args()
    options = args[0]
    
    text = options.text.decode('utf-8').encode('utf-8')
    tokenize(text.decode('utf-8'), int(options.n))