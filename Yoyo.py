import sys
import ply.yacc as yacc
from Llollo import tokens

# Reglas gramaticales

def p_programa_1(t):
  '''programa : classStar decVarStar functionStar main'''

def p_classStar_1(t):
  '''classStar  : class classStar
                | '''

def p_class_1(t):
  '''class  : CLASS ID extends bodyclass'''

def p_extends_1(t):
  '''extends  : HAMON ID
              | '''

def p_bodyclass_1(t):
  '''bodyclass  : LLAVEA decVarClassStar functionClassStar LLAVEC'''

def p_decVarClassStar_1(t):
  '''decVarClassStar  : decVarclass decVarClassStar
                      | '''

def p_functionClassStar_1(t):
  '''functionClassStar  : functionClass functionClassStar
                        | '''

def p_functionClass_1(t):
  '''functionClass  : FUNC access typeReturn ID parameters body'''


def p_decVarStar_1(t):
  '''decVarStar   : decVar decVarStar
                  | '''

def p_functionStar_1(t):
  '''functionStar   : function functionStar
                    | '''

def p_decVarclass_1(t):
  '''decVarclass  : access decVar'''


def p_function_1(t):
  '''function   : FUNC typeReturn ID parameters body'''

def p_main_1(t):
  '''main   : PUBLIC STAND JOJO PARA PARC body'''

def p_body_1(t):
  '''body   : LLAVEA decVarStar actionStar LLAVEC'''

def p_actionStar_1(t):
  '''actionStar   : action actionStar
                  | '''

def p_action_1(t):
  '''action   : assign
              | input
              | output
              | condition
              | while
              | funCall SEMICOLON
              | return '''

def p_paramters_1(t):
  '''parameters : PARA parametersPos PARC'''

def p_parametersPos_1(t):
  '''parametersPos  : ref typeDec ID parametersStar
                    | '''

def p_parametersStar_1(t):
  '''parametersStar : COLON ref typeDec ID parametersStar
                    | '''

def p_ref_1(t):
  ''' ref : REF
          | '''

def p_decVar_1(t):
  '''decVar : typeDec decVar2 decVarColonStar SEMICOLON'''

def p_decVarColonStar_1(t):
  '''decVarColonStar   : COLON decVar2 decVarColonStar
                  | '''

def p_decVar2_1(t):
  '''decVar2  : ID corchetesPosCte decVar2Star'''

def p_decVar2Star_1(t):
  '''decVar2Star  : DOT ID corchetesPosCte decVar2Star
                  | '''

def p_var_1(t):
  '''var  : ID corchetesPosExp varDotPos'''

def p_varDotPos_1(t):
  '''varDotPos  : DOT var
                | '''

def p_corchetesPosExp_1(t):
  '''corchetesPosExp  : CORCHA expression CORCHC
                      | '''

def p_corchetesPosCte_1(t):
  '''corchetesPosCte  : CORCHA CTE_INT CORCHC
                      | '''

def p_funCall_1(t):
  '''funCall  : ID corchetesPosExp funCallStar PARA funCallParams PARC'''

def p_funCallStar_1(t):
  '''funCallStar  : DOT ID corchetesPosExp funCallStar
                  | '''

def p_funCallParams_1(t):
  '''funCallParams  : expression funCallParamsStar
                    | '''

def p_funCallParamsStar_1(t):
  '''funCallParamsStar  : COLON expression
                        | '''

def p_condition_1(t):
  '''condition  : IF PARA expression PARC LLAVEA actionStar LLAVEC conditionElse'''

def p_conditionElse_1(t):
  '''conditionElse    : ELSE conditionElsePos
                      | '''

def p_conditionElsePos_1(t):
  '''conditionElsePos   : IF PARA expression PARC LLAVEA actionStar LLAVEC conditionElse
                        | LLAVEA actionStar LLAVEC'''

def p_assign_1(t):
  '''assign   : var EQUAL assignExpID SEMICOLON'''

def p_assignExpID_1(t):
  '''assignExpID  : expression
                  | NEW ID PARA PARC'''

def p_input_1(t):
  '''input  : GETS PARA var PARC SEMICOLON'''

def p_output_1(t):
  '''output   : PRINTS PARA expression PARC SEMICOLON'''


def p_while_1(t):
  '''while  : WHILE PARA expression PARC LLAVEA actionStar LLAVEC'''

def p_return_1(t):
  '''return   : ZADUST expressionPos SEMICOLON'''

def p_expressionPos_1(t):
  '''expressionPos  : expression
                    | '''

def p_expression_1(t):
  '''expression   : expressionAND expressionORStar'''

def p_expressionORStar_1(t):
  '''expressionORStar   : OR expressionAND expressionORStar
                        | '''

def p_expressionAND_1(t):
  '''expressionAND  : expressionNOT expressionANDStar'''

def p_expressionANDStar_1(t):
  '''expressionANDStar  : AND expressionNOT expressionANDStar
                        | '''

def p_expressionNOT_1(t):
  '''expressionNOT  : simbolExclamationStar expressionCompare'''


def p_expressionCompare_1(t):
  '''expressionCompare  : expressionAS expressionComparePos
                        | '''

def p_expressionComparePos_1(t):
  '''expressionComparePos : simbolCompare expressionAS
                          | '''


def p_expressionAS_1(t):
  '''expressionAS   : expressionMDM expressionASStar'''

def p_expressionASStar_1(t):
  '''expressionASStar : simbolAS expressionMDM expressionASStar
                      | '''

def p_expressionMDM_1(t):
  '''expressionMDM  : expressionL expressionMDMStar'''

def p_expressionMDMStar_1(t):
  '''expressionMDMStar  : simbolMDM expressionL expressionMDMStar
                        | '''

def p_expresionL_1(t):
  '''expressionL  : PARA expression PARC
                  | simbolASPoss value'''


def p_simbolCompare_1(t):
  '''simbolCompare  : LESSTHAN
                    | LESSEQUALS
                    | GREATERTHAN
                    | GREATEREQUALS
                    | EQUALS
                    | NOTEQUALS '''

def p_simbolExclamationStar_1(t):
  '''simbolExclamationStar  : NOT simbolExclamationStar
                            | '''

def p_simbolMDM_1(t):
  '''simbolMDM  : MULT
                | DIV
                | MOD '''

def p_simbolAS_1(t):
  '''simbolAS   : ADD
                | SUBS'''

def p_simbolASPoss_1(t):
  '''simbolASPoss : simbolAS
                  | '''

def p_value_1(t):
  '''value  : var 
            | funCall 
            | const'''

def p_const_1(t):
  '''const  : CTE_INT 
            | CTE_REAL 
            | CTE_STR
            | CTE_BOOL'''

def p_access_1(t):
  '''access : PUBLIC 
            | PRIVATE
            | '''

def p_typeReturn_1(t):
  '''typeReturn   : typeDec
                  | STAND'''

def p_typeDec_1(t):
  '''typeDec  : type
              | ID'''

def p_type_1(t):
  '''type : INT 
          | REAL
          | BOOL 
          | STRING'''

#def p_error(t):
#    print "Illegal character '%s'" % t.value[0]
#    print(t.lexer.lineno)


parser = yacc.yacc()


if __name__ == '__main__':
  if (len(sys.argv) > 1):
    archivo = sys.argv[1]
    try:
      file = open(archivo,'r')
      info = file.read()
      file.close()
      yacc.parse(info, tracking=True)

      print("Compilacion Finalizada")

    except EOFError:
        print(EOFError)
  else:
    print('Error en archivo')