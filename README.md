# _py-advanced_

#### By _**Alejandro Socarras**_

#### _Week 3 Code Review_

## Description

Practice generating fake data using the `Faker` library and writing to/reading from JSON files.

_Assignment Instructions_

* Use Python's Faker library to generate a list of twenty colors. Call it color_list.

* Write a function called remove_dups to remove any duplicates from color_list.

* Once color_list only has unique values (no duplicates) use a dictionary comprehension to create a dictionary from it. Each key should be the name of the color, and its value should be the length of the name. Call it color_dict.

* For instance, the list ["pink"] would create the dictionary {"pink": 4}, because the word "pink" has four letters.

* Write color_dict into a JSON file. Include this file in your GitHub repository.

* Read the color_dict back out of the JSON file. If the value is 4 or more, print a string saying the color name and the length of the name.

* Make a file called test_remove_dups.py. In it, use @pytest.mark.parametrize() to test remove_dups() with a list containing duplicates, an empty list, and a string.


## Setup/Installation Requirements

_To run the project from your local system:_

1. Make a directory on your disk where you would like to clone the repo.

2. Copy the repo link: https://github.com/apsocarras/py-intermediate.git (available if you click the green "Code" dropdown button on this page).

3. Open your terminal and change into the directory you made (`cd /path/to/new/directory`).

4. Type `git clone ` and paste the URL.

## Known Bugs

_No known bugs._

## License

_[MIT License](https://opensource.org/licenses/MIT)_

Copyright (c) _11.18.22_ Alejandro Socarras

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
