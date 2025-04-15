import Semester from "../Types/Semester";
import Course from "../Types/Course";
import Course_Error from "../Types/Course_Error";

const course_in_semesters = (semesters: Semester[], c: Course): boolean => {
  for (const semester of semesters) {
    for (const course of semester.courses) {
      if (course.code == c.code) {
        return true;
      }
    }
  }
  return false;
};

// returns a list of course errors (if the list is empty, there are no errors)
const validate_course = (
  course: Course,
  semesters: Semester[]
): Course_Error[] => {
  let errors: Course_Error[] = [];
  for (const c of course.prerequisites) {
    if (!course_in_semesters(semesters, c)) {
      errors.push({
        loc: course.code,
        msg: "Prequisite course " + c.code + " not in plan",
      });
    }
  }

  return errors;
};

export { validate_course };
