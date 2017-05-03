import sys
import pprint
import copy
import ply.yacc as yacc
from Llollo import tokens
from Classes.DicClases import DicClass
from Classes.DicFunc import DicFunction
from Classes.CuboSemantico import TypeConvertion
from Classes.CuboSemantico import SemanticCube
from Classes.Cuadruplo import Quadruple
from Classes.DataStructures.Queue import Queue
from Classes.DataStructures.Stack import Stack
from Classes.Memoria import Memory
from Classes.Util import Error
from Classes.Util import Util
from Classes.VirtualMachine import VM


# Reglas gramaticales

def p_programa_1(t):
  '''programa : gotoMain classStar globalScope decVarPos functionStar main'''

def p_gotoMain_1(t):
  '''gotoMain : '''
  quads.append(typeConv.convertOp("era"))
  quads.append(typeConv.convertOp("gosub"))
  quads.append(typeConv.convertOp("end"))

def p_decVarPos_1(t):
  '''decVarPos  : VARIABLES decVar decVarStar VARIABLES
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
    sys.exit()

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
    sys.exit()

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
  '''functionClass  : FUNC accessPos typeReturn ID defScopeClass parameters body genEndproc'''

def p_genEndProc_1(t):
  '''genEndproc   : '''
  mem.endFunction() 
  quads.append(typeConv.convertOp("endProc"))

def p_defScopeClass_1(t):
  '''defScopeClass : '''
  global sScope
  global sTipo
  global sAccess
  sScope = t[-1]

  if dictionaryClass.insertMethod(sClassName, sScope, typeConv.convertType(sTipo), typeConv.convertAccess(sAccess)) == 0:
    sError = "Metodo: " + sScope
    errorHandling.printError(4, sError, t.lexer.lineno)
    sys.exit()
  # TODO: Agregar el metodo a la memoria del objeto

  iMem = mem.createFunction()
  dictionaryClass.setMemFunc(sClassName, sScope, iMem)
  dictionaryClass.setQuadInicial(sClassName, sScope, quads.size())

  

  atributes = dictionaryClass.getAtributes(sClassName);
  print atributes
  print "METO ATRIBUTOS"
  for at, res in atributes.items():
    print at
    print res.tipo
    if dictionaryClass.insertVar(sClassName, sScope, at, res.tipo) == 0:
      sError = "Variable: " + variable
      errorHandling.printError(2, sError, t.lexer.lineno)
      sys.exit()
    iMem = mem.addVariableLocal(res.tipo)
    dictionaryClass.setMemVar(sClassName, sScope, at, res.tipo)
    dictionaryClass.pprint()



def p_decVarStar_1(t):
  '''decVarStar   : decVar decVarStar
                  | '''

def p_functionStar_1(t):
  '''functionStar   : function functionStar
                    | '''

def p_decVarclass_1(t):
  '''decVarclass  : accessPos decVar'''


def p_function_1(t):
  '''function   : FUNC typeReturn ID defScope parameters body genEndproc'''
  

def p_defScope_1(t):
  '''defScope : '''
  global sScope
  sScope = t[-1]

  if dictionaryFunction.insertFunction(sScope, typeConv.convertType(t[-2])) == 0:
    sError = "Funcion: " + sScope
    errorHandling.printError(3, sError, t.lexer.lineno)
  iMem = mem.createFunction()
  dictionaryFunction.setMemFunc(sScope, iMem)
  dictionaryFunction.setQuadInicial(sScope, quads.size())

def p_main_1(t):
  '''main   : PUBLIC STAND JOJO defScope gotMain PARA PARC body genEndproc'''

def p_gotMain_1(t):
	'''gotMain  : '''
	global sScope
	quads.fill(0, dictionaryFunction.getMemFunc(sScope), 1)
	quads.fill(1, quads.size())

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

  iTipo = typeConv.convertType(sTipo)
  iResult = 0

  if bClass:
    iResult = dictionaryClass.insertParam(sClassName, sScope, variable, iTipo)
    # TODO
    
    iMem = mem.addVariableLocal(iTipo)
    dictionaryClass.actualizaParam(sClassName, sScope, iMem)
    dictionaryClass.setMemVar(sClassName, sScope, variable, iMem)
    
  else:
    iResult = dictionaryFunction.insertParam(sScope, variable, iTipo)
    iMem = mem.addVariableLocal(iTipo)
    dictionaryFunction.actualizaParam(sScope, iMem)
    dictionaryFunction.setMemVar(sScope, variable, iMem)

  if iResult == 0:
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
  '''decVar2  : ID decVar3 corchetesPosCte'''

def p_decVar3_1(t):
  '''decVar3  : '''
  global variable
  variable = t[-1]
  global sAccess
  global sScope
  global sTipo
  global iTipo
  global bClass

  iTipo = typeConv.convertType(sTipo)
  iAccess = typeConv.convertAccess(sAccess)

  if bClass:
    if sScope == "_Atributes":
      if not (0 <= iTipo and iTipo <= 3):
        sError = "Atributo: " + variable
        errorHandling.printError(17, sError, t.lexer.lineno)
        sys.exit()
        
      if dictionaryClass.insertAtribute(sClassName, variable, iTipo, iAccess) == 0:
        sError = "Atributo: " + variable
        errorHandling.printError(1, sError, t.lexer.lineno)
        sys.exit()
       # TODO:
      '''
      print variable
      print iTipo
      print t.lexer.lineno
      iMem = mem.addVariableLocal(iTipo)
      dictionaryClass.setMemObjAtr(sScope, variable, iMem)
      '''
    else:

      if iTipo < 4:
        if dictionaryClass.insertVar(sClassName, sScope, variable, iTipo) == 0:
          sError = "Variable: " + variable
          errorHandling.printError(2, sError, t.lexer.lineno)
          sys.exit()
        # TODO:
        iMem = mem.addVariableLocal(iTipo)
        dictionaryClass.setMemObjFuncVar(sScope, variable, iMem)
      else:
        iAtribute = dictionaryClass.getAtributes(iTipo)
        for i, j in iAtribute.items():
          if dictionaryClass.insertVar(sClassName, sScope, variable + "." + i, j.tipo) == 0:
            sError = "Variable: " + variable
            errorHandling.printError(2, sError, t.lexer.lineno)
            sys.exit()
          iMem = mem.addVariableLocal(j[0])
          dictionaryClass.setMemObjFuncVar(sScope, variable + "." + i, iMem)
      
  else:
    if iTipo < 4:
      if dictionaryFunction.insertVar(sScope, variable, iTipo) == 0:
        sError = "Variable: " + variable
        errorHandling.printError(2, sError, t.lexer.lineno)
        sys.exit()
      iMem = 0
      if dictionaryFunction.isLocal(sScope, variable):
        iMem = mem.addVariableLocal(iTipo)
      else:
        iMem = mem.addVariableGlobal(iTipo)
      dictionaryFunction.setMemVar(sScope, variable, iMem)
    else:
      dictionaryFunction.insertVar(sScope, variable, iTipo)
      iAtribute = dictionaryClass.getAtributes(iTipo)
      for i, j in iAtribute.items():
          if dictionaryFunction.insertVar(sScope, variable + "." + i, j.tipo) == 0:
            sError = "Variable: " + variable
            errorHandling.printError(2, sError, t.lexer.lineno)
            sys.exit()
          if dictionaryFunction.isLocal(sScope, variable + "." + i):
            iMem = mem.addVariableLocal(j.tipo)
          else:
            iMem = mem.addVariableGlobal(j.tipo)
          dictionaryFunction.setMemVar(sScope, variable + "." + i, iMem)



def p_var_1(t):
  '''var  : getVariableID corchetesPosExp varDotPos'''
 

def p_getVariableID_1(t):
  '''getVariableID  : ID'''
  stVariables.push(t[1])
  

def p_varDotPos_1(t):
  '''varDotPos  : activateIsVarClass DOT dot var
                | varRevisa'''

def p_activateIsVarClass_1(t):
  '''activateIsVarClass   : '''
  global bIsVarClass
  bIsVarClass = True

def p_varRevisa_1(t):
  '''varRevisa  : '''
  global sClassName
  global bClass
  global bDot      
  global bArray
  vartype = 0
  # TODO: Revisar esto
  if bClass:
    if bDot:
      sVariable = stVariables.pop()
      sClass = stVariables.pop()
      sObjeto = sClass + "." + sVariable
      atributos = dictionaryClass.getAtributes(sClassName)
      if atributos[sVariable].encap == 1:
        print "Variable privada"
        sys.exit()
      iMemoria = dictionaryClass.getMemVar(sClassName, sScope, sObjeto)
      varType = dictionaryClass.getVariableType(sClass,sScope, sObjeto)
      if not bArray:
        stID.push([iMemoria, vartype, sVariable])
      bArray = False
    else:
      print "Objeto"
      sVariable = stVariables.pop()
      vartype = dictionaryClass.getVariableType(sClassName, sScope, sVariable)
      iMemoria = dictionaryClass.getMemVar(sClassName, sScope, sVariable)
      if not bArray:  
        stID.push([iMemoria, vartype, sVariable])
      else:
        stVariables.pop()
      bArray = False
  else:
    if bDot:
      sVariable  =stVariables.pop()
      sClass = stVariables.pop()
      sObjeto = sClass + "." + sVariable
      iTipo = dictionaryFunction.getVariableType(sScope, sClass)
      atributos = dictionaryClass.getAtributes(sClassName)
      if atributos[sVariable].encap == 1:
        print "Variable privada"
        sys.exit()
      iMemoria = dictionaryFunction.getMemVar(sScope, sObjeto)
      varType = dictionaryFunction.getVariableType(sScope, sObjeto)
      if not bArray:  
        stID.push([iMemoria, vartype, sObjeto])
      bArray = False

    else:
      sVariable = stVariables.pop()
      vartype = dictionaryFunction.getVariableType(sScope, sVariable)
      iMemoria = dictionaryFunction.getMemVar(sScope, sVariable)
      if not bArray:  
        stID.push([iMemoria, vartype, sVariable])
      else:
        stVariables.pop()
      bArray = False


  if vartype == -1:
    sError = "Variable: " + sVariable
    errorHandling.printError(8, sError, t.lexer.lineno)
    sys.exit()
  bDot = False

def p_corchetesPosExp_1(t):
  '''corchetesPosExp  :  CORCHA mandaArrSt expression arrAc CORCHC
                      | '''

def p_mandaArrSt_1(t):
  '''mandaArrSt   : '''
  # stVariables.push(copy.deepcopy(stVariables))
  # stVariables.clear()


def p_arrAc_1(t):
  '''arrAc : '''       
  global stVariables     
  global bArray
  bArray = True
  global sScope
  var = stID.pop()
  offset = dictionaryFunction.getVarOffset(sScope, stVariables.top())
  size = dictionaryFunction.getVarSize(sScope, stVariables.top())
  quads.append(typeConv.convertOp("ver"), var[0], 0, size-1)

  iDirCte = mem.addVariableConstante(0,offset)
  iDirTemp = mem.addVariableTemporal(var[1], 0)
  quads.append(typeConv.convertOp("*"), var[0], iDirCte, iDirTemp)

  iDirTemp2 = mem.addVariableTemporal(var[1], 0)
  iMemoria = dictionaryFunction.getMemVar(sScope, stVariables.top())
  iDirTemp3 = mem.addVariableConstante(0, iMemoria)
  iMemoria = dictionaryFunction.getMemVar(sScope, stVariables.top())
  quads.append(typeConv.convertOp("+"), iDirTemp3, iDirTemp, iDirTemp2)
  res_type = dictionaryFunction.getVariableType(sScope, t[-3])
  stID.push([[iDirTemp2], var[1], var[0]])
  # stVariables = stVariables.pop()

def p_corchetesPosCte_1(t):
  '''corchetesPosCte  : CORCHA CTE_INT cte_int arrInit CORCHC
                      | '''

def p_arrInit_1(t):
  '''arrInit : '''
  stID.pop()
  global sScope
  global sClassName
  global iTipo
  typeA = dictionaryFunction.getVariableType(sScope, t[-3])
  if typeA <= 4 :
    dictionaryFunction.setVarSizeOff(sScope, t[-5], t[-2], 1)
    global variable
    if dictionaryFunction.isLocal(sScope, variable):
      iMem = mem.addVariableLocal(iTipo,0 ,t[-2]-1)
    else:
      iMem = mem.addVariableGlobal(iTipo, 0 ,t[-2]-1)
  else:
    numAt = dictionaryClass.getNumAtribute(t[-4])
    dictionaryFunction.setVarSizeOff(sScope, t[-4], t[-2], numAt)




def p_funCall_1(t):
  '''funCall  : ZAWARUDO funCallId funCall2'''
  validaFuncion(t)

def p_funCall2_1(t):
  '''funCall2  : funCallStar genEra PARA funCallParamsStart funCallParams PARC'''

def p_funCallId_1(t):
  '''funCallId  : ID'''
  stFunc.push(t[1])

def p_genEra_1(t):
  '''genEra   : '''
  print "FUNCION"
  print stFunc.top()
  global bMethodCall
  global sClassName
  print sClassName
  if bMethodCall:
    iMem = dictionaryClass.getMemFunc(sClassName, stFunc.top())
  else:
    iMem = dictionaryFunction.getMemFunc(stFunc.top())
  quads.append(typeConv.convertOp("era"), iMem)

def p_funCallStar_1(t):
  '''funCallStar  : funCallIsObject corchetesPosExp DOT dot funCallId funCallStar
                  | '''

def p_dot_1(t):
  '''dot  : '''
  global bDot
  bDot = True

def p_funCallIsObject_1(t):
  '''funCallIsObject  : '''
  global bMethodCall
  bMethodCall = True

def p_funCallParamsStart_1(t):
  '''funCallParamsStart   : '''
  global stParams
  global quParams

  stParams.push(copy.deepcopy(quParams))
  quParams.clear()

def p_funCallParams_1(t):
  '''funCallParams  : expression genParam funCallParamsStar
                    | '''

def p_funCallParamsStar_1(t):
  '''funCallParamsStar  : COLON expression genParam funCallParamsStar
                        | '''

def p_genParam_1(t):
  '''genParam   : '''
  var = stID.pop()
  quParams.push(var)

def p_condition_1(t):
  '''condition  : IF PARA expression parcGTF LLAVEA actionStar LLAVEC conditionElse endif'''

def p_parcGTF_1(t):
  '''parcGTF  : PARC'''
  var = stID.pop()

  if var[1] != 2:
    sError = "Variable: " + str(var[0]) + " Type: " + str(var[1]) + " Expected: Bool"
    errorHandling.printError(9, sError, t.lexer.lineno)

  quads.append(typeConv.convertOp("gotoF"), var[0], None, None)
  stSaltos.push(quads.size() - 1)

def p_endif_1(t):
  '''endif  : '''
  end = stSaltos.pop()
  quads.fill(end, quads.size())


def p_conditionElse_1(t):
  '''conditionElse    : else conditionElsePos
                      | '''

def p_else_1(t):
  '''else    : ELSE'''
  quads.append(typeConv.convertOp("goto"), None, None, None)
  false = stSaltos.pop()
  stSaltos.push(quads.size())
  quads.fill(false, quads.size() + 1)


def p_conditionElsePos_1(t):
  '''conditionElsePos   : IF PARA expression parcGTF LLAVEA actionStar LLAVEC conditionElse endif
                        | LLAVEA actionStar LLAVEC'''

def p_assign_1(t):
  '''assign   : var equal assignExpID SEMICOLON'''
  varR = stID.pop()
  varL = stID.pop()
  
  oper = typeConv.convertOp(stOper.pop())
  res_type = semanticCube.exists(varL[1], oper, varR[1])
  global iTempCont

  if res_type == -1:
    sError = "VariableL: " + str(varL[0]) + " TypeL: " + str(typeConv.convertType(varL[1])) + "\n"
    sError = sError + "VariableR: " + str(varR[0]) + " TypeR: " + str(typeConv.convertType(varR[1]))
    errorHandling.printError(9, sError, t.lexer.lineno)

  quads.append(oper, varR[0], None, varL[0])
  
    

def p_equal_1(t):
  '''equal : EQUAL'''
  stOper.push(t[1])

def p_assignExpID_1(t):
  '''assignExpID  : expression
                  | NEW ID PARA PARC'''

def p_input_1(t):
  '''input  : GETS PARA var PARC SEMICOLON'''
  var = stID.pop()
  quads.append(typeConv.convertOp("gets"), var[0], var[1])

def p_output_1(t):
  '''output   : PRINTS PARA expression PARC SEMICOLON'''
  var = stID.pop()
  quads.append(typeConv.convertOp("prints"), var[0])


def p_while_1(t):
  '''while  : whilecondition PARA expression parcGTF LLAVEA actionStar LLAVEC'''
  end = stSaltos.pop()
  ret = stSaltos.pop()
  quads.append(typeConv.convertOp("goto"), None, None, ret)
  quads.fill(end, quads.size())


def p_whilecondition_1(t):
  '''whilecondition  : WHILE'''
  stSaltos.push(quads.size())


def p_return_1(t):
  '''return   : ZADUST expressionPos SEMICOLON'''
  validaReturn(t)
  

def p_expressionPos_1(t):
  '''expressionPos  : expression isExpressionT
                    | isExpressionF'''

def p_isExpressionF_1(t):
  '''isExpressionF  : '''
  global isExpression
  isExpression = False

def p_isExpressionT_1(t):
  '''isExpressionT   : '''
  global isExpression
  isExpression = True

def p_expression_1(t):
  '''expression   : expressionAND expressionORStar'''

def p_expressionORStar_1(t):
  '''expressionORStar   : or expressionAND checkOR expressionORStar
                        | '''

def p_checkOR_1(t):
  '''checkOR : '''
  if stOper.top() == '||':
    asociIzq(t)


def p_or_1(t):
  '''or : OR'''
  stOper.push(t[1])                        

def p_expressionAND_1(t):
  '''expressionAND  : expressionNOT expressionANDStar'''


def p_expressionANDStar_1(t):
  '''expressionANDStar  : and expressionNOT checkAND expressionANDStar
                        | '''

def p_checkAND_1(t):
  '''checkAND : '''
  if stOper.top() == '&&':
    asociIzq(t)


def p_and_1(t):
  '''and : AND'''
  stOper.push(t[1])  


def p_expressionNOT_1(t):
  '''expressionNOT  : simbolExclamationStar expressionCompare '''


def p_expressionCompare_1(t):
  '''expressionCompare  : expressionAS expressionComparePos'''

def p_expressionComparePos_1(t):
  '''expressionComparePos : simbolCompare expressionAS checkCompare
                          | '''   

def p_checkCompare_1(t):
  '''checkCompare : '''
  relOper = {'<','<=','>','>=','==', '!='}
  if stOper.top() in relOper:
    asociIzq(t)


def p_expressionAS_1(t):
  '''expressionAS   : expressionMDM expressionASStar'''

def p_expressionASStar_1(t):
  '''expressionASStar : simbolAS expressionMDM checkAS expressionASStar
                      | '''

def p_checkAS_1(t):
  '''checkAS  : '''
  if stOper.top() == '+' or stOper.top() == '-':
    asociIzq(t)


def p_expressionMDM_1(t):
  '''expressionMDM  : expressionL expressionMDMStar'''

def p_expressionMDMStar_1(t):
  '''expressionMDMStar  : simbolMDM expressionL checkMDM expressionMDMStar
                        | '''


def p_checkMDM_1(t):
  '''checkMDM  : '''
  if stOper.top() == '*' or stOper.top() == '/' or stOper.top() == '%':
    asociIzq(t)


def p_expressionL_1(t):
  '''expressionL  : para expression parc
                  | simbolASPoss value expressionNegativo '''

def p_expresionNegativo_1(t):
  '''expressionNegativo   : '''
  global bSigno
  global iTempCont

  if bSigno:
    return
  
  var = stID.pop()
  if not (var[1] == 0 or var[1] == 1):
    sError = "Type: " + str(typeConv.convertType(var[1])) + " Expected: Int/Real"
    errorHandling.printError(9, sError, t.lexer.lineno)
    res_type = var[1]

  iTempCont += 1
  result = iTempCont
  iDirTemp = mem.addVariableTemporal(var[1], 0)
  quads.append(typeConv.convertOp("-"), 0, var[0], iDirTemp)
  stID.push([iDirTemp, var[1], result])
  bSigno = True


def p_para_1(t):
  '''para  : PARA '''
  stOper.push('(')

def p_parc_1(t):
  '''parc  : PARC'''
  if stOper.top() != '(':
    print("SOMETHING JUST WENT WRONG IN p_parc_1")
    sys.exit()
  stOper.pop()


def p_simbolCompare_1(t):
  '''simbolCompare  : LESSTHAN
                    | LESSEQUALS
                    | GREATERTHAN
                    | GREATEREQUALS
                    | EQUALS
                    | NOTEQUALS '''
  stOper.push(t[1])

def p_simbolExclamationStar_1(t):
  '''simbolExclamationStar  : not simbolExclamationStar checkNOT
                            | '''

# Falta checar el Not en cubo semantico
def p_checkNOT_1(t):
  '''checkNOT : '''

  if stOper.top() == '!':
    var = stID.pop()

    oper = typeConv.convertOp(stOper.pop())
    res_type = semanticCube.exists(var[1], oper)
    global iTempCont

    if res_type == -1:
      print t.lexer.lineno
      sys.exit()

      if res_type == -1:
        sError = "VariableL: " + str(var[0]) + " TypeL: " + str(typeConv.convertType(var[1])) + " Expected: Bool"
        errorHandling.printError(9, sError, t.lexer.lineno)
        res_type = var[1]

    iTempCont += 1
    result = iTempCont

    iDirTemp = mem.addVariableTemporal(var[1], 0)
    quads.append(oper, var[0], None, iDirTemp)
    stID.push([iDirTemp, res_type, result])


def p_not_1(t):
  '''not : NOT'''
  stOper.push(t[1])  


def p_simbolMDM_1(t):
  '''simbolMDM  : MULT
                | DIV
                | MOD '''
  stOper.push(t[1])

def p_simbolAS_1(t):
  '''simbolAS   : ADD
                | SUBS'''
  stOper.push(t[1])

def p_simbolASPoss_1(t):
  '''simbolASPoss : simbolAS guardaSigno
                  | '''

def p_guardaSigno_1(t):
  '''guardaSigno  : '''
  global bSigno
  
  if stOper.pop() == '-':
    bSigno = False


def p_value_1(t):
  '''value  : var 
            | funCall 
            | const'''

def p_const_1(t):
  '''const  : CTE_INT cte_int 
            | CTE_REAL cte_real
            | CTE_STR cte_str
            | CTE_BOOL cte_bool'''
  t[0] = t[1]

def p_cte_int_1(t):
  '''cte_int  : '''
  valor = int(t[-1])
  iDirCte = mem.addVariableConstante(0,valor)
  stID.push([iDirCte, 0, t[-1]])

def p_cte_real_1(t):
  '''cte_real  : '''
  valor = float(t[-1])
  iDirCte = mem.addVariableConstante(1,valor)
  stID.push([iDirCte, 1, t[-1]])

def p_cte_bool_1(t):
  '''cte_bool  : '''
  valor = True
  if t[-1] == "false":
    valor = False
  iDirCte = mem.addVariableConstante(2,valor)
  stID.push([iDirCte, 2, t[-1]])

def p_cte_str_1(t):
  '''cte_str  : '''
  sCte = t[-1]
  sCte = sCte[1:-1]
  iDirCte = mem.addVariableConstante(3, sCte)
  stID.push([iDirCte, 3, sCte])

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
    sError = "Token: " + str(t.value)
    errorHandling.printError(0, sError, t.lexer.lineno)
    sys.exit()

def asociIzq(t):
  varR = stID.pop()
  varL = stID.pop()
  
  oper = typeConv.convertOp(stOper.pop())
  res_type = semanticCube.exists(varL[1], oper, varR[1])
  global iTempCont

  if res_type == -1:
    sError = "VariableL: " + str(varL[0]) + " TypeL: " + str(typeConv.convertType(varL[1])) + "\n"
    sError = sError + "VariableR: " + str(varR[0]) + " TypeR: " + str(typeConv.convertType(varR[1]))
    errorHandling.printError(9, sError, t.lexer.lineno)
    res_type = varL[1]

  iTempCont += 1
  result = iTempCont
 
  iDirTemp = mem.addVariableTemporal(varL[1], 0)
  quads.append(oper, varL[0], varR[0], iDirTemp)
  stID.push([iDirTemp, res_type, result])

def validaReturn(t):
  global isExpression

  global bclass

  global sScope
  global sClassName
  global bClass

  sError = ""
  iTypeFunc = -1

  if bClass:
    iTypeFunc = dictionaryClass.getMethodReturnType(sClassName, sScope)
  else:
    iTypeFunc = dictionaryFunction.getFunctionReturnType(sScope)

  if isExpression:
    var = stID.pop()
    if iTypeFunc == var[1]: 
      if bClass:
        atributes = dictionaryClass.getAtributes(sClassName)
        listat  = []
        for at, pe in atributes.items():
          listat.append(dictionaryClass.getMemVar(sClassName, sScope, at))
        quads.append(typeConv.convertOp("return"), [listat, var[0]])
      else:
        quads.append(typeConv.convertOp("return"), var[0])
    else:
      sError = "Error en Zadust 1"
  else:
    if iTypeFunc == 4:
      quads.append(typeConv.convertOp("return"), None)
    else:
      sError = "Error en Zadust 2"

  if sError != "": 
    errorHandling.printError(11, sError, t.lexer.lineno)
    print str(var[1])
    print str(iTypeFunc)




def validaParams(t, params):
  global quParams
  global stParams

  # Validar tipos de parametro y argumento
  i = 0
  while quParams.empty() == False and i < len(params):
    par = quParams.pop()
    if par[1] != params[i][1]:
      sError = "Parametro numero: " + str(i)
      errorHandling.printError(12, sError, t.lexer.lineno)
      sys.exit()
    quads.append(typeConv.convertOp("param"), par[0], None, params[i][0])
    i += 1

  # Validar tamanos de argumentos y parametros
  if quParams.empty() == False:
    sError = "Argumentos sobrantes: " + str(quParams.size())
    errorHandling.printError(13, sError, t.lexer.lineno)
    sys.exit()

  if i != len(params):
    sError = "Argumentos faltantes: " + str(len(params) - i)
    errorHandling.printError(13, sError, t.lexer.lineno)
    sys.exit()

  quParams = stParams.pop()


def validaMetodo(t, bIsDouble=False, sClass=None):
  global sClassName
  global sScope

  
  sMethod = stFunc.pop()
  if sClass is None:
    sClass = stFunc.pop()

  sObjeto = sClass
  sNClass = ""
  print sClass
  if bIsDouble and bClass:
    sClass = dictionaryClass.getVariableType(sClassName, sScope, sClass)
  elif bIsDouble and not bClass:
    print "entre funcion"
    dictionaryFunction.pprint()
    sClass = dictionaryFunction.getVariableType(sScope, sClass)

  # Validar que existe la clase
  bExist = dictionaryClass.existsClass(sClass)

  if not bExist:
    sError = "Clase: " + str(sClass)
    errorHandling.printError(14, sError, t.lexer.lineno)
    sys.exit()

  # Validar que existe el metodo
  dictionaryClass.pprint()
  bExist = dictionaryClass.existsMethod(sClass, sMethod)
  if not bExist:
    sError = "Metodo: " + sMethod
    errorHandling.printError(15, sError, t.lexer.lineno)
    sys.exit()

  iPrivate = dictionaryClass.getMethodEncap(sClass, sMethod)
  if iPrivate == 1:
    sError = "Metodo: " + sMethod
    errorHandling.printError(16, sError, t.lexer.lineno)
    sys.exit()

  varType = dictionaryClass.getMethodReturnType(sClass, sMethod)
  params = dictionaryClass.getParams(sClass, sMethod)

  atributes = dictionaryClass.getAtributes(sClass)
  listat = []
  for at, pe in atributes.items():
    sObjCall = sObjeto + "." +  at
    if bClass:
      iMem = dictionaryClass.getMemVar(sClassName, sScope, sObjCall)
      iMem2 = dictionaryFunction.getMemAtr(sClassName, at)
      listat.append(iMem)
    else:
      iMem = dictionaryFunction.getMemVar(sScope, sObjCall)
      iMem2 = dictionaryClass.getMemVar(sClass, sMethod, sObjCall)
      listat.append(iMem)

    quads.append(typeConv.convertOp("param"), iMem, None, iMem2)

  quads.append(27, listat)

  validaParams(t, params)
  print "METODO"
  print sMethod
  print "CLASE"
  print sClass
  varType = dictionaryClass.getMethodReturnType(sClass, sMethod)
  print varType
  if varType != 4:
    stID.push([sScope, varType, sScope])

  quads.append(typeConv.convertOp("gosub"), sClass, sMethod, dictionaryClass.getQuadInicial(sClass, sMethod))
  bMethodCall = False

def validaFuncion(t):
  global bMethodCall
  global bClass
  global sClassName

   #divide metodos de funciones
  if bMethodCall:
    validaMetodo(t, True)
    return
  
  if bClass:
    validaMetodo(t, False, sClassName)
    return

  sScope = stFunc.pop()
  # Validar que existe la funcion
  bExist = dictionaryFunction.existsFunction(sScope)

  # Validar tipos de retorno
  varType = dictionaryFunction.getFunctionReturnType(sScope)
  params = dictionaryFunction.getParams(sScope)
  if varType == -1:
    sError = "Funcion: " + str(sScope)
    errorHandling.printError(9, sError, t.lexer.lineno)

  validaParams(t, params)

  quads.append(typeConv.convertOp("gosub"), sScope, None ,dictionaryFunction.getQuadInicial(sScope))
  itype = dictionaryFunction.getFunctionReturnType(sScope) 
  if itype != 4:
    iDirTemp = mem.addVariableTemporal(itype)
    quads.append(typeConv.convertOp("="), dictionaryFunction.getMemFunc(sScope), None, iDirTemp)
    stID.push([iDirTemp, itype, iDirTemp])
  bMethodCall = False


global dictionaryClass
global dictionaryFunction
global typeConv
global semanticCube
global errorHandling
global quads
global util

global stID
global stOper
global stSaltos
global stVariables
global stParams

global iTempCont
global iTipo

global bSigno
global bClass
global bFunc
global bIsExpression
global bMethodCall
global bArray
global bIsVarClass
global bDot

global sTipo
global sScope
global sAccess
global sClassName
global variable

iTempCont = 0

bSigno = True
bClass = False
bFunc = False
bIsExpression = True
bMethodCall = False
bArray = False
bIsVarClass = False
bDot = False

sTipo = ""
sScope = ""
sAccess = ""
sClassName = ""

mem = Memory([100000, 100000], [200000, 100000, 1000000, 10000], [300000, 100000])

dictionaryClass = DicClass()
dictionaryFunction = DicFunction()
typeConv = TypeConvertion()
semanticCube = SemanticCube()
errorHandling = Error()
quads = Quadruple()
util = Util()

stID = Stack()
stOper = Stack()
stSaltos = Stack()
stFunc = Stack()
stVariables = Stack()
stParams = Stack()

quParams = Queue()
stVariables = Stack()

parser = yacc.yacc()


if __name__ == '__main__':
  if (len(sys.argv) > 1):
    archivo = sys.argv[1]
    try:
      file = open(archivo,'r')
      info = file.read()
      file.close()

      print(" ******************************************************* ") 
      yacc.parse(info, tracking=True)
      if errorHandling.hasError() or stOper.size() > 0 or stID.size() > 0 or stSaltos.size() > 0:
        print(" *************** Compilacion con errores *************** ")
        print stOper.size()
        print stID.size()
        print stSaltos.size()
        print stID.list
        #sys.exit()
      print(" *************** Compilacion Finalizada **************** ")
      print("\n")
      quads.pprint(dictionaryFunction, mem)
      #mem.pprint()
      vm = VM(mem, quads)
      vm.run()

      
      # util.printAll(dictionaryClass, dictionaryFunction, quads, stOper, stID, stSaltos)
      # util.printAll(dictionaryClass, dictionaryFunction, quads, stOper, stID, stSaltos)
      # util.printQuadruples(quads)

      # print (stOper.items)
      # pprint.pprint (stID.items)

    except EOFError:
        print(EOFError)
  else:
    print('Error en archivo')