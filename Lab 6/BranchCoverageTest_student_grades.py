import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# =====================================================================
# Branch Coverage Tests for letter_grade(marks)
# Tests both True and False branches and edge boundaries for each condition
# =====================================================================

def test_letter_grade_negative_marks():
    # Branch: marks < 0 (True)
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-1)

def test_letter_grade_greater_than_100():
    # Branch: marks < 0 (False), marks > 100 (True)
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(101)

def test_letter_grade_s_boundary():
    # Branch: marks >= 90 (True)
    assert letter_grade(90) == "S"
    assert letter_grade(100) == "S"

def test_letter_grade_a_boundary():
    # Branch: marks >= 90 (False), marks >= 80 (True)
    assert letter_grade(80) == "A"
    assert letter_grade(89) == "A"

def test_letter_grade_b_boundary():
    # Branch: marks >= 80 (False), marks >= 70 (True)
    assert letter_grade(70) == "B"
    assert letter_grade(79) == "B"

def test_letter_grade_c_boundary():
    # Branch: marks >= 70 (False), marks >= 60 (True)
    assert letter_grade(60) == "C"
    assert letter_grade(69) == "C"

def test_letter_grade_d_boundary():
    # Branch: marks >= 60 (False), marks >= 50 (True)
    assert letter_grade(50) == "D"
    assert letter_grade(59) == "D"

def test_letter_grade_e_boundary():
    # Branch: marks >= 50 (False), marks >= 40 (True)
    assert letter_grade(40) == "E"
    assert letter_grade(49) == "E"

def test_letter_grade_f_boundary():
    # Branch: marks >= 40 (False) -> returns 'F'
    assert letter_grade(0) == "F"
    assert letter_grade(39) == "F"


# =====================================================================
# Branch Coverage Tests for final_marks(internal, external, has_project)
# =====================================================================

def test_final_marks_internal_out_of_range():
    # Branch: internal > 40 (True)
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(41, 50, False)

def test_final_marks_external_out_of_range():
    # Branch: internal > 40 (False), external > 60 (True)
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(35, 61, False)

def test_final_marks_no_project():
    # Branch: has_project (False)
    assert final_marks(35, 50, False) == 85

def test_final_marks_with_project_no_cap():
    # Branch: has_project (True), total > 100 (False)
    assert final_marks(35, 50, True) == 90

def test_final_marks_with_project_capped():
    # Branch: has_project (True), total > 100 (True)
    assert final_marks(40, 58, True) == 100


# =====================================================================
# Branch Coverage Tests for exam_eligibility(attendance, fees_paid, has_medical)
# =====================================================================

def test_exam_eligibility_fees_not_paid():
    # Branch: not fees_paid (True) -> returns 'blocked'
    assert exam_eligibility(85, False, False) == "blocked"

def test_exam_eligibility_attendance_75_or_more():
    # Branch: not fees_paid (False), attendance >= 75 (True) -> returns 'eligible'
    assert exam_eligibility(75, True, False) == "eligible"

def test_exam_eligibility_medical_eligible():
    # Branch: attendance >= 75 (False), attendance >= 65 (True) and has_medical (True) -> returns 'eligible'
    assert exam_eligibility(65, True, True) == "eligible"

def test_exam_eligibility_attendance_65_without_medical():
    # Branch: attendance >= 65 (True) but has_medical (False) -> returns 'detained'
    assert exam_eligibility(70, True, False) == "detained"

def test_exam_eligibility_attendance_below_65_with_medical():
    # Branch: attendance >= 65 (False) -> returns 'detained'
    assert exam_eligibility(64, True, True) == "detained"

def test_exam_eligibility_attendance_below_65_without_medical():
    # Branch: attendance < 65 and has_medical False -> returns 'detained'
    assert exam_eligibility(50, True, False) == "detained"

