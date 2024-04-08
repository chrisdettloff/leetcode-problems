class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square_pref_count = students.count(1)  # Count students who like square sandwiches
        circular_pref_count = students.count(0)  # Count students who like circular sandwiches

        for sandwich in sandwiches:
            if sandwich == 0 and circular_pref_count > 0:
                circular_pref_count -= 1
            elif sandwich == 1 and square_pref_count > 0:
                square_pref_count -= 1
            else:  # No students left who want the current sandwich type
                return circular_pref_count + square_pref_count

        return 0  # All students were able to eat
