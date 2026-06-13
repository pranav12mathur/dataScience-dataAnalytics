# task based query 2
 **faculty based database**

1. create a database named "university"

2. create a table named "faculty" with the following columns: faculty_id (primary key), faculty_name, department, and country_id (foreign key referencing the country table) and provides email as unique key in faculty tables.

3. insert at least 5 records into the faculty table.

4. create a table named "courses" with the following columns: course_id (primary key), course_name, and faculty_id (foreign key referencing the faculty table).

5. insert at least 3 records into the courses table.  

6. create a table named "students" with the following columns: student_id (primary key), student_name, age, and country_id (foreign key referencing the country table).

7. insert at least 5 records into the students table.

8. create a table named "enrollments" with the following columns: enrollment_id (primary key), student_id (foreign key referencing the students table), course_id (foreign key referencing the courses table), and enrollment_date.

9. insert at least 5 records into the enrollments table.


10. write a query to select all enrollments along with student names and course names.

11. write a query to find the total number of students enrolled in each course.

12. write a query to find the faculty member teaching the most courses.

13. write a query to update the department of a faculty member with a specific faculty_id.

14. write a query to delete a student with a specific student_id.

**Note: after creating database and tables you will insert some data in that tables then you will apply all the queries on that data to understand better**
 
**answers**
1. create database university;

2. create table country (
    country_id int AUTO_INCREMENT primary key,
    country_name varchar(255)
);
   create table faculty (
    faculty_id int AUTO_INCREMENT primary key,
    faculty_name varchar(255),
    department varchar(255),
    email varchar(255) unique,
    country_id int references country(country_id)
);

3. insert into faculty  values
(null, 'Dr. Smith', 'Computer Science',  'dr.smith@gmail.com', 3),
(null, 'Dr. Johnson', 'Mathematics',  'dr.johnson@gmail.com', 2),
(null, 'Dr. Williams', 'Physics',  'dr.williams@gmail.com', 1),
(null, 'Dr. Brown', 'Mathematics',  'dr.brown@gmail.com', 6),
(null, 'Dr. Davis', 'Computer Science',  'dr.davis@gmail.com', 5),
(null, 'Dr. Miller', 'Computer Science',  'dr.miller@gmail.com', 4);

4. create table courses (
    course_id int AUTO_INCREMENT primary key,
    course_name varchar(255),
    faculty_id int references faculty(faculty_id)
);

5. insert into courses  values
(null, 'Computer Science', 4),
(null, 'Mathematics', 2),
(null, 'Physics', 3);
(null,'Computer Science', 2),
(null, 'Mathematics', 1),
(null, 'Computer Science', 3);

6. create table students (
    student_id int AUTO_INCREMENT primary key,
    student_name varchar(255),
    age int,
    country_id int,
    constraint fk_student_country foreign key (country_id) references country(country_id)
);

7. insert into students  values
(null, 'John', 20, 1),
(null, 'Lionel', 22, 2),
(null, 'Harry', 21, 3),
(null, 'George', 23, 4),
(null, 'Cristiano', 20, 5),
(null, 'Messi', 22, 6);

8. create table enrollments (
    enrollment_id int AUTO_INCREMENT primary key,
    enrollment_date date,
    student_id int,
    course_id int,
    constraint fk_enrollment_student foreign key (student_id) references students(student_id),
    constraint fk_enrollment_course foreign key (course_id) references courses(course_id)
);

9. insert into enrollments values
(null,'2026-01-15',1,1),
(null, '2026-01-16',2, 2),
(null, '2026-01-17',3, 3),
(null, '2026-01-18',4, 1),
(null, '2026-01-19',5, 2);

10. select enrollment_id, student_name, course_name from enrollments e join students s on e.student_id = s.student_id join courses c on e.course_id = c.course_id;

11. select course_name, count(*) as total_students from enrollments e join courses c on e.course_id = c.course_id group by course_name;

12. select faculty_name, count(*) as total_courses from courses c join faculty f on c.faculty_id = f.faculty_id group by faculty_name order by total_courses desc limit 1;

13. update faculty set department = 'Data Science' where faculty_id = 1;

14. delete from enrollements where student_id = 1;
    delete from students where student_id = 1; 