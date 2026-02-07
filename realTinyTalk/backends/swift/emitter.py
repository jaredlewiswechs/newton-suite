from realTinyTalk.parser import Program, Literal, Identifier, Call, ASTNode

class SwiftEmitter:
    def __init__(self, include_runtime=True):
        self.include_runtime = include_runtime

    def emit(self, ast: Program) -> str:
        """Transpile TinyTalk AST to Swift code."""
        swift_code = []

        if self.include_runtime:
            swift_code.append(self._emit_runtime())

        for statement in ast.statements:
            swift_code.append(self._emit_node(statement))

        return "\n".join(swift_code)

    def _emit_runtime(self) -> str:
        """Emit Swift runtime helpers."""
        return """// Swift runtime helpers
func printWrapper(_ message: String) {
    print(message)
}
"""

    def _emit_node(self, node: ASTNode) -> str:
        """Emit Swift code for a single AST node."""
        if isinstance(node, Literal):
            return self._emit_literal(node)
        elif isinstance(node, Identifier):
            return self._emit_identifier(node)
        elif isinstance(node, Call):
            return self._emit_function_call(node)
        else:
            raise NotImplementedError(f"Node type {node.type} not supported.")

    def _emit_literal(self, node: Literal) -> str:
        return str(node.value)

    def _emit_identifier(self, node: Identifier) -> str:
        return node.name

    def _emit_function_call(self, node: Call) -> str:
        if isinstance(node.callee, Identifier) and node.callee.name == "show":
            return f"printWrapper({self._emit_node(node.args[0])})"
        args = ", ".join(self._emit_node(arg) for arg in node.args)
        return f"{self._emit_node(node.callee)}({args})"