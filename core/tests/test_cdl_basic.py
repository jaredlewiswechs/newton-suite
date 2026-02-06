from core.cdl import CDLEvaluator, RatioConstraint, Operator


def test_ratio_less_than():
    evaluator = CDLEvaluator()
    c = RatioConstraint(f_field="a", g_field="b", operator=Operator.RATIO_LT, threshold=2.0)
    res = evaluator._evaluate_ratio(c, {"a": 3, "b": 2})
    assert res.passed is False


def test_ratio_le_pass():
    evaluator = CDLEvaluator()
    c = RatioConstraint(f_field="a", g_field="b", operator=Operator.RATIO_LE, threshold=2.0)
    res = evaluator._evaluate_ratio(c, {"a": 3, "b": 2})
    assert res.passed is True
