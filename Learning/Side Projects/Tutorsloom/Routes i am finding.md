
```table-of-contents
```
- https://tutorsloom.com/ -> being logged in and not having account is almost shows same structure 
	- Except that navigation in logged in state has ![[Pasted image 20260524164716.png]] things like My Posts, Find Tutors, Wallet, Reviews  and  a `Post Requirement` button
## find-tutors?subject=Physics&location=Islamabad

![[Pasted image 20260524165952.png]]
Searching for tutors go by -> Subject/ Topic and Location, url follows url query params
	  https://tutorsloom.com/find-tutors?subject=Physics&location=Islamabad
- This shows that its definitely using supabase as back-end technology
### Online
```txt
GET https://riirrjpdczuojemhjlcc.supabase.co/rest/v1/teacher_profiles?select=teacher_id,headline,bio,subjects,country,city,hourly_rate_min,hourly_rate_max,rate_currency,experience_years,online_teaching_years,teaching_experience_years,total_experience_years,profile_photo_url,profiles!teacher_profiles_teacher_id_fkey(full_name)&offset=0&limit=10&teaches_online=eq.true 
```
### Home
```txt
GET
	https://riirrjpdczuojemhjlcc.supabase.co/rest/v1/teacher_profiles?select=teacher_id,headline,bio,subjects,country,city,hourly_rate_min,hourly_rate_max,rate_currency,experience_years,online_teaching_years,teaching_experience_years,total_experience_years,profile_photo_url,profiles!teacher_profiles_teacher_id_fkey(full_name)&offset=0&limit=10&teaches_in_person=eq.true
```
### Assignment
```txt
GET
	https://riirrjpdczuojemhjlcc.supabase.co/rest/v1/teacher_profiles?select=teacher_id,headline,bio,subjects,country,city,hourly_rate_min,hourly_rate_max,rate_currency,experience_years,online_teaching_years,teaching_experience_years,total_experience_years,profile_photo_url,profiles!teacher_profiles_teacher_id_fkey(full_name)&offset=0&limit=10&helps_homework=eq.true
```

