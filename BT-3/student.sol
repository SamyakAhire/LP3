// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DS {
    struct Student{
        string name;
        uint256 age;
    }

    Student[] students;

    function addstudent(string memory name, uint256 age) public {
        students.push(Student(name,age));
    }

    function display(uint256 index) public view returns(string memory,uint256) {
        require(index < students.length, "Invalid Index");
        return (students[index].name, students[index].age);
    }

    function getcount() public view returns(uint) {
        return students.length;
    }

    receive() external payable { }

    fallback() external payable { }

}