
##grouping/counting

##query strings

##SELECT examples
```sql
SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5
```
```python
df[["total_bill", "tip", "smoker", "time"]].head(5)
```

```sql
SELECT *, tip/total_bill as tip_rate
FROM tips
LIMIT 5
```
```python
df.assign(tip_rate=df["tip"] / df["total_bill"]).head(5)
```

##WHERE examples
```sql
SELECT * FROM tips WHERE time = 'Dinner' LIMIT 5;
```
```python
   df[df["time"] == "Dinner"].head(5)
```

```sql
SELECT * FROM tips WHERE time = 'Dinner' AND tip > 5.00;
```
```python
df[(df["time"] == "Dinner") & (df["tip"] > 5.00)]
```

```sql
SELECT * FROM tips WHERE size >= 5 OR total_bill > 45
```
```python
df[(df["size"] >= 5) | (df["total_bill"] > 45)]
```



Import an excel sheet, with select columns and set types
incCols = ['Case/Charts Number','Chargeback Status/Action','Record Type','Merchant Number','Dispute Amount']
xlsx = pd.read_excel('4445036984757 CB Database.xlsx',
sheet_name=0,
dtype={
'Merchant Number': str
},
usecols=incCols
)


Series: 1d array
Dataframe: 2d grid
Panel: 3d

Different ways to create a dataframe

A single column of values
data = ['A','B','C','D','E']
df = pd.DataFrame(data)

By rows
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data)

By columns
data = {
'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
'Age':[28,34,29,42]
}
df = pd.DataFrame(data)

By row of different sizes
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)

By excel sheet
df = pd.read_excel(‘file.xlsx', sheet_name=0, dtype=str)

.describe()
.head()
.tail()
.dtypes() show datatypes of columns


Benefits…
* Pretty prints objects


Dataframe
How to type entire columns
Type columns
