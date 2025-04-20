import PrequisiteGroup from "./PrequisiteGroup";

interface Course {
  name: string;
  description: string;
  code: string;
  credits: number;
  prerequisites: PrequisiteGroup[];
  prequisite_string: string;
}

export default Course;
