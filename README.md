Run
====================

    $ git clone https://github.com/nabilmoiun/u-tech.git
    $ cd u-tech
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py insert_data

**python manage.py insert_data** command will insert all of the existing data to the newly created "Sale" model from the provided "xyz_sales_data.csv" dataset.

 ***Now Go to http://localhost:8000/api-docs/ to get the api listing/documentation***


Apis
====================
+ http://localhost:8000/login/ returns a login token for authenticating user
+ http://localhost:8000/register-user/ creates a new user
+ http://localhost:8000/generate-pdf-report/ returns a pdf file containing the following information from Sale Data :

    + Total number of orders count per year
    + Total count of distinct customers
    + Top 3 customers who have ordered the most with their total amount of transactions.
    + Customer Transactions per Year
    + Region basis sales performance pie chart
    + Sales performance line chart over the years
+ http://localhost:8000/insert-sale/ inserts new sale entry to the Sale Model
+ http://localhost:8000/retrieve-update-delete-sale/{id}/  gets, updates and deletes (manipulates) a single record from Sale Model containing {id}
