import sys
import ply.yacc as yacc
from Llollo import tokens

# Reglas gramaticales

def p_programa_1(t):
	'''programa	: classStar decVarStar functionStar main'''

def p_classStar_1(t):
	'''classStar	: class classStar
					| '''

def p_class_1(t):
	'''class 	: CLASS ID extends bodyclass'''

def p_extends_1(t):
	'''extends 	: HAMON ID
				| '''

def p_bodyclass_1(t):
	'''bodyclass 	: LLAVEA decVarClassStar functionClassStar LLAVEC'''

def p_decVarClassStar_1(t):
	'''decVarClassStar 	: decvarclass decVarClassStar
						| '''

def p_functionClassStar_1(t):
	'''functionClassStar 	: functionClass functionClassStar
							| '''

def p_functionClass_1(t):
	'''functionClass 	: FUNC access typereturn ID parameters bodyclass'''


def p_decVarStar_1(t):
	'''decVarStar 	: decvar decVarStar
					| '''

def p_functionStar_1(t):
	'''functionStar 	: function functionStar
						| '''

def p_decvarclass_1(t):
	'''decvarclass 	: access decvar'''


def p_function_1(t):
	'''function 	: FUNC typereturn ID parameters bodyclass'''



def p_main_1(t):
	'''main 	: PUBLIC STAND JOJO PARA PARC body'''

def p_body_1(t):
	'''body 	: PARA decVarStar actionStar PARC'''

def p_actionStar_1(t):
	'''actionStar 	: action actionStar
					| '''

def p_action_1(t):
	'''action 	: assign
				| input
				| output
				| condition
				| while
				| funcall
				| return '''


Parameters	::= '(' ('ref'? (Type | 'id') 'id') (',' 'ref'? (Type | 'id') 'id')* ')'


DecVar2		::= 'id' ('[' cte_int ']')? ('.' 'id' ('[' cte_int ']')?)*

def p_decVar_1(t):
	'''decVar 	: type decVar2 decVarStar SEMICOL'''

def p_decVarStar_1(t):
	'''decVarStar 	: COLON decVar2 decVarStar
					| '''

def p_decVar2_1(t):
	'''decVar2 	: ID corchPos decVar2Star'''


def p_decVar2_1(t)

Var        	::= 'id' (
                    |   ('[' Expression ']' ('.' Var)? )
                    |   ( '.' Var) )


Funcall		::= 'id' ('[' Expression ']')? ('.' 'id'  ('[' Expression ']')? )* '(' Expression (',' Expression)* ')' ';'


def p_condition_1(t):
	'''condition 	: IF PARA expression PARC LLAVEA actionStar LLAVEC conditionElseIf conditionElse'''

def p_conditionElseIf_1(t):
	'''conditionElseIf 	: ELSEIF PARA expression PARC LLAVEA actionStar LLAVEC conditionElseIf
						| '''

def p_conditionElse_1(t):
	'''conditionElse 	: ELSE LLAVEA actionStar LLAVEC
						| '''

def p_assign_1(t):
	'''assign 	: var EQUAL assignExpID SEMICOL'''

def p_assignExpID_1(t):
	'''assignExpID 	: expression
					| NEW ID PARA PARC'''

def p_input_1(t):
	'''input 	: GETS PARA var PARC SEMICOL'''

def p_output_1(t):
	'''output 	: PRINTS PARA expression PARC SEMICOL'''


def p_while_1(t):
	'''while 	: WHILE PARA expression PARC LLAVEA actionStar LLAVEC'''

def p_return_1(t):
	'''return 	: ZADUST expressionPos SEMICOL'''

def p_expressionPos_1(t):
	'''expressionPos 	: expression
						| '''

def p_expression_1(t):
	'''expression 	: expressionAND expressionORStar'''

def p_expressionORStar_1(t):
	'''expressionORStar 	: OR expressionAND expressionORStar
							| '''

def p_expressionAND_1(t):
	'''expressionAND 	: expressionNOT expressionANDStar'''

def p_expressionANDStar_1(t):
	'''expressionANDStar 	: AND expressionNOT expressionANDStar
							| '''

def p_expressionNOT_1(t):
	'''expressionNOT 	: simbolExclamationStar expressionCompare'''


def p_expressionCompare_1(t):
	'''expressionCompare 	: expressionAS expressionComparePos
							| '''

def p_expressionComparePos_1(t):
	'''expressionComparePos : simbolCompare expressionAS
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
						| LESSEQUALS
						| GREATER
						| GREATEREQUALS
						| EQUALS
						| NOTEQUALS '''

def p_simbolExclamationStar_1(t):
	'''simbolExclamationStar 	: NOT simbolExclamationStar
								| '''

def p_simbolMDM_1(t):
	'''simbolMDM 	: MULT
					| DIV
					| MOD '''

def p_simbolAS_1(t):
	'''simbolAS 	: ADD
					| SUBS'''

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
	'''access 	: PUBLIC 
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