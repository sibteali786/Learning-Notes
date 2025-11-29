```table-of-contents
```
## ERP 
- Cargo bussines operates from here in pakistan
- 7 to 8 brnahces in UAE ( total 15 )
- every week one ship closes 
- Consolidated report for each ship at end of month
- Vouchers cannot be uplaoded to QuickBook
- Basic recording
- Availability of flexibility of operations in future 
- Courier service is only avaiblable by the company
- Only one accountant in UAE Head Office.
### Summary of Software 
Daily sales record karen 
Daily Expenditure Record karen 
- Limited access to software except head office
- Cost of good sale is 
- what


### Proposal Prompt For Claude 
Our first most task is to prepare a Project Proposal for the company `Asia Group Of Companies`

the proposal already contains details like

- Bussiness nature
    
- what are requirements and scope level
    
- Role Based access for each branch except head branch, becuase only head branch have full access to sales and expenses, while all other branches only write daily expenses and sales.
    
- the Erp must be able to generate consolidate report for proft and loss at end of each month for each branch
    
- Currently team uses Quickbook to record sales expenses and there is no ability to upload vouchers so our erp should also have ability to store vouchers
    
- The head branch in UAE should have maimum rights while other branches should only have access to enter sales and expenditures on daily basis or weekly.
    
- The team on all branches except Head Office UAE is non accountant and do not understand accounting thus the software should have a UI that is easier for them to understand.
    

The Owners want to have two proposals

1. Multi ERP system which support both Cargo and Construction Bussiness so we can handle both from same ERP system without need to create separate software for both
    
2. ERP for each ( Cargo and Construction Bussiness ) so that each bussiness can be dealt separately and not together, offcourse the first one is more cost effective and manageable as compare to this one but we have to create proposal so Stakeholders can understand what they are stepping into
    

Further Details from the accountant

- When recording inter bank transactions ( transactions sheet csv will be uploaded ) if we transfer a transaction from Bank A to Bank B it should not be accumulated to 2x the original value and must subtract from Bank A and Add to Bank B
    
- There are about 14 to 15 branches in UAE and some other countries which take parcel from customer and deliver it back to Pakistan
    
- Every single branch except Head Branch records simple revenue transaction and the expenses against the same and share the data with the Headoffice.
    
- For Branches client want an ERP to record these daily transaction along with the option to upload supporting document (vouchers and receipt).
    
- Customer also want data entry and access restriction for their employees in sub branches ( only Head Office has max access ).
    
- The system shall be integrated so the branches data can easily be accessible from the head office in the real time.
    
- No any further data is being shared by the branches like the complete set of Financial Statements only list of daily driven revenue and expenses.
    
- For the Headoffice complete ERP access is required to tackle the need of Full Financial statement.
    
- No complex revenue and accounting standards need to be incorporated in the ERP for now, there should be flexibility
    

Now what do i need from your side

1. First consider you are an Software Engineering Architect and ACCA qualified Accountant who deeply understands financials, You have to check this proposal and use this information as much as you can efficiently to prepare a proposal for the Executives of the `Company Asia Group of Companies`
    
2. We are a group of Team with a backend dev, frontend dev, UI Designer, the guy who brought the project
    
3. Make sure you research the the web freelance paltforms like Fiverr, Upwork etc to find rates of ERP system development of the scale and info i provided above according to the Pakistani market.
    
4. Make sure the timeline we share is reasonable considering that we would ask the company to let us make MVP at first and then full fledge software, Asynchronous communication since we all work remotely, client meetings, revisions, roadmaps, planning, designing UI, designing and developing software architecture, training we have to provide to the team at each branch of the company.

### Clarity 
GODAM SAMAN is items that were to referenced to the sale of SHIP XYZ but wasnt loaded due to capacity constraints or non clearance from custom at that time or due to packaging issue.
	1. These are sent GODAM and then packed and cleared from customs and sent in another shipment
	2. There is always a possibility that ship may leave some items behind in GODAM.
When the next ship comes over and we load things from GODAM do we reference the last ship it was meant to be loaded to ? 
Do we randomly throw stuff into next ship or make sure that first we load items leftover from last ship and then new items
	- I think we first load left-over items and then new ones assigned to current ship because its a FIFO ( First In First Out process )
	  
	  
## Prompt
Retained Goods: We will need to implement it since its part of core operations and profit and loss include this thing Construction Business: For now we only focus on Cargo Business construction stuff will be dealt later but we will architect application in a manner that we can later expand it for different use cases and features

Ship Assignment: yes they know and mention the ships as well

One clarity that numbers used are only numeric representation of order in which ship closed and not actual name or reference

- The ship numbers are only numeric values based on when this business started and now this number is around five hundred something.

