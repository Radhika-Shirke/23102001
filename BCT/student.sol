// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;
struct Student {
    uint256 roll;
    string name;
    string div;
}
contract school {
    Student[] public students;
    function addStudent(
        uint256 _roll,
        string memory _name,
        string memory _div
    ) public {
        Student memory newStudent = Student({
            roll: _roll,
            name: _name,
            div: _div
        });
        students.push(newStudent);
    }
    event log(
        string _functionName,
        address _sender,
        uint256 _value,
        bytes _data
    );
    fallback() external payable {
        emit log("fallback", msg.sender, msg.value, msg.data);
    }
    receive() external payable {
        emit log("receive", msg.sender, msg.value, "");
    }
}