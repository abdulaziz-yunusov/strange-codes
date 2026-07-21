/**
 * cursed_cpp_tokens.cpp
 * =====================
 * WHAT IS THIS?
 * Fully standard, valid C++ code written completely without brackets [],
 * braces {}, '#' directives, or standard logical operators.
 *
 * HOW IT WORKS:
 * Uses C++ Digraphs and Alternative Operator Tokens defined in the language spec:
 *   <%  ->  {            %>  ->  }
 *   <:  ->  [            :>  ->  ]
 *   %:  ->  #
 *   and ->  &&           or  ->  ||           not -> !
 */

%:include <iostream>

int main() <%
    int arr<:3:> = <%10, 20, 30%>;
    bool flag1 = true;
    bool flag2 = false;

    if (flag1 and not flag2) <%
        std::cout << "Element at index 1: " << arr<:1:> << std::endl;
    %>
    return 0;
%>
