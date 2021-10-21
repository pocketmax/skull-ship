#Panda notes
https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

load, prepare, manipulate, model, and analyze.

increase the number of columns for .describe()
```
pd.options.display.max_columns=20
```

##import examples
###DB - SQL
###DB - NOSQL

###CSV

###JSON

###XML





## type casting
### https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
df = pd.DataFrame({
'a':['foobar','1.0', '2', -3,.34,54.322,'foo'],
'b':['1','0',1,0,True,False,'bar']
})
### cast a column to numbers
df["a"] = pd.to_numeric(df["a"], downcast='signed', errors='coerce')
df["a"] = df["a"].fillna(0) #changes NaN to 0

### cast b column to boolean
df["b"] = pd.to_numeric(df["b"], downcast='signed', errors='coerce')
df["b"] = df["b"].astype(bool)
df["b"] = df["b"].fillna(False) #changes NaN to False

print("[a]is na:", df["a"].isna())
print("[b]is na:", df["b"].isna())
print(df.dtypes)
print(df)