- It can take a week or more depending upon workload when ship is closed.

- GODAM SAMAN ( Warehouse ) is items that were to referenced to the sale of SHIP XYZ but wasn't loaded due to capacity constraints or non clearance from custom at that time or due to packaging issue.

1. These are sent GODAM ( Warehouse ) and then packed and cleared from customs and sent in another shipment

2. There is always a possibility that ship may leave some items behind in GODAM ( Warehouse ).

- we first load left-over items from the last ship and then new ones assigned to current ship because its a FIFO ( First In First Out )

- The names in the reports like SALE-AJMAN, AJMAN-EXPENSE, AJMAN-SAMAN and PACK-AJMAN include the name of the branch as AJMAN while SALE ( sales ), EXPENSE, PACK ( packaging ) and Godam Saman ( Warehouse ) are all details added by the accountant himself to identify what kind of expense is this

Further Details from a person working in one of UAE branches ( not head office )

- We start with creating an inovice were we write complete details about customer,we weight the items customer provides us, write its rate, custom duty,

- if duty is taken from customer its mentioned there in invoice

- If we provide packing mention charges

- If we provide wooden box we mention charges in invoice

- If a customer asks to pick using vehicle we also include its charges

- The cost of items which are left to be loaded to assigned ship are not added to details of that ship but packing cost is associated with that item

- Then when a new ship comes we load items left from last ship to this ship and mention cost of items in this ship. Also mention X amount which was removed from WAREHOUSE (GODAM)

- There are five branches named

1. Alain

2. ⁠Musaffah

3. ⁠Sanaya 12

4. ⁠Sanaya 17

5. ⁠Bada Zaid

- There are three states Dubai, Abu dhabi& sharjah
    
    & there are division of branches among them!
    
    All the profit will be given to `dill marjan` but first head office recieve two states amount directly which was Dubai & sharjah! while abu dhabi states branches amount will be directly given to `dill marjan`! but records is maintained by branches of the Abu Dhabi State.
    
- First branch did the sales by issuing invoice to customer & receive payment against the sales( Sales include different things Packing amount, Nug amount, Woodeen box discount etc as mentioned above)
    
- Now they spent amount against these sales in branches which were there own expense & then they send all other branch profit to head office, then head office also have their some expenses they do that expenses from that amount which was given by branches & then they load All the nugs ( Items ) in containers & some of the leftover they store in godam ( warehouse ) & use FIFO ( First In First OUT ) for the next ship to be load! then the amount which was left from headoffice expenses they also give some amount to containers company! & the leftover amount will be their profit
    
- Now the profit will be given to `dill marjan` so we also have a ledger of `dillmarjan` Bcz they receive `abu dhabi` state amount directly & also collect other amount from head office of other two states! & then they will be given to Pakistan head office & they pay some amount in custom & other all will be their profit
    

fruther more

We also need to include an invoice system so that the head office continuously receives the actual data online. The same invoice will be provided to the client as well. since for now its done manually, there can be issues, as anyone can add or change things on their own. An online system will prevent these problems and provide security and avoid fraudulent activities

- The discount amount is fixed ranging from 1 to 20 Dirham. 
- While amount for vehicle charges, packaging and wooden charges are not fixed and depends what the person ( branch person ) responsible decides with customer.
- The amount for wooden box is also shown in packing charges but only packing charges are counted since wooden box is a form of packaging.
- Also there is a report list for a given ship where we mention the amount for wooden boxes.
  
  
  
  
## Re Enforce the promt again
Some Clarifications

- DilMarjan is a Hawaladar ( Hawala, which means "transfer" or "trust" in Arabic, operates through a network of brokers called hawaladars who rely on a system of mutual trust and balancing of accounts over time ). It receives profit from all three states and transfer them to pakistan head office.
    
- Which pay some amount in custom & remianing all will be their profit
    
- The Shipment number started when the company was started so its a sequential number, We will need to get this info from company and then we can start from there to reflect and manage new records accordingly.
    
- Which means we might start from ship number 570 or 610
    
- Expenses should be available as dropdown
 - Owner Branch Expense ( Personal Expense ), it can be 
- Reminders for receivables for each branch 
- A way to track how to make sure if a branch person receives amount X and also send amount X to head office ( There should be some way to track it , by some technique)
- Each branch has 1 or 2 person who records expense and sells.
- Individual Expense should be there along with Invoice / receipt  so it can be tracked and verified who did what.
- Different countries have different credentials ( Multi Tenant System)
- Left over items can be from last  5th or 6th ship as well ( not immediate last ship)
## Expense Category 
Loading Expense ( Travel Expense ) -> Operating 
Travel Expense 
Meas and Entertainement
Utilities
Liscence Fee ( Professional Fees & Workers liscence ( IQAMA ), Taxes for vehicle ) -> Renewal Fee 
Tax 
Consultation Fee

