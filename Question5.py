def apply_operation(left_operand, right_operand, operator):
    return {
        '+': left_operand + right_operand,
        '-': left_operand - right_operand,
        '*': left_operand * right_operand,
        '/': left_operand / right_operand

    }[operator]