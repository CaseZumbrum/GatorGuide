import Course from "./Course";
import RequiredGroup from "./RequiredGroup";

interface Major {
  name: string;
  critical_tracking: Course[];
  required: Course[];
  groups: RequiredGroup[];
}

export default Major;
