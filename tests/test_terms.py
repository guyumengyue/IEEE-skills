from ieee_skills import find_term_issues, normalize_terms


def test_normalize_terms_rewrites_common_phrases():
    text = "The load flow calculation uses smart grids and charging piles."
    normalized, issues = normalize_terms(text)
    assert "power flow analysis" in normalized
    assert "EV chargers" in normalized
    assert len(issues) == 3


def test_find_term_issues_is_conservative():
    assert find_term_issues("The optimal power flow is solved by ADMM.") == []
