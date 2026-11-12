// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    uint256 private Balance ;

    function deposite (uint256 amount) public {
        Balance += amount;
    }

    function withdraw(uint256 am) public {
        require(Balance >= am, "Insufficient Balance");
        Balance-=am;
    }

    function checkbal() public view returns(uint256) {
        return Balance;
    }
}