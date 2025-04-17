import Course from "./Course";
import Required_Group from "./Required_Group";

interface Major{
    name:string,
    critical_tracking: Course[],
    required: Course[],
    groups: Required_Group[]
};

export default Major;