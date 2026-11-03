import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# --- Tests for letter_grade ---
def test_letter_grade_s():
    assert letter_grade(95) == "S"

def test_letter_grade_a():
    assert letter_grade(85) == "A"

def test_letter_grade_b():
    assert letter_grade(75) == "B"

def test_letter_grade_c():
    assert letter_grade(65) == "C"

def test_letter_grade_d():
    assert letter_grade(55) == "D"

def test_letter_grade_e():
    assert letter_grade(45) == "E"

def test_letter_grade_f():
    assert letter_grade(30) == "F"

def test_letter_grade_invalid_negative():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-5)

def test_letter_grade_invalid_over_100():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(105)


# --- Tests for final_marks ---
def test_final_marks_valid_no_project():
    assert final_marks(30, 50, False) == 80

def test_final_marks_valid_with_project():
    assert final_marks(30, 50, True) == 85

def test_final_marks_cap_at_100():
    assert final_marks(40, 58, True) == 100

def test_final_marks_invalid_internal():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(45, 50, False)

def test_final_marks_invalid_external():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(35, 65, False)


# --- Tests for exam_eligibility ---
def test_exam_eligibility_fees_not_paid():
    assert exam_eligibility(85, False, False) == "blocked"

def test_exam_eligibility_high_attendance():
    assert exam_eligibility(80, True, False) == "eligible"

def test_exam_eligibility_medical_condonation():
    assert exam_eligibility(70, True, True) == "eligible"

def test_exam_eligibility_detained():
    assert exam_eligibility(60, True, False) == "detained"
