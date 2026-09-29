SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode[.]com$'
  AND RIGHT(BINARY mail, 13) = '@leetcode.com';