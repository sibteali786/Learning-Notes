```table-of-contents
```
We have come up with another side quest before we work with Cargo Business,

- Asia Builders, as name suggests this part of business works on constructing houses and then selling them.
- They create Excel Sheet for each house where Master File sheet contains data for received and paid cash to different vendors ( we can pre-add all vendors so we can track them individually as well )
- Fields like Description, Debits, Credits, Balance are self explanatory.
- Fax No shows their own version of track record or Physical file which can they can reference for their own discussion purposes.
- Then we have individual vendors and contractors sheets by their names which show Total amount, paid amount to them

What they want

- Things i know for now
- They want to track each house and its expenses, vendors and contractors expenses they pay since they allocate initial amount to each one and track how much they used from initial amount.
- They want to be able to later show track of each payment made to Government Auditors so that thye haev proof of what expenses they did, how much and where and to whom they did it since its what moslty Auditors require.
- They want to have a dashboard where details about different Projects ( House Projects ) can be seen with summary
- Place where owner can know what how much profit or loss they have in a given project or overall ( different kind of filters can be added in this case by month, by year, by project etc )
- New Contractors and Vendors info can be seen at Birds eye view to identify how much money is debited or credited from a given contractor / vendor for either all or any given project / house.

Have attached the Excel Sheet ( .xlsx ) as well lets see what more insights we can gather from the excel sheet

- Provide suggestions from your own creativity as well how best we can make a really helpfull web application using this info


## Answer 
1. Its ad-hoc as written in sheets their is no mention of milestones, but we can propose it in our proposal or benefits of having milestones, But remember the person entering all this is an accountant, for him creating milestones along with entering data is going to be exhaustive and then also track milestone when it finishes, so i think no need to complicate it further
2. Will answer
3. Its only a sequential number to physical files nothing else
4. Ideally it should be able to edit transactions or request the accountant to by creating a request for edit or proof for any given transaction.
5. No for now lets keep it free, we can decide later if need to pre-define categories 
6. For now lets only deal with PKR ( we can leave room for extensibility but keep it simple for now )
7. Allow both one file or multiple files as well so that if there are multliple reciepents to show a single transaction ( accumulation ) it can be possible.
8. Will answer 
9. Rauf sb is the only income source, no banks if its a bank we can write the name of the bank instead of Rauf Sb so this field sould be editable so we can clearly write who provided capital investment. 
10. yes Excel migration should be possible since they might want to migrate existing project details to newly created website

# Proposal for Asia Builder 
# ASIA BUILDERS - CONSTRUCTION MANAGEMENT SYSTEM

## Software Development Proposal

**Prepared For:** Mr. Rauf Khan, CEO - Asia Group of Companies  
**Prepared By:** Diginammo  
**Date:** January 28, 2026  

---

## EXECUTIVE SUMMARY

This proposal outlines a comprehensive **Desktop Web Application** for Construction Management designed specifically for Asia Builders to digitize and streamline house construction project operations. The system will replace manual Excel-based tracking with an automated platform that provides real-time financial visibility, vendor management, and government-audit-ready reporting.

**Platform:** Desktop/Laptop Web Application (accessible via Chrome, Firefox, Safari, Edge)  
**Access:** Works on Windows, Mac, Linux - any device with a web browser  
**Internet:** Required for real-time data sync across users

**Key Benefits:**

- Track multiple house projects simultaneously with complete financial transparency
- Eliminate manual calculations and reduce human errors
- Generate government audit reports in minutes instead of days
- Access real-time profit/loss across all projects from anywhere (on laptop/desktop)
- Maintain complete payment history with digital receipt storage
- Monitor vendor performance and outstanding payments at a glance

**Investment Required:**

- **MVP (Phase 1):** PKR 350,000 over 3 months
- **Advanced Features (Phase 2):** PKR 250,000 over 2 months
- **Total Investment:** PKR 600,000 over 5 months
- **Mobile App (Optional Add-on):** PKR 400,000 (see Appendix C)

**Return on Investment:**

- Save 15+ hours per month on manual data entry and calculations
- Reduce accounting errors by 90%
- Complete government audit preparation in 1 hour vs 3 days
- Make faster, data-driven investment decisions

---

## CURRENT CHALLENGES & OUR SOLUTION

### What You Face Today:

1. **Manual Excel Management:**
    
    - Maintaining separate Excel files for each project
    - Risk of data loss or corruption
    - Difficult to get overall financial picture across projects
    - Time-consuming to update multiple vendor sheets
2. **Limited Visibility:**
    
    - Hard to know real-time profit/loss
    - Cannot quickly compare performance across projects
    - Difficult to identify which vendors are paid on time
3. **Audit Preparation:**
    
    - Collecting receipts from multiple physical files
    - Manually compiling expense reports
    - Time-intensive process when government auditors request documentation
