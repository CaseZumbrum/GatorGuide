from GatorGuide.database.models import (
    Major,
    RequiredGroup,
)
import pathlib
from GatorGuide.database.db_engine import DB_Engine


def populate(engine: DB_Engine):
    """Populate the majors

    Args:
        engine (DB_Engine): Database API
    """

    # COMPUTER ENGINEERING
    # https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CPE_BSCO/#criticaltrackingtext
    print("-----------------------")
    print("Adding Computer Engineering...")
    CPE = Major(
        name="Computer Engineering",
    )

    # Required Courses
    CPE.required.append(engine.read_course("CDA3101"))
    CPE.required.append(engine.read_course("CEN3031"))
    CPE.required.append(engine.read_course("COP3502C"))
    CPE.required.append(engine.read_course("COP3503C"))
    CPE.required.append(engine.read_course("COP3530"))
    CPE.required.append(engine.read_course("COT3100"))
    CPE.required.append(engine.read_course("EEL3701C"))
    CPE.required.append(engine.read_course("EEL4744C"))
    CPE.required.append(engine.read_course("ENC3246"))

    # Critical Tracking
    CPE.critical_tracking.append(engine.read_course("MAC2311"))
    CPE.critical_tracking.append(engine.read_course("MAC2312"))
    CPE.critical_tracking.append(engine.read_course("MAC2313"))
    CPE.critical_tracking.append(engine.read_course("MAP2302"))
    CPE.critical_tracking.append(engine.read_course("PHY2048"))
    CPE.critical_tracking.append(engine.read_course("PHY2049"))

    # CPE Design Courses
    CPE.groups.append(
        RequiredGroup(
            name="CpE Design 1",
            credits=3,
            courses=[engine.read_course("CEN3907C"), engine.read_course("EGN4951")],
        )
    )
    CPE.groups.append(
        RequiredGroup(
            name="CpE Design 2",
            credits=3,
            courses=[engine.read_course("CEN4908C"), engine.read_course("EGN4952")],
        )
    )

    # Technical Electives
    CPE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=18)

    engine.add_to_group(
        CPE_TECH_ELECTIVES,
        "^(?!.*(CIS4940|CIS4949|EEL4837|EEL4948|EEL4949|CIS4914|EEL4924C|CDA3101|CEN3031|COP3502C|COP3503C|COP3530|COT3100|EEL3701C|EEL4744C|ENC3246|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(EEL4|COP4|MHF4|MAC4|STA4|PHY3|PHY4|PHZ3|PHZ4|EEE3308C|EEE3396|EEE3773|EEL3112|EEL3211C|EEL3402|EEL3472|EEL3850|CAP3020|CAP3027)",
    )

    CPE_ENRICHMENT_ELECTIVES = RequiredGroup(name="Enrichment Electives", credits=7)

    engine.add_to_group(
        CPE_ENRICHMENT_ELECTIVES,
        "^(?!.*(CIS|COP|MHF|MAC|STA|PHY)).*^(\w{3}4|\w{3}3)",
    )

    CPE.groups.append(CPE_TECH_ELECTIVES)
    CPE.groups.append(CPE_ENRICHMENT_ELECTIVES)

    engine.write(CPE)
    print("Done!")
    
    CS = Major(
        name="Computer Science",
    )

    # Required Courses
    CS.required.append(engine.read_course("CDA3101"))  # Introduction to Computer Organization
    CS.required.append(engine.read_course("CEN3031"))  # Introduction to Software Engineering
    CS.required.append(engine.read_course("CIS4301"))  # Information and Database Systems 1
    CS.required.append(engine.read_course("COP3502C"))  # Programming Fundamentals 1
    CS.required.append(engine.read_course("COP3503C"))  # Programming Fundamentals 2
    CS.required.append(engine.read_course("COP3530"))  # Data Structures and Algorithm
    CS.required.append(engine.read_course("COP4533"))  # Algorithm Abstraction and Design
    CS.required.append(engine.read_course("COP4600"))  # Operating Systems
    CS.required.append(engine.read_course("COP4020"))  # Programming Language Concepts
    CS.required.append(engine.read_course("CNT4007"))  # Computer Network Fundamentals
    CS.required.append(engine.read_course("ENC3246"))  # Professional Communication for Engineers
    CS.required.append(engine.read_course("EGS4034"))  # Engineering Ethics and Professionalism
    CS.required.append(engine.read_course("STA3032"))  # Engineering Statistics
    CS.required.append(engine.read_course("MAS3114"))  # Computational Linear Algebra

    # Critical Tracking Courses
    CS.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    CS.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    CS.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    CS.critical_tracking.append(engine.read_course("COT3100"))  # Applications of Discrete Structures
    CS.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    CS.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Senior Project Requirement
    CS.groups.append(
        RequiredGroup(
            name="Senior Project",
            credits=3,
            courses=[engine.read_course("CIS4914"), engine.read_course("EGN4952")],
        )
    )

    # Major Electives
    CS_MAJOR_ELECTIVES = RequiredGroup(name="Major Electives", credits=18)

    # Adding eligible courses to Major Electives
    engine.add_to_group(
        CS_MAJOR_ELECTIVES,
        "^(CIS4|COP4|COT4|CDA4|CEN4|CAP4|CNT4)",
    )

    # Interdisciplinary Electives
    CS_INTERDISCIPLINARY_ELECTIVES = RequiredGroup(name="Interdisciplinary Electives", credits=14)

    # Adding eligible courses to Interdisciplinary Electives
    engine.add_to_group(
        CS_INTERDISCIPLINARY_ELECTIVES,
        "^(?!.*(CIS|COP|COT|CDA|CEN|CAP|CNT)).*^(\w{3}3|\w{3}4)",
    )

    CS.groups.append(CS_MAJOR_ELECTIVES)
    CS.groups.append(CS_INTERDISCIPLINARY_ELECTIVES)

    AE = Major(
    name="Aerospace Engineering",
    )
  
    # Critical Tracking Courses (NOT in Required Courses)
    AE.critical_tracking.append(engine.read_course("CHM2045"))   # General Chemistry 1
    AE.critical_tracking.append(engine.read_course("CHM2045L"))  # General Chemistry 1 Laboratory
    AE.critical_tracking.append(engine.read_course("MAC2311"))   # Analytic Geometry and Calculus 1
    AE.critical_tracking.append(engine.read_course("MAC2312"))   # Analytic Geometry and Calculus 2
    AE.critical_tracking.append(engine.read_course("MAC2313"))   # Analytic Geometry and Calculus 3
    AE.critical_tracking.append(engine.read_course("MAP2302"))   # Elementary Differential Equations
    AE.critical_tracking.append(engine.read_course("PHY2048"))   # Physics with Calculus 1
    AE.critical_tracking.append(engine.read_course("PHY2048L"))  # Physics with Calculus 1 Laboratory
    AE.critical_tracking.append(engine.read_course("PHY2049"))   # Physics with Calculus 2
    AE.critical_tracking.append(engine.read_course("PHY2049L"))  # Physics with Calculus 2 Laboratory

    # Required Courses (Excluding Critical Tracking Courses)
    AE.required.append(engine.read_course("EGM2511"))  # Engineering Mechanics - Statics
    AE.required.append(engine.read_course("EGM3401"))  # Engineering Mechanics - Dynamics
    AE.required.append(engine.read_course("EGM3520"))  # Mechanics of Materials
    AE.required.append(engine.read_course("EGM3344"))  # Numerical Methods for Engineering
    AE.required.append(engine.read_course("EML3100"))  # Thermodynamics
    AE.required.append(engine.read_course("EML4140"))  # Heat Transfer
    AE.required.append(engine.read_course("EML4312"))  # Control of Mechanical Systems
    AE.required.append(engine.read_course("EAS2011"))  # Introduction to Aerospace Engineering
    AE.required.append(engine.read_course("EAS4101"))  # Aerodynamics
    AE.required.append(engine.read_course("EAS4200"))  # Aerospace Structures
    AE.required.append(engine.read_course("EAS4300"))  # Aerospace Propulsion
    AE.required.append(engine.read_course("EAS4400"))  # Stability and Control of Aerospace Vehicles
    AE.required.append(engine.read_course("EAS4510"))  # Astrodynamics
    AE.required.append(engine.read_course("EAS4810C"))  # Aerospace Sciences Laboratory

    # Aerospace Design Courses
    AE.groups.append(
        RequiredGroup(
            name="Aerospace Design 1",
            credits=3,
            courses=[engine.read_course("EAS4700")],  # Aerospace Design 1
        )
    )
    AE.groups.append(
        RequiredGroup(
            name="Aerospace Design 2",
            credits=3,
            courses=[engine.read_course("EAS4710")],  # Aerospace Design 2
        )
    )

    # Technical Electives
    AE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=6)
    engine.add_to_group(
        AE_TECH_ELECTIVES,
        "^(EAS4|EML4|EGM4|EGN4|MAE4|PHY4)",
    )
    AE.groups.append(AE_TECH_ELECTIVES)

    engine.write(AE)

    BE = Major(
    name="Biological Engineering",
)

    # Critical Tracking Courses (NOT in Required Courses)
    BE.critical_tracking.append(engine.read_course("CHM2045"))   # General Chemistry 1
    BE.critical_tracking.append(engine.read_course("CHM2045L"))  # General Chemistry 1 Laboratory
    BE.critical_tracking.append(engine.read_course("MAC2311"))   # Analytic Geometry and Calculus 1
    BE.critical_tracking.append(engine.read_course("MAC2312"))   # Analytic Geometry and Calculus 2
    BE.critical_tracking.append(engine.read_course("MAC2313"))   # Analytic Geometry and Calculus 3
    BE.critical_tracking.append(engine.read_course("MAP2302"))   # Elementary Differential Equations
    BE.critical_tracking.append(engine.read_course("PHY2048"))   # Physics with Calculus 1
    BE.critical_tracking.append(engine.read_course("PHY2048L"))  # Physics with Calculus 1 Laboratory
    BE.critical_tracking.append(engine.read_course("PHY2049"))   # Physics with Calculus 2
    BE.critical_tracking.append(engine.read_course("PHY2049L"))  # Physics with Calculus 2 Laboratory
    BE.critical_tracking.append(engine.read_course("BSC2010"))   # Integrated Principles of Biology 1
    BE.critical_tracking.append(engine.read_course("BSC2010L"))  # Integrated Principles of Biology 1 Laboratory

    # Required Courses (Excluding Critical Tracking Courses)
    BE.required.append(engine.read_course("ABE2012C"))  # Introduction to Biological Engineering
    BE.required.append(engine.read_course("ABE3000C"))  # Applications in Biological Engineering
    BE.required.append(engine.read_course("ABE3212C"))  # Land and Water Resources Engineering
    BE.required.append(engine.read_course("ABE3612C"))  # Heat and Mass Transfer in Biological Systems
    BE.required.append(engine.read_course("ABE3652C"))  # Physical and Rheological Properties of Biological Materials
    BE.required.append(engine.read_course("ABE4042C"))  # Biological Engineering Design 1
    BE.required.append(engine.read_course("ABE4043C"))  # Biological Engineering Design 2
    BE.required.append(engine.read_course("ABE4931"))   # Professional Issues in Agricultural and Biological Engineering
    BE.required.append(engine.read_course("CHM2200"))   # Organic Chemistry
    BE.required.append(engine.read_course("STA3032"))   # Engineering Statistics
    BE.required.append(engine.read_course("EGM2511"))   # Engineering Mechanics - Statics
    BE.required.append(engine.read_course("EGM3520"))   # Mechanics of Materials
    BE.required.append(engine.read_course("CGN3421"))   # Computer Methods in Civil Engineering
    BE.required.append(engine.read_course("ENV3040C"))  # Basic Environmental Engineering

    # Concentration Groups
    # Example for Biosystems Engineering Concentration
    BE.groups.append(
        RequiredGroup(
            name="Biosystems Engineering Concentration",
            credits=12,
            courses=[
                engine.read_course("ABE4033"),  # Fundamentals and Applications of Biosensors
                engine.read_course("ABE4662"),  # Quantification of Biological Processes
                engine.read_course("ABE4812"),  # Food and Bioprocess Engineering Unit Operations
                engine.read_course("ABE4905"),  # Independent Study
            ],
        )
    )

    # Technical Electives
    BE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=6)
    engine.add_to_group(
        BE_TECH_ELECTIVES,
        "^(ABE4|EGN4|EGS4|ENV4|CHM4|BSC4|PHY4)",
    )
    BE.groups.append(BE_TECH_ELECTIVES)

    engine.write(BE)

    print("Adding Chemical Engineering...")
    CHE = Major(
        name="Chemical Engineering",
    )

    # Required Courses
    CHE.required.append(engine.read_course("BME3406"))
    CHE.required.append(engine.read_course("COT3502"))
    CHE.required.append(engine.read_course("ECH2934"))
    CHE.required.append(engine.read_course("ECH3023"))
    CHE.required.append(engine.read_course("ECH3101"))
    CHE.required.append(engine.read_course("ECH3203"))
    CHE.required.append(engine.read_course("ECH3223"))
    CHE.required.append(engine.read_course("ECH3264"))
    CHE.required.append(engine.read_course("ECH4224L"))
    CHE.required.append(engine.read_course("ECH4404L"))
    CHE.required.append(engine.read_course("ECH4504"))
    CHE.required.append(engine.read_course("ECH4604"))
    CHE.required.append(engine.read_course("ECH4644"))
    CHE.required.append(engine.read_course("ECH4714"))
    CHE.required.append(engine.read_course("ECH4824"))

    # Critical Tracking
    CHE.critical_tracking.append(engine.read_course("CHM2045"))
    CHE.critical_tracking.append(engine.read_course("CHM2046"))
    CHE.critical_tracking.append(engine.read_course("MAC2311"))
    CHE.critical_tracking.append(engine.read_course("MAC2312"))
    CHE.critical_tracking.append(engine.read_course("MAC2313"))
    CHE.critical_tracking.append(engine.read_course("MAP2302"))
    CHE.critical_tracking.append(engine.read_course("PHY2048"))
    CHE.critical_tracking.append(engine.read_course("PHY2049"))

    # Technical Electives
    CHE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        CHE_TECH_ELECTIVES,
        "^(?!.*(BME3406|COT3502|ECH2934|ECH3023|ECH3101|ECH3203|ECH3223|ECH3264|ECH4224L|ECH4404L|ECH4504|ECH4604|ECH4644|ECH4714|ECH4824|CHM2045|CHM2046|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(ECH4|CHM4|BME4|EGN4|ENV4|EMA4|EEL4|EGS4|EGM4|EML4|COT3|COT4|COP3|COP4|MAP4|MAC4|STA4|PHY3|PHY4|PHZ3|PHZ4)",
    )

    CHE.groups.append(CHE_TECH_ELECTIVES)

    engine.write(CHE)
    print("Done!")

    print("Adding Civil Engineering...")
    CIV = Major(
    name="Civil Engineering",
    )

    # Required Courses
    CIV.required.append(engine.read_course("CGN2328"))  # Technical Drawing and Visualization
    CIV.required.append(engine.read_course("CGN3710"))  # Experimentation and Instrumentation in Civil Engineering
    CIV.required.append(engine.read_course("CGN3421"))  # Computer Methods in Civil Engineering
    CIV.required.append(engine.read_course("CGN4160"))  # Civil Engineering Practice
    CIV.required.append(engine.read_course("CGN3501C"))  # Civil Engineering Materials
    CIV.required.append(engine.read_course("CEG4011"))  # Soil Mechanics
    CIV.required.append(engine.read_course("CES3102"))  # Mechanics of Engineering Structures
    CIV.required.append(engine.read_course("CWR3201"))  # Hydrodynamics
    CIV.required.append(engine.read_course("TTE4004C"))  # Transportation Engineering
    CIV.required.append(engine.read_course("EGM2511"))  # Engineering Mechanics: Statics
    CIV.required.append(engine.read_course("EGM3400"))  # Elements of Dynamics
    CIV.required.append(engine.read_course("EGM3520"))  # Mechanics of Materials
    CIV.required.append(engine.read_course("EEL3003"))  # Elements of Electrical Engineering

    # Critical Tracking Courses
    CIV.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    CIV.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    CIV.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    CIV.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    CIV.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    CIV.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    CIV.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Technical Electives
    CIV_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        CIV_TECH_ELECTIVES,
        "^(?!.*(CGN2328|CGN3710|CGN3421|CGN4160|CGN3501C|CEG4011|CES3102|CWR3201|TTE4004C|EGM2511|EGM3400|EGM3520|EEL3003|CHM2045|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(CEG4|CES4|CGN4|CWR4|TTE4|ENV4|SUR4|EGN4|EMA4|EEL4|EGS4|EGM4|EML4|COT3|COT4|COP3|COP4|MAP4|MAC4|STA4|PHY3|PHY4|PHZ3|PHZ4)",
    )

    CIV.groups.append(CIV_TECH_ELECTIVES)

    engine.write(CIV)
    print("Done!")

    print("Adding Coastal and Oceanographic Engineering...")
    COE = Major(
        name="Coastal and Oceanographic Engineering",
    )

    # Required Courses
    COE.required.append(engine.read_course("EGM5816"))  # Intermediate Fluid Dynamics
    COE.required.append(engine.read_course("EOC6196"))  # Littoral Processes
    COE.required.append(engine.read_course("EOC6430"))  # Coastal Structures
    COE.required.append(engine.read_course("OCP6050"))  # Physical Oceanography
    COE.required.append(engine.read_course("OCP6165"))  # Ocean Waves I: Linear Theory
    COE.required.append(engine.read_course("OCP6168"))  # Data Analysis Techniques for Coastal and Ocean Engineers

    # Critical Tracking Courses
    COE.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    COE.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    COE.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    COE.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    COE.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    COE.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    COE.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Technical Electives
    COE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        COE_TECH_ELECTIVES,
        "^(?!.*(EGM5816|EOC6196|EOC6430|OCP6050|OCP6165|OCP6168|CHM2045|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(EOC6|OCP6|EGM6|CGN6|CEG6|CES6|CWR6|TTE6|ENV6|SUR6|EGN6|EMA6|EEL6|EGS6|EGM6|EML6|COT6|COP6|MAP6|MAC6|STA6|PHY6|PHZ6)",
    )

    COE.groups.append(COE_TECH_ELECTIVES)

    engine.write(COE)
    print("Done!")

    print("Adding Digital Arts and Sciences...")
    DAS = Major(
        name="Digital Arts and Sciences",
    )

    # Required Courses
    DAS.required.append(engine.read_course("DIG3713C"))  # Game Design Practices
    DAS.required.append(engine.read_course("DIG3873"))  # Game Systems Development
    DAS.required.append(engine.read_course("DIG4151C"))  # Digital Audio
    DAS.required.append(engine.read_course("DIG4293"))  # Applied Digital Media Protocols
    DAS.required.append(engine.read_course("DIG4527C"))  # Game Design and Production
    DAS.required.append(engine.read_course("DIG4715C"))  # Game Development
    DAS.required.append(engine.read_course("DIG4932"))  # Colloquium in Digital Arts and Sciences
    DAS.required.append(engine.read_course("DIG4940"))  # Internship

    # Critical Tracking Courses
    DAS.critical_tracking.append(engine.read_course("DIG2005"))  # Introduction to Digital Technologies
    DAS.critical_tracking.append(engine.read_course("DIG2021"))  # Foundations of Digital Culture
    DAS.critical_tracking.append(engine.read_course("DIG2121"))  # Principles of Digital Visualization
    DAS.critical_tracking.append(engine.read_course("DIG3020"))  # Foundations of Digital Arts and Sciences
    DAS.critical_tracking.append(engine.read_course("DIG3171"))  # Interdisciplinary Design Methods for Digital Arts and Sciences

    # Technical Electives
    DAS_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        DAS_TECH_ELECTIVES,
        "^(?!.*(DIG3713C|DIG3873|DIG4151C|DIG4293|DIG4527C|DIG4715C|DIG4932|DIG4940|DIG2005|DIG2021|DIG2121|DIG3020|DIG3171)).*^(DIG3|DIG4)",
    )

    DAS.groups.append(DAS_TECH_ELECTIVES)

    engine.write(DAS)
    print("Done!")

    print("Adding Electrical Engineering...")
    EE = Major(
        name="Electrical Engineering",
    )

    # Required Courses
    EE.required.append(engine.read_course("EEL3000"))  # Introduction to Electrical and Computer Engineering
    EE.required.append(engine.read_course("EEL3111C"))  # Circuits 1
    EE.required.append(engine.read_course("EEL3112"))  # Circuits 2
    EE.required.append(engine.read_course("EEL3135"))  # Signals and Systems
    EE.required.append(engine.read_course("EEL3701C"))  # Digital Logic and Computer Systems
    EE.required.append(engine.read_course("EEL3744C"))  # Microprocessor Applications
    EE.required.append(engine.read_course("EEL3923C"))  # Electrical Engineering Design 1
    EE.required.append(engine.read_course("EEL4924C"))  # Electrical Engineering Design 2
    EE.required.append(engine.read_course("EEL3472C"))  # Electromagnetic Fields and Applications 1
    EE.required.append(engine.read_course("EEL4514C"))  # Communication Systems and Components
    EE.required.append(engine.read_course("EEL4657C"))  # Linear Control Systems
    EE.required.append(engine.read_course("EEL3211C"))  # Basic Electric Energy Engineering
    EE.required.append(engine.read_course("EEL3308C"))  # Electronic Circuits 1

    # Critical Tracking Courses
    EE.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    EE.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    EE.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    EE.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    EE.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    EE.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    EE.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Technical Electives
    EE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=17)

    engine.add_to_group(
        EE_TECH_ELECTIVES,
        "^(?!.*(EEL3000|EEL3111C|EEL3112|EEL3135|EEL3701C|EEL3744C|EEL3923C|EEL4924C|EEL3472C|EEL4514C|EEL4657C|EEL3211C|EEL3308C|CHM2045|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(EEL4|EEL5|EEL6|EEL7|EEL8|EEL9|EEL10|EEL11|EEL12|EEL13|EEL14|EEL15|EEL16|EEL17|EEL18|EEL19|EEL20|EEL21|EEL22|EEL23|EEL24|EEL25|EEL26|EEL27|EEL28|EEL29|EEL30|EEL31|EEL32|EEL33|EEL34|EEL35|EEL36|EEL37|EEL38|EEL39|EEL40|EEL41|EEL42|EEL43|EEL44|EEL45|EEL46|EEL47|EEL48|EEL49|EEL50|EEL51|EEL52|EEL53|EEL54|EEL55|EEL56|EEL57|EEL58|EEL59|EEL60|EEL61|EEL62|EEL63|EEL64|EEL65|EEL66|EEL67|EEL68|EEL69|EEL70|EEL71|EEL72|EEL73|EEL74|EEL75|EEL76|EEL77|EEL78|EEL79|EEL80|EEL81|EEL82|EEL83|EEL84|EEL85|EEL86|EEL87|EEL88|EEL89|EEL90|EEL91|EEL92|EEL93|EEL94|EEL95|EEL96|EEL97|EEL98|EEL99)",
    )

    EE.groups.append(EE_TECH_ELECTIVES)

    engine.write(EE)
    print("Done!")
    
    print("Adding Environmental Engineering...")
    ENV = Major(
        name="Environmental Engineering",
    )

    # Required Courses
    ENV.required.append(engine.read_course("ENV3040C"))  # Environmental Engineering
    ENV.required.append(engine.read_course("ENV3040L"))  # Environmental Engineering Lab
    ENV.required.append(engine.read_course("ENV3930"))   # Environmental Engineering Seminar
    ENV.required.append(engine.read_course("ENV4101"))   # Elements of Atmospheric Pollution
    ENV.required.append(engine.read_course("ENV4120"))   # Air Pollution Control Design
    ENV.required.append(engine.read_course("ENV4351"))   # Solid and Hazardous Waste Management
    ENV.required.append(engine.read_course("ENV4430"))   # Water Treatment Process Design
    ENV.required.append(engine.read_course("ENV4514C"))  # Water and Wastewater Treatment
    ENV.required.append(engine.read_course("ENV4601"))   # Environmental Resources Management
    ENV.required.append(engine.read_course("ENV4612"))   # Sustainability and Environmental Restoration

    # Critical Tracking Courses
    ENV.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    ENV.critical_tracking.append(engine.read_course("CHM2046"))  # General Chemistry 2
    ENV.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    ENV.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    ENV.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    ENV.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    ENV.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    ENV.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Technical Electives
    ENV_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        ENV_TECH_ELECTIVES,
        "^(?!.*(ENV3040C|ENV3040L|ENV3930|ENV4101|ENV4120|ENV4351|ENV4430|ENV4514C|ENV4601|ENV4612|CHM2045|CHM2046|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(ENV4|ENV5|ENV6|ENV7|ENV8|ENV9|ENV10|ENV11|ENV12|ENV13|ENV14|ENV15|ENV16|ENV17|ENV18|ENV19|ENV20|ENV21|ENV22|ENV23|ENV24|ENV25|ENV26|ENV27|ENV28|ENV29|ENV30|ENV31|ENV32|ENV33|ENV34|ENV35|ENV36|ENV37|ENV38|ENV39|ENV40|ENV41|ENV42|ENV43|ENV44|ENV45|ENV46|ENV47|ENV48|ENV49|ENV50|ENV51|ENV52|ENV53|ENV54|ENV55|ENV56|ENV57|ENV58|ENV59|ENV60|ENV61|ENV62|ENV63|ENV64|ENV65|ENV66|ENV67|ENV68|ENV69|ENV70|ENV71|ENV72|ENV73|ENV74|ENV75|ENV76|ENV77|ENV78|ENV79|ENV80|ENV81|ENV82|ENV83|ENV84|ENV85|ENV86|ENV87|ENV88|ENV89|ENV90|ENV91|ENV92|ENV93|ENV94|ENV95|ENV96|ENV97|ENV98|ENV99)",
    )

    ENV.groups.append(ENV_TECH_ELECTIVES)

    engine.write(ENV)
    print("Done!")

    print("Adding Industrial and Systems Engineering...")
    ISE = Major(
        name="Industrial and Systems Engineering",
    )

    # Required Courses
    ISE.required.append(engine.read_course("EIN2002"))   # Introduction to Industrial and Systems Engineering
    ISE.required.append(engine.read_course("EIN3354"))   # Engineering Economy
    ISE.required.append(engine.read_course("EIN3451"))   # Industrial Quality Control
    ISE.required.append(engine.read_course("EIN4243"))   # Human Factors and Ergonomics
    ISE.required.append(engine.read_course("EIN4335"))   # Systems Engineering
    ISE.required.append(engine.read_course("EIN4360C"))  # Facilities Planning and Work Design
    ISE.required.append(engine.read_course("EIN4453"))   # Manufacturing Systems Engineering
    ISE.required.append(engine.read_course("ESI3327C"))  # Matrix and Numerical Methods in Systems Engineering
    ISE.required.append(engine.read_course("ESI4313"))   # Operations Research 2
    ISE.required.append(engine.read_course("ESI4356"))   # Decision Support Systems for ISEs
    ISE.required.append(engine.read_course("ESI4610"))   # Introduction to Data Analytics
    ISE.required.append(engine.read_course("ESI4611"))   # Advanced Data Analytics
    ISE.required.append(engine.read_course("ESI4523"))   # Industrial Systems Simulation
    ISE.required.append(engine.read_course("EEL3003"))   # Elements of Electrical Engineering
    ISE.required.append(engine.read_course("EGM2511"))   # Engineering Mechanics: Statics
    ISE.required.append(engine.read_course("EML2023"))   # Computer Aided Graphics and Design
    ISE.required.append(engine.read_course("EML3100"))   # Thermodynamics

    # Critical Tracking Courses
    ISE.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    ISE.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    ISE.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    ISE.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    ISE.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    ISE.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    ISE.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2

    # Technical Electives
    ISE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        ISE_TECH_ELECTIVES,
        "^(?!.*(EIN2002|EIN3354|EIN3451|EIN4243|EIN4335|EIN4360C|EIN4453|ESI3327C|ESI4313|ESI4356|ESI4610|ESI4611|ESI4523|EEL3003|EGM2511|EML2023|EML3100|CHM2045|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(EIN4|ESI4|EGM4|EML4|EEL4|COP4|STA4|MAP4|MAC4|PHY4)",
    )

    ISE.groups.append(ISE_TECH_ELECTIVES)

    engine.write(ISE)
    print("Done!")

    print("Adding Materials Science and Engineering...")
    MSE = Major(
        name="Materials Science and Engineering",
    )

    # Required Courses
    MSE.required.append(engine.read_course("EMA3010"))  # Introduction to Materials
    MSE.required.append(engine.read_course("EMA3011"))  # Fundamental Principles of Materials
    MSE.required.append(engine.read_course("EMA3050"))  # Introduction to Inorganic Materials
    MSE.required.append(engine.read_course("EMA3066"))  # Introduction to Organic Materials
    MSE.required.append(engine.read_course("EMA3080C"))  # Materials Laboratory 1
    MSE.required.append(engine.read_course("EMA3013C"))  # Materials Laboratory 2
    MSE.required.append(engine.read_course("EMA3413"))  # Electronic Properties of Materials
    MSE.required.append(engine.read_course("EMA3513C"))  # Analysis of the Structure of Materials
    MSE.required.append(engine.read_course("EMA4223"))  # Mechanical Behavior of Materials
    MSE.required.append(engine.read_course("EMA4324"))  # Thermodynamics of Materials
    MSE.required.append(engine.read_course("EMA4125"))  # Transport Phenomena in Materials Processing
    MSE.required.append(engine.read_course("EMA4714"))  # Materials Selection and Failure Analysis
    MSE.required.append(engine.read_course("ENC3246"))  # Professional Communication for Engineers

    # Critical Tracking Courses
    MSE.critical_tracking.append(engine.read_course("CHM2045"))  # General Chemistry 1
    MSE.critical_tracking.append(engine.read_course("CHM2045L"))  # General Chemistry 1 Laboratory
    MSE.critical_tracking.append(engine.read_course("CHM2046"))  # General Chemistry 2
    MSE.critical_tracking.append(engine.read_course("CHM2046L"))  # General Chemistry 2 Laboratory
    MSE.critical_tracking.append(engine.read_course("MAC2311"))  # Analytic Geometry and Calculus 1
    MSE.critical_tracking.append(engine.read_course("MAC2312"))  # Analytic Geometry and Calculus 2
    MSE.critical_tracking.append(engine.read_course("MAC2313"))  # Analytic Geometry and Calculus 3
    MSE.critical_tracking.append(engine.read_course("MAP2302"))  # Elementary Differential Equations
    MSE.critical_tracking.append(engine.read_course("PHY2048"))  # Physics with Calculus 1
    MSE.critical_tracking.append(engine.read_course("PHY2048L"))  # Laboratory for Physics with Calculus 1
    MSE.critical_tracking.append(engine.read_course("PHY2049"))  # Physics with Calculus 2
    MSE.critical_tracking.append(engine.read_course("PHY2049L"))  # Laboratory for Physics with Calculus 2

    # Technical Electives
    MSE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        MSE_TECH_ELECTIVES,
        "^(?!.*(EMA3010|EMA3011|EMA3050|EMA3066|EMA3080C|EMA3013C|EMA3413|EMA3513C|EMA4223|EMA4324|EMA4125|EMA4714|ENC3246|CHM2045|CHM2045L|CHM2046|CHM2046L|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2048L|PHY2049|PHY2049L)).*^(EMA4|EMA5|EMA6|EMA7|EMA8|EMA9|EMA10|EMA11|EMA12|EMA13|EMA14|EMA15|EMA16|EMA17|EMA18|EMA19|EMA20|EMA21|EMA22|EMA23|EMA24|EMA25|EMA26|EMA27|EMA28|EMA29|EMA30|EMA31|EMA32|EMA33|EMA34|EMA35|EMA36|EMA37|EMA38|EMA39|EMA40|EMA41|EMA42|EMA43|EMA44|EMA45|EMA46|EMA47|EMA48|EMA49|EMA50|EMA51|EMA52|EMA53|EMA54|EMA55|EMA56|EMA57|EMA58|EMA59|EMA60|EMA61|EMA62|EMA63|EMA64|EMA65|EMA66|EMA67|EMA68|EMA69|EMA70|EMA71|EMA72|EMA73|EMA74|EMA75|EMA76|EMA77|EMA78|EMA79|EMA80|EMA81|EMA82|EMA83|EMA84|EMA85|EMA86|EMA87|EMA88|EMA89|EMA90|EMA91|EMA92|EMA93|EMA94|EMA95|EMA96|EMA97|EMA98|EMA99)",
    )

    MSE.groups.append(MSE_TECH_ELECTIVES)

    engine.write(MSE)
    print("Done!")

    print("Adding Mechanical Engineering...")
    ME = Major(
        name="Mechanical Engineering",
    )

    # Required Courses
    ME.required.append(engine.read_course("EML2023"))    # Computer Aided Graphics and Design
    ME.required.append(engine.read_course("EML2322L"))   # Design and Manufacturing Laboratory
    ME.required.append(engine.read_course("EML3005"))    # Mechanical Engineering Design 1
    ME.required.append(engine.read_course("EML3100"))    # Thermodynamics
    ME.required.append(engine.read_course("EML3301C"))   # Mechanics of Materials Laboratory
    ME.required.append(engine.read_course("EML4140"))    # Heat Transfer
    ME.required.append(engine.read_course("EML4147C"))   # Thermal Sciences Design and Laboratory
    ME.required.append(engine.read_course("EML4312"))    # Control of Mechanical Engineering Systems
    ME.required.append(engine.read_course("EML4314C"))   # Dynamics and Controls System Design Laboratory
    ME.required.append(engine.read_course("EML4321"))    # Manufacturing Engineering
    ME.required.append(engine.read_course("EML4501"))    # Mechanical Engineering Design 2
    ME.required.append(engine.read_course("EML4502"))    # Mechanical Engineering Design 3
    ME.required.append(engine.read_course("EGN3353C"))   # Fluid Mechanics
    ME.required.append(engine.read_course("EEL3003"))    # Elements of Electrical Engineering
    ME.required.append(engine.read_course("EGM2511"))    # Engineering Mechanics: Statics
    ME.required.append(engine.read_course("EGM3344"))    # Introduction to Numerical Methods of Engineering Analysis
    ME.required.append(engine.read_course("EGM3401"))    # Engineering Mechanics: Dynamics
    ME.required.append(engine.read_course("EGM3520"))    # Mechanics of Materials
    ME.required.append(engine.read_course("EMA3010"))    # Introduction to Materials Science and Engineering
    ME.required.append(engine.read_course("ENC3246"))    # Professional Communication for Engineers

    # Critical Tracking Courses
    ME.critical_tracking.append(engine.read_course("CHM2045"))     # General Chemistry 1
    ME.critical_tracking.append(engine.read_course("CHM2045L"))    # General Chemistry 1 Laboratory
    ME.critical_tracking.append(engine.read_course("MAC2311"))     # Analytic Geometry and Calculus 1
    ME.critical_tracking.append(engine.read_course("MAC2312"))     # Analytic Geometry and Calculus 2
    ME.critical_tracking.append(engine.read_course("MAC2313"))     # Analytic Geometry and Calculus 3
    ME.critical_tracking.append(engine.read_course("MAP2302"))     # Elementary Differential Equations
    ME.critical_tracking.append(engine.read_course("PHY2048"))     # Physics with Calculus 1
    ME.critical_tracking.append(engine.read_course("PHY2048L"))    # Physics with Calculus 1 Laboratory
    ME.critical_tracking.append(engine.read_course("PHY2049"))     # Physics with Calculus 2
    ME.critical_tracking.append(engine.read_course("PHY2049L"))    # Physics with Calculus 2 Laboratory

    # Technical Electives
    ME_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        ME_TECH_ELECTIVES,
        "^(?!.*(EML2023|EML2322L|EML3005|EML3100|EML3301C|EML4140|EML4147C|EML4312|EML4314C|EML4321|EML4501|EML4502|EGN3353C|EEL3003|EGM2511|EGM3344|EGM3401|EGM3520|EMA3010|ENC3246|CHM2045|CHM2045L|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2048L|PHY2049|PHY2049L)).*^(EML4|EML5|EML6|EML7|EML8|EML9|EML10|EML11|EML12|EML13|EML14|EML15|EML16|EML17|EML18|EML19|EML20|EML21|EML22|EML23|EML24|EML25|EML26|EML27|EML28|EML29|EML30|EML31|EML32|EML33|EML34|EML35|EML36|EML37|EML38|EML39|EML40|EML41|EML42|EML43|EML44|EML45|EML46|EML47|EML48|EML49|EML50|EML51|EML52|EML53|EML54|EML55|EML56|EML57|EML58|EML59|EML60|EML61|EML62|EML63|EML64|EML65|EML66|EML67|EML68|EML69|EML70|EML71|EML72|EML73|EML74|EML75|EML76|EML77|EML78|EML79|EML80|EML81|EML82|EML83|EML84|EML85|EML86|EML87|EML88|EML89|EML90|EML91|EML92|EML93|EML94|EML95|EML96|EML97|EML98|EML99)",
    )

    ME.groups.append(ME_TECH_ELECTIVES)

    engine.write(ME)
    print("Done!")

    print("Adding Nuclear Engineering...")
    NE = Major(
        name="Nuclear Engineering",
    )

    # Required Courses
    NE.required.append(engine.read_course("ENU4001"))    # Nuclear Engineering Analysis 1
    NE.required.append(engine.read_course("ENU4003"))    # Nuclear Engineering Analysis 2
    NE.required.append(engine.read_course("ENU4103"))    # Reactor Analysis and Computation 1
    NE.required.append(engine.read_course("ENU4104"))    # Reactor Analysis and Computation 2
    NE.required.append(engine.read_course("ENU4134"))    # Reactor Thermal Hydraulics
    NE.required.append(engine.read_course("ENU4145"))    # Risk Assessment and Economic Analysis of Nuclear Systems
    NE.required.append(engine.read_course("ENU4180"))    # Introduction to the Nuclear Fuel Cycle
    NE.required.append(engine.read_course("ENU4191"))    # Elements of Nuclear and Radiological Engineering Design
    NE.required.append(engine.read_course("ENU4192"))    # Nuclear and Radiological Engineering Design
    NE.required.append(engine.read_course("ENU4505L"))   # Nuclear and Radiological Engineering Laboratory 1
    NE.required.append(engine.read_course("ENU4612"))    # Nuclear Radiation Detection and Instrumentation
    NE.required.append(engine.read_course("ENU4612L"))   # Nuclear Radiation Detection and Instrumentation Laboratory
    NE.required.append(engine.read_course("ENU4630"))    # Fundamental Aspects of Radiation Shielding

    # Critical Tracking Courses
    NE.critical_tracking.append(engine.read_course("CHM2045"))     # General Chemistry 1
    NE.critical_tracking.append(engine.read_course("CHM2045L"))    # General Chemistry 1 Laboratory
    NE.critical_tracking.append(engine.read_course("CHM2046"))     # General Chemistry 2
    NE.critical_tracking.append(engine.read_course("MAC2311"))     # Analytic Geometry and Calculus 1
    NE.critical_tracking.append(engine.read_course("MAC2312"))     # Analytic Geometry and Calculus 2
    NE.critical_tracking.append(engine.read_course("MAC2313"))     # Analytic Geometry and Calculus 3
    NE.critical_tracking.append(engine.read_course("MAP2302"))     # Elementary Differential Equations
    NE.critical_tracking.append(engine.read_course("PHY2048"))     # Physics with Calculus 1
    NE.critical_tracking.append(engine.read_course("PHY2048L"))    # Physics with Calculus 1 Laboratory
    NE.critical_tracking.append(engine.read_course("PHY2049"))     # Physics with Calculus 2
    NE.critical_tracking.append(engine.read_course("PHY2049L"))    # Physics with Calculus 2 Laboratory

    # Technical Electives
    NE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=12)

    engine.add_to_group(
        NE_TECH_ELECTIVES,
        "^(?!.*(ENU4001|ENU4003|ENU4103|ENU4104|ENU4134|ENU4145|ENU4180|ENU4191|ENU4192|ENU4505L|ENU4612|ENU4612L|ENU4630|CHM2045|CHM2045L|CHM2046|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2048L|PHY2049|PHY2049L)).*^(ENU4|ENU5|ENU6|ENU7|ENU8|ENU9|ENU10|ENU11|ENU12|ENU13|ENU14|ENU15|ENU16|ENU17|ENU18|ENU19|ENU20|ENU21|ENU22|ENU23|ENU24|ENU25|ENU26|ENU27|ENU28|ENU29|ENU30|ENU31|ENU32|ENU33|ENU34|ENU35|ENU36|ENU37|ENU38|ENU39|ENU40|ENU41|ENU42|ENU43|ENU44|ENU45|ENU46|ENU47|ENU48|ENU49|ENU50|ENU51|ENU52|ENU53|ENU54|ENU55|ENU56|ENU57|ENU58|ENU59|ENU60|ENU61|ENU62|ENU63|ENU64|ENU65|ENU66|ENU67|ENU68|ENU69|ENU70|ENU71|ENU72|ENU73|ENU74|ENU75|ENU76|ENU77|ENU78|ENU79|ENU80|ENU81|ENU82|ENU83|ENU84|ENU85|ENU86|ENU87|ENU88|ENU89|ENU90|ENU91|ENU92|ENU93|ENU94|ENU95|ENU96|ENU97|ENU98|ENU99)",
    )

    NE.groups.append(NE_TECH_ELECTIVES)

    engine.write(NE)
    print("Done!")


    




if __name__ == "__main__":
    sqlite_file_name = (
        pathlib.Path(__file__).parent.resolve().joinpath("../database.db")
    )
    e = DB_Engine(sqlite_file_name)
    populate(e)
