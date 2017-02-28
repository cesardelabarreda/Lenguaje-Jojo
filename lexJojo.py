import ply.lex as lex

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'neutral' : 'NEUTRAL',
   'int' : 'INT',
   'real' : 'REAL',
   'string' : 'STRING',
   'bool' : 'BOOL',
   'tril' : 'TRIL',
   'stand' : 'STAND',
   'public' : 'PUBLIC',
   'private' : 'PRIVATE',
   'func' : 'FUNC',
   'class' : 'CLASS',
   'jojo' : 'JOJO',
   'size' : 'SIZE',
   'gets' : 'GETS',
   'prints' : 'PRINTS',
   'new' : 'NEW', 
   'zadust' : 'ZADUST',
   'ref' : 'REF',
   'hamon' : 'HAMON',
   'zawarudo' : 'ZAWARUDO',  
}


tokens = [
   'PARI',
   'PARD',
   'LLAVEI',
   'LLAVED',
   'CORCHI',
   'CORCHD',
   'COMA',
   'PUNTOYCOMA',
   'PUNTO',
   'COMP',
   'AND',
   'SUMRES',
   'MULDIV',
   'NOT',
   'OR',
   'IGUAL',   
   'CTEI',
   'CTER',
   'CTES',
   'CTEB',
   'ID',
] + list(reserved.values())


t_PARI  	  	= r'\('
t_PARD  	  	= r'\)'
t_LLAVEI	 	= r'{'
t_LLAVED	 	= r'}'
t_CORCHI 		= r'\['
t_CORCHD 		= r'\]'
t_COMA 			= r','
t_PUNTOYCOMA 	= r';'
t_PUNTO 		= r'.'
t_COMP 			= r'[\<|\>|==|\<=|\>=|\<=|!=]'
t_AND 			= r'&&'
t_SUMRES 		= r'[\+|-]'
t_MULDIV 		= r'[\*|\/|%]'
t_NOT 			= r'!'
t_OR 			= r'\|\|'
t_IGUAL 		= r'='
t_CTES 			= r'\".*\"'


def t_CTER(t):
    r'([0-9]+[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEB(t):
    r'[true | false]'
    t.value = bool(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

