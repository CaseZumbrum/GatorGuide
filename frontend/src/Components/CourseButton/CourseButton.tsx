import React from "react";
import { BUTTON_SIZES, BUTTON_VARIANTS } from "../../Constants/enums";
import styles from "./Button.module.scss"

// CourseButton takes in variant and size tags to define the actual function of itself
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: BUTTON_VARIANTS,
    size?: BUTTON_SIZES,
}

const CourseButton = ({children,
    variant = BUTTON_VARIANTS.addCoruse, 
    size = BUTTON_SIZES.Small}: ButtonProps) => {
    return (
        <button 
            className={`${styles.btn} ${styles[variant]} ${styles[size]}`}
            >
            {children}
        </button>
    )
}

export default CourseButton