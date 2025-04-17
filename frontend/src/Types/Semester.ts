import Course from "./Course";

interface Semester {
    courses: Course[],
    credits: number,
    name: string
  }
  
  export default Semester;
  