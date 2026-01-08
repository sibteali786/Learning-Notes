
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

# Website Analysis 
### Home Page
#### Container Details 
![[containerDetails.pdf]]
##### Questions
- What is unit of weight here in Column `Total Weight` ? i am assuming its Kilogram 
- What are `nugs` values here ? are these no of items ?
	- These are meant Items / Bilties carried in a particular Trip
- What is currency for packing amount ? should there be more than one currencies we can show it or should there be option to change currency format 
	- Currency is AED in UAE
- What is TGBU XXXX, TEMU XXXX etc 
	- These are container names 

If we 
#### Flow for Row click in first column Trip Info OR Trip load to Container
Clicking on each line opens up a new Page ( Show Trip Detail with query param tripId)
like 48-2065 at url
This can also be opened from Home Page Dropdown by entering trip id like `06-1308` and then `Trip Load to Container`
https://mainoffice.superasiacargo.com/showtripdetail.php?tripid=48-2065
![[TripInfoDetailsByTripId.png]]
##### Questions
- What is `Marka No` ? 
	- It is kind of like `invoice number` in normal financial softwares used to track a particular item being sent in cargo.
	- `Bilty No` and `Marka No` 
	- The suffix or number after dash ( - ) is denotes the number of items in this `marka`  like `0178597-1` means it has one item and if there is also `0178597-2` its the second item in this marka
- What does `unit price` denotes here ? is it currency or what
- What does `custom duty` , `discount` value represents ? again is it currency
	- The amount paid as Customs duty and discount applied to given item ranging from 0 to 20 as per employees
- What does `City` value here means
	- The city means to which destination it will be shipped to.
- Office Expense Details probably means the expense office made related to this shipment or Ship No ? 
	- Yes exactly
- Log Data probably shows any changes in this specific `Branch` and made by which person
	- These are logs for changes made directly to database by head office employees and its not allowed to individuals from sub branches
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
	- It show those cities which are mispelled and then appear in this report
	- They are corrected from another portal

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
### Ship Wise Qarza Detail
- We can use ship no to search how much Qarza ( Debt / Loan ) this ship is carrying for specific items 
![[QarzaByShipNoReport.pdf]]
- Qarza Kiya => Amount which was debt / or loan taken for specific item
- Qarza Wasool => Amount received for given debt item / loan which was paid for given item 
- Bilty Status => kind of dropdown thing which has values like `Cleared From Customs`,  `Loaded at Container(Trip)`, `Loaded at Container(Godam)`, `Sent to Godam`
- ![[Screenshot 2025-12-29 at 10.04.43 PM.png]]

### Box Ship Wise Report 
- ![[Pasted image 20251220134407.png]]
- ![[boxWiseShipReport.pdf]]
- The update `input` is not used by employees (it was originally to add or update expense column)
## Godam Loading
### Show Godam Report
- We can enter a ship number `554`
- Container = Godam 
- Godam Loading Date ( Start Date)
- To Date ( End Date)
![[GodamWiseShipReport.png]]
- If we enter ship 554 and click `Show Godam Report` it shows all items that were left out from 554 and previous ships  
-  If we enter 553 the list of items it shows are all those which are loaded into next ship i.e 554 but were left out from Ship 553.
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
- This one shows a report which is specifically designed to accommodate Saudi Arabia branches GODAM
- ![[SaudiGodamReport.png]]
- This report shows what proerties it has as compare to previous Godam Report 
- Clearly it is Office Wise as compare to Ship Wise from Last Godam Reports we saw for all other offices. 
## Master Data
In Navigation panel we have Master Data and it has several tabs lets look at each and what does each of them have 
### Document Info
- Click on `Document Info`
- This page is used for various purposes
	- Adding New or Updating existing document's expiry or Renewal Date ![[Pasted image 20251129224503.png]]