4. **Investment Tracking:**
    
    - No clear view of where profits are reinvested
    - Difficult to track which project's profit funded what investment

### How Our System Solves This:

✅ **Centralized Platform:** All projects, vendors, and transactions in one secure system  
✅ **Real-Time Dashboard:** See profit/loss across all projects instantly  
✅ **Digital Receipt Storage:** Upload and attach payment proofs directly to transactions  
✅ **One-Click Reports:** Generate audit-ready expense reports in seconds  
✅ **Investment Portfolio:** Track where profits are reinvested with complete traceability  
✅ **Multi-User Access:** Owner can view reports from phone, Accountant enters data, Reviewer audits everything

---

## SYSTEM MODULES & FEATURES

### 📊 **MODULE 1: Project Dashboard**

**What It Does:**  
Provides a bird's-eye view of all ongoing and completed house construction projects.

**Features You'll Use:**

- See all projects on one screen with key metrics (budget, spent, remaining, profit/loss)
- Filter projects by status: Active, Completed, On Hold
- Quick overview cards showing total investment, total expenses, and overall profit
- Click any project to see detailed financial breakdown
- Visual indicators for projects going over budget

**Business Value:**  
Mr. Rauf can open the system on his phone and instantly know the financial health of every project without asking the accountant.

**Example View:**

```
┌─────────────────────────────────────────────────────────┐
│ Total Active Projects: 3                                │
│ Total Investment: PKR 12,000,000                        │
│ Total Profit (Completed): PKR 2,500,000                │
└─────────────────────────────────────────────────────────┘

Project Name        Location        Budget      Spent      Status
─────────────────────────────────────────────────────────────────
Plot 930 G-11/2    Islamabad      5.0M        4.9M       Active
Plot 45 F-10       Islamabad      4.5M        2.1M       Active  
Villa Bahria       Rawalpindi     6.0M        6.0M       Completed
```

---

### 💰 **MODULE 2: Transaction Management**

**What It Does:**  
Records every rupee coming in and going out of each project with complete audit trail.

**Features You'll Use:**

- Add income transactions (Owner investment, bank loan, partner funding)
- Record expense transactions with description, amount, date, and category
- Attach digital receipts/invoices (PDF, images, multiple files per transaction)
- Link transactions to specific vendors/contractors
- Add physical file reference number (your current "Fax No")
- Running balance calculated automatically after each transaction
- Edit or delete transactions with complete history tracking
- Search transactions by date range, vendor name, or amount
- Bulk import existing Excel data for historical projects

**Business Value:**  
Accountant saves 10+ hours per month on manual calculations. No more Excel formula errors. Every payment has digital proof attached.

**Example Entry:**

```
Date: 04-Dec-2025
Description: Paid to Nisar Contractor
Amount: PKR 100,000 (Debit)
Vendor: Nisar Contractor
Physical File: Fax #3
Receipts: [cash_cheque_123.pdf] [delivery_note.jpg]
Balance After Transaction: PKR 246,800
Entered By: Accountant (Shahid)
```

---

### 👷 **MODULE 3: Vendor & Contractor Management**

**What It Does:**  
Maintains complete profiles of all contractors, suppliers, and service providers.

**Features You'll Use:**

- Store vendor details (Name, CNIC, Phone, Address, Bank Account)
- Create vendor agreements with total contract amount
- Track how much has been paid vs how much is pending
- See payment history for each vendor across all projects
- Calculate vendor performance (on-time work completion rate)
- View which projects a specific vendor worked on
- Outstanding balance alerts for vendors waiting for payment
- Generate vendor-specific payment statements

**Business Value:**  
Instantly know "How much do we owe Nisar Contractor?" or "Which vendors have we paid the most?" Useful for negotiating future contracts.

**Example Vendor Profile:**

```
Vendor: Nisar Contractor
Contact: 0300-1234567
CNIC: 12345-6789012-3

Current Agreements:
- Plot 930 G-11/2: PKR 1,400,000 (Paid: 780K, Pending: 620K)
- Plot 45 F-10: PKR 900,000 (Paid: 200K, Pending: 700K)

Total Paid (All Projects): PKR 980,000
Payment History: 12 transactions
Last Payment: 22-Jan-2026 (PKR 100,000)
```

---

### 📈 **MODULE 4: Financial Reports**

**What It Does:**  
Generates professional reports for internal review and government audits.

**Features You'll Use:**

**For Owner:**

- Profit & Loss Statement (per project or overall)
- Cashflow Summary (money in vs money out by month)
- Project Comparison Report (which projects are most profitable)
- Investment Portfolio Summary

**For Reviewer:**

- Expense Breakdown by Category (Materials, Labor, Utilities, etc.)
- Vendor Payment Summary (who got paid how much)
- Date Range Reports (show all transactions between two dates)
- Physical File Cross-Reference Report

