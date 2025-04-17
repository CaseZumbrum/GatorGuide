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
  for (const pg of course.prerequisites) {
    let check = false;
    let str = "";
    for (const c of pg.courses) {
      if (course_in_semesters(semesters, c)) {
        check = true;
      }
      str += c.code + " or ";
    }
    if (!check) {
      errors.push({
        loc: course.code,
        msg:
          "Prequisite courses " + str.slice(0, str.length - 4) + " not in plan",
      });
    }
  }

  return errors;
};

export { validate_course };