### Further things about last prompt for MVP
Retained Goods: We will need to implement it since its part of core operations and profit and loss include this thing Construction Business: For now we only focus on Cargo Business construction stuff will be dealt later but we will architect application in a manner that we can later expand it for different use cases and features Ship Assignment: yes they know and mention the ships as well One clarity that numbers used are only numeric representation of order in which ship closed and not actual name or reference - The ship numbers are only numeric values based on when this business started and now this number is around five hundred something.

- It can take a week or more depending upon workload when ship is closed.
- GODAM SAMAN ( Warehouse ) is items that were to referenced to the sale of SHIP XYZ but wasn't loaded due to capacity constraints or non clearance from custom at that time or due to packaging issue. 1. These are sent GODAM ( Warehouse ) and then packed and cleared from customs and sent in another shipment 2. There is always a possibility that ship may leave some items behind in GODAM ( Warehouse ).
- we first load left-over items from the last ship and then new ones assigned to current ship because its a FIFO ( First In First Out )
- The names in the reports like SALE-AJMAN, AJMAN-EXPENSE, AJMAN-SAMAN and PACK-AJMAN include the name of the branch as AJMAN while SALE ( sales ), EXPENSE, PACK ( packaging ) and Godam Saman ( Warehouse ) are all details added by the accountant himself to identify what kind of expense is this Further Details from a person working in one of UAE branches ( not head office )
- We start with creating an inovice were we write complete details about customer,we weight the items customer provides us, write its rate, custom duty,
- if duty is taken from customer its mentioned there in invoice
- If we provide packing mention charges
- If we provide wooden box we mention charges in invoice
- If a customer asks to pick using vehicle we also include its charges
- The cost of items which are left to be loaded to assigned ship are not added to details of that ship but packing cost is associated with that item
- Then when a new ship comes we load items left from last ship to this ship and mention cost of items in this ship. Also mention X amount which was removed from WAREHOUSE (GODAM)
- There are five branches named
- Alain
- ⁠Musaffah
- ⁠Sanaya 12
- ⁠Sanaya 17
- ⁠Bada Zaid
- There are three states Dubai, Abu dhabi& sharjah & there are division of branches among them! All the profit will be given to `dill marjan` but first head office recieve two states amount directly which was Dubai & sharjah! while abu dhabi states branches amount will be directly given to `dill marjan`! but records is maintained by branches of the Abu Dhabi State.
- First branch did the sales by issuing invoice to customer & receive payment against the sales( Sales include different things Packing amount, Nug amount, Woodeen box discount etc as mentioned above)
- Now they spent amount against these sales in branches which were there own expense & then they send all other branch profit to head office, then head office also have their some expenses they do that expenses from that amount which was given by branches & then they load All the nugs ( Items ) in containers & some of the leftover they store in godam ( warehouse ) & use FIFO ( First In First OUT ) for the next ship to be load! then the amount which was left from headoffice expenses they also give some amount to containers company! & the leftover amount will be their profit
- Now the profit will be given to `dill marjan` so we also have a ledger of `dillmarjan` Bcz they receive `abu dhabi` state amount directly & also collect other amount from head office of other two states! & then they will be given to Pakistan head office & they pay some amount in custom & other all will be their profit

fruther more * We also need to include an invoice system so that the head office continuously receives the actual data online. The same invoice will be provided to the client as well. since for now its done manually, there can be issues, as anyone can add or change things on their own. An online system will prevent these problems and provide security and avoid fraudulent activites I have again shared REQUIREMENT DOCUMENT so you can understand it again with details and pointer i provided now.

## Website Analysis 
### Home Page
#### Container Details 
![[containerDetails.pdf]]
##### Questions
- What is unit of weight here in Column `Total Weight` ? i am assuming its Kilogram 
- What are `nugs` values here ? are these no of items ? 
- What is currency for packing amount ? should there be more than one currencies we can show it or should there be option to change currency format
- What is TGBU XXXX, TEMU XXXX etc 

If we 
#### Flow for Row click in first column Trip Info
Clicking on each line opens up a new Page ( Show Trip Detail with query param tripId)
like 48-2065 at url
https://mainoffice.superasiacargo.com/showtripdetail.php?tripid=48-2065
![[TripInfoDetailsByTripId.png]]
##### Questions
- What is `Marka No` ? 
	- It is kind of like `invoice number` in normal financial softwares used to track a particular item being sent in cargo.
	- `Bilty No` and `Marka No` 
	- The suffix or number after dash ( - ) is denotes the number of items in this `marka`  like `0178597-1` means it has one item and if there is also `0178597-2` its the second item in this marka