**For Government Audit:**

- Complete Expense Register with Payment Proofs
- Vendor Payment Statements with CNIC/NTN details
- Project-wise Income & Expense Summary
- Tax Deduction Reports (if applicable)

**Export Options:**

- PDF (for printing and email)
- Excel (for further analysis)
- Government-approved templates

**Business Value:**  
Generate FBR-ready audit reports in 10 minutes instead of 3 days of manual compilation. Impress auditors with professional documentation.

**Example Report:**

```
═══════════════════════════════════════════════════════════
               PROFIT & LOSS STATEMENT
         Plot 930, Street 55, G-11/2, Islamabad
               Period: Nov 2025 - Jan 2026
═══════════════════════════════════════════════════════════

INCOME
  Owner Investment (Rauf sb)               PKR 4,972,279
                                          ──────────────
  TOTAL INCOME                             PKR 4,972,279

EXPENSES
  Contractors                              PKR 1,080,000
  Materials (Steel, Bricks, Cement)        PKR 2,515,500
  Equipment Rental                         PKR   79,000
  Utilities                                PKR    7,931
  Other                                    PKR 1,260,298
                                          ──────────────
  TOTAL EXPENSES                           PKR 4,942,729

NET PROFIT                                 PKR    29,550
                                          ══════════════
```

---

### 📁 **MODULE 5: Document Management**

**What It Does:**  
Stores all payment receipts, invoices, and proofs digitally with easy retrieval.

**Features You'll Use:**

- Upload unlimited documents (PDF, images, scanned receipts)
- Attach multiple files to single transaction
- Organize by project or vendor automatically
- Search documents by date, vendor, or amount
- Preview documents before downloading
- Batch download all receipts for a project (for audit submission)
- Secure cloud storage with backup

**Business Value:**  
No more searching through physical files. When auditor asks "Show me proof of payment to Nisar on 4th December", find it in 5 seconds.

---

### 💼 **MODULE 6: Investment Portfolio Tracker**

**What It Does:**  
Tracks where project profits are reinvested for complete financial transparency.

**Features You'll Use:**

