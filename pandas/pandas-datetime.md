# pandas date and time notes

## https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html
### tutorial stuff goes here

## https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
### tutorial stuff goes here



### casting
### formatting
### relative time
### handling TZ
### calculations

* Date handling
    * Format dates
        * moment().format('MMMM Do YYYY, h:mm:ss a'); // April 1st 2021, 1:45:10 am
        * moment().format('dddd');                    // Thursday
        * moment().format("MMM Do YY");               // Apr 1st 21
        * moment().format('YYYY [escaped] YYYY');     // 2021 escaped 2021
        * moment().format();        // 2021-04-01T01:45:56-07:00
    * Relative time
        * moment("20111031", "YYYYMMDD").fromNow(); // 9 years ago
        * moment("20120620", "YYYYMMDD").fromNow(); // 9 years ago
        * moment().startOf('day').fromNow();        // 2 hours ago
        * moment().endOf('day').fromNow();          // in a day
        * moment().startOf('hour').fromNow();       // an hour ago
    * Calendar Time
      moment().subtract(10, 'days').calendar(); // 03/22/2021
      moment().subtract(6, 'days').calendar();  // Last Friday at 1:47 AM
      moment().subtract(3, 'days').calendar();  // Last Monday at 1:47 AM
      moment().subtract(1, 'days').calendar();  // Yesterday at 1:47 AM
      moment().calendar();                      // Today at 1:47 AM
      moment().add(1, 'days').calendar();       // Tomorrow at 1:47 AM
      moment().add(3, 'days').calendar();       // Sunday at 1:47 AM
      moment().add(10, 'days').calendar();      // 04/11/2021
    * Multiple Locale Support
      moment.locale();         // en
      moment().format('LT');   // 1:47 AM
      moment().format('LTS');  // 1:47:53 AM
      moment().format('L');    // 04/01/2021
      moment().format('l');    // 4/1/2021
      moment().format('LL');   // April 1, 2021
      moment().format('ll');   // Apr 1, 2021
      moment().format('LLL');  // April 1, 2021 1:47 AM
      moment().format('lll');  // Apr 1, 2021 1:47 AM
      moment().format('LLLL'); // Thursday, April 1, 2021 1:47 AM
      moment().format('llll'); // Thu, Apr 1, 2021 1:47 AM
    * Filter rows by a date
        * Only fetch rows with a date in a date range
* Cleaning up placeholder data and replacing with proper value
    * Replace “None” with 0
* Grouping/counting values in a column
* Boolean operations
    * Union of two DFs
    * Diff of two DFs
    * Intersect of two DFs
* Type casting columns
* Using query string
