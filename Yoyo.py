import sys
import ply.yacc as yacc
from Llollo import tokens

# Reglas gramaticales

def p_programa_1(t):
	'''programa	: classStar decVarStar functionStar main'''

def p_classStar_1(t):
	'''classStar	: class classStar
					| '''

def p_class_t(t):
	'''class 	: CLASS ID extends bodyclass'''

def p_extends_t(t):
	'''extends 	: HAMON ID
				| '''

def p_bodyclass_t(t):
	'''bodyclass 	: LLAVEA decVarClassStar functionClassStar LLAVEC'''

def p_decVarClassStar_t(t):
	'''decVarClassStar 	: decvarclass decVarClassStar
						| '''

def p_functionClassStar_t(t):
	'''functionClassStar 	: functionClass functionClassStar
							| '''

def p_functionClass_t(t):
	'''functionClass 	: FUNC access typereturn ID parameters bodyclass'''


def p_decVarStar_1(t):
	'''decVarStar 	: decvar decVarStar
					| '''

def p_functionStar_1(t):
	'''functionStar 	: function functionStar
						| '''

def p_decvarclass_t(t):
	'''decvarclass 	: access decvar'''


def p_function_t(t):
	'''function 	: FUNC typereturn ID parameters bodyclass'''

Parameters	::= '(' ('ref'? (Type | 'id') 'id') (',' 'ref'? (Type | 'id') 'id')* ')'


def p_main_t(t):
	'''main 	: PUBLIC STAND JOJO PARA PARC body'''

def p_body_t(t):
	'''body 	: PARA decVarStar actionStar PARC'''

def p_actionStar_t(t):
	'''actionStar 	: action actionStar
				| '''

def p_action_t(t):
	'''action 	: assign
				| input
				| output
				| condition
				| while
				| funcall
				| return '''

def p

DecVar		::= Type DecVar2 (',' DecVar2)* ';'
DecVar2		::= 'id' ('[' cte_int ']')? ('.' 'id' ('[' cte_int ']')?)*

Var        	::= 'id' (
                    |   ('[' Expression ']' ('.' Var)? )
                    |   ( '.' Var) )


Funcall		::= 'id' ('[' Expression ']')? ('.' 'id'  ('[' Expression ']')? )* '(' Expression (',' Expression)* ')' ';'

Assign		::=	Var '=' (Expression | 'new' 'id' '(' ')') ';'

def p_input_1(t):
	'''input 	: GETS PARA var PARC SEMICOL'''

def p_output_1(t):
	'''output 	: PRINTS PARA expression PARC SEMICOL'''

Condition	::= 'if' '(' Expression ')' '{' Action* '}' ('else' 'if' '(' Expression ')' '{' Action* '}')* ('else' '{' Action* '}')?

While		::= 'while' '(' Expression ')' '{' Action* '}'

Return		::= 'zadust' Expression? ';'

Expression 			::= 'ExpressionNot' (('<' | '>' | '==' | '<=' | '>=' | '!=') 'ExpressionNot')?

def p_expressionNOT_1(t):
	'''expressionNOT 	: simbolExclamationStar expressionOR'''

def p_expressionOR_1(t):
	'''expressionOR 	: expressionAND expressionORStar'''

def p_expressionORStar_1(t):
	'''expressionORStar 	: OR expressionAND expressionORStar
							| '''

def p_expressionAND_1(t):
	'''expressionAND 	: expressionAS expressionANDStar'''

def p_expressionANDStar_1(t):
	'''expressionANDStar 	: AND expressionAS expressionANDStar
							| '''

def p_expressionAS_1(t):
	'''expressionAS 	: expressionMDM expressionASStar'''

def p_expressionASStar_1(t):
	'''expressionASStar : simbolAS expressionMDM expressionASStar
						| '''

def p_expressionMDM_1(t):
	'''expressionMDM 	: expressionL expressionMDMStar'''

def p_expressionMDMStar_1(t):
	'''expressionMDMStar 	: simbolMDM expressionL expressionMDMStar
							| '''

def p_expresionL_1(t):
	'''expressionL 	: PARA expression PARC
					| simbolASPoss value'''


def p_simbolCompare_1(t):
	'''simbolCompare 	: LESS
						| LESSTHAN
						| GREATER
						| GREATERTHAN
						| EQUALS
						| NOTEQUALS '''

def p_simbolExclamationStar_1(t):
	'''simbolExclamationStar 	: NOT simbolExclamationStar
								| '''

def p_simbolMDM_1(t):
	'''simbolMDM 	: MULTIPLICATION
					| DIVISION
					| MOD '''

def p_simbolAS_1(t):
	'''simbolAS 	: ADD
					| SUBSTRACTION'''

def p_simbolASPoss_1(t):
	'''simbolASPoss : simbolAS
					| '''

def p_value_1(t):
	'''value 	: var 
				| funCall 
				| const'''

def p_typereturn_1(t):
	'''typereturn 	: type
					| STAND 
					| ID'''

def p_const_1(t):
	'''const 	: CTE_INT 
				| CTE_REAL 
				| CTE_STRING 
				| CTE_BOOL'''

def p_access_1(t):
	'''type : PUBLIC 
			| PRIVATE
			| '''

def p_type_1(t):
	'''type : INT 
			| REAL
			| BOOL 
			| STRING'''


parser = yacc.yacc()


fFile = input('Archivo: ')
sContenido = open(fFile).read()
yacc.parse(sContenido)
print("\n\n***** Ejecucion terminada. *****\n\n")