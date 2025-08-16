# Feedback Log

## Feedback Received

**Feedback From:** Jordan Leal-Walker
**When:** 14/08/2025
**What docs checked:** ERD table and chosen database explanation & comparison

>## Feedback on ERD
>
>**Suggestions:**
>
>- Since you're using a physical ERD, add not null values to columns where required
>- You've put default current date for date in attempts, could do the same for climbs (unless that's for future climbs?)
>- 32 characters seems too short for name values based on some preliminary research
>- It's not immediately obvious what attempts and climbs mean and how they interact, i'd need an explanation to provide feedback
>- Gym ratings could benefit from a review date
>- Since gym ratings has a many to one relationship with gym and users it could use both FK's as a composite primary key, unless you have a specific reason for using a separate serial PK
>- Technically one gym could be owned by many companies but for the purpose of this its fine to leave as one to many
>- I'm not sure what difficulty grade you're using but check if it needs a length of 32 characters
>- Upon further review of climbs and attempts, there seems to be no reason for climbs to have user id and be linked directly to users table, as I understand it attempts should be a junction table between users and climbs. One climb can be attempted by many users, one user can attempt many climbs, and again climb_id and user_id could be composite primary key for attempts table
>
>## Feedback on database comparison
>
>**What I like:**
>
>- You mention the data integrity benifits of using SQL
>- You point out the need for validation checks in your API and link that to SQL natively enforcing that
>- You touch on atomicity being important
>- You talk about the inclusion of username and password access and the advantages of SQL for security
>- The lack of need for horizontal scaling is covered and how that relates to NoSQL usage
>- You include a brief section on future considerations
>- You compare the strengths and weaknesses of 3 SQL database systems
>
>**Suggestions:**
>
>- You already cover how atomicity and consistency is relevant to your project, I would enjoy seeing you expand on that by very briefly covering each point in ACID and BASE and comparing which of the 2 sets of properties is more relevant to your API
>- You do a great job comparing 3 SQL database systems, and mentioning why you chose those three to compare would give me greater context
>- Expanding on those comparisons, your strengths and weaknesses are very detailed and I would like to hear why they're a strength or weakness for your project, as well as mention of your familiarity with different systems and how that influenced your choice
>- If you choose too, references to support some of the points you make would increase academic integrity, but it doesn't seem to be a requirement.

## Reflections

- ERD needs further clarity including not null constraints
- some columns makes sense for users familiar with climbing but not for beginner user, needs clarity in purpose and usage statements
- some varchar statements are too limited or not appropriate
- including a brief point covering ACID v BASE would provide further clarity on choosing Relational Database
- comparing the three database management systems could again be more contextual and nuanced
- difficulty_grade examples should be included in the readme Usage Instructions

## Action Plan

1. Add NOT NULL constraints to all required columns
2. Research suggested lenghts of varchar data types and change as required
3. Add a Usage Instructions section to show flow of the app
4. Change purpose of app to include a little more about climbing and how this app is intended to work, as well as future development goals
5. Add ACID and BASE comparison to plan
6. Include further detail and context on the decisions made between the three SQL DBMS

## Implementation

1. NOT NULL constraints added to ERD
2. Changed name variables from 32 to 100 which should cover most extreme edge cases of name lengths for individuals or corporations
3. 
4. Updated README with clearer description of purpose and user stories.
5. 

---

