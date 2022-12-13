
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEPOWERAND_OR BOOL CLOSE_PAR COLON DIVIDE ELSE END EQUALS IDENTIFIER IF MINUS NOT NUM OPEN_PAR PLUS POWER REL_OP THEN TIMES TO WHILEprogram : statement other_statementstatement : assign\n                 | expression\n                 | if\n                 | while\n    while : WHILE OPEN_PAR bool_expression CLOSE_PAR program ENDassign : IDENTIFIER EQUALS expressionother_statement : statement other_statement\n                       | empty\n    expression : num_expression\n                  | bool_expression\n                  | func\n                  | call_func\n    bool_expression : BOOLbool_expression : NOT bool_expressionbool_expression : num_expression REL_OP num_expressionbool_expression : bool_expression AND_OR bool_expressionbool_expression : OPEN_PAR bool_expression CLOSE_PARbool_expression : COLON IDENTIFIERnum_expression : num_expression PLUS num_expression\n                      | num_expression MINUS num_expression\n                      | num_expression TIMES num_expression\n                      | num_expression DIVIDE num_expression\n                      | num_expression POWER num_expression\n    num_expression : OPEN_PAR num_expression CLOSE_PARnum_expression : MINUS num_expressionnum_expression : NUMnum_expression : COLON IDENTIFIERfunc : TO IDENTIFIER OPEN_PAR opt_args CLOSE_PAR program ENDopt_args : IDENTIFIER opt_args\n                | emptyopt_params : expression opt_params\n                  | emptycall_func : IDENTIFIER opt_paramsif : IF OPEN_PAR bool_expression CLOSE_PAR THEN statement possible_else ENDpossible_else : ELSE statement\n                     | emptyempty :'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,16,17,18,20,21,24,25,26,27,28,40,42,43,44,47,50,51,52,53,54,55,56,57,58,60,61,64,66,67,69,70,73,76,78,81,83,84,],[7,7,-2,-3,-4,-5,24,-10,-11,-12,-13,-27,43,-14,48,7,24,24,24,-34,-33,-26,64,-19,-15,66,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,70,7,70,7,7,-6,7,-29,-35,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,16,18,21,24,26,27,28,40,43,44,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[12,12,-2,-3,-4,-5,-38,-10,-11,-12,-13,-27,-14,12,-38,-38,-34,-33,-26,-19,-15,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,12,12,12,-6,12,-29,-35,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,16,18,21,24,26,27,28,40,43,44,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[14,14,-2,-3,-4,-5,-38,-10,-11,-12,-13,-27,-14,14,-38,-38,-34,-33,-26,-19,-15,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,14,14,14,-6,14,-29,-35,]),'OPEN_PAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,21,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,43,44,46,48,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[13,13,-2,-3,-4,-5,13,-10,-11,-12,-13,36,13,39,41,-27,-14,46,13,13,13,13,-34,-33,41,41,41,41,41,41,46,46,46,-26,41,-19,-15,46,67,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,13,13,13,-6,13,-29,-35,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,13,15,16,18,19,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,60,61,63,64,65,66,69,73,76,78,81,83,84,],[15,15,-2,-3,-4,-5,15,30,-11,-12,-13,15,15,-27,-14,15,15,15,15,15,-34,-33,15,15,15,15,15,15,15,15,30,15,-26,15,-19,-15,30,15,-7,-32,-20,-21,-22,-23,-24,30,-17,-25,-18,30,-28,30,-19,15,15,15,-6,15,-29,-35,]),'NUM':([0,2,3,4,5,6,7,8,9,10,11,13,15,16,18,19,21,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,43,44,46,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[16,16,-2,-3,-4,-5,16,-10,-11,-12,-13,16,16,-27,-14,16,16,16,16,16,-34,-33,16,16,16,16,16,16,16,16,16,-26,16,-19,-15,16,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,16,16,16,-6,16,-29,-35,]),'COLON':([0,2,3,4,5,6,7,8,9,10,11,13,15,16,18,19,21,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,43,44,46,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[17,17,-2,-3,-4,-5,17,-10,-11,-12,-13,17,42,-27,-14,47,17,17,17,17,-34,-33,42,42,42,42,42,42,47,47,47,-26,42,-19,-15,47,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,17,17,17,-6,17,-29,-35,]),'BOOL':([0,2,3,4,5,6,7,8,9,10,11,13,16,18,19,21,24,25,26,27,28,35,36,39,40,43,44,46,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[18,18,-2,-3,-4,-5,18,-10,-11,-12,-13,18,-27,-14,18,18,18,18,18,-34,-33,18,18,18,-26,-19,-15,18,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,18,18,18,-6,18,-29,-35,]),'NOT':([0,2,3,4,5,6,7,8,9,10,11,13,16,18,19,21,24,25,26,27,28,35,36,39,40,43,44,46,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[19,19,-2,-3,-4,-5,19,-10,-11,-12,-13,19,-27,-14,19,19,19,19,19,-34,-33,19,19,19,-26,-19,-15,19,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,19,19,19,-6,19,-29,-35,]),'TO':([0,2,3,4,5,6,7,8,9,10,11,16,18,21,24,25,26,27,28,40,43,44,50,51,52,53,54,55,56,57,58,60,61,64,66,69,73,76,78,81,83,84,],[20,20,-2,-3,-4,-5,20,-10,-11,-12,-13,-27,-14,20,20,20,20,-34,-33,-26,-19,-15,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,20,20,20,-6,20,-29,-35,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,18,21,22,23,24,26,27,28,40,43,44,49,50,51,52,53,54,55,56,57,58,60,61,64,66,78,83,84,],[0,-38,-2,-3,-4,-5,-38,-10,-11,-12,-13,-27,-14,-38,-1,-9,-38,-38,-34,-33,-26,-19,-15,-8,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,-6,-29,-35,]),'END':([2,3,4,5,6,7,8,9,10,11,16,18,21,22,23,24,26,27,28,40,43,44,49,50,51,52,53,54,55,56,57,58,60,61,64,66,74,77,78,79,80,82,83,84,85,],[-38,-2,-3,-4,-5,-38,-10,-11,-12,-13,-27,-14,-38,-1,-9,-38,-38,-34,-33,-26,-19,-15,-8,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,78,-38,-6,83,84,-37,-29,-35,-36,]),'ELSE':([3,4,5,6,7,8,9,10,11,16,18,24,26,27,28,40,43,44,50,51,52,53,54,55,56,57,58,60,61,64,66,77,78,83,84,],[-2,-3,-4,-5,-38,-10,-11,-12,-13,-27,-14,-38,-38,-34,-33,-26,-19,-15,-7,-32,-20,-21,-22,-23,-24,-16,-17,-25,-18,-28,-19,81,-6,-29,-35,]),'EQUALS':([7,],[25,]),'PLUS':([8,16,37,40,43,45,52,53,54,55,56,57,60,63,64,65,66,],[29,-27,29,-26,-28,29,-20,-21,-22,-23,-24,29,-25,29,-28,29,-28,]),'TIMES':([8,16,37,40,43,45,52,53,54,55,56,57,60,63,64,65,66,],[31,-27,31,31,-28,31,31,31,-22,-23,-24,31,-25,31,-28,31,-28,]),'DIVIDE':([8,16,37,40,43,45,52,53,54,55,56,57,60,63,64,65,66,],[32,-27,32,32,-28,32,32,32,-22,-23,-24,32,-25,32,-28,32,-28,]),'POWER':([8,16,37,40,43,45,52,53,54,55,56,57,60,63,64,65,66,],[33,-27,33,33,-28,33,33,33,-22,-23,-24,33,-25,33,-28,33,-28,]),'REL_OP':([8,16,37,40,43,45,52,53,54,55,56,60,64,65,66,],[34,-27,34,-26,-28,34,-20,-21,-22,-23,-24,-25,-28,34,-28,]),'AND_OR':([9,16,18,38,40,43,44,52,53,54,55,56,57,58,59,60,61,62,64,66,],[35,-27,-14,35,-26,-19,35,-20,-21,-22,-23,-24,-16,35,35,-25,-18,35,-28,-19,]),'CLOSE_PAR':([16,18,37,38,40,43,44,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,75,],[-27,-14,60,61,-26,-19,-15,-20,-21,-22,-23,-24,-16,-17,68,-25,-18,69,60,-28,60,-19,-38,-38,76,-31,-30,]),'THEN':([68,],[73,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,69,76,],[1,74,79,]),'statement':([0,2,21,69,73,76,81,],[2,21,21,2,77,2,85,]),'assign':([0,2,21,69,73,76,81,],[3,3,3,3,3,3,3,]),'expression':([0,2,7,21,24,25,26,69,73,76,81,],[4,4,26,4,26,50,26,4,4,4,4,]),'if':([0,2,21,69,73,76,81,],[5,5,5,5,5,5,5,]),'while':([0,2,21,69,73,76,81,],[6,6,6,6,6,6,6,]),'num_expression':([0,2,7,13,15,19,21,24,25,26,29,30,31,32,33,34,35,36,39,41,46,69,73,76,81,],[8,8,8,37,40,45,8,8,8,8,52,53,54,55,56,57,45,45,45,63,65,8,8,8,8,]),'bool_expression':([0,2,7,13,19,21,24,25,26,35,36,39,46,69,73,76,81,],[9,9,9,38,44,9,9,9,9,58,59,62,38,9,9,9,9,]),'func':([0,2,7,21,24,25,26,69,73,76,81,],[10,10,10,10,10,10,10,10,10,10,10,]),'call_func':([0,2,7,21,24,25,26,69,73,76,81,],[11,11,11,11,11,11,11,11,11,11,11,]),'other_statement':([2,21,],[22,49,]),'empty':([2,7,21,24,26,67,70,77,],[23,28,23,28,28,72,72,82,]),'opt_params':([7,24,26,],[27,27,51,]),'opt_args':([67,70,],[71,75,]),'possible_else':([77,],[80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement other_statement','program',2,'p_program','main.py',110),
  ('statement -> assign','statement',1,'p_statement','main.py',115),
  ('statement -> expression','statement',1,'p_statement','main.py',116),
  ('statement -> if','statement',1,'p_statement','main.py',117),
  ('statement -> while','statement',1,'p_statement','main.py',118),
  ('while -> WHILE OPEN_PAR bool_expression CLOSE_PAR program END','while',6,'p_while','main.py',124),
  ('assign -> IDENTIFIER EQUALS expression','assign',3,'p_assign','main.py',129),
  ('other_statement -> statement other_statement','other_statement',2,'p_other_statement','main.py',138),
  ('other_statement -> empty','other_statement',1,'p_other_statement','main.py',139),
  ('expression -> num_expression','expression',1,'p_expression','main.py',148),
  ('expression -> bool_expression','expression',1,'p_expression','main.py',149),
  ('expression -> func','expression',1,'p_expression','main.py',150),
  ('expression -> call_func','expression',1,'p_expression','main.py',151),
  ('bool_expression -> BOOL','bool_expression',1,'p_bool_expression_bool','main.py',157),
  ('bool_expression -> NOT bool_expression','bool_expression',2,'p_bool_expression_not','main.py',164),
  ('bool_expression -> num_expression REL_OP num_expression','bool_expression',3,'p_bool_expression_rel_op','main.py',172),
  ('bool_expression -> bool_expression AND_OR bool_expression','bool_expression',3,'p_bool_expression_and_or','main.py',191),
  ('bool_expression -> OPEN_PAR bool_expression CLOSE_PAR','bool_expression',3,'p_bool_expression_bool_expression','main.py',200),
  ('bool_expression -> COLON IDENTIFIER','bool_expression',2,'p_bool_expression_identifier','main.py',205),
  ('num_expression -> num_expression PLUS num_expression','num_expression',3,'p_num_expression','main.py',210),
  ('num_expression -> num_expression MINUS num_expression','num_expression',3,'p_num_expression','main.py',211),
  ('num_expression -> num_expression TIMES num_expression','num_expression',3,'p_num_expression','main.py',212),
  ('num_expression -> num_expression DIVIDE num_expression','num_expression',3,'p_num_expression','main.py',213),
  ('num_expression -> num_expression POWER num_expression','num_expression',3,'p_num_expression','main.py',214),
  ('num_expression -> OPEN_PAR num_expression CLOSE_PAR','num_expression',3,'p_num_expression_parenthesis','main.py',226),
  ('num_expression -> MINUS num_expression','num_expression',2,'p_num_expression_minus','main.py',231),
  ('num_expression -> NUM','num_expression',1,'p_num_expression_num','main.py',236),
  ('num_expression -> COLON IDENTIFIER','num_expression',2,'p_num_expression_identifier','main.py',241),
  ('func -> TO IDENTIFIER OPEN_PAR opt_args CLOSE_PAR program END','func',7,'p_func','main.py',246),
  ('opt_args -> IDENTIFIER opt_args','opt_args',2,'p_opt_args','main.py',287),
  ('opt_args -> empty','opt_args',1,'p_opt_args','main.py',288),
  ('opt_params -> expression opt_params','opt_params',2,'p_opt_params','main.py',296),
  ('opt_params -> empty','opt_params',1,'p_opt_params','main.py',297),
  ('call_func -> IDENTIFIER opt_params','call_func',2,'p_call_func','main.py',305),
  ('if -> IF OPEN_PAR bool_expression CLOSE_PAR THEN statement possible_else END','if',8,'p_if','main.py',319),
  ('possible_else -> ELSE statement','possible_else',2,'p_possible_else','main.py',349),
  ('possible_else -> empty','possible_else',1,'p_possible_else','main.py',350),
  ('empty -> <empty>','empty',0,'p_empty','main.py',365),
]