### All 
```txt
GET
	https://riirrjpdczuojemhjlcc.supabase.co/rest/v1/teacher_profiles?select=teacher_id,headline,bio,subjects,country,city,hourly_rate_min,hourly_rate_max,rate_currency,experience_years,online_teaching_years,teaching_experience_years,total_experience_years,profile_photo_url,profiles!teacher_profiles_teacher_id_fkey(full_name)&offset=0&limit=10
```
- Response
```json
[{"teacher_id":"ad86f800-b612-4b9c-8329-23dd55428727","headline":"O-level Mathematics Teacher","bio":"I am a dedicated Mathematics teacher with a strong focus on building clear concepts and problem-solving skills. My teaching style is simple, structured, and highly interactive, ensuring that students not only understand the “how” but also the “why” behind every concept.\n\nI specialize in breaking down complex topics into easy, step-by-step explanations, making mathematics approachable even for students who struggle with it. My sessions are designed to be exam-focused while also strengthening core understanding, so students can perform confidently in both school assessments and competitive exams.\n\nIn my classes, students can expect:\n• Clear concept building from basics to advanced level\n• Regular practice with past paper and exam-style questions\n• Personalized attention to address weak areas\n• A supportive and motivating learning environment\n• Proven strategies to improve speed, accuracy, and confidence\n\nI believe every student has the potential to excel with the right guidance, and my goal is to help students achieve their best results while developing a genuine understanding of mathematics.","subjects":null,"country":"Pakistan","city":"Islamabad","hourly_rate_min":null,"hourly_rate_max":null,"rate_currency":null,"experience_years":null,"online_teaching_years":1,"teaching_experience_years":2,"total_experience_years":2,"profile_photo_url":"https://riirrjpdczuojemhjlcc.supabase.co/storage/v1/object/public/teacher-photos/ad86f800-b612-4b9c-8329-23dd55428727/profile.jpg?t=1773814964423","profiles":null}, 
 {"teacher_id":"5f40d21a-0df6-4239-a1fe-0b143e83aa0b","headline":"O Level Computer Science Tutor ","bio":"I am a dedicated Mathematics instructor with over 5 years of experience teaching O Level, A Level, and advanced problem-solving mathematics. My goal is not just to help students solve questions, but to build strong concepts that allow them to think independently and confidently.\nMy teaching style focuses on clarity, structure, and deep understanding. I break down complex topics into simple, easy-to-follow steps and guide students from basic concepts to exam-level mastery. Whether it is algebra, trigonometry, calculus, or problem-solving techniques, I ensure that every concept is fully understood before moving forward.\nI specialize in: • O Level & A Level Mathematics\n• Exam preparation and past paper practice\n• Olympiad-style and advanced problem solving\n• Building strong fundamentals for long-term success\nWhat makes my teaching unique is my ability to simplify difficult ideas and train students to approach questions strategically rather than memorizing methods. I also focus on identifying weak areas and improving them through targeted practice and personalized guidance.\nIn my classes, students can expect: • Clear explanations with step-by-step solutions\n• Regular practice and feedback\n• Exam techniques and time management strategies\n• A supportive and focused learning environment\nIf you are looking to improve your grades, strengthen your concepts, or achieve top results in Mathematics, I am here to help you reach that goal.","subjects":null,"country":"Saudi Arabia","city":"Riadh","hourly_rate_min":null,"hourly_rate_max":null,"rate_currency":null,"experience_years":null,"online_teaching_years":5,"teaching_experience_years":1,"total_experience_years":1,"profile_photo_url":"https://riirrjpdczuojemhjlcc.supabase.co/storage/v1/object/public/teacher-photos/5f40d21a-0df6-4239-a1fe-0b143e83aa0b/profile.webp","profiles":null}, 
 {"teacher_id":"ecda1f15-6b55-4bd5-82ad-0ab1183620a5","headline":"O-level Mathematics Tutor","bio":"My students start to love Math.. and when you love something, you always excel at it!","subjects":null,"country":"Pakistan","city":"Islamabad","hourly_rate_min":null,"hourly_rate_max":null,"rate_currency":null,"experience_years":null,"online_teaching_years":2,"teaching_experience_years":14,"total_experience_years":14,"profile_photo_url":"https://riirrjpdczuojemhjlcc.supabase.co/storage/v1/object/public/teacher-photos/ecda1f15-6b55-4bd5-82ad-0ab1183620a5/profile.jpeg","profiles":null}]
```
#### Levels 
##### Beginner
```txt
GET
	https://riirrjpdczuojemhjlcc.supabase.co/rest/v1/teacher_profiles?select=teacher_id,headline,bio,subjects,country,city,hourly_rate_min,hourly_rate_max,rate_currency,experience_years,online_teaching_years,teaching_experience_years,total_experience_years,profile_photo_url,profiles!teacher_profiles_teacher_id_fkey(full_name)&offset=0&limit=10&levels=cs.{Beginner}
```
##### Intermediate
##### Expert
## teacher/islamabad-ad86f800-b612-4b9c-8329-23dd55428727
![[tutorsloom.com_route_teacher.har]]
![[Pasted image 20260524171054.png]]
## /
The dashboard page
![[tutorsloom.com_dashboard.har]]

## student-dashboard/my-jobs
![[tutorsloom.com_myPosts.har]]
This page has sub page or form for creating a `Post Your Study Needs`
## student-dashboard/wallet
![[tutorsloom.com_student-dashboard_wallet.har]]
![[tutorsloom.com_student-dashboard-wallet-history.har]]

## reviews
![[tutorsloom.com_reviews.har]]

## student-dashboard/post-job
- steps resolved are clickable
![[tutorsloom.com_post-requirement-1.har]]![[Pasted image 20260524172309.png]]

![[Pasted image 20260524172320.png]]

![[Pasted image 20260524172405.png]]![[Pasted image 20260524172505.png]]
## student-dashboard/my-jobs

![[tutorsloom.com_submit-post-requirement.har]]![[Pasted image 20260524172553.png]]

## student-dashboard/inbox
![[tutorsloom.com_inbox.har]]![[Pasted image 20260524172726.png]]

## settings
![[tutorsloom.com_settings.har]]![[Pasted image 20260524172824.png]]

## teacher/onboarding
![[tutorsloom.com_teacher-obnboarding-1.har]]

### Basic Details
![[tutorsloom.com_teacher-obnboarding-2-basic-details.har]]

