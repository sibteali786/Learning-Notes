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

- The expense and sales of these branch is recorded online but cash is recorded to a ledger account Named `DilMarjan` which is a Hawala ( Person or entity ) which takes cash and provides it to owners back in Pakistan and not directly through head office.
