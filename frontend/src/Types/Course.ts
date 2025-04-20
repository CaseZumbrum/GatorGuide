import PrequisiteGroup from "./PrequisiteGroup";

interface Course {
  name: string;
  description: string;
  code: string;
  credits: number;
  prerequisites: PrequisiteGroup[];
}

export default Course;
