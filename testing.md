## Testing Documentation

## Test Cases

| Test Case | Description            | Steps                                                                                           | Expected Outcome                                         | Actual Outcome                                       |
|---|---|---|---|---|
| TC-001    | Login Form Validation | 1. Open the login page<br>2. Leave username and password fields blank<br>3. Click on the submit button | Error message should be displayed indicating required fields | Error message displayed as expected.               |
| TC-002    | Successful Login      | 1. Open the login page<br>2. Enter valid username and password<br>3. Click on the submit button  | User should be redirected to the dashboard            | Logged in successfully, able to view cookbook       |
| TC-003    | Invalid Credentials   | 1. Open the login page<br>2. Enter invalid username or password<br>3. Click on the submit button | Error message should be displayed indicating invalid credentials | Received an error message indicating invalid credentials. User prompted to retry. |
| TC-004    | Create New Recipe     | 1. Login to the application<br>2. Navigate to the "Create Recipe" page<br>3. Fill in all required fields<br>4. Click on the submit button | Recipe should be successfully created                  | Recipe successfully created as expected.           |
| TC-005    | View Recipe Details   | 1. Login to the application<br>2. Navigate to the "Recipes" section<br>3. Click on a recipe to view details | Recipe details should be displayed                     | Recipe details displayed as expected.              |
| TC-006    | Registration:**       | 1. Open the registration page.                                                                   | User account should be successfully created.        |                                                      |
|           |                        | 2. Enter valid, username, password, and confirm password.                          | User should be redirected to the login page. |    Works as expected                                                  |
| TC-007    | Edit Existing Recipe:** | 1. Login to the application.                                                                   | Recipe details should be updated successfully.        |   Works as expected                                                     |
|           |                        | 2. Navigate to the "Recipes" section.                                                              | Updated recipe information should be reflected when viewing the recipe. |  Workes as expected                                                      |
|           |                        | 3. Click on a recipe to edit.                                                                    |                                                      |
|           |                        | 4. Modify the recipe details (e.g., ingredients, instructions).                                 |                                                      |
|           |                        | 5. Click the save button.                                                                       |                                                      |
| TC-008    | Delete Recipe:**       | 1. Login to the application.                                                                   | Recipe should be deleted successfully.                |      Works as expected. User receives a confirmation alert message prompting them to confirm recipe deletion before proceeding.                                         |
|           |                        | 2. Navigate to the "Recipes" section.                                                              | Recipe should no longer be displayed in the recipe list |      Works as expected.                                                |
|           |                        | 3. Click on a recipe to view details.                                                              |                                                      |
|           |                        | 4. Click the delete button (confirmation might be required).                                      |                                                      |

### Summary

Total Tests: 8  
Pass: 8
Fail: 0 