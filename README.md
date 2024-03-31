Last updated 30 March, 2024

### Introduction-to-Computer-Science-II

**Initial class note**: This may be an introduction course to computer science (CS), but that does not mean it will always be easy.  This is a continuation of an introduction to programming design, testing, and implementation concepts using the Python programming language as a tool.  You should also expect to do some reading, much practicing and searching, and much discussion of the topics we cover.


---

### 1. Course description, including expected pre-requisites or co-requisites:

Presents the second course in a three-term sequence that introduces foundational concepts and practices in computer science and software engineering.  Includes coverage of object oriented programming, inheritance, error handling, recursive algorithms, algorithm complexity, and an introduction to abstract data types.  Emphasizes experiences with professional engineering practices.

**Prerequisites**: Introduction to Computer Science I with a grade of \"C\" or better; or constructor consent.

---

### 2. Class Time-space:
1. Lecture + initial demos: asynchronous
2. Lab: W 12-1350, MKH101 and Zoom

---

### 3. Measurable Student Learning Outcomes:

On completion of this course, students will be able to:
1.  Apply concepts of object-oriented programming (OOP) to the design of application solutions for specified problems and to implement advanced OOP structures using the language under study.  
2. Design and implement applications using error and exception handling techniques.  
3. Read, trace, design, and implement recursive algorithms.  
4. Build and use both array-like and linked linear structures to assist in the design and implementation of problem solutions.  
5. Apply professional engineering practices to programming projects.  

### 4. Oregon Statewide General Education Outcomes:

1. Gather, comprehend, and communicate scientific and technical information in order to explore ideas, models, and solutions and generate further questions,  
2. Apply scientific and technical modes of inquiry, individually, and collaboratively, to critically evaluate existing or alternative explanations, solve problems, and make evidence-based decisions in an ethical manner,  
3. Assess the strengths and weaknesses of scientific studies and critically examine the influence of scientific and technical knowledge on human society and the environment.  


---

### 5. Learning resources:

1. **Note:** All class materials will be freely available in a digital format  
2. The Python language – available through several media.  We will discuss this some in class,  
3. A recent Python interpreter (anything from the last couple of years) – I will use the interpreter available from https://www.python.org/downlaods/, we can discuss this more in class,  
4. I will plan to use VS Code as an integrated development environment (IDE), available here: https://code.visualstudio.com/download,
   1. We will discuss some capabilities of IDEs during the course.  
5. (**strongly recommended**) A desire to learn, experiment, design, test, and problem solve with and without code (both on and off of a computer).

### 6. Other course materials required:
1. fairly regular Internet Access (to access our interactive textbook, submit assignments, and participate in remote or  asynchronous discussions),  
2. An email or other online account for communicating with the instructor or fellow students (I use Discord, which we will go over in class),  
3. (optional) A Zoom account (for joining us live remotely),

### 7. Other Learning resources that you might consider using:  
(these are not required, but you might find helpful, along with many other resources we could talk about in class)
1. [A Byte of Python (free and openly accessible!)(in case you need some of the basics!): ](https://python.swaroopch.com/),
2. [Other freely available books online that might help you study topics that interest you: ](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-subjects.md)  

---

### 8. Grading:

1. Assignment grades will be available when the instructor gets to them.  Grades will be made available through our Learning Management System’s gradebook, generally during the week following the submission’s due date.  
   1. My favorite grading method is to have people show me their work throughout the week so we can discuss approaches and improvements.  
  (Don’t worry, I will try to encourage each of you to show me what you have as we get through materials as well, there is no judgment here, just some ideas on improvement, regardless of how well we understand it at first🙂!)  

2. Students are required to at least turn in a draft of each coursework item before 23:59 (Pacific Time Zone) on the date that they are due (generally the first meeting day of the week in my courses, so we have a chance to discuss assignments just before they are due), resubmissions will be allowed and are expected.  Late work will be accepted, but the later the work, the less volume and detailed the feedback will be for that late work.  

3. We will have the following graded coursework items:  
   1. a weekly code-related project (40% overall)(such as programming, design, or writing tests for some programmed solution to a problem), which will have a number of specific requirements (such as, use if statements and loops to accomplish task X, use a function that accomplishes task Y, describe what function Z does, design a program that does T without coding any of it, write a function that tests whether another function returns a specific result A when given inputs B, C, and D),  
   2. a weekly discussion (10% overall)(such as reading an article, tutorial, or someone else’s code and responding to a related prompt); these will generally only have a post (you discussing what you found) and reply requirement (find something related to what someone else originally posted).  
   3. a singular final project (50% overall), which will have a number of specific requirements (similar to weekly projects, just more involved and able to be used to make up for missed work earlier in the course).  

4. Generally each project will include specific requirements (designed to challenge and solidify design, coding, and testing skills) which will be graded with the following in mind:  

   1. **Program Design** (20%)  
       |**Rating** | **Criteria**                                                                 |
       |--------:|--------------------------------------------------------------------------------|
       |20       | Solution well thought out                                                      |
       |10       | Solution partially planned out                                                 |
       |0        | ad hoc solution; program was "designed at the keyboard" or no design submitted |
       
   2. **Program Execution** (20%)  
       |**Rating** | **Criteria**                                                                                    |
       |----------:|-------------------------------------------------------------------------------------------------|
       |20         | Program runs very well under a variety of conditions, as submitted                              |
       |10         | Program runs much of the time, may be missing required files or instructions for libraries used |
       |0          | Program runs very poorly, not at all, or requires several modifications or files before it runs |
            
   3. **Specification Satisfaction** (20%)  
       |**Rating** | **Criteria**                                             |
       |----------:|----------------------------------------------------------|
       |20         | Program satisfies specification completely and correctly |
       |10         | Important parts of the specification not implemented     |
       |0          | Program poorly satisfies specification, or not at all    |   
            
   4. **Coding Style** (20%)  
       |**Rating** | **Criteria**                                                                                         |
       |----------:|------------------------------------------------------------------------------------------------------|
       |20         | Well-formatted, understandable code and appropriate use of language capabilities                     |
       |10         | Code difficult to follow in one reading or poor use of language capabilities                         |
       |0          | Incomprehensible code, poor use of language capabilities, or a need to scroll up and down repeatedly |
            
   5. **Comments and Documentation** (20%)  
       |**Rating** | **Criteria**                                                                                 |
       |----------:|----------------------------------------------------------------------------------------------|
       |20         | Concise, meaningful, and well-formatted comments and other documentation                     |
       |10         | Partial, poorly written, or poorly formatted comments and other documentation                |
       |0          | Wordy, incorrect, badly written or formatted, or none or nearly no comments and documentation|

> **Note**: careful design, systematic testing, consistent style, and readability of code are important software quality factors (all of which are subject to interpretation but graded by the instructor based on the spirit and letter of the requirements, so be sure to explain your decisions).
>
> **Note** **well**: Your submission should be explained and able to be compiled and run from just your submitted files in your final submission for that project. This means that you need to include any files provided to you that are necessary for your project to compile or run, especially mentioning how we get ahold of the version of any third-party libraries that you might link to!
>
> **Note** **very well**: Source code and related documents submitted must be designed and implemented by the student submitting the work and any code must compile and run on one of the instructor\'s machines in order to be graded (to create a working program quickly: get it working simply, then add to it; if at some point it stops compiling you will better know where an error was introduced).
>
> **This means that while you can use tools like tutoring, [Stackoverflow](https://stackoverflow.com/), or AI systems to help you learn how to write code, documentation, tests, and designs from various sources, you need to cite that you got help from outside sources (we all keep tabs open to various resources on the web!), and you need to understand what you create and make any code your own.**

4. **Make-up Work**: I do not care when you learn it, as long as you learn it. To support this idea I allow missing work, even after the term for many, to be made up for in the final project (just be sure I know you are trying to make it up in the final project submission!).

5. **Final grades** will be given out based on the following based on score in the class:\
    90-100%: A  
    80-89%: B  
    70-79%: C  
    60-69%: D  
    00-59%: F  

6. **Reminder**: A passing grade in order to count for course requirements for CS classes is generally a C or above.  

---

### 9 Course Topics List (a more detailed schedule available in [schedule.md](schedule.md)):
| **Week** | **Topics**                                                                                           |
|---------:|:-----------------------------------------------------------------------------------------------------|
|1         |Course intro, variables, conditionals, loops, functions, input, scope, comments, docstrings,          | 
|          |Classes, methods, objects, eval, basic testing ideas, version control systems,                        |
|2         |Files, file IO, reflection, design, testing, type hints, version control systems,                     |
|          |Testing, code style: coding support, organization, decomposition, identification, teamwork, and tools,|
|3         |Recursion: behavior, and structures,                                                                  |
|          |Some interesting features, variables and functions to classes, basic GUIs and components, PyTest,     |
|4         |Communication, access, interfaces, aggregation, more GUIs, Tkinter Canvas class,                      |
|          |Events, MVC, command attribute, command line arguments,                                               |
|5         |More on Canvas, wrapper functions, event listeners, multiple components,                              |
|          |Searching algorithms, more recursion,                                                                 |
|6         |Sorting algorithms, yet more recursion,                                                               |
|          |A bunch of unit testing in pytest, still not yet exhaustive,                                          |
|7         |Inheritance, exceptions, exception classes, polymorphism,                                             |
|          |More GUI components, inheritance, working with custom GUI componnts,                                  |
|8         |Discuss final projects, more work on inheritance and exceptions, start an in-class project,           |
|          |Review class topics, in-class project, final projects,                                                |
|9         |Continue in-class project or help with final projects,                                                |
|10        |Help with final projects, begin final project presentations,                                          |
|11        |Final projects and any last final project presentations.                                              |

---

### 10. Other Administrative Information:

For a list of general administration information (note that this list is not intended to be exhaustive), such as:
1. contacting me (Discord, in-person, or email),
2. accessibility resources,
3. expectations of student conduct,
4. communications,
5. student assistance,
6. miscellany,
7. nondiscrimination & nonharrasment (don't be a jerk to anybody even if you think they deserve it),

(each section contains a number of sub-sections and is not meant to be exhaustive of all situations)  
see my [*Additional Administrative Information*](https://docs.google.com/document/d/1NTerBXVow4rFbZGEpWJKpkpA9DpyOSAfjzJ4FKhf0FU/) "Additional Administrative Information (Google Doc)".

### License
---
Each file included in this repository not otherwise licensed is licensed under the [CC BY License](LICENSE).
