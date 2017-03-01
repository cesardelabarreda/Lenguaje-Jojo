import ply.lex as lex

reserved = {
   'else if' : 'ELSEIF'
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
   'PARA',
   'PARC',
   'LLAVEA',
   'LLAVEC',
   'CORCHA',
   'CORCHC',
   'COLON',
   'SEMICOLON',
   'DOT',
   'LESSTHAN',
   'GREATERTHAN',
   'EQUALS',
   'LESSEQUALS',
   'GREATEREQUALS',
   'NOTEQUALS',
   'SUM',
   'SUBS',
   'MULT',
   'DIV',
   'MOD',
   'AND',
   'NOT',
   'OR',
   'IGUAL',   
   'CTEI',
   'CTER',
   'CTES',
   'CTEB',
   'ID',
] + list(reserved.values())


t_PARA  	  	= r'\('
t_PARC  	  	= r'\)'
t_LLAVEA      = r'{'
t_LLAVEC      = r'}'
t_CORCHA      = r'\['
t_CORCHC      = r'\]'
t_COLON 			= r','
t_SEMICOLON 	= r';'
t_DOT         = r'.'
t_LESSTHAN    = r'<'
t_GREATERTHAN = r'>'
t_EQUALS      = r'=='
t_LESSEQUALS  = r'<='
t_GREATEREQUALS =r'>='
t_NOTEQUALS   = r'!='
t_ADD         = r'\+'
t_SUBS        = r'\-'
t_MULT        = r'\*'
t_DIV         = r'\/'
t_MOD         = r'\%'
t_AND         = r'&&'
t_NOT         = r'!'
t_OR 			    = r'\|\|'
t_EQUAL 		  = r'='


def t_CTE_REAL(t):
    r'([\+|-]?[0-9]+[\.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[\+|-]?\d+'
    t.value = int(t.value)
    return t

def t_CTE_BOOL(t):
    r'true|false'
    t.value = bool(t.value)
    return t

def t_CTE_STR(t):
    r'\"(\\.|[^"])*\"'
    return t

def t_ID(t):
    r'[a-zA-Z](_?[a-zA-Z0-9])*'
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