- Record new investments (property, stocks, business ventures, new projects)
- Link investment to source project (which project's profit funded this)
- Track investment performance over time
- See total capital deployed vs available for reinvestment
- Generate portfolio summary report

**Business Value:**  
Clear visibility of how business profits are growing the overall wealth. Useful for planning future investments.

**Example Investment Entry:**

```
Investment Name: DHA Phase 8 Plot
Amount Invested: PKR 1,500,000
Source: Profit from Plot 930 G-11/2 Project
Date: 15-Jan-2026
Category: Real Estate
Expected Return: 25% in 2 years
Notes: 10 Marla residential plot, Block H
```

---

### 👥 **MODULE 7: User Access Control**

**What It Does:**  
Different team members see only what they need to see based on their role.

**Three User Roles:**

**1. Owner (Mr. Rauf Khan)**

- View all projects, reports, and dashboards
- Cannot add/edit transactions (to prevent accidental changes)
- Can request changes from Accountant if needed
- Desktop browser access from office or home computer
- Optional: Mobile app for on-the-go viewing (see Appendix C)

**2. Accountant (Data Entry)**

- Add new projects and transactions
- Upload payment receipts
- Create vendor profiles
- Generate routine reports
- Cannot delete completed projects (safety control)

**3. Reviewer (Internal Auditor)**

- View all data like Owner
- Edit any transaction with full audit trail
- Approve or request corrections from Accountant
- Access all reports for verification

**Business Value:**  
Prevents unauthorized changes while giving everyone the access they need. Complete audit trail shows who did what and when.

---

## DEVELOPMENT APPROACH - PHASED DELIVERY

We propose a two-phase approach to minimize risk and deliver value quickly:

### **PHASE 1: MVP (Minimum Viable Product)**

**Timeline:** 3 months  
**Platform:** Desktop Web Application (browser-based)  
**Objective:** Get core system operational quickly for immediate use

**Includes:**

- All 7 modules listed above
- Desktop web application accessible from any browser
- Responsive design (works on laptop/desktop screens)
- Excel data import tool
- User authentication and role-based access
- PDF report generation
- Cloud hosting and daily backups

**What You Can Do After Phase 1:** ✅ Stop using Excel for new projects  
✅ Track 3-5 active projects simultaneously  
✅ Generate audit reports for government  
✅ View real-time profit/loss  
✅ Store digital receipts  
✅ Access from office computers/laptops

---

### **PHASE 2: Advanced Features**

**Timeline:** 2 months (starts after Phase 1 completion)  
**Objective:** Add convenience features based on your feedback

**Includes:**

- WhatsApp notifications (payment reminders to vendors)
- Email alerts (weekly summary to Owner)
- Advanced analytics (trend charts, forecasting)
- Custom report builder (design your own reports)
- Bulk operations (pay multiple vendors at once)
- Bank statement import (auto-match transactions)
- Multi-currency support (if needed later)
- Milestone tracking for contractor agreements
- Export to government-approved formats
- Advanced search and filtering
- Audit trail enhancements

**Business Value:**  
These features increase convenience but are not critical for day-to-day operations. We add them after you've used Phase 1 and provided feedback.

**Note:** Mobile and tablet apps are available as a separate add-on (see Appendix C for pricing).

---

## PROJECT TIMELINE WITH MILESTONES

### **PHASE 1 - MVP DEVELOPMENT (12 Weeks)**

```
Month 1 (Weeks 1-4)
├── Week 1-2: Project Setup & Design
│   ├── Database design and setup
│   ├── User interface mockups for approval
│   └── Security infrastructure
├── Week 3: Module 1 - Project Dashboard
│   └── Deliverable: View all projects with basic metrics
└── Week 4: Module 2 - Transaction Management (Part 1)
    └── Deliverable: Add income/expense transactions

Month 2 (Weeks 5-8)
├── Week 5: Module 2 - Transaction Management (Part 2)
│   └── Deliverable: Upload receipts, edit transactions
├── Week 6: Module 3 - Vendor Management
│   └── Deliverable: Create vendors, track agreements
├── Week 7: Module 4 - Financial Reports (Basic)
│   └── Deliverable: Generate P&L, expense summary
└── Week 8: Module 5 - Document Management
    └── Deliverable: Upload/organize receipts

Month 3 (Weeks 9-12)
├── Week 9: Module 6 - Investment Portfolio
│   └── Deliverable: Track profit reinvestment
├── Week 10: Module 7 - User Access Control
│   └── Deliverable: Three user roles operational
├── Week 11: Excel Data Migration Tool
│   └── Deliverable: Import historical project data
└── Week 12: Testing, Training & Deployment
    ├── Bug fixes and refinements
    ├── User training sessions
    └── Go-live support
```

---

### **PHASE 2 - ADVANCED FEATURES (8 Weeks)**

```
Month 4 (Weeks 13-16)
├── Week 13-14: Advanced Analytics & Reporting
│   ├── Visual dashboards with charts
│   ├── Custom report builder
│   └── Forecasting tools
├── Week 15: WhatsApp & Email Notifications
│   └── Deliverable: Automated alerts & reminders
└── Week 16: Bulk Operations & Import Tools
    └── Deliverable: Bank statement import, bulk payments

Month 5 (Weeks 17-20)
├── Week 17: Contractor Milestone Tracking
│   └── Deliverable: Payment linked to work stages
├── Week 18: Multi-Currency & Advanced Filters
│   └── Deliverable: Handle foreign transactions
├── Week 19: Government Audit Enhancements
│   └── Deliverable: FBR-ready export formats
└── Week 20: Final Polish & Enhancement
    ├── Performance optimization
    ├── Feature refinements based on feedback
    └── Additional training session
```

---

## PRICING STRUCTURE - MILESTONE-BASED PAYMENTS

### **PHASE 1: MVP - PKR 350,000**

|Milestone|Deliverable|Payment|Timeline|
|---|---|---|---|
|**M1**|Project kickoff + Database setup + UI mockups approved|PKR 70,000 (20%)|Week 2|
|**M2**|Dashboard + Transaction module working (demo-able)|PKR 87,500 (25%)|Week 6|
|**M3**|Vendor management + Reports + Documents complete|PKR 87,500 (25%)|Week 10|
|**M4**|Full system deployed + Training + Excel migration|PKR 105,000 (30%)|Week 12|

**Phase 1 Total: PKR 350,000**

---

### **PHASE 2: ADVANCED FEATURES - PKR 250,000**

|Milestone|Deliverable|Payment|Timeline|
|---|---|---|---|
|**M5**|Analytics + Notifications + Bulk Operations|PKR 125,000 (50%)|Week 16|
|**M6**|All Phase 2 features complete + Final handover|PKR 125,000 (50%)|Week 20|

**Phase 2 Total: PKR 250,000**

---

### **TOTAL PROJECT INVESTMENT**

|Phase|Duration|Investment|Payment Terms|
|---|---|---|---|
|Phase 1 (MVP)|3 months|PKR 350,000|4 milestone payments|
|Phase 2 (Advanced)|2 months|PKR 250,000|2 milestone payments|
|**TOTAL**|**5 months**|**PKR 600,000**|**6 milestone payments**|

---

## WHAT'S INCLUDED IN THE PRICE

✅ **Software Development:**

- Complete web application with all modules
- Mobile-responsive design (works on phone/tablet/computer)
- Secure user authentication
- Role-based access control

✅ **Data Migration:**

- Import tool to transfer existing Excel data
- Data validation and cleanup
- Historical transaction preservation

✅ **Hosting & Infrastructure (First Year):**

- Cloud server hosting
- Daily automated backups
- SSL security certificate
- 99.9% uptime guarantee

✅ **Training & Documentation:**

- 3 training sessions (Owner, Accountant, Reviewer)
- User manual in English/Urdu
- Video tutorials for common tasks
- Quick reference guides

✅ **Support (First 3 Months):**

- Bug fixes and issue resolution
- Phone/WhatsApp support
- Small feature adjustments
- Performance optimization

---

## WHAT'S NOT INCLUDED (ADDITIONAL COSTS)

❌ **Annual Hosting Renewal:** PKR 60,000/year (after first year)  
❌ **Major Feature Additions:** Quoted separately if requested  
❌ **Hardware:** You need computers/tablets to access the system  
❌ **Internet:** You need internet connection  
❌ **Integration with Other Software:** If you want to connect to QuickBooks, etc.

---

## TECHNOLOGY STACK (NON-TECHNICAL EXPLANATION)

**What This Means for You:**

- **Modern & Fast:** Built with latest web technologies for speed
- **Secure:** Bank-level encryption for your financial data
- **Scalable:** Can handle 100+ projects without slowing down
- **Browser-Based:** Works on any computer with Chrome, Firefox, Safari, or Edge
- **No Installation:** Just open browser and log in
- **Reliable:** Uses proven technologies trusted by Fortune 500 companies
- **Future-Proof:** Easy to add new features as your business grows

**Technical Details (For Your IT Reference):**

- Frontend: React.js (User Interface)
- Backend: Node.js (Business Logic)
- Database: PostgreSQL (Data Storage)
- Hosting: AWS/Digital Ocean (Cloud Infrastructure)
- Platform: Desktop Web Application (browser-based)

**Mobile App Technology (Optional Add-on):**

- Mobile: React Native (iOS/Android Apps)
- See Appendix C for mobile app proposal

---

## RISK MITIGATION & QUALITY ASSURANCE

### How We Ensure Success:

**1. Milestone-Based Delivery:**

- You see working features every 2-3 weeks
- Payment only after you approve each milestone
- No surprises at the end

**2. Regular Demos:**

- Weekly video calls to show progress
- Your feedback incorporated immediately
- Course-correction before it's too late

**3. User Acceptance Testing:**

- You test each module before we move forward
- We fix issues until you're satisfied
- Training happens during testing

**4. Data Security:**

- Daily backups to prevent data loss
- Encrypted connections (https)
- Regular security audits
- Role-based access control

**5. Documentation:**

- Every feature documented
- Code commented for future developers
- Database structure clearly defined

---

## SUCCESS METRICS - HOW WE MEASURE VALUE

After 6 months of using the system, you should see:

|Metric|Current (Excel)|With Our System|Improvement|
|---|---|---|---|
|Time to generate audit report|3 days|1 hour|95% faster|
|Monthly accounting hours|40 hours|25 hours|37% reduction|
|Data entry errors|10-15/month|1-2/month|90% reduction|
|Time to check project profit|30 minutes|10 seconds|Instant|
|Receipt retrieval time|15 minutes|5 seconds|99% faster|
|Multi-project visibility|Manual comparison|Real-time dashboard|Instant|

---

## TRAINING & ONBOARDING PLAN

### **Week 12: System Handover Training**

**Session 1 - For Accountant (3 hours):**

- How to create new projects
- Adding transactions and uploading receipts
- Managing vendor information
- Generating routine reports
- Excel data import process

**Session 2 - For Reviewer (2 hours):**

- Reviewing and editing transactions
- Audit trail and history tracking
- Generating audit reports
- Requesting corrections from Accountant

**Session 3 - For Owner (1 hour):**

- Navigating the dashboard
- Viewing profit/loss reports
- Checking project status
- Investment portfolio overview
- Mobile access guide

### **Post-Training Support:**

- WhatsApp group for quick questions
- Screen-sharing sessions if needed
- Video tutorials for reference
- User manual in PDF format

---

## MAINTENANCE & SUPPORT PLAN

### **Included in First 3 Months (Free):**

- Bug fixes and error resolution
- Minor feature adjustments
- Phone/WhatsApp/email support (Mon-Fri, 9 AM - 6 PM)
- Monthly system health check
- Performance optimization

### **After 3 Months (Optional Annual Contract):**

**Standard Support Plan: Can be decided **

- Includes:
    - Hosting and server maintenance
    - Daily backups
    - Security updates
    - Email support (response within 24 hours)
    - Bug fixes

**Premium Support Plan: Can be decided**

- Everything in Standard, plus:
    - Phone/WhatsApp support (response within 4 hours)
    - Monthly feature enhancement request
    - Quarterly training refresher
    - Priority bug fixes
    - Dedicated account manager

---

## TERMS & CONDITIONS

### **Payment Terms:**

- Milestone-based payments as per pricing table
- Payment due within 7 days of milestone completion
- Bank transfer to provided account
- Invoice provided for each payment

### **Project Timeline:**

- Estimated timeline: 5 months (20 weeks)
- Actual timeline may vary by ±2 weeks due to:
    - Client feedback cycles
    - Change requests
    - Data migration complexity
- Major delays (beyond our control): Timeline extended accordingly

### **Scope Changes:**

- Changes within defined scope: No extra charge
- Major feature additions: Quoted separately
- Change requests evaluated within 48 hours

### **Intellectual Property:**

- Source code ownership: Asia Group of Companies
- We retain right to use non-confidential learnings
- Your business data remains 100% yours

### **Warranty:**

- 3 months free bug fixes after final delivery
- Software works as documented
- Does not cover user errors or misuse

### **Confidentiality:**

- Your financial data kept strictly confidential
- Non-disclosure agreement signed if required
- Data not shared with third parties

### **Termination:**

- Either party can terminate with 30 days notice
- Payment due for completed milestones
- Source code handed over for completed modules

---

## WHY CHOOSE OUR TEAM

### **Our Experience:**

- 4-person specialized team:
    - Backend developer (2-3 years experience)
    - Frontend developer (4 years experience)
    - UI/UX designer (3 years experience)
    - Chartered Accountant consultant (Big 4 firm experience)
- Successfully delivered ERP solutions for logistics and construction industries
- Deep understanding of Pakistani business practices and audit requirements

### **Our Approach:**

- Client-first methodology
- Regular communication and transparency
- Agile development (working features delivered incrementally)
- Quality over speed
- Long-term partnership mindset

### **Our Commitment:**

- On-time delivery
- Within-budget execution
- Post-launch support
- Knowledge transfer (you're not dependent on us forever)
- Honest advice (we tell you what you need, not what we can sell)

---

## NEXT STEPS

### **If You Approve This Proposal:**

**Step 1:** Sign proposal acceptance (digital signature accepted)  
**Step 2:** First milestone payment (PKR 70,000)  
**Step 3:** Project kickoff meeting (Zoom/in-person)  
**Step 4:** Week 1 begins immediately

### **If You Have Questions:**

We can arrange a meeting to:

- Walk through the proposal in detail
- Demo similar systems we've built
- Adjust scope or pricing if needed
- Answer any technical or business questions

### **Timeline to Decide:**

This proposal is valid for **30 days** from the date above. Pricing and timeline are subject to our team availability if acceptance is delayed beyond this period.

---

## APPENDIX A: FREQUENTLY ASKED QUESTIONS

**Q1: Can we start with Phase 1 only and skip Phase 2?**  
A: Yes, absolutely. Phase 1 is a complete, working system. Phase 2 is optional enhancements based on your experience.

**Q2: What if we want changes during development?**  
A: Minor changes within scope are free. Major feature additions will be quoted separately and may extend timeline.

**Q3: Can we add more users later?**  
A: Yes, unlimited users at no extra cost.

**Q4: What if we want to switch developers later?**  
A: Source code is yours. We'll provide complete documentation for any developer to take over.

**Q5: Is our data safe if server crashes?**  
A: Daily backups stored separately. Maximum data loss: 24 hours (can be reduced to 1 hour for extra PKR 10K/year).

**Q6: Can we host on our own server?**  
A: Yes, but you'll handle hosting, backups, and security. We can provide installation support for PKR 25,000.

**Q7: What happens after 1 year of hosting is over?**  
A: You choose: (a) Renew with us for PKR 60K/year, or (b) Move to your own hosting.

**Q8: Can we customize reports format?**  
A: Yes, basic customization included. Complex custom templates: PKR 10-20K per report type.

**Q9: Is internet required all the time?**  
A: Yes, for the desktop web application. For offline capability on mobile devices, see the optional Mobile App add-on (Appendix C).

**Q10: Can we export data to Excel anytime?**  
A: Yes, all reports exportable to Excel/PDF. Complete database backup available anytime.

---

## APPENDIX B: SAMPLE SCREENSHOTS (CONCEPTUAL)

_Note: Final design will be created after UI approval in Week 1-2_

**Dashboard View:**

```
╔══════════════════════════════════════════════════════════╗
║  ASIA BUILDERS - DASHBOARD                               ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Active Projects: 3          Total Investment: 12.0M    ║
║  Completed: 2                Total Profit: 2.5M         ║
║                                                          ║
║  ┌──────────────────┐  ┌──────────────────┐            ║
║  │ Plot 930 G-11/2  │  │ Plot 45 F-10     │            ║
║  │ Budget: 5.0M     │  │ Budget: 4.5M     │            ║
║  │ Spent: 4.9M      │  │ Spent: 2.1M      │            ║
║  │ Status: Active   │  │ Status: Active   │            ║
║  │ [View Details]   │  │ [View Details]   │            ║
║  └──────────────────┘  └──────────────────┘            ║
║                                                          ║
║  Recent Transactions:                                   ║
║  04-Dec-2025  Paid to Nisar Contractor  -100,000       ║
║  11-Dec-2025  Received from Rauf sb     +1,325,150     ║
║  18-Dec-2025  Paid to Wali Akbar        -96,000        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## APPENDIX C: MOBILE APPLICATION ADD-ON (OPTIONAL)

### **Overview**

While the desktop web application covers all business requirements, a dedicated mobile application can provide additional convenience for on-the-go access. This is offered as a separate add-on for clients who need mobile functionality.

### **Mobile App Features**

**iOS App (iPhone/iPad):**

- Native iOS application from App Store
- Optimized for iPhone and iPad screens
- Touch-friendly interface
- Push notifications for alerts
- Camera integration for receipt capture
- Offline mode with automatic sync

**Android App (Phones/Tablets):**

- Native Android application from Play Store
- Optimized for various screen sizes
- Material Design interface
- Push notifications
- Camera integration
- Offline mode with automatic sync

**Core Capabilities:**

- View project dashboard and reports
- Add/edit transactions on the go
- Capture and upload receipts using phone camera
- View vendor information
- Receive payment reminders
- Check project profit/loss
- Offline work with sync when online
- Biometric login (fingerprint/face ID)

### **Who Needs Mobile App?**

**Consider mobile app if:** ✓ Owner wants to check reports while traveling  
✓ Site manager needs to log expenses from construction site  
✓ Accountant works from multiple locations  
✓ Need to capture receipts immediately at vendor shops  
✓ Want push notifications for important updates

**Desktop web is sufficient if:** ✓ All work happens from office computers  
✓ Receipts collected and scanned later  
✓ Email notifications are adequate  
✓ Budget is primary concern

### **Mobile App Development Timeline**

```
Month 1 (Weeks 1-4)
├── Week 1-2: Mobile UI/UX Design
│   ├── iOS interface design
│   ├── Android interface design
│   └── User flow optimization for mobile
├── Week 3: Core Features - iOS
│   ├── Dashboard and reports
│   └── Transaction management
└── Week 4: Core Features - Android
    ├── Dashboard and reports
    └── Transaction management

Month 2 (Weeks 5-8)
├── Week 5: Advanced Features - iOS
│   ├── Camera integration
│   ├── Offline mode
│   └── Push notifications
├── Week 6: Advanced Features - Android
│   ├── Camera integration
│   ├── Offline mode
│   └── Push notifications
├── Week 7: Testing & Refinement
│   ├── iOS testing on multiple devices
│   ├── Android testing on multiple devices
│   └── Performance optimization
└── Week 8: App Store Submission & Training
    ├── Submit to Apple App Store
    ├── Submit to Google Play Store
    ├── User training for mobile app
    └── Documentation

Month 3 (Weeks 9-10)
├── Week 9: App Store Review Period
│   └── Wait for Apple/Google approval
└── Week 10: Launch & Support
    ├── Apps available for download
    ├── Post-launch support
    └── Bug fixes if any
```

**Total Timeline:** 10 weeks (2.5 months)

### **Mobile App Pricing**

**Development Cost: PKR 400,000**

|Milestone|Deliverable|Payment|Timeline|
|---|---|---|---|
|**M1**|Mobile UI/UX design approved + Development started|PKR 100,000 (25%)|Week 2|
|**M2**|Core features working on both iOS & Android (beta)|PKR 120,000 (30%)|Week 5|
|**M3**|All features complete + Testing done|PKR 100,000 (25%)|Week 7|
|**M4**|Apps live on App Store & Play Store + Training|PKR 80,000 (20%)|Week 10|

**Mobile App Total: PKR 400,000**

### **What's Included in Mobile App Price**

✅ **iOS Application:**

- iPhone app (iOS 14+)
- iPad optimization
- App Store listing and submission
- First year App Store developer account ($99 included)

✅ **Android Application:**

- Android phone app (Android 8+)
- Tablet optimization
- Play Store listing and submission
- One-time Play Store fee ($25 included)

✅ **Backend Integration:**

- API modifications for mobile sync
- Offline data storage
- Push notification server setup
- Image upload optimization

✅ **Testing & Quality Assurance:**

- Testing on 5+ iPhone models
- Testing on 10+ Android devices
- Performance optimization
- Security testing

✅ **Training & Support:**

- Mobile app user training (2 hours)
- Installation guide
- Troubleshooting documentation
- 2 months post-launch support

### **What's Not Included**

❌ **Annual App Store Fees (After Year 1):**

- Apple Developer Account: $99/year (~PKR 28,000)
- Google Play (one-time fee already paid)

❌ **App Updates for New OS Versions:**

- Major iOS/Android updates: PKR 30-50K per year
- Included in Premium Support Plan

❌ **Custom Mobile-Only Features:**

- Features not in desktop version require separate quote

### **Mobile App Maintenance**

**Post-Launch Support (First 2 Months):** Free

- Bug fixes
- Performance issues
- Minor adjustments

**After 2 Months (Optional):**

**Standard Plan: Cna be decided later**

- Compatibility updates for new iOS/Android versions
- Critical bug fixes
- App Store/Play Store compliance updates

**Premium Plan: Can be decided later**

- Everything in Standard
- Feature updates quarterly
- Priority bug fixes (within 24 hours)
- Monthly performance optimization

### **Combined Package Pricing**

**If ordered together with desktop system:**

| Package                      | Desktop Web + Mobile | Discount | Final Price       |
| ---------------------------- | -------------------- | -------- | ----------------- |
| **Phase 1 MVP + Mobile**     | 350K + 400K = 750K   | 50K off  | **PKR 700,000**   |
| **Complete System + Mobile** | 600K + 400K = 1000K  |          | **PKR 1,000,000** |

**Timeline if ordered together:**

- Desktop Phase 1: Weeks 1-12
- Mobile App: Weeks 8-18 (runs parallel from Week 8)
- Desktop Phase 2: Weeks 13-20
- Total: 20 weeks (5 months) for everything

### **Recommendation**

**Start with Desktop Web (Phase 1):**

- Covers all core needs: PKR 350K
- Test workflows for 2-3 months
- Collect user feedback

**Add Mobile Later (If Needed):**

- After confirming desktop meets needs
- Based on actual field requirements
- When budget allows

**Or Get Everything Together:**
- Simultaneous delivery
- Better long-term value

### **Mobile App FAQs**

**Q1: Can we add mobile app later?**  
A: Yes, anytime. Price remains PKR 400K even if added 6 months later.

**Q2: Do we need both iOS and Android?**  
A: No, we can develop just one for PKR 250K (iOS) or PKR 220K (Android). But most businesses need both.

**Q3: Will mobile app work without desktop?**  
A: No, mobile app requires desktop backend. It's an add-on, not standalone.

**Q4: Can we test mobile app before full payment?**  
A: Yes, after M2 (50% paid), you'll get beta version for testing.

**Q5: What if app gets rejected by Apple/Google?**  
A: Rare, but we'll fix issues and resubmit at no extra cost. Typically takes 1-2 attempts.

**Q6: Can accountant use phone, owner use desktop?**  
A: Yes, same data, different interfaces. Use whatever device you prefer.

**Q7: How much internet data does mobile app use?**  
A: ~5-10 MB per day with moderate use. Offline mode reduces data usage.

**Q8: Will mobile app slow down if many users?**  
A: No, backend scales automatically. Tested for 50+ concurrent users.

**Q9: Can we white-label the app (our company name)?**  
A: Yes, included. App will show "Asia Builders" branding.

**Q10: What happens after 2 months free support?**  
A: You choose: (a) Annual maintenance for PKR 30-60K, or (b) Pay per fix basis.

---

## CONCLUSION

Asia Builders has grown significantly, and manual Excel-based tracking is holding you back from scaling further. This Construction Management System is designed specifically for your workflow, not a generic off-the-shelf product.

**Investment Summary:**

- Desktop Web System: PKR 600,000 (5 months)
- Mobile App (Optional): PKR 400,000 (2.5 months)
- Combined Package: PKR 1,000,000

**ROI:** System pays for itself in 12-15 months through time savings alone

**Risk-Free Approach:**

- Pay only after milestone approval
- See working features every 2-3 weeks
- Cancel anytime (pay only for completed work)

**Flexible Deployment:**

- Start with desktop web (sufficient for most needs)
- Add mobile later based on actual field requirements
- Or get everything together for maximum savings

**We're Ready When You Are:** Our team can start within 7 days of your approval. The sooner we begin, the sooner you stop wrestling with Excel and start making data-driven investment decisions.

---

**Proposal Prepared By:**
Diginammo
---

**For Acceptance:**

I, _________________________, on behalf of Asia Group of Companies / Asia Builders, approve this proposal and authorize commencement of work as per the terms outlined above.

Signature: _____________________  
Date: _____________________  
Name: _____________________  
Designation: _____________________

---

_This proposal is confidential and intended only for Asia Group of Companies. Unauthorized distribution is prohibited._