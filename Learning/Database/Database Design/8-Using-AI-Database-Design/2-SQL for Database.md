```sql
create table brand (

brand_id INT not null,

brand_name VARCHAR(100) not null,

constraint pk_brand primary key (brand_id)

)

  

create table model (

model_number CHAR(4) not null,

model_name VARCHAR(100) not null,

constraint pk_model primary key (model_number)

)

  

create table spaceship (

serial_number CHAR(17) not null,

reccomended_price NUMERIC(8,2) not null,

year_number smallint not null,

constraint pk_spaceship primary key (serial_number)

)

  

  

CREATE TABLE address (

address_id INT NOT NULL,

street_address VARCHAR(255) NOT NULL,

suburb VARCHAR(100),

city VARCHAR(100) NOT NULL,

state_province VARCHAR(100) NOT NULL,

postal_code VARCHAR(20),

country CHAR(2) NOT NULL,

  

CONSTRAINT pk_address PRIMARY KEY (address_id)

);

  

create table dealer (

dealer_id INT NOT NULL,

dealer_name VARCHAR(100) NOT NULL,

address_id INT NOT NULL,

country_code VARCHAR(5),

dealer_phone_number VARCHAR(15) NOT NULL,

email_address VARCHAR(100) NOT NULL,

website_url VARCHAR(255) NOT null,

constraint pk_dealer primary key (dealer_id),

constraint fk_dealer_address foreign key (address_id) references address(address_id),

constraint uq_dealer_email unique (email_address),

constraint uq_dealer_phone unique (country_code, dealer_phone_number)

)

  

CREATE TABLE customer (

customer_id INT NOT NULL,

customer_name VARCHAR(100) NOT NULL,

address_id INT NOT NULL,

country_code VARCHAR(5),

customer_phone_number VARCHAR(15) NOT NULL,

email_address VARCHAR(100) NOT NULL,

  

CONSTRAINT pk_customer PRIMARY KEY (customer_id),

CONSTRAINT fk_customer_address FOREIGN KEY (address_id) REFERENCES address(address_id),

CONSTRAINT uq_customer_email UNIQUE (email_address),

CONSTRAINT uq_customer_phone UNIQUE (country_code, customer_phone_number)

);
```
- This is sql where most relationships are not defined except address, dealer and customer