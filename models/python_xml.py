# import xml.etree.ElementTree as ET
#
#
# # XML data (assuming it is stored in a variable called xml_data)
# xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
# <Library>
#     <Books>
#         <Book id="B001" isbn="978-3-16-148410-0">
#             <Title>Introduction to Algorithms</Title>
#             <Author id="A001">Thomas H. Cormen</Author>
#             <Author id="A002">Charles E. Leiserson</Author>
#             <Author id="A003">Ronald L. Rivest</Author>
#             <Author id="A004">Clifford Stein</Author>
#             <Genre>Computer Science</Genre>
#             <Publisher>MIT Press</Publisher>
#             <Year>2009</Year>
#             <Copies>
#                 <Copy id="C001" status="available"/>
#                 <Copy id="C002" status="borrowed"/>
#             </Copies>
#         </Book>
#         <Book id="B002" isbn="978-0-201-63361-0">
#             <Title>The Art of Computer Programming</Title>
#             <Author id="A005">Donald E. Knuth</Author>
#             <Genre>Computer Science</Genre>
#             <Publisher>Addison-Wesley</Publisher>
#             <Year>1997</Year>
#             <Copies>
#                 <Copy id="C003" status="available"/>
#                 <Copy id="C004" status="available"/>
#             </Copies>
#         </Book>
#         <Book id="B003" isbn="978-1-491-94747-0">
#             <Title>Python for Data Analysis</Title>
#             <Author id="A006">Wes McKinney</Author>
#             <Genre>Data Science</Genre>
#             <Publisher>O'Reilly Media</Publisher>
#             <Year>2017</Year>
#             <Copies>
#                 <Copy id="C005" status="borrowed"/>
#             </Copies>
#         </Book>
#     </Books>
#     <Authors>
#         <Author id="A001">
#             <Name>Thomas H. Cormen</Name>
#             <Nationality>American</Nationality>
#         </Author>
#         <Author id="A002">
#             <Name>Charles E. Leiserson</Name>
#             <Nationality>American</Nationality>
#         </Author>
#         <Author id="A003">
#             <Name>Ronald L. Rivest</Name>
#             <Nationality>American</Nationality>
#         </Author>
#         <Author id="A004">
#             <Name>Clifford Stein</Name>
#             <Nationality>American</Nationality>
#         </Author>
#         <Author id="A005">
#             <Name>Donald E. Knuth</Name>
#             <Nationality>American</Nationality>
#         </Author>
#         <Author id="A006">
#             <Name>Wes McKinney</Name>
#             <Nationality>American</Nationality>
#         </Author>
#     </Authors>
#     <Members>
#         <Member id="M001">
#             <Name>Jane Doe</Name>
#             <Email>jane.doe@example.com</Email>
#             <Phone>123-456-7890</Phone>
#             <Address>
#                 <Street>123 Main St</Street>
#                 <City>Anytown</City>
#                 <State>CA</State>
#                 <Zip>12345</Zip>
#             </Address>
#             <BorrowedBooks>
#                 <BorrowedBook id="C002" borrowDate="2024-05-01" dueDate="2024-05-21"/>
#                 <BorrowedBook id="C005" borrowDate="2024-05-10" dueDate="2024-05-30"/>
#             </BorrowedBooks>
#         </Member>
#         <Member id="M002">
#             <Name>John Smith</Name>
#             <Email>john.smith@example.com</Email>
#             <Phone>987-654-3210</Phone>
#             <Address>
#                 <Street>456 Elm St</Street>
#                 <City>Othertown</City>
#                 <State>NY</State>
#                 <Zip>67890</Zip>
#             </Address>
#             <BorrowedBooks>
#                 <BorrowedBook id="C001" borrowDate="2024-05-15" dueDate="2024-06-04"/>
#             </BorrowedBooks>
#         </Member>
#     </Members>
#     <Genres>
#         <Genre>Computer Science</Genre>
#         <Genre>Data Science</Genre>
#         <Genre>Fiction</Genre>
#         <Genre>Non-Fiction</Genre>
#     </Genres>
#     <BorrowingRecords>
#         <Record memberId="M001" bookId="C002" borrowDate="2024-05-01" dueDate="2024-05-21" returnDate="2024-05-20"/>
#         <Record memberId="M001" bookId="C005" borrowDate="2024-05-10" dueDate="2024-05-30" returnDate=""/>
#         <Record memberId="M002" bookId="C001" borrowDate="2024-05-15" dueDate="2024-06-04" returnDate=""/>
#     </BorrowingRecords>
# </Library>
# '''
#
# # Parse the XML data
# root = ET.fromstring(xml_data)
#
# # Find all Copy elements and get their id attributes
# copy_ids = [copy.attrib['id'] for copy in root.findall('.//Copy')]
#
# # Print the list of Copy IDs
# print(copy_ids)

import requests

url1 = 'https://random-word-api.herokuapp.com/word?number=10'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

r = requests.get(url1, headers=headers)
print(r.text)
r = requests.get(url1, headers=headers)  # Dergon http get request
r.raise_for_status()  # ben throw error nqs statusi eshte i ndryshem nga 200
data = r.json()  # formaton response ne json

print(data)

url2 = 'https://httpbin.org/anything'

r = requests.post(url2, json={"a": 32, 'b': 12}, headers=headers)  # Dergon body
r.raise_for_status()
print(r.json())  # printon pergjigjjen e marr nga serveri