- What does `unit price` denotes here ? is it currency or what
- What does `custom duty` , `discount` value represents ? again is it currency
- What does `City` value here means
- Office Expense Details probably means the expense office made related to this shipment or Ship No ? 
- Log Data probably shows any changes in this specific `Branch` and made by who 
- The line at top `## OFFICE: AVEER branch TRIP ID: 48-2065, DATED: 07-Nov-25 Prepared By:zeeshan` has details like `branch name` , `trip id`, `date` and `Person prepared these details` ? if so from where these details are recorded and how 
### Office Trip Detail Report ( Trip Income/Expense )
From Home page chose option `Trip Income/Expense`
![[TripIncomeExpense.pdf]]
- What kind of info `Trip Info` shows for instance `01-1680:02-11-25` ? seems to be trip id and date ? right
- Does `Cont:Weight` shows => Container Weight ? 
- `Cargo Amt` loaded means Amount Worth of items loaded into Cargo ?
- `C.Packing Amt ` means Amount Worth for Packing for given container ? Similarly `Godam Packing` , `G.Cargo Amt` => `Godam Cargo Amount`  
- What is `Extra Amount`
- what is `Asmat Kharcha` and `Dis` means and what does it denote.

### Bilty Report by Bilty Number
The bilty Number i got was `0343975-1` where we need to remove `1` at end to make it work for options like `Container Loading Details` and `Bilty` option on `HomePage`
![[biltyByBiltyNumber.pdf]]
- What is `Marka No` 
- What is `C.Duty`, `Packing` values here ?
- Container No shows multiple values ? what isexact value here ? 


### Container Details by Container No
![[containerDetailsByContainerNo.pdf]]

### Trip Print
We can use Trip Id from top of Home Page and get `Trip Print` screen 
![[TripPrint.pdf]]
- What does this page specifically shows, i could not understand `Trip Print`
- what in your opinion would be better way to show table at below with values like `Trip Expenses` , `Extra Amount`, `Packing` and `Qarza Kiya` ![[Pasted image 20251127112108.png]]
-  Where is reciept for these Expenses ?  is there any place we can find it 
![[Pasted image 20251127112500.png]]
- What is `Load` here
	- The `Load` column is ticked while loading items into ship to show they were successfully loaded into ship physically.
	- There should be a way to do it via software so employees do not have to print document and mark tick on physical sheet.
### Bilty Search by Container No 
What is the purpose of this table as i think we saw almost similar one in  [[#Bilty Report by Bilty Number]]
![[biltySearchByMobileNumber 1.pdf]]

### Missing Cities 
- We can use `Missing Cities` to see this table or details ![[Pasted image 20251127125839.png]]
![[missingCities.pdf]]

- What does it represents ? what does these values show 

### All Container Report 
- We can write value like 554 as ship no ![[allContainerReport.pdf]]
### Agent Report
- Use ship no to view this table ( like 554 ) 
![[agentReport.pdf]]

### Box Ship Wise Report 
- We can use `Ship` no to get Box Wise Report
- ![[boxShipWiseReport.pdf]]
- We can update values but what does it update specifically ?
### Packing Godam Report


### Godam Loading
- We can enter a ship number `554`
- Container = Godam 
- Godam Loading Date ( Start Date)
- To Date ( End Date)
![[GodamWiseShipReport.png]]
#### How to load a given item into given Cargo ( Ship ) 
- As in the picture we can mark as check a given item which shows it is loaded from godam into given container .
- We mark an item using `check` 
- Then select a container from top Container drop-down and press `Load Checked Marka to Container` ![[Pasted image 20251129213518.png]]
- Then this item goes away from this list since its no longer part of Godam list.
#### Getting Date Wise Godam Report 
- Enter Ship No 
- Select GODAM
- Start Date ( GODAM LOADING DATE)
- To Date
- Click on `DATE WISE GODAM LOADING REPORT`
![[Pasted image 20251129215947.png]]
- This Is with a Date Filter otherwise its shows whole report with all time until today irrespective of Ship No 
#### Saudi Godam
This one shows a report which is specifically designed to accommodate Saudi Arabia branches GODAM

## Top Bar
- Shows expiry of different things like Vehicle, Office 
- Ship No and Trip id 
- Marka No -> Invoice No / Bilty No
- Bilty no followed by 1,2 shows number of items 
- `LOAD` value is usually a Tick sign on physical paper
- Expiring check info using `Document Info` 
- Expiured items should only show for few days after
- `Document Upload` Section in Master Data
- CIty Info is not imortant 
- Local office should have receipt upload 
- File Size upload issue from head-office should be catered