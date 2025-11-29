### How to integrate Chat App into External Applications
- First of all create a pending registration entry in chat app backend and database
- Then create a pending verification entry
- finally send a verify request to chat app and now a simple sign in should work with chat app
#### Others
Beside this there are few other items to note down'
1. Both frontend and backend domain needs to e configured in CORS_ORIGIN env variable of chat app
2. Eternal Customer backed should have requests to send initSSO request to chat app

Steps
1. Make curl request to generate-credentials
2. Change variables in whatnetplease backend to be taken from .env so that when we deploy backend we have required ALLOWED_DOMAINS from .env, tenantId we sent to create tenant entry in chat database and name of tenant
	1. This will help us when we will make request from Frontend to integrate whatsnextplease to chat app
	2. [x] We will later add these variables to AWS SECRETS MANAGER
- [x] the requets to chat endpoints should be rate limited
- [x] Allowed origins should also contain the frontned of chat itself  staging was missing it )
- [x] There are way too many errors before app gets stable and starts working, figure out why its happening 
- [ ] The erros from chat app should be processed and showed using toast in wnp app
- [ ] the accessToken and refreshToken are not getting saved in production for wnp figure out why and fix it


- [ ] Multiple task agents with same task wtih different deadlines
### Logs System
- [ ] Having Logs for each task so that we can track how a given person did what on which day (Similar to Jira).
	- [ ] Then Handle Multiple people 
### Serial Number Feature
Handle Serial Numbers for the  OR Filter Tasks based on requirements
We have a new feature Handle Serial Numbers for the OR Filter Tasks based on requirements 
- [ ] Client or Company Name followed by Numbers 
- [ ] If they are are duplicates we can go for number as suffix, the client name as suffix
- [ ] Way better Allow clients to search tasks based on Title, Description, Company Name, Priority etc. 
- [ ] There might be a CODE assigned to a given task 
## Context and Background 
- Project Managers in our organization want that there should be some way they can reference the tasks to clients, teams and others usually like in github issues are assigned issue number which can be referenced across whole github , 
- we need somehting like that but it should be simpler and easy to recall so a person can recall it easily. as in notes
- [ ] Edit Client Does not work.
- [ ] Task Supervisors Can Edit Clients as well
- [ ] Ability to assign Clients to a given task
- [ ] Provide login details to Kevin, Dan, Hamza and jeniffer logins for client.
- [ ] Make process for whatnextplease on whimsical
- [ ] When you add or edit task to chose a customer and the project manager 
- [ ] Priority should be defined for clients ( some way they should ) some way to educate them
- [ ] Specify templates for most common tasks to each skill
- [ ] Based on the Task Title and Description we should figure out what should be task category. ( Kind of NLP thing to do )
## Wnp Gantt Chart Stuff

