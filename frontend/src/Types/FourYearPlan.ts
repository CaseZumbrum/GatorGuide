import Course from "./Course";
import Major from "./Major";
import Semester from "./Semester";

interface FourYearPlan {
  semesters: Semester[];
  activeSemester: number;
  major: Major;
}

export default FourYearPlan;

//  I have a 4 year plan with a default of 12 semesters
//  I have an active semester that is the first one out of them
//  I make all of the functions directly relate to the active semester
//  I add a method that allows the switching of the active semester
//  I make it so that switching the active semester changes what values are displayed underneath (which should be simple (hopefully))
//  I make it so that semesters tally up the sum of all of the credits for courses within them and flag if they go over 18
