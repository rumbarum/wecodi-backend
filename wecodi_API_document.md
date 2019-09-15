
| Title            | Singing up New User                                          |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /user/signup                                                 |
| URL Params       | None                                                         |
| Data Params      | {<br />fisrt_name: [string],<br />last_name: [string], <br />email: [string] ,<br />password: [string]<br />} |
| Success Response | **Code**:200, **Content**: "message":"SUCCES"                |
| Error Response   | **Code**: 400  **Conetent**: "message": "EMAIL_ALREADY_EXISTS"<br />**Code**: 400,  **Conetent**: "message": "INVALID" |
| Sample Call      | {<br />fisrt_name: "바름",<br />last_name: "한" ,<br />email: "barum@mail.com",<br />password: "pass1234"<br />} |
| Notes            | None                                                         |



| Title            | Loging in User                                               |
| ---------------- | ------------------------------------------------------------ |
| URL              | /user/login                                                  |
| Method           | `POST`                                                       |
| URL Params       | None                                                         |
| Data Params      | {<br />email: [string], <br />password: [string]<br />}      |
| Success Response | **Code**:200, **Content**: "TOKEN":"tokenvalue"              |
| Error Response   | **Code**: 400  **Conetent**: "message": "INVALID_PASSWORD"<br />**Code**: 400,  **Conetent**: "message": "INVALID_EMAIL_ADDRESS" |
| Sample Call      | {<br />email: "barum@mail.com"<br />password: "pass1234"<br />} |
| Notes            | None                                                         |



| Title            | Getting All Category Article                                 |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /article/allcategory                                         |
| URL Params       | None                                                         |
| Data Params      | None                                                         |
| Success Response | **Code**:200, **Content**: "RESULT":"LOADED",<br />"DATA":[<br />...<br />{<br />"article_id": [integer],<br />"title":[string],<br />"categoryname":[string],<br />"thumb_img":[string]<br />}<br />]<br />**Code**:200, **Content**: "RESULT":"NO_MORE_PAGE" |
| Error Response   | **Code**: 400  **Conetent**: "RESULT":"WRONG_INPUT"<br />**Code**: 400,  **Conetent**: RESULT":"INPUT_QUERY_NUMBER"" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Getting Specific Category Article                            |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /article/category/:category_id?offset=:offset&limit=:limit   |
| URL Params       | **Required:** `category_id=[integer]` (1: Fashioin Tip, 2: Inside Wecodi, 3: Outfit Idea)<br />**Optional**: `offset=[integer](default=0), limit=[integer](default=9)` |
| Data Params      | None                                                         |
| Success Response | **Code**:200, **Content**: "RESULT":"LOADED",<br />"DATA":[<br />...<br />{<br />"article_id": [integer],<br />"title":[string],<br />"categoryname":[string],<br />"thumb_img":[string]<br />}<br />]<br />**Code**:200, **Content**: "RESULT":"NO_MORE_PAGE" |
| Error Response   | **Code**: 400  **Conetent**: "RESULT":"WRONG_INPUT"<br />**Code**: 400,  **Conetent**: RESULT":"INPUT_QUERY_NUMBER"<br />**Code**: 400,  **Conetent**: "RESULT":"WRONG_REQUEST" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Getting Article Detail                                       |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /article/category/:article_id                                |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | None                                                         |
| Success Response | **Code**:200, **Content**: "RESULT":"LOADED",<br />"DATA":{<br />"TITLE": [string],<br />"CATEGORY":[string],<br />"CONTENT":[string],<br />"CREATED_AT":[string],<br />"UPDATED_AT": [string]<br />} |
| Error Response   | **Code**: 400  **Conetent**: "RESULT":"NO_ARTICLE"<br />**Code**: 400,  **Conetent**: "RESULT":"WRONG_INPUT" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Getting Recommended Articles with same category and styletag Excluding Chosen article |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /article/recommend/:article_id?quantity=:quantity            |
| URL Params       | **Required:** `article_id=[integer]`<br />**Optional**: `quantity=[integer](default=3)` |
| Data Params      | None                                                         |
| Success Response | **Code**:200, **Content**: "RESULT":"DONE",<br />"DATA":[<br />...<br />{<br />"article_id": [integer],<br />"title":[string],<br />"category":[string],<br />"thumb_img":[string],<br />"styletag": [string]<br />}<br />]<br /> |
| Error Response   | **Code**: 400  **Conetent**: "RESULT":"WRONG_ARTICLE"<br />**Code**: 400,  **Conetent**: "RESULT":"INPUT_QUERY_NUMBER" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Getting Articles Sorted by Category and Styletag             |
| ---------------- | ------------------------------------------------------------ |
| Method           | `POST`                                                       |
| URL              | /article/sort/:category_id/:styletag?offset=:offset&limit=:limit |
| URL Params       | **Required:** `article_id=[integer]`<br />**Optional**: `quantity=[integer](default=3)` |
| Data Params      | None                                                         |
| Success Response | **Code**:200, **Content**: "RESULT":"DONE",<br />"DATA":[<br />...<br />{<br />"article_id": [integer]<br />"title":[string]<br />"category":[string]<br />"thumb_img":[string]<br />"styletag": [string]<br />}<br />]<br /> |
| Error Response   | **Code**: 400  **Conetent**: "RESULT":"WRONG_ARTICLE"<br />**Code**: 400,  **Conetent**: "RESULT":"INPUT_QUERY_NUMBER" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Changing Status on Heart Mark for Independant User           |
| ---------------- | ------------------------------------------------------------ |
| URL              | /heartcheck/:article_id                                      |
| Method           | `POST`                                                       |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | None                                                         |
| Success Response | **Code:** 200 **Content:** "HEART_CHECK":"HEART_ON", "HEART_COUNT": [integer]<br /> **Code:** 200 **Content:** "HEART_CHECK":"HEART_OFF", "HEART_COUNT": [integer]<br /> |
| Error Response   | **Code:** 400 **Content**: "RESULT":"NO_ARTICLE"             |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Getting All Comment on Article                               |
| ---------------- | ------------------------------------------------------------ |
| URL              | /commnet/list/:article_id                                    |
| Method           | `GET`                                                        |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | None                                                         |
| Success Response | **Code:** 200 **Content:** "RESULT":"LOADED","DATA":[<br />...<br />{<br />"comment_id":[integer],<br />"user_name":[string],<br />"updated_at":[string],<br />"comment":[string]<br />},<br />] |
| Error Response   | **Code:** 400 **Content**: "RESULT":"NO_ARTICLE"<br />**Code:** 400 **Content**: "RESULT":"WRONG_INPUT" |
| Sample Call      | None                                                         |
| Notes            | None                                                         |



