# Climbing Progression Tracker

This project is a relational database app which tracks user progression of bouldering across a variety of Climbing Gyms.
---

## Table of Contents

1. [Purpose](#purpose-of-the-project)
2. [Installation Guide]
3. [Usage Instructions]
4. [Features and Functionality]
5. [Dependencies]
6. [Ethical Considerations]
7. [Privacy Policy]
8. [Future Development]

---

## Purpose of the Project

This project is created as an assessment for unit DEV1002 of CoderAcademy's FullStack Web Development Boot Camp course. The assessment calls for the creation of a web server linked to a chosen database system. This is designed to ensure a thorough practical application of Database and Server studies, as well as increasing exposure to planning and feedback gathering.

The web server is designed for climbers!

The intended use is to allow users to track progression of their climbing, and to allow non users to see gym ratings to choose a gym that will work for their skill level. Initially the app will rely on users posting data, and only allow users to track their own climbs and attempts. Future development would see the creation of admin roles, allowing for dedicated users to create climbs for a whole gym's set each week.

### Detailed Description

Climbing is an incredibly subjective sport, with a wide variety of skill levels and understanding of climbing terminology, styles of boulder problems, and even of the difficulty grading systems used across multiple gyms. As there is an extreme level of diversity between gyms in Australia, even in Melbourne alone, the majority of data collected is created directly by the users.

Companies which operate gyms often operate multiple locations, but have a centralised website. At the moment there is very little in regard to widely circulated information about the climbs at each gym. Due to this subjectivity I have allowed for users to add their own climbs, as two users may view a climb completely differently depending on skill level and personal style.

One example of a fully realised version of this project is [toplogger](app.toplogger.nu). An app at this scale with an included front end is not currently within my abilities, but is the idealised final product. A major difference between toplogger and my project other than scale, is to allow users to comment on their own climbs, allowing for reflection on progress in a more journalised way. Many climbers experience a plateau or perceived plateau in their climbing abilities at the intermediate level. However incremental increases on particular styles, problems, moves can be logged a little more clearly with the ability to include a fun rating and comments on each attempt.

New climbs are set each week under most normal circumstances, and there can be any number of new climbs on the same amount of wall space at each gym. Difficulty gradings are also not standardised amongst all gyms, and between different countries and continents there are different "standard" difficulty scales used. For the purposes of this app the gym's chosen grading styles will be used (eg. Northside use colour grading system "Yellow" being easiest "Black" being most difficult, BlocHaus use colour grading "Blue" being the easiest "White" being the most difficult, BoulderLab use numbered grading system "1" being the easiest "10" being the most difficult.)

Gyms also vary in the skill levels which are catered for, some gyms offer climbs which are graded as low difficulty but are actually objectively more difficult than other gyms and vice versa. Therefore users are able to recommend the skill level of gyms with their ratings and leave a review with more detail if they would like.

**Primary function:**  
*An app for climbers to check their own progress across multiple gyms.*

Users will create an account with a username and password, which will be linked to all of their personal climbing data. Climbers will first add the climb they are going to work on, including the gym, the style they perceive for the climb, the difficulty grade assigned by the gym, and the date it was set if known. They will then log their attempts on the climb, including a rating of how fun the climb was for them, any comments about the climb and their progress, whether it was completed or not, and finally the date of the attempt. Most users will not carry their phone with them as they are climbing, but can log attempts at a later date or after the session is finished.

**Secondary function:**  
*Allows users to give gyms ratings, and all visitors to check listed gym's difficulty/skill level.*

Users will login and create reviews for the gyms they climb at. The reviews will be for particular gym locations, and will include an overall difficulty rating, as well as a recommended skill level for anyone wishing to climb at the gym. Non-user visitors will be able to check out these reviews individually or to view aggregated results. All users will also be able to check out which gyms a company operates and where they are located.

**User Stories:**  
A *climber* wants to *mark which climbs they have attempted at which gyms, mark it as completed when completed, and check their progression over time so they can keep a record of climbs they have completed, and their comments/reflections on difficult problems* to *track their progression over time*.

Example PostgreSQL output:

```text
 id | user_id | climb_id | fun_rating |                comments                 | completed | attempt_date 
----+---------+----------+------------+-----------------------------------------+-----------+--------------
  1 |       1 |        1 |          4 | This was hard, almost have it           | f         | 2025-02-01
  2 |       1 |        1 |          4 | This was fun! Got it on my second visit | t         | 2025-04-01
  3 |       2 |        3 |          4 | Almost there! just need to try again    | f         | 2025-05-01
  4 |       2 |        3 |          5 | Sent it weeeheew                        | t         | 2025-05-01
  5 |       2 |        4 |          5 | Flashed it!                             | t         | 2025-05-01
```
  
A *beginner climber* wants to *check the difficulty rating of gyms*,  to *pick a beginner friendly gym, and track their progress to see if they improve over time*.

Example PostgreSQL output:

```text
 id | gym_id | user_id | difficulty_rating | recommended_skill_level |                                 review                                  
----+--------+---------+-------------------+-------------------------+-------------------------------------------------------------------------
  1 |      1 |       1 |                 7 | Beginner                | This gym is great for all skill levels, it's beginner friendly
  2 |      2 |       2 |                10 | Intermediate            | This gym has some tough climbs, even the easiest are intermediate level
```

### Functionality

**CRUD Operations**
Users of the API will be able to:

**Create:**
Add gym ratings for each gym
Add climbs as they are set
Add attempts when attempting climbs at gyms
Create user profile with unique email, username, with password login

**Read:**
Selected queries for individual gyms, gym ratings, locations, companies
Aggregate functions for overall gym ratings and checking climbing progression

**Update:**
Update attempt progression and comments
Update user attributes
Update gym rating and review

**Delete:**
Delete their own user profile and all associated relationships
Delete attempts
Delete gym rating

### User Access

Users will create climbs and only be able to view their own climbs, but all data will be held online. At a later date if this app become more widely used, I would initiate admins to create and standardise climbs and difficulties across multiple gyms, but as most gyms in Australia don't follow any standardised difficulty levels this is not applicable at this stage.

Anyone who accesses the site can see gyms and all related entities.

## Diagrams

The data for this project is presented in a non-normalised format below:

![Base Table Data](./assets/images/De-Normalised%20Data.png)

Here is the plan with entities, attributes, relationships.

![Rough Draft of ERD](./assets/images/Concept_ERD.png)

Here is an ERD with cardinality included for all tables.

![ERD with cardinality](./assets/images/Climbing%20Tracker%20-%20ERD%20Diagram.png)

After receiving Feedback the ERD was revised to reflect all NOT NULL columns, as well as more appropriate VARCHAR limits.

![ERD with revised values for VARCHAR and all NOT NULL columns](./assets/images/Climbing%20Tracker%20-%20ERD%20Diagram%20Revised.png)

## Chosen Database System

### Database Decision

**Structured Relationships:**

Pictured in my ERD are the below relationships:

- Company connects to Gym
- Gym connects to Climbs and Gym_Ratings
- Users connects to Attempts, Gym_Ratings, and Climbs
- Climbs connects to Attempts

As I have many related tables to consider in this project, with the User and Gym entities being closely related to multiple other entities, the clearly structured nature of a Relational Database is ideal to ensure the data integrity of these related tables. All connections must be Valid, for example an Attempt cannot exist without a User or Climb. This also protects the database from orphaned records, as upon deleting a Gym, all associated Climbs will be deleted.

In addition, my database uses enumerated data (ENUM) and validation checks which are natively enforced in a relational database.

At the current scale of the project (where I expect a number in the realm of thousands of records), a relational database system with strong ACID compliance is ideal. All attempts and ratings are atomic (all or nothing), so if at any point a server crash occurs, there will be no partial records which could threaten the integrity of the database.

SQL queries for this database are lightweight, able to be enacted using simple joins.

A feature of the app is to allow users to ONLY view their own climbs. Native support for UNIQUE constraints, ACID protection of password and username creation, and strict schema validations (such as for password hash length) is a benefit for creating authorisations.

Relational databases are more easily integrated with other tools to auto-hash passwords.

In future if the scale of the app continues to grow, the addition of roles such as admin/owner are more easy to create and manage.

**Why not NoSQL?:**
A non-relational database would be more appropriate if I required horizontal scalability (was expecting a high number of records in the millions), or if the data being stored was arbitrary or unstructured.

Validation and simple relationships in a NoSQL database require a much larger codebase, and add a lot of unnecessary work. For ENUM and CHECK constraints, a lot of application side checks and extra code would be required to achieve the same level of validation. This means unless you take extra steps with extra code, users can enter incorrect data which would affect any visitors to the site looking for objective data.

Querying data based on the relationships described in my ERD would involve much more complicated queries, which presents more risk for error on the application side.

NoSQL Databases do not enforce foreign key cascading natively, meaning upon deletion of records, querying a non-existant record can lead to errors.

In future a hybrid format including Non-Relational Database systems for Climbs and Attempts could be cool, especially if I wanted to include the ability to post a photo of a climb, or other types of but for the beginning of this app I will focus purely on Relational Databases.

### Database Management System

I will be using the PostgreSQL as my DMS for this project, and SQLite for any error testing, as I am studying this in my CoderAcademy course, and have used SQLite for error testing in my classwork.

I will compare the strengths and weaknesses of PostgreSQL and MySQL below in the context of my project, as well as describing the strengths and weaknesses of SQLite.

**PostgreSQL Strengths:**

- Allows use of JSON, custom data types and advanced joins
- Supports and encourages strict data integrity, especially useful for ENUM and foreign key data
- More scalable than MySQL for heavy record loads
- Always rejects invalid data, and will log errors when invalid data occurs

**PostgreSQL Weaknesses:**

- Harder to setup than SQLite

**MySQL Strengths:**

- Great for simple web apps with fast read requirements
- Faster for read-heavy loads, though due to the scale of the project this is neglible
- Easier setup

**MySQL Weaknesses:**

- Less strict data validation by default, and does not warn when invalid data is entered.
  - Example:
    - username is valid if 32 or below characters.
    - user enters a username of 50 characters
    - MySQL will truncate the data to 32 characters but not flag this by default
    - user now has a username which no longer matches their entry
    - no error is logged by default, so fixing corrupt or invalid data is more difficult

**SQLite Strengths:**

- Best for tiny apps with low or no network traffic
- No setup or server requirements
- Great for testing due to its discrete nature

**SQLite Weaknesses:**

- No user authentication or built in user management
- No concurrent data writing will cause failures if multiple users edit data at once