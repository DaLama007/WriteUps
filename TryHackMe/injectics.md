We get presented with a sie with a normal login and admin login.

After investigating the page source we find out that several SQL -inejction keywords are banned:

``` const invalidKeywords = ['or', 'and', 'union', 'select', '"', "'"];
            for (let keyword of invalidKeywords) {
                if (username.includes(keyword)) {
                    alert('Invalid keywords detected');
                   return false;
                }
            }
```

So, obviously we look into this and find out we get an alert when inputing words such as select ... .

```
const invalidKeywords = ['or', 'and', 'union', 'select', '"', "'"];
```

This indicates the requirement for some form of encoding method for the injection.