| Title            | Adding Comment on Article                                    |
| ---------------- | ------------------------------------------------------------ |
| URL              | /commnet/add/:article_id                                     |
| Method           | `POST`                                                       |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | {<br />comment:[string]<br />}                               |
| Success Response | **Code:** 200 **Content:** "RESULT":"ADDED","DATA":[<br />...<br />{<br />"comment_id":[integer],<br />"user_name":[string],<br />"updated_at":[string],<br />"comment":[string]<br />}<br />] |
| Error Response   | **Code:** 400 **Content**: "RESULT":"NO_ARTICLE"<br />**Code:** 400 **Content**: "RESULT":"WRONG_INPUT" |
| Sample Call      | {<br />comment: "안녕하세요, 게시물 잘 읽었습니다."<br />}   |
| Notes            | None                                                         |



| Title            | Updating Comment on Article                                  |
| ---------------- | ------------------------------------------------------------ |
| URL              | /commnet/update/:article_id                                  |
| Method           | `POST`                                                       |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | {<br />comment:[string],<br />comment_id: [integer]<br />}   |
| Success Response | **Code:** 200 **Content:** "RESULT":UPDATED","DATA":<br />{<br />"comment_id":[integer],<br />"user_name":[string],<br />"updated_at":[string],<br />"comment":[string]<br />} |
| Error Response   | **Code:** 400 **Content**: "RESULT":"WRONG_COMMENT_ID"<br />**Code:** 400 **Content**: "RESULT":"WRONG_INPUT" |
| Sample Call      | {<br />comment_id: 100,<br />comment: "안녕하세요, 코멘트 수정합니다."<br />} |
| Notes            | None                                                         |



| Title            | Deleting Comment on Article                                  |
| ---------------- | ------------------------------------------------------------ |
| URL              | /commnet/delete/:article_id                                  |
| Method           | `POST`                                                       |
| URL Params       | **Required:** `article_id=[integer]`                         |
| Data Params      | {<br />comment_id: [integer]<br />}                          |
| Success Response | **Code:** 200 **Content:** ""                                |
| Error Response   | **Code:** 400 **Content**: "RESULT":"WRONG_COMMENT_ID"<br />**Code:** 400 **Content**: "RESULT":"WRONG_INPUT"<br />**Code:** 400 **Content**: "RESULT":"NO_COMMENT"<br />**Code:** 400 **Content**: "RESULT":"NO_ARTICLE" |
| Sample Call      | {<br />comment_id: 100<br />}                                |
| Notes            | None                                                         |

