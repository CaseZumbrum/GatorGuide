import Major from "../Types/Major";
import FourYearPlan from "../Types/FourYearPlan";
import Semester from "../Types/Semester";
import Course from "../Types/Course";
import Major_Error from "../Types/Major_Error";
import Required_Group from "../Types/Required_Group";

fetch(import.meta.env.VITE_API_HOST + "/courses", {
  credentials: "include",
  method: "GET",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
}).then((response) => {
  if (response.status == 200) {
    response.json().then((courses) => {
      console.log(courses);
    });
  }
});

// get_majors().then((majors: Major[]) => {use_majors(majors)})
const get_majors = async (): Promise<Major[]> => {
  const response = await fetch(import.meta.env.VITE_API_HOST + "/majors", {
    credentials: "include",
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  if (response.status != 200) {
    alert("Could not gather majors");
    throw new Error("Could not fetch majors");
  }
  return response.json();
};

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

const count_credits_for_group = (
  semesters: Semester[],
  group: Required_Group
): number => {
  let sum = 0;
  for (const semester of semesters) {
    for (const course of semester.courses) {
      if (group.courses.includes(course)) {
        sum += course.credits;
      }
    }
  }
  return sum;
};

// returns a list of major errors
const validate_plan = (plan: FourYearPlan): Major_Error[] => {
  const s = plan.semesters;
  const m = plan.major;
  let errors: Major_Error[] = [];

  for (const c of m.critical_tracking) {
    if (!course_in_semesters(s, c)) {
      errors.push({
        loc: "critical_tracking",
        msg: "Critical tracking course " + c.code + " not in plan",
      });
    }
  }

  for (const c of m.required) {
    if (!course_in_semesters(s, c)) {
      errors.push({
        loc: "required",
        msg: "Required course " + c.code + " not in plan",
      });
    }
  }

  for (const g of m.groups) {
    if (count_credits_for_group(s, g) < g.credits) {
      errors.push({
        loc: "groups",
        msg:
          g.name +
          " not at enough credits, " +
          (g.credits - count_credits_for_group(s, g)) +
          " short",
      });
    }
  }

  return errors;
};

export { get_majors, validate_plan, course_in_semesters };
