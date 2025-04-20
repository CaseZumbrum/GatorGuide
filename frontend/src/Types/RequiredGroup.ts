import Course from "./Course";

interface RequiredGroup {
  name: string;
  credits: number;
  courses: Course[];
}

export default RequiredGroup;
