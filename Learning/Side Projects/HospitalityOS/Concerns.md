### Multi Tenancy
- application has to be used by multiple hotels, restaurants, hostels etc
- Thus we might need to make it multi-tenant
- How do we handle multi tenants like use multiple databases ? or severs horizontal scaling ?
- Or should we scale vertically but still how do mutliple tenant traffic route ideally ?
### TimeZones
- People might be booking from different time zones like a person might be booking from Pakistan a hostel in Portugal , how does that is catered for now ?
- How we handle conflicting bookings in this case.\
### Micro Servie Architecture 
- What if services fail what happens then ? do we have a fallback for that so each service can work independently  
- We are using SSE to call external platforms like AirBnb, booking.com etc how safe and efficient is that instead of using something like RPC protocol ? 
### Apollo Client 
- Is apollo client the right choice for such an application which might have to deal with large number of tenants with their encapsulated data layers, webhooks, may be real time notifications and push notifications in future.
- 