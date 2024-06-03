# Testing Documentation

## Test Cases

| Test Case | Description            | Steps                                                                                           | Expected Outcome                                         | Actual Outcome                                       |
|-----------|------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------|
| TC-001    | Login Form Validation | 1. Open the login page<br>2. Leave username and password fields blank<br>3. Click on the submit button | Error message should be displayed indicating required fields | Error message displayed as expected.               |
| TC-002    | Successful Login      | 1. Open the login page<br>2. Enter valid username and password<br>3. Click on the submit button  | User should be redirected to the dashboard            | Logged in successfully, able to view cookbook       |
| TC-003    | Invalid Credentials   | 1. Open the login page<br>2. Enter invalid username or password<br>3. Click on the submit button | Error message should be displayed indicating invalid credentials | Received an error message indicating invalid credentials. User prompted to retry. |
| TC-004    | Create New Recipe     | 1. Login to the application<br>2. Navigate to the "Create Recipe" page<br>3. Fill in all required fields<br>4. Click on the submit button | Recipe should be successfully created                  | Recipe successfully created as expected.           |
| TC-005    | View Recipe Details   | 1. Login to the application<br>2. Navigate to the "Recipes" section<br>3. Click on a recipe to view details | Recipe details should be displayed                     | Recipe details displayed as expected.              |

### Summary

Total Tests: 5  
Pass: 5 
Fail: 0