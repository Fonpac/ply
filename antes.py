from ply.lex import lex
from ply.yacc import yacc
import yaml
import re

from node import new_leaf, new_node, append_node


reserved_words = {
    'TRUE': 'BOOL',
    'FALSE': 'BOOL',
    'NOT': 'NOT',
    'TO': 'TO',
    'END': 'END'
}

tokens = ['IDENTIFIER', 'MINUS', 'EQUALS', 'COLON', 'REL_OP', 'AND_OR',
          'NUMBER_OP', 'OPEN_PAR', 'CLOSE_PAR', 'NUM'] + list(reserved_words.values())

# Ignored characters
t_ignore = ' \t'
t_NUMBER_OP = '\+|\*|/'
t_AND_OR = '\&&|\|\|'
t_REL_OP = '\==|\<=|>=|!=|>|<'
t_MINUS = '-'
t_EQUALS = '='
t_COLON = ':'
t_NOT = 'NOT'
t_TO = 'TO'
t_END = 'END'
t_OPEN_PAR = '\('
t_CLOSE_PAR = '\)'

symbol_table = {
    # 'FD': {
    #     'type': 'IDENTIFIER',
    #     'value': 'TO FD value :value END'
    # }
}


# program : statement other_statement
# other_statement : statement other_statement | empty
# statement : assign | expression
# assign: id = num_expression
# func : TO id opt_args statement END
# opt_args: IDENTIFIER opt_args | empty
# expression : num_expression | bool_expression | func | call_func
# num_expression: num_expression OP num_expression | (num_expression) | - num_expression  | NUM
# bool_expression: num_expression REL_OP num_expression | bool_expression AND_OR bool_expression | (bool_expression) | NOT bool_expression | BOOL
# call_func: id opt_args
# empty :


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_BOOL(t):
    r'TRUE|FALSE'
    t.value = bool(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    if t.value in reserved_words:
        t.type = reserved_words[t.value]

    return t


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


def p_error(p):
    if p:
        print(f'Syntax error at {p.value!r}')


def p_program(p):
    '''program : statement other_statement'''
    node = new_node("program")
    append_node(node, p[1])
    if p[2]:
        append_node(node, p[2])
    p[0] = node


def p_statement(p):
    '''statement : assign
                 | expression
    '''
    node = new_node("statement")
    append_node(node, p[1])
    p[0] = node


def p_assign(p):
    '''assign : IDENTIFIER EQUALS expression'''
    node = new_node("assign")
    append_node(node, new_leaf("SET " + p.slice[1].type, value=p[1]))
    append_node(node, new_leaf(p.slice[2].type, value=p[2]))
    append_node(node, p[3])
    p[0] = node


def p_other_statement(p):
    '''other_statement : statement other_statement
                       | empty
    '''
    if p[1]:
        node = new_node("other_statement")
        append_node(node, p[1])
        if p[2]:
            append_node(node, p[2])
        p[0] = node


def p_expression(p):
    '''expression : num_expression
                  | bool_expression
                  | func
                  | call_func
    '''
    node = new_node("expression")
    append_node(node, p[1])
    p[0] = node


def p_bool_expression_bool(p):
    '''bool_expression : BOOL'''
    node = new_node("bool_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    p[0] = node


def p_bool_expression_not(p):
    '''bool_expression : NOT bool_expression'''
    node = new_node("bool_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    append_node(node, p[2])
    p[0] = node


def p_bool_expression_rel_op(p):
    '''bool_expression : num_expression REL_OP num_expression'''
    node = new_node("bool_expression")
    append_node(node, p[1])
    append_node(node, new_leaf(p.slice[2].type, value=p[2]))
    append_node(node, p[3])
    p[0] = node


def p_bool_expression_and_or(p):
    '''bool_expression : bool_expression AND_OR bool_expression'''
    node = new_node("bool_expression")
    append_node(node, p[1])
    append_node(node, new_leaf(p.slice[2].type, value=p[2]))
    append_node(node, p[3])
    p[0] = node


def p_bool_expression_bool_expression(p):
    '''bool_expression : OPEN_PAR bool_expression CLOSE_PAR'''
    node = new_node("bool_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    append_node(node, p[2])
    append_node(node, new_leaf(p.slice[3].type, value=p[3]))
    p[0] = node


def p_bool_expression_identifier(p):
    '''bool_expression : COLON IDENTIFIER'''
    node = new_node("bool_expression")
    append_node(node, new_leaf("GET " + p.slice[2].type, value=p[2]))
    p[0] = node


def p_num_expression(p):
    '''num_expression : num_expression NUMBER_OP num_expression'''
    node = new_node("num_expression")
    append_node(node, p[1])
    append_node(node, new_leaf(p.slice[2].type, value=p[2]))
    append_node(node, p[3])
    p[0] = node


def p_num_expression_parenthesis(p):
    '''num_expression : OPEN_PAR num_expression CLOSE_PAR'''
    node = new_node("num_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    append_node(node, p[2])
    append_node(node, new_leaf(p.slice[3].type, value=p[3]))
    p[0] = node


def p_num_expression_minus(p):
    '''num_expression : MINUS num_expression'''
    node = new_node("num_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    append_node(node, p[2])
    p[0] = node


def p_num_expression_num(p):
    '''num_expression : NUM'''
    node = new_node("num_expression")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    p[0] = node


def p_num_expression_identifier(p):
    '''num_expression : COLON IDENTIFIER'''
    node = new_node("num_expression")
    append_node(node, new_leaf("GET " + p.slice[2].type, value=p[2]))
    p[0] = node


def p_func(p):
    'func : TO IDENTIFIER opt_args statement END'

    node = new_node("func")
    append_node(node, new_leaf(p.slice[1].type, value=p[1]))
    append_node(node, new_leaf("SET " + p.slice[2].type, value=p[2]))
    append_node(node, p[3])
    append_node(node, p[4])
    append_node(node, new_leaf(p.slice[5].type, value=p[5]))
    p[0] = node


def p_opt_args(p):
    '''opt_args : expression opt_args 
                | empty'''
    node = new_node("opt_args")
    if p[1]:
        append_node(node, new_leaf(p.slice[1].type, value=p[1]))
        if len(p[2]['children']) > 0:
            append_node(node, p[2])
    p[0] = node


def p_call_func(p):
    '''call_func : IDENTIFIER opt_args'''
    node = new_node("call_func")
    append_node(node, new_leaf("GET " + p.slice[1].type, value=p[1]))
    append_node(node, p[2])
    p[0] = node


def p_empty(p):
    'empty :'
    pass


# Build the lexer object
lexer = lex()

# Build the parser
parser = yacc()

ast = parser.parse('''
                    TO sum value + 10 END
                   ''',
                   lexer=lexer, tracking=False)

print(yaml.dump(ast, sort_keys=False, indent=2))
