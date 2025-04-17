interface Course {
  name: string;
  description: string;
  code: string;
  credits: number;
  prerequisites: Course[];
}

export default Course;