- Like Alain was one i added to check how does it work![[Pasted image 20251129224545.png]]
- I added `Alain` in remarks input and `Document` was `cheque` with `30 Nov, 2025` as expiry date.
- There are two places to see it one is [[#Top Bar]] at Home Page or Below New Update section using `Search Dcoument` and selecting Document ( Type ) in our case it was `Cheque`![[DocumentSearch_DocInfo.png]]
#### Document Search
This input is used to search documents using their Document ( Type ) such as ![[Pasted image 20251129225159.png]]
- It has different things like 
	- `Edit` which fills the New/Update Input at top and fils values there and then we can edit `Remarks` input and Document ( Type ) and Expiry/Renewal Date  
	- `Del` for deleting this Document 
	- `View` which opens up the document 
		- ![[Pasted image 20251129225849.png]]
		- If the file was uploaded it will show here otherwise we can upload it from here and then we can see it
#### Document 
- This section is last and allows to effectively add a new Document ( Type) in the dropdown for `Document`![[Pasted image 20251129230047.png]]
- Like i added here `Alain2` with all other existing ones
	- I am not seeing any place to delete it, there should be a way to do so

### Trip Upload 
- Each Individual branches sometimes cannot export their trip documents directly from software so this section is used to upload that
- The branch shares the export of database and then we use this to upload that file in main branch office website so that both remain in sync ( Manually )![[Pasted image 20251129232713.png]]
### Ship Info
- This page is used to 
#### Create New/Update ExisitingShip
- We can add new ship or update exisiting one 
#### Show Last 5 Ships 
- Shows data for last 5 active ships 
- ![[Pasted image 20251129233024.png]]
- It has sections as 
	- Edit Ship Info 
		- Seems like three options but it only adds ship value at Top `Ship` Input and then we can modify its `From` and `To Date`
- This is linked with next Page [[#Container Info]] where the newly added ship appears since the most recent ship added is considered as the current ship so that appears in the [[#Container Info]] page
### Container Info
![[Pasted image 20251201234913.png]]
- After adding a new ship it shows here in Container Info under property `Select Ship` 
- Ideally its assumed by Head Office employees to never change it since it shows current on going Ship 
- But software allows us to change to previous ships  which in turn leads to errors and thus we have to make sure this is fixed value and can only be updated from [[#Ship Info]] page
- Using `Container Name` we can add new container in current ship by Button `Create/Update Container`
#### Agent
![[containerInfoAgentListDetails.png]]
- `Agent Name` are ones in Karachi which are used to do clearance of containers 
- The Values like `KICT` are used for Port so it can be another column as well in our new software
- We need to ask team to provide know port values in a list 
- For each container there is a corresponding `agent` and its `passport` for clearance from Customs 
- Each agent can provide multiple passports 
- Clicking on `Show` takes to another page with report for `Container Number`  at [[#Container Details from Container Info]]
-  When container gets cleared at Karachi port then they send an amount or rate at which container is cleared , its named as `Agent Kharch (Expense)` 
- Similarly the expense for `Supply` is written in `Supply Kharch` 
- `Container Full` check is used to denote that a given container is full now.  This also shows at another page `Office` section and  `Daily Office Dashboard` 
- Agent and Passport numbers are written when a ship gets closed.
- `Container Loading, Ship Loadin and Clearance` are date values 
#### Edit Container Info
- `Edit Cotainer Info` fills the top values which can then be edited, like we can use `Update Container Ship` to change the ship of a given container ( as previously said if someone mistakenly assign container to previous ship which was closed already )
![[Pasted image 20251202001157.png]]
### Container Details from Container Info 
- Probably shows all the bilties ( Invoices ) from `Office`s , quantity, weight and each `Station` items from this container would go to
- This table shows the items belonging to each station in `Pakistan`
![[containerdetailsFromContainerInfo.pdf]]
### Main Station
![[Pasted image 20251202001518.png]]
- Main Station dropdown shows all available stations 
- This tab is used to update Station from Old to new 
- Or sometimes sub branch employees enter a station which is out of order now so this page is used by head branch to change it from that to new 
- like `batkhaila` is an old station and if someone needs to send an item to there then its changed to `Peshawar` station or `Peshawara Tarnol` 
- Its also used to fix wrong city names sometimes, Wrong city names are displayed under [[#Missing Cities]] page
### City Info
- Can be used to see list of all cities in English and Urdu and also have ability to add new and edit existing city 
	![[cityInfo.png]]
- Import City button is not working

### Trip Info

#### Trip Expense Date Updation 
- For a given `ship` and `container` we can change dates of all the expenses which were done in connection to given ship ![[Pasted image 20251203202141.png]]
- After selecting a date we can click on `Trip Expense Date Updation` to update date for given expenses., marka ( Bilty No ).
- ![[TripPrintByGivenTripId.pdf]]
- At bottom we can see the date as 28 Nov, 2025 which we set a while ago to check how it works ![[TripPrintByGivenTripId2.pdf]]
- We can go to [[#Reports]] in the [[#Accounts ]] sections 
#### Trip Lock / Unlock
- We can also lock and unlock a particular trip
- What it means any changes made to a trip info ( after it locked ) from a sub branch are not updated in head office website, that changed data is not shown here after a trip is locked for that trip 
#### Ship Lock
- Same goes for Ship Lock / unlock 
- So locking it wont update any things or data for given ship after its locked 
#### Trip expense Delete 
As the name suggests allows us to delete an expense from the data for a given ![[Pasted image 20251204003614.png]]
- After we select a trip and then press `Trip Exp Deletion` we see this list from where clicking Delete would delete this expense
- What is ==Trans.ID== here 
#### Show Trip
- This shows all items which are in godam and are not loaded to container, it appears in red color with Godam at top
![[GodamItemForTrip.png]]
- Once loaded they show Container number at top like as in picture
![[ShowTrip.png]]
- Q.Status show Qarz or Debt status, `N` means no Debt, `Q` means `Debt` 

### Bilty Hold/Deletion
- ![[Pasted image 20251218223417.png]]
- This tab allows us to `hold` a particular bilty 
  What does `hold` here means ? 
#### Hold
- A bilty is kept on `hold` in cases like when `payment` is not made for bilty or when there is some item which is prohibited or not allowed to be shipped like Electronic Items, medical supplies for example.
- Clicking on this once `Holds` it while clicking again `Unhold`
#### Deletion 
- Once a bilty is exported all its details are shown online afterwards 
Lets search a bilty using [[#Bilty Report by Bilty Number]]
We can see the report here and it shows all the items for a given `bilty` 
![[Pasted image 20251219003424.png]]
- Sometimes a customer says they do not want to ship an item like `FOAM(foom)` as its shipment is costly thus would like to delete it or remove from shipment.
- In that case we use the `marka no` along with value after dash like for FOAM it would be `0342533-4` this is specific invoice no or marka no for this item `FOAM` 
- Similarly we also sometimes can delete a bilty by using its number in input box and pressing Delete Bilty 

### KSA Qarza Detail
- This has no realation to UAE headoffice as for Qarza stuff we can go to Home and [[#Ship Wise Qarza Detail]] report to see qarza / debt for a given ship
## How Debt system works
There are two ways Qarz or Debt is handled 
- If someone sents an item and does it on `debt` the employees in sub brnach sends the amount to headoffice from their own pocket and ask for debt from the person or customer as per their own commitment.
OR
- From the [[Trip Load to Container]] tab when we mark a bilty as `Q` using `Qarz Status update` button after checking the `Check All` column and specific row or bilty value , in the main website where customer can see their bilty status its details are shows as `HOLD` which forbids the people in Karachi port to see the details of the customer bilty like `Destination address`, customer details like mobile number, stopping them to deliver it until head office marks it as `R` for receieved.  
## Branch Office (Website)
This website seems to be for individual branches 
[Branch Office](https://branchoffice.superasiacargo.com/)
![[Pasted image 20251202104029.png]]
- We then take  a Trip Id from [[#Missing Cities]] list and put it into Dropdown and select [[#Trip Container Loading]]
- ![[Pasted image 20251202112854.png]]
### Trip Container Loading 
- This tab has info about specific `Trip id`
- ![[TripContainerLoadingBranchOffice.png]]
- AS we can at its bottom we have line `Maston Maston Update` 
- This line if clicked takes us to another page where we can fix the wrong name entered 
#### Update City 
At [updateCity](https://branchoffice.superasiacargo.com/updatecity.php) we see this page where we can update wrongly entered city name
![[Pasted image 20251202113339.png]]
![[Pasted image 20251202113555.png]]
- There are 4 rows of wrong city names in trip id `01-352` so updating this would fix names for these four.
- After this change these wrong city names are updated in the [[#Trip Container Loading]] list

## Karachi Office 
go to [Karachi Office](https://pakoffice.superasiacargo.com/)
![[Pasted image 20251202235315.png]]
- This is used by people in karachi office 
- Go to Reports tab
### Reports 
![[Pasted image 20251202235528.png]]
- This always shows the current ship and container 
- Selecting city from list does not matter 
- ![[Pasted image 20251202235710.png]]
- The kidn of report we select does matter in our case we want to see [[#Container Loading Report]] 
- ![[Pasted image 20251202235849.png]] we can also chose the container to see its one detailed report a well
#### Container Loading Report
After selecting a container and then choosing `Container Loading Report` we this report 
![[Pasted image 20251202235815.png]]
- This report shows us what items | bilty a particular container has and which station and city it will be delivered or go to.

## Accounts 
### Reports ( Accounts ) 
![[Pasted image 20251203235559.png]]
- We can use this to check different report types like `Cash Book`, `Accoutns Master File`, `Cargo Mix Kharch` and `Office Exp`, `Account type Report`, `Office Ledger`, `Saudi Cash book` , `Bajwa Ledger` and `Shipline ledger`
- For now lets just see [[#Cash Book]]
#### Cash Book
- ![[cashbook.pdf]]
- This is how a cash book report looks like for given Account Type and Account 
- This shows that all expenses for given trip id i.e `01-1699` are dated as `28 Nov, 2025`
- Note all other were added later on same date
#### Cargo Mix kharch and office Expense
![[CargoMixKharchExpense.pdf]]
- There are no associated receipts for these expenses so there should be some which we have to add in new software 
## Pak Accounts 
In this section we have different pages for now we will only look at [[#Reports]]
### Reports ( Pak Accounts )


## SMS
### Container SMS
- This tab in navigation is used for purpose 
- When container is loaded from UAE, for example `558` is being loaded currently, so we will select container on ship 558 and provide a date and then have several options
#### Received at Pakistan
- When the container or shipment is reaches Karachi and gets cleared from customs, then we use this button after selecting a particular container. 
- This changes the bilty status for all items in that container to `Cleared From Customs`
- This info is relayed over social media apps like Whatsapp by employees in Karachi office that an item is cleared from customs and then head office comes to this tab and choses container, date and press `Received At Pakistan`
#### Container Custom Cleared SMS
- This sends sms to all customers that their item is cleared from customs ( Karachi ).
### Container Nug Loaded SMS 
- When ship gets closed then we select each container and click on `Container Nug Loaded SMS` and customers get sms that their item is loaded into container ( sent from UAE )
#### Enter Container Message
- This can be used to enter a custom message or status for a given bilty ( Bilty Status )
#### Contact No / Bilty No
- It can be used to get list contact nos for a given container  
- ![[ContactNoBiltyNo.png]]
- For some reason if message is not sent then we can use a manual approach and get these contact numbers and manually send messages to customers .
## Trip Load To Container 
- This is used for several purposes 
### Select File to Upload 
![[Pasted image 20251220120149.png]]
- Sometimes in local branches when we are not able to export trips via our website for some reason, we export txt files from database and import it using this section
![[ManualExportTripFromDatabaseExample.mp4]]
- This video shows that if web export option in [[#Database]] does not works then we use manual file exported as `text`  in File system drive C and upload it in [[#Select File to Upload]]
### Show Trip Bilties
- Shows the bilties list which are in Godam or in any selected container
- ![[ShowTripBilties.png]]
- This trip had bilties which are in Godam thus its Red once loaded it will appear as white 
### Load Checked Marka to Container 
- Go to [[#Trip Load To Container]] enter a trip id let say `01-1717` and then click on [[#Show Trip Bilties]] then choose any row or all rows in `Check all` column, select a container from the list and press `LOAD CHECKED MARKA TO CONTAINER` and it will load that item to container and it will go away from `GODAM` list like shown ![[ShowTripBilties.png]]
- Now this trip items are loaded to container ad its no longer in `Godam` aka `Warehouse` but in a container with ship 559 `TEMU 8669560:SHIP # 559` 
- ![[showTripBilitiesGodam.png]]
- Selecting items in the Container and then clicking again on the button `LOAD CHECKED MARKA TO CONTAINER` would send them to GODAM or `Warehouse`
### Box / UnBox Markas
- Select a marka from [[#Show Trip Bilties]] and Click this button to associate a box with this `marka` or `item` , this means this item was sent in a wooden box
- ![[Pasted image 20251220134047.png]]
- Clicking again would change `BOX` column value from `1` to `0` 
## Booking 
- This tab was added to add and ( Pickpup ) track bookings, but this functionality is incomplete thus wont be there in our MVP for Asia Group Of Companies
## Office
- This section has dashboard and reports for each office
### Daily Office Dashboard 
![[Pasted image 20251220151143.png]]
- This shows how much `items` (Nug) each office has/have received today are their in the office ( Not in Office Godam , not in Head Office nor in Head Office Godam)
- The red table shows `offices` which have received no nugs today.
- `Trip Nugs` means the no of Nugs head Office receives as a Trip from this office.
- The red portion shows the details about last trip from this branch which arrived at Head OFfice 
- ![[Pasted image 20251220151229.png]]
- When a container gets full, this is where we see that this container is full now ![[Pasted image 20251220151321.png]] which is marked from [[#Container Info]] tab, so what we do is 
- We clcik on `Last 10 Ship Containers` and from list click `Edit Container Info` and then click on `Cotnainer Full` which will mark the container as full
- ![[Pasted image 20251220161924.png]]
- ![[Pasted image 20251220163446.png]]
- Then we at start of this screen we also have individual office reports ( As Card element probably ) 
- ![[Pasted image 20251220205117.png]]
- Nugs arrived at Local Office from customers like `03:Commercial` has 28 Nugs since `16-12-2025`
- This shows all `Nugs` / `Items` which are received from `Commercial` branch since `16-12-2025`
- Local branch employee exports the trip from Database as `Web Export` and then only we can see those trip details like Nugs/ Items no received at given branch here in [[#Daily Office Dashboard]] as the video in [[#Select File to Upload]] shows this
- C.Amount means Cargo Amount 
- G.Nugs means Godam Nugs or Warehouse Items which are left in the Head Office Godam not in the local office Godam or Warehouse. It can also be checked from [[#Show Godam Report]] and we can also see for a particular branch how many items they have in their Godam by visiting [Branch Office](https://branchoffice.superasiacargo.com/)
### Daily Office Report
Not used by Head Office ( Probably not working at all) since most of stuff is already taken care of in [[#Misc Reports]]
### Office Godam Report
- This shows us the reports similar to one in [[#Godam]] from Branch Office website. 

## Misc Reports
This page as per Head office is mostly used only for [[#Container Office Wise Report]], [[#Container Marka Wise Details Report]] , and [[#]]
### Container Marka Wise Details Report
![[ContainerMarkaWiseReport_MiscReports.pdf]]

### Container Office Wise Report
- ![[CotnainerOfficeWiseReport_MiscReports.pdf]]
- this is office wise and the previous one was Marka Wise 
### Container Packing List Report 
- Usually shows all kind of item details 
- ![[CotnainerPackingList_MiscReports.pdf]]
### Ship Office Summarize Report 
- For this report we only need to mention Ship no and select `Office Wise Summarized Report`
![[OfficeWiseSummaryReportForSHip_MiscReports.pdf]]

## Accounts 
- This section is mostly used to record any kind of transactions, expenses made throughout Asia Cargo by the employees.
-  
lets start with [[#Account Types]]
### Account Types
- Main or Primary Accounts across the organization are made using this section
- It has only five types `Bank`, `Cash`, `Expense` , `Income` and `ExpenseIncome` by default but they are extended to many other as well.
- For example if the organization needed an account where employees took loan to get a car they created a main account beside five listed above named `Gari Qist Loan` or in English `Vehicle Installment Loan` .
- Every Entry made for this account type for a given sub account would show for Report under this Main Account 
![[Screenshot 2026-01-06 at 10.24.00 AM.png]]
- Lets say `Zulfiqar Passport` sub Account entry was made under `Gari Qist Loan`, now report `Gari Qist Loan` would contain `Zulfiqar Passport` in it.
- These accounts are listed as `Select Account Type` in the [[#Reports ( Accounts ) -> Accounts Section]] section of [[#Accounts]] module.
![[Screenshot 2026-01-06 at 10.25.51 AM.png]]
- Lets create a dummy account for our understanding named `Bussiness Loan` under `ExpenseIncome` type.![[Screenshot 2026-01-06 at 10.45.42 AM.png]] After this we go to [[#Accounts Master File]] 
- We can also  select `Account Main Type` and click `View Sub:Account Report` to see list of Sub Accounts in Main Account Type. 
- ![[Screenshot 2026-01-06 at 11.11.53 AM.png]]
- ![[Screenshot 2026-01-06 at 11.13.42 AM.png]] We can press `Submit` to also show list of all sub accounts in Main Account as in picture shared above.
### Reports ( Accounts ) -> Accounts Section
- This section allows us to view reports for Main Account Types like we saw previously in Account Types section
- For instance `Select Acccount` chose `Mustafa Qarza` (Account for debt of all employees in Super Asia Cargo)
- Then chose `Account Type Report` as `Select Report`  while `Select Account Type` is `Asmat All Ladger` by default.
- ![[MustafaQarza_AccountReportType.pdf]] It has fields like S.No, Account Name, Opening Balance, Amt. Paid/ Deposited, Amt.Received/ Withdrawal and Balance Amt.
- We can see the `Account Type Report` for sub Account ( Dummy ) `Bussiness Loan` for Main Account `ExpenseIncome`
- ![[Screenshot 2026-01-06 at 11.44.08 AM.png]] This shows Account Type Report for each legder in the `Bussiness Loan` sub Account. 
#### Cash Book
- This shows Cash Book Report from a given date to given Date.
- ![[cashbook_dated.pdf]] It has different kind of report merged into one as we can see here in pdf
- Income Account, Narration and Amount Recieved. We also have associated Trip Id for reference 
#### Accounts Master File
- ![[Screenshot 2026-01-06 at 12.15.31 PM.png]] We can select `Accounts Master File` in `Select Report` and get all `Account Sub Type` for a given Main Account i.e `Bussiness Loan` ![[Screenshot 2026-01-06 at 12.17.31 PM.png]]
- Like we made `Naeem Account` as `Account Sub Type` from [[#Accounts Master File]] section in [[#Accounts]] 
- If we click `Edit` button at the right most column `Edit` it takes us to [[#Accounts Master File]] ![[Screenshot 2026-01-06 at 12.21.25 PM.png]]
- But this time we are `Updating Record` as the button says it, while the details for sub account are already filled, that can be changed as needed.
- This section is a different file since [[#Accounts Master File]] do not have Account Id field at top, its the Edit version of [[#Accounts Master File]]
- 
### Accounts Master File
- In this section we create a `Account Name/Description` for which we are going to create an Entry.
- As per Head Office employees, they use it to create a Ledger for a sub account in given Main Account.
- ![[Screenshot 2026-01-06 at 11.25.01 AM.png]]
- We can chose to write `Address` or leave empty, also `Opening Balance` can be used to assign any opening balance for this account.
- This when submitted goes into the list of `Select Account` in [[#Reports ( Accounts ) -> Accounts Section]]  ![[Screenshot 2026-01-06 at 11.41.28 AM.png]] `Naeem Account` appears as Account in `Select Account` while `Bussiness Loan` sub Account for Main Account appears under `Select Account Type`.
#### Ledger
- Every entity be it employee, customer , vehicle, transport etc has their Ledger Account.
- ![[Pasted image 20260106123620.png]] This is a ledger Account detail report from a given date to a given date for a given `Sub Account Name` `Rauf Dubai Ledger` . 
- Whatever amount is paid to this ledger would be recorded as an expense in this Sub Account i.e `Rauf Dubai Ledger`
- Ledger report is also used to see what expenses are made by a particular ledger account. For Instance how many expenses were made by `Naeem Account` so we can get its ledger report and see all expenses made in name of this account.
### Expense/ Income Voucher Entry
- In this section we can create expense entries for any sub account for a given Main Account.
- ![[Screenshot 2026-01-07 at 12.39.21 PM.png]]
- Expense/ Income Account means Sub Account, in our case it can be `Naeem Account` we created as dummy
- `Narration` shows details about the expense made.
- Amount paid and received and self explanatory.
- Specifc Accounts are made to record receiving of Debt or `Qarza` for instance, if `Naeem Account` was given 5000 AED it will show in its ledger and as `Amount Paid` when it returns this money it will be transferred to another account `Qarza Wasooli` ( or Debt Collected ) using [[#Bank/Other Account Deposit Voucher]]
- ![[Qarza_Wasoolu_Ledger.pdf]] This doc shows the Amount on Money paid and received in the Debt Collection Account `Qarza Wasooli Ledger`
- 
### Bank/Other Account Deposit Voucher
- This is used to record a double entry, that is transfer of Amount from one account to another account. 
- For example the amount paid to `Naeem Account` was paid back by `Naeem` so now it will be transferred to `Qarza Wasooli Ledger` using this section. 
![[Screenshot 2026-01-07 at 12.54.16 PM.png]]
- This then would show changes in both account tables, `Qarza Wasooli Ledger` would paid this amount while `Naeem Account` would be Receiving this amount. Its a bit confusing but 
- The account from which we transferred is termed as `Received` since it had taken debt and now we received the debt. 
- The account to which we transferred this amount i.e `Qarza Wasool Ledger` is Paid this amount.
### Search Voucher ( Edit/ Delete) 
- This section is used to edit or delete a `Voucher` or `Transaction` using its `V.ID` i.e `43157` in this example
![[Screenshot 2026-01-07 at 1.18.28 PM.png]]
- We can change its date, Change the `Debit Account` or `Credit Account` or things like `Narration` , `Amount Paid` and click on `Update Record`
- We can also upload a picture for the transaction made using this section, from button `Choose a signature/invoice picture`
- 
## Branch Office Website 
[Link](https://branchoffice.superasiacargo.com/) 
![[Pasted image 20251220225347.png]]
- Go to Godam
### Godam
- Here we can see All Items in this Branch's Godam in our Example its for Sanaya
- ![[BranchOffice_Godam_Report.png]]
- It shows both items from Local Godam ( Warehouse ) and Main Office Godam (Warehouse)
- At Bottom it has also items list which are loaded into container and sent to Head Office 
## Define a Trip 
- It means that from a particular office like Alain or Sanaya when some items / nugs are loaded into a Vehicle and sent to UAE head office and details about these items is exported from database using web export. Its called as TRIP
- We search a trip using Trip id as in [[#Trip Load To Container]] to get Trip.
- Trip Id is generated automatically when we create a trip.
## Top Bar

## Saudia Branch Things 
- `Bajwa Payment` Tab in the [[#Master Data]] tab is only for KSA ( Kingdom of Saudi Arabia) branch 
- Enquire about it from Saudia Branch office.
- Similalry [[#KSA Qarza Detail]] is another tab in [[#Master Data]] which belongs particularly to Saudia Branch Office.

### Inter Bank Transactions 
- When money is transferred from UAE to Pakistan branch then we need to convert the profit and loss amount into PKR from AED
- Rate for currency conversion should be custom so user can enter a custom rate since Currency Rate is not fixed and changes constantly 
	- This can be protected further by making sure entered rate is in compliance with Local banks so that fraud related activity can be prevented
### Audit Tracking
Every accounts related entry should be double entry ? what it means that 
- IF they are recording an expense, there should be answers to questions like from which branch they are recording these. Make sure accounting transactions are double entry
- Because currently when an accountant gets the expense report of a given Branch Godam, there is no way to track who did what expense, or who was responsible for making given expense.
- We should track each expense using the account with which the person logged in and did expense and if an entry was edited, who edited this entry
- Each Cash sale should be recorded and we should have answers to questions such as Where did the money from given sale went to and done by who?
- There should be a way to track who received which salary and when, verify if a person has already received a salary. 
- List off all employees so we know how many people are there in our organization.

## Local Branch Software
This is is probably made using Visual Basics but its not confirmed for now since i have not been able to open it in Microsoft Access ( 64 bit version )
- It has a user base which needs a login system and credentials to login into it
- Each of local branch office posses it and have their own credentials for it.
The main screen looks something like
![[Screenshot 2025-12-25 at 7.58.26 PM.png]]
Now we will dive into each module which is used by the employees ( not all modules are used regularly ).
### Bilty Module
It has several options as shown in screens shot
![[Screenshot 2025-12-25 at 8.01.09 PM.png]]
- From here we will look into [[#Bilty Form]] which is used to create bilty invoices, something which is created when a customer comes to Super Asia Cargo local branch to send any item or list of items, there they create this invoice
#### Bilty Form
 ![[Screenshot 2025-12-25 at 8.08.18 PM.png]]
- To add a new Bilty ( Invoice / Similar to Item but a Bilty can contain multiple Items or Nugs ) we click on `Add New Bilty` button as shown in screenshot
- The `Marka No` or `Bilty No` is auto created when we click `Add New Bilty` button to create a new Bilty. This shows this value is Auto Increment 
- Then first thing is `Customer Name`, then `EID No` or `Emaraat ID No` seems similar to CNIC no in Pakistan or other countries. 
- If a person is on visit then he/she can use `Passport No` instead of `EID No`.
- Contact No 1 and 2 are used for functionalities like integrating whatsapp and trying to send message to customers (like we saw in [[#SMS]] section how we send sms to each customer using containers details from [[#Container SMS]] sectiom in [[#SMS]]).
- Similarly `Rceiever Name` for the person who will receieve the item in Pakistan and his/her two contact numbers as in `Rec: Contact No 1` and `Rec: Contact No 2`  
- City field has to ways 
	- Custom Value which leads to wrong names but it taken care of in this system later in Trip Load module
	- Drop-down shows list of all available cities which can be modified from [[#City Information]] module in this software.
	- ![[Screenshot 2025-12-25 at 8.44.56 PM.png]]
	- The problem of [[#Missing Cities]] is caused for another reason, actually old Bilties which were created with wrong names by local employees and now when that old customer come with old invoice we come up with wrong city name and it leads us to [[#Missing Cities]] .
- `Receiver's Address` obvious from its name
- `Item` is a dropdown which contains list of all items that can be delivered. These are stored in another module [[#Items Information]] in this software where it can be edited along with the relevant prices, so if we select an item like `fridge` its price appears automatically in the `U.Price` or `Unit Price` input field. These values can only selected.
- `Unit Price` or `U.Price` is counted as per kg so, `Total` is calculated as `Unit Price * Weight` + `Custom Duty * Weight` since `C.Duty` is also per kg.
- The input next to it can be used to name the item 
- `Weight` is allowed to be edited and its unit though not shown is in `Kg or Kilogram`
- `P.Rate Or Packing Rate` and `Box` are values for `Rate` ( Amount ) they are counted once but Box amount shows we packed items in a `Box` 
- `C.Duty` or `Custom Duty` is the amount of Custom Duty that is already known by the local employees like 14 AED is custom duty / kg for electronic items while normal items are 3.5 AED 
- The small `Add` button is used to `Add` a nug or item in a Bilty since Bilty can have more than one items or nugs in it.
- `V CH` Vehicle Charges is the amount of money taken by the pickup vehicle to pick cutomer items. This entry is added by the local branch employee and its cannot be confirmed if thy are honest about it or not since there is no way to verify it like using a receipt.
- `Remarks` are added by local branch employee to explan about the bilty it can be anything, For Example if customer packed the item himself/herself, `Remarks` may contain sentence like `Since customer packed it themself so its safety is not guranteed`.
- VAT Rate is like Tax in UAE its value is normally 5% and it goes to government of UAE. This is not applicable in Cargo Bussiness but usually its there in other items bought accross UAE.
- `Discount` is amount in discount as obvious by its name
- `Amt Received` or `Amount Received` is the amount employee received from user, ideally it should ne equal to the `Total` value in `Bilty Form`![[Screenshot 2025-12-25 at 10.00.25 PM.png]]
##### Preview of Form and Upload to Asia Cargo Website, Whatsapp Integration
- Then if we press Print Icon we can get the print view of Invoice, Opens a new tab to whastaap number of the customer, another tab is opened like ![[Screenshot 2025-12-25 at 10.02.31 PM.png]] screenshot where when refreshed exports this bilty created is sent to [[#Website Analysis]] website![[Screenshot 2025-12-25 at 10.05.07 PM.png]]
- This the preview of the print as we can, at bottom we can see the remarks, place for Customer Signature and Manager Signature which can be added from [[#Bilty Form]]  
- Things like logo, Terms and Conditions, Contact Numbers etc are set from `Settings` and the [[#Bilty Form]] itself.
- The bilty itself can be checked also by customer by visiting https://superasiacargo.com/ and ![[Screenshot 2025-12-28 at 1.13.53 PM.png]] by entering country, Bilty Number and Contact No to track the bilty.
- The numbers in the form beside text `Pakistan City Station No:` is retrieved based on the city selected by us in the [[#Bilty Form]] ![[Screenshot 2025-12-28 at 1.19.05 PM.png]]
##### Signature
- We have a separate section for signature in the [[#Bilty Form]], click on the Sign button and using the machine where customer signs we can use that as Customer Signature.
- ![[Screenshot 2025-12-28 at 1.45.16 PM.png]]
##### Message
- If we have to show a custom message beside `Remarks` we can use `MSG` button to enter a custom message in the form.![[Screenshot 2025-12-28 at 1.49.27 PM.png]]
- This is what we see after clicking `MSG` button in the [[#Bilty Form]] , we can write a custom message here. 
- As per local branch employees they usually write things like Delayed Delivery like 90Days etc when something similar happens.
- ![[Screenshot 2025-12-28 at 2.04.42 PM.png]]
- `Baqaya Amt: Received` and `Baqaya Received Date` are not used any longer. Its called Debt Amount in English language.
##### Old Print 
![[Screenshot 2025-12-28 at 2.06.33 PM.png]]
- `Old Print` shows the old print format which is no longer in use now.![[Screenshot 2025-12-28 at 2.07.39 PM.png]]
##### Bilties Report 
- Clicking this button opens a modal first `Enter Start Date` and then `Enter End Date` which then reveals 
- ![[Screenshot 2025-12-28 at 2.11.14 PM.png]]
- Shows all the Bilties made in between a specific range of time![[Screenshot 2025-12-28 at 2.10.48 PM.png]]
- The report is shown as above. This version is shown in our main website at [[#Daily Office Dashboard]] 
##### Bilties at Office 
- Shows all the bilties which are still in the Local Branch office.![[Screenshot 2025-12-28 at 2.14.50 PM.png]]
#### Shipment Info
After ![[Pasted image 20251229003426.png]] a ship is closed this tab can be used add a new ship (number) usually 
 ![[Screenshot 2025-12-29 at 12.36.22 AM.png]]
 - We write new ship number and press [] tick box and then every new bilty or invoice created would be for this ship

#### Items Information
- This is the section from where we add or edit the item names, description, rate etc ![[Screenshot 2025-12-29 at 12.38.14 AM.png]]
- This is unique for each office branch so eahc office has its version of Items Information page and all others we discussed for this software ( Which is not a good practice).
#### City Information
- This section has list of all cities along with their contact number ![[Screenshot 2025-12-29 at 9.45.08 PM.png]]
- The number we see on the invoice in [[#Preview of Form and Upload to Asia Cargo Website, Whatsapp Integration]] preview is taken from this info
- 
### Trip Information 
- Loading the ![[Screenshot 2025-12-28 at 5.04.23 PM.png]]bilities to trip depends on how much weight given office has accumulated in form of Items.
- Usually its in between 2500 to 3000 kg per office when they can send a trip
- OR
- Sometimes when a ship is leaving from Head Office and some space is remaining in container, then Head Office call or request trips from near by local branch office.
- `Extra Raqam` is amount of packing or carton box sold by the local branch to customers, its ideally not part of Bilty or Trip but a customer can buy carton or boxes or packing for their own purposes which is not relevant to business scope but the amount is counted
- ==This is loophole which can and should be tracked so if something is sold it should have a receipt to make it traceable ==
- `Kharcha` is the amount of money spent by the branch for this trip ( things like offering coffee or tea and snacks to a customer etc. )
- `Bilty ID` is a dropdown to select list of bilties present in the office currently. ( the ones we create using [[#Bilty Form]])
- `Bilty Load to Trip` would load this bilty to the trip which appears as shown ![[Screenshot 2025-12-28 at 5.14.09 PM.png]]
- That field `Kharcha` ( or `Expense` in English ) is filled from [[#Accounts Module]] and after adding a expense or kharcha press `Refresh` button in thsi form and the expense would show up here ![[Pasted image 20251229002342.png]]
- If we press `Print Preview` button we can see the Trip Expense value in the preview as well ![[Screenshot 2025-12-29 at 12.24.29 AM.png]]
- Same Trip Info can be exported to Web or [[#Website Analysis]] main website and it gets exported to main website  ![[Screenshot 2025-12-29 at 12.25.35 AM.png]] after we go to this page and press Refresh or Just refresh page 

#### All Load or Bilty Loaded to Trip
- There are two ways to do this individually select each trip or Click on All Load 
- Usually employees in local branch offices use `Bilty Loaded to Trip` so that no item is left to be loaded to trip
#### City Correction
If a bilty in a given trip contains a Wrong City name its found in the `City Correction` tab which can be opened by clicking on button `City Correction`
![[Screenshot 2025-12-29 at 12.30.56 AM.png]]
- Unless this tab has a value ( means there is a wrong city name ) we cannot print preview or web export.
### Accounts Module
- Inside the Accounts Module we have [[#Vouchers Entry]] where we have Expense Payment Voucher Form ![[Screenshot 2025-12-28 at 11.59.11 PM.png]] to enter the details about `Kharcha` field in the [[#Trip Information]] form.![[Screenshot 2025-12-29 at 12.01.34 AM.png]]
- Here in Cash/Bank Account we use `CASH IN HAND` option
- ![[Screenshot 2025-12-29 at 12.02.11 AM.png]]
- We then select `Expense Account` as `Mix Ledger` and lets chose an amount of `120` for value to `Amount Paid` then select the `Trip ID` from the dropdown ![[Screenshot 2025-12-29 at 12.03.52 AM.png]]
- The `Narration` field can contain the any custom value let say we write `loading`.
- Remember the `Narration` field ideally should be a dropdown and should have a way to add new kind of expense since this can allow employees to add any kind of weird expense which does not even exists.
- Then we click `Floppy Disk` icon to save and `Add` icon to Add record to database and ultimately update the [[#Trip Information]] form
### System Administrator
- This section has [[#User Account Creation]] to create user accounts
#### User Account Creation 
![[Screenshot 2025-12-29 at 9.52.00 PM.png]]
- We can chose `Office`, `User Name`, `password` and `Group` ( permission level). 
![[Screenshot 2025-12-29 at 9.52.25 PM.png]]
- ![[Screenshot 2025-12-29 at 9.53.28 PM.png]]
- As we can it has different roles or permission or group
- `Full Level` is normally used.
#### System Settings 
- This is another section in [[#System Administrator]] module
-  ![[Screenshot 2025-12-29 at 9.58.45 PM.png]]
- `Office Manager Name1` shows name of the person who is logged into software.
- `ArabicShraaait` is Terms and Condition text in the [[#Preview of Form and Upload to Asia Cargo Website, Whatsapp Integration]] written in Arabic, while اردو شراءط is for `Urdu Terms and Condition`. Its made for Afaghanistan only
- ![[Screenshot 2025-12-29 at 10.04.16 PM.png]]
- ![[Screenshot 2025-12-29 at 10.04.43 PM.png]]
- This picture shows the list of `Trip Status` 
#### Office Contact Info
![[Screenshot 2025-12-29 at 10.13.25 PM.png]]
#### Bilty Edit Form
![[Screenshot 2025-12-29 at 10.15.32 PM.png]]
- Write the bilty ID or bilty No and then we can edit the bilty details 
- Its no longer allowed to local branch office since it can causes problems
- But head office can use it.