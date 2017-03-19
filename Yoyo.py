import sys
import ply.yacc as yacc
from Llollo import tokens
from Classes.DicClases import DicClass
from Classes.DicFunc import DicFunction
from Classes.CuboSemantico import TypeToInt
from Classes.CuboSemantico import SemanticCube
from Classes.Error import Error

dictionaryClass = DicClass()
dictionaryFunction = DicFunction()
typeConv = TypeToInt()
semanticCube = SemanticCube()
errorHandling = Error()

# Reglas gramaticales

def p_programa_1(t):
  '''programa : classStar globalScope decVarPos functionStar main'''

def p_decVarPos_1(t):
  '''decVarPos  : VARIABLES  decVar decVarStar VARIABLES
                | '''

def p_globalScope_1(t):
  '''globalScope : '''
  global sScope
  sScope = "_Global"

def p_classStar_1(t):
  '''classStar  : classOn class classStar
                | classOff'''

def p_classOn_1(t):
  '''classOn  : '''
  global bClass
  bClass = True

def p_classOff_1(t):
  '''classOff  : '''
  global bClass
  bClass = False

def p_class_1(t):
  '''class  : CLASS ID scopeClass extends bodyclass'''

def p_scopeClass_1(t):
  ''' scopeClass : '''
  global sClassName
  sClassName = t[-1]

  if dictionaryClass.insertClass(sClassName) == 0:
    sError = "Clase: " + sClassName
    errorHandling.printError(5, sError, t.lexer.lineno)

def p_extends_1(t):
  '''extends  : HAMON ID scopeHamon 
              | '''

def p_scopeHamon_1(t):
  ''' scopeHamon : '''
  herencia = t[-1]
  global sClassName

  if dictionaryClass.insertHamon(sClassName, herencia) == 0:
    sError = sClassName + " intenta heredar de " + herencia
    errorHandling.printError(6, sError, t.lexer.lineno)

def p_bodyclass_1(t):
  '''bodyclass  : LLAVEA decVarClassPos funcOn functionClassStar funcOff LLAVEC'''

def p_funcOn_1(t):
  '''funcOn  : '''
  global bFunc
  bFunc = True

def p_funcOff_1(t):
  '''funcOff  : '''
  global bFunc
  bFunc = False

def p_decVarClassPos_1(t):
  '''decVarClassPos   : VARIABLES defScopeVarClass decVarclass decVarClassStar VARIABLES
                      | '''

def p_defScopeVarClass_1(t):
  '''defScopeVarClass   : '''
  global sScope
  sScope = "_Atributes"

def p_decVarClassStar_1(t):
  '''decVarClassStar  : decVarclass decVarClassStar
                      | '''

def p_functionClassStar_1(t):
  '''functionClassStar  : functionClass functionClassStar
                        | '''

def p_functionClass_1(t):
  '''functionClass  : FUNC accessPos typeReturn ID defScopeClass parameters body'''

def p_defScopeClass_1(t):
  '''defScopeClass : '''
  global sScope
  sScope = t[-1]

  if dictionaryClass.insertMethod(sClassName, sScope, typeConv.convert(t[-2]), typeConv.convert(t[-3])) == 0:
    sError = "Metodo: " + sScope
    errorHandling.printError(4, sError, t.lexer.lineno)

def p_decVarStar_1(t):
  '''decVarStar   : decVar decVarStar
                  | '''

def p_functionStar_1(t):
  '''functionStar   : function functionStar
                    | '''

def p_decVarclass_1(t):
  '''decVarclass  : accessPos decVar'''


def p_function_1(t):
  '''function   : FUNC typeReturn ID defScope parameters body'''
  

def p_defScope_1(t):
  '''defScope : '''
  global sScope
  sScope = t[-1]

  if dictionaryFunction.insertFunction(sScope, typeConv.convert(t[-2])) == 0:
    sError = "Funcion: " + sScope
    errorHandling.printError(3, sError, t.lexer.lineno)

def p_main_1(t):
  '''main   : PUBLIC STAND JOJO defScope PARA PARC body'''

def p_body_1(t):
  '''body   : LLAVEA decVarPos actionStar LLAVEC'''

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
  '''parametersPos  : ref typeDec ID funVarTab parametersStar
                    | '''

def p_parametersStar_1(t):
  '''parametersStar : COLON ref typeDec ID funVarTab parametersStar
                    | '''

def p_funcVarTab_1(t):
  '''funVarTab : '''
  variable = t[-1]
  global sTipo
  global sScope
  global bClass

  iTipo = typeConv.convert(sTipo)

  if bClass:
    if dictionaryClass.insertParam(sClassName, sScope, variable, iTipo) == 0:
      sError = "Variable: " + variable
      errorHandling.printError(2, sError, t.lexer.lineno)
  else:
    if dictionaryFunction.insertParam(sScope, variable, iTipo) == 0:
      sError = "Variable: " + variable
      errorHandling.printError(2, sError, t.lexer.lineno)


def p_ref_1(t):
  ''' ref : REF
          | '''

def p_decVar_1(t):
  '''decVar : typeDec decVar2 decVarColonStar SEMICOLON'''

def p_decVarColonStar_1(t):
  '''decVarColonStar  : COLON decVar2 decVarColonStar
                      | '''

def p_decVar2_1(t):
  '''decVar2  : ID corchetesPosCte decVar2Star'''
  variable = t[1]
  global sAccess
  global sScope
  global sTipo
  global bClass

  iTipo = typeConv.convert(sTipo)
  iAccess = typeConv.convert(sAccess)

  if bClass:
    if sScope == "_Atributes":
      if dictionaryClass.insertAtribute(sClassName, variable, iTipo, iAccess) == 0:
        sError = "Atributo: " + variable
        errorHandling.printError(1, sError, t.lexer.lineno)
    else:
      if dictionaryClass.insertVar(sClassName, sScope, variable, iTipo) == 0:
        sError = "Variable: " + variable
        errorHandling.printError(2, sError, t.lexer.lineno)
  else:
    if dictionaryFunction.insertVar(sScope, variable, iTipo) == 0:
      sError = "Variable: " + variable
      errorHandling.printError(2, sError, t.lexer.lineno)
        

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
  '''expressionCompare  : expressionAS expressionComparePos'''

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

def p_accessPos_1(t):
  '''accessPos  : access 
                | accessEmtpy'''

def p_accessEmtpy_1(t):
  '''accessEmtpy  : '''
  global sAccess
  sAccess = "public"


def p_access_1(t):
  '''access : PUBLIC 
            | PRIVATE'''
  t[0]=t[1]
  global sAccess
  sAccess=t[0]

def p_typeReturn_1(t):
  '''typeReturn   : typeDec
                  | STAND'''
  t[0]=t[1]
  global sTipo
  sTipo = t[0]

def p_typeDec_1(t):
  '''typeDec  : type
              | ID'''
  t[0]=t[1]
  global sTipo
  sTipo = t[0]

def p_type_1(t):
  '''type : INT 
          | REAL
          | BOOL 
          | STRING'''
  t[0]=t[1]
  global sTipo
  sTipo = t[0]

def p_error(t):
    sError = "Token: " + t.value
    errorHandling.printError(0, sError, t.lexer.lineno)
    sys.exit()


sTipo = ""
sScope = ""
sAccess = ""
sClassName = ""
bClass = False
bFunc = False


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

      #print (dictionaryClass)
      #print (dictionaryFunction)

    except EOFError:
        print(EOFError)
  else:
    print('Error en archivo')