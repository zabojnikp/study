#!/usr/bin/env python3
# Copyright (c) 2009 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
BNF

    FORMULA     ::= ('provšechna' | 'existuje') SYMBOL ':' FORMULA
                 |  FORMULA '->' FORMULA      # zprava asociativní
                 |  FORMULA '|' FORMULA       # zleva asociativní
                 |  FORMULA '&' FORMULA       # zleva asociativní
                 |  '~' FORMULA
                 |  '(' FORMULA ')'
                 |  TERM '=' TERM
                 |  'pravda'
                 |  'nepravda'
    TERM        ::= SYMBOL | SYMBOL '(' TERM_LIST ')'
    TERM_LIST   ::= TERM | TERM ',' TERM_LIST
    SYMBOL      ::= [a-zA-Z]\w*
"""

import ply.lex
import ply.yacc
from pyparsing_py3 import (alphanums, alphas, delimitedList, Forward,
        Group, Keyword, Literal, opAssoc, operatorPrecedence,
        ParserElement, ParseException, ParseSyntaxException, Suppress,
        Word)
ParserElement.enablePackrat()


def pyparsing_parse(text):
    """
    >>> formula = "a = b"
    >>> print(pyparsing_parse(formula))
    ['a', '=', 'b']
    >>> formula = "provšechna x: a = b"
    >>> print(pyparsing_parse(formula))
    ['provšechna', 'x', ['a', '=', 'b']]
    >>> formula = "a & b"
    >>> print(pyparsing_parse(formula))
    ['a', '&', 'b']
    >>> formula = "~pravda -> ~b = c"
    >>> print(pyparsing_parse(formula))
    [['~', 'pravda'], '->', ['~', ['b', '=', 'c']]]
    >>> formula = "~pravda -> ~(b = c)"
    >>> print(pyparsing_parse(formula))
    [['~', 'pravda'], '->', ['~', ['b', '=', 'c']]]
    >>> formula = "existuje y: a -> b"
    >>> print(pyparsing_parse(formula))
    ['existuje', 'y', ['a', '->', 'b']]
    >>> formula = "provšechna x: existuje y: a = b"
    >>> print(pyparsing_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', ['a', '=', 'b']]]
    >>> formula = "provšechna x: existuje y: a = b -> a = b & ~ a = b -> a = b"
    >>> print(pyparsing_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', [['a', '=', 'b'], '->', [[['a', '=', 'b'], '&', ['~', ['a', '=', 'b']]], '->', ['a', '=', 'b']]]]]
    >>> formula = "(provšechna x: existuje y: a = b) -> a = b & ~ a = b -> a = b"
    >>> print(pyparsing_parse(formula))
    [['provšechna', 'x', ['existuje', 'y', ['a', '=', 'b']]], '->', [[['a', '=', 'b'], '&', ['~', ['a', '=', 'b']]], '->', ['a', '=', 'b']]]
    >>> formula = "(provšechna x: existuje y: pravda) -> pravda & ~ pravda -> pravda"
    >>> print(pyparsing_parse(formula))
    [['provšechna', 'x', ['existuje', 'y', 'pravda']], '->', [['pravda', '&', ['~', 'pravda']], '->', 'pravda']]
    >>> formula = "a = b -> c = d & e = f"
    >>> result1 = pyparsing_parse(formula)
    >>> formula = "(a = b) -> (c = d & e = f)"
    >>> result2 = pyparsing_parse(formula)
    >>> result1 == result2
    True
    >>> result1
    [['a', '=', 'b'], '->', [['c', '=', 'd'], '&', ['e', '=', 'f']]]
    >>> formula = "provšechna x: existuje y: pravda -> pravda & pravda | ~ pravda"
    >>> print(pyparsing_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', ['pravda', '->', [['pravda', '&', 'pravda'], '|', ['~', 'pravda']]]]]
    >>> formula = "~ pravda | pravda & pravda -> provšechna x: existuje y: pravda"
    >>> print(pyparsing_parse(formula))
    [[['~', 'pravda'], '|', ['pravda', '&', 'pravda']], '->', ['provšechna', 'x', ['existuje', 'y', 'pravda']]]
    >>> formula = "pravda & provšechna x: x = x"
    >>> print(pyparsing_parse(formula))
    ['pravda', '&', ['provšechna', 'x', ['x', '=', 'x']]]
    >>> formula = "pravda & (provšechna x: x = x)" # stejné jako předchozí
    >>> print(pyparsing_parse(formula))
    ['pravda', '&', ['provšechna', 'x', ['x', '=', 'x']]]
    >>> formula = "provšechna x: x = x & pravda"
    >>> print(pyparsing_parse(formula))
    ['provšechna', 'x', [['x', '=', 'x'], '&', 'pravda']]
    >>> formula = "(provšechna x: x = x) & pravda" # jiné než předchozí
    >>> print(pyparsing_parse(formula))
    [['provšechna', 'x', ['x', '=', 'x']], '&', 'pravda']
    >>> formula = "provšechna x: = x & pravda"
    >>> print(pyparsing_parse(formula))
    Syntax error:
    provšechna x: = x & pravda
           ^
    []
    """
    left_parenthesis, right_parenthesis, colon = map(Suppress, "():")
    forall = Keyword("provšechna")
    exists = Keyword("existuje")
    implies = Literal("->")
    or_ = Literal("|")
    and_ = Literal("&")
    not_ = Literal("~")
    equals = Literal("=")
    boolean = Keyword("nepravda") | Keyword("pravda")
    symbol = Word(alphas, alphanums)
    term = Forward()
    term << (Group(symbol + Group(left_parenthesis +
                   delimitedList(term) + right_parenthesis)) | symbol)
    formula = Forward()
    forall_expression = Group(forall + symbol + colon + formula)
    exists_expression = Group(exists + symbol + colon + formula)
    operand = forall_expression | exists_expression | boolean | term
    formula << operatorPrecedence(operand, [
                                  (equals, 2, opAssoc.LEFT),
                                  (not_, 1, opAssoc.RIGHT),
                                  (and_, 2, opAssoc.LEFT),
                                  (or_, 2, opAssoc.LEFT),
                                  (implies, 2, opAssoc.RIGHT)])
    try:
        result = formula.parseString(text, parseAll=True)
        assert len(result) == 1
        return result[0].asList()
    except (ParseException, ParseSyntaxException) as err:
        print("Syntaktická chyba:\n{0.line}\n{1}^".format(err,
              " " * (err.column - 1)))
        return []


def ply_parse(text):
    """
    >>> formula = "a = b"
    >>> print(ply_parse(formula))
    ['a', '=', 'b']
    >>> formula = "provšechna x: a = b"
    >>> print(ply_parse(formula))
    ['provšechna', 'x', ['a', '=', 'b']]
    >>> formula = "a & b"
    >>> print(ply_parse(formula))
    ['a', '&', 'b']
    >>> formula = "~pravda -> ~b = c"
    >>> print(ply_parse(formula))
    [['~', 'pravda'], '->', ['~', ['b', '=', 'c']]]
    >>> formula = "~pravda -> ~(b = c)"
    >>> print(ply_parse(formula))
    [['~', 'pravda'], '->', ['~', ['b', '=', 'c']]]
    >>> formula = "existuje y: a -> b"
    >>> print(ply_parse(formula))
    ['existuje', 'y', ['a', '->', 'b']]
    >>> formula = "provšechna x: existuje y: a = b"
    >>> print(ply_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', ['a', '=', 'b']]]
    >>> formula = "provšechna x: existuje y: a = b -> a = b & ~ a = b -> a = b"
    >>> print(ply_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', [['a', '=', 'b'], '->', [[['a', '=', 'b'], '&', ['~', ['a', '=', 'b']]], '->', ['a', '=', 'b']]]]]
    >>> formula = "(provšechna x: existuje y: a = b) -> a = b & ~ a = b -> a = b"
    >>> print(ply_parse(formula))
    [['provšechna', 'x', ['existuje', 'y', ['a', '=', 'b']]], '->', [[['a', '=', 'b'], '&', ['~', ['a', '=', 'b']]], '->', ['a', '=', 'b']]]
    >>> formula = "(provšechna x: existuje y: pravda) -> pravda & ~ pravda -> pravda"
    >>> print(ply_parse(formula))
    [['provšechna', 'x', ['existuje', 'y', 'pravda']], '->', [['pravda', '&', ['~', 'pravda']], '->', 'pravda']]
    >>> formula = "a = b -> c = d & e = f"
    >>> result1 = ply_parse(formula)
    >>> formula = "(a = b) -> (c = d & e = f)"
    >>> result2 = ply_parse(formula)
    >>> result1 == result2
    True
    >>> result1
    [['a', '=', 'b'], '->', [['c', '=', 'd'], '&', ['e', '=', 'f']]]
    >>> formula = "provšechna x: existuje y: pravda -> pravda & pravda | ~ pravda"
    >>> print(ply_parse(formula))
    ['provšechna', 'x', ['existuje', 'y', ['pravda', '->', [['pravda', '&', 'pravda'], '|', ['~', 'pravda']]]]]
    >>> formula = "~ pravda | pravda & pravda -> provšechna x: existuje y: pravda"
    >>> print(ply_parse(formula))
    [[['~', 'pravda'], '|', ['pravda', '&', 'pravda']], '->', ['provšechna', 'x', ['existuje', 'y', 'pravda']]]
    >>> formula = "pravda & provšechna x: x = x"
    >>> print(ply_parse(formula))
    ['pravda', '&', ['provšechna', 'x', ['x', '=', 'x']]]
    >>> formula = "pravda & (provšechna x: x = x)" # stejné jako předchozí
    >>> print(ply_parse(formula))
    ['pravda', '&', ['provšechna', 'x', ['x', '=', 'x']]]
    >>> formula = "provšechna x: x = x & pravda"
    >>> print(ply_parse(formula))
    ['provšechna', 'x', [['x', '=', 'x'], '&', 'pravda']]
    >>> formula = "(provšechna x: x = x) & pravda" # jiné než předchozí
    >>> print(ply_parse(formula))
    [['provšechna', 'x', ['x', '=', 'x']], '&', 'pravda']
    >>> formula = "provšechna x: = x & pravda"
    >>> print(ply_parse(formula))
    Syntax error, line 2: EQUALS
    []
    """
    keywords = {"existuje": "EXISTS", "provšechna": "FORALL",
                "pravda": "TRUE", "nepravda": "FALSE"}
    tokens = (["SYMBOL", "COLON", "COMMA", "LPAREN", "RPAREN",
               "EQUALS", "NOT", "AND", "OR", "IMPLIES"] +
              list(keywords.values()))

    def t_SYMBOL(t):
        r"[a-zA-Z]\w*"
        t.type = keywords.get(t.value, "SYMBOL")
        return t


    t_EQUALS = r"="
    t_NOT = r"~"
    t_AND = r"&"
    t_OR = r"\|"
    t_IMPLIES = r"->"
    t_COLON = r":"
    t_COMMA = r","
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    t_ignore = " \t\n"

    def t_newline(t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(t):
        line = t.value.lstrip()
        i = line.find("\n")
        line = line if i == -1 else line[:i]
        raise ValueError("Syntax error, line {0}: {1}"
                         .format(t.lineno + 1, line))
    
    def p_formula_quantifier(p):
        """FORMULA : FORALL SYMBOL COLON FORMULA
                   | EXISTS SYMBOL COLON FORMULA"""
        p[0] = [p[1], p[2], p[4]]

    def p_formula_binary(p):
        """FORMULA : FORMULA IMPLIES FORMULA
                   | FORMULA OR FORMULA
                   | FORMULA AND FORMULA"""
        p[0] = [p[1], p[2], p[3]]

    def p_formula_not(p):
        "FORMULA : NOT FORMULA"
        p[0] = [p[1], p[2]]

    def p_formula_boolean(p):
        """FORMULA : FALSE
                   | TRUE"""
        p[0] = p[1]

    def p_formula_group(p):
        "FORMULA : LPAREN FORMULA RPAREN"
        p[0] = p[2]

    def p_formula_symbol(p):
        "FORMULA : SYMBOL"
        p[0] = p[1]

    def p_formula_equals(p):
        "FORMULA : TERM EQUALS TERM"
        p[0] = [p[1], p[2], p[3]]

    def p_term(p):
        """TERM : SYMBOL LPAREN TERMLIST RPAREN
                | SYMBOL"""
        p[0] = p[1] if len(p) == 2 else [p[1], p[3]]

    def p_termlist(p):
        """TERMLIST : TERM COMMA TERMLIST
                    | TERM"""
        p[0] = p[1] if len(p) == 2 else [p[1], p[3]]
       
    def p_error(p):
        if p is None:
            raise ValueError("Neznámá chyba")
        raise ValueError("Syntaktická chyba, řádek {0}: {1}".format(
                         p.lineno + 1, p.type))

# od nejnižší po nejvyšší precedenci!
    precedence = (("nonassoc", "FORALL", "EXISTS"),
                  ("right", "IMPLIES"),
                  ("left", "OR"),
                  ("left", "AND"),
                  ("right", "NOT"),
                  ("nonassoc", "EQUALS"))

    lexer = ply.lex.lex()
    parser = ply.yacc.yacc()
    try:
        return parser.parse(text, lexer=lexer)
    except ValueError as err:
        print(err)
        return []
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
