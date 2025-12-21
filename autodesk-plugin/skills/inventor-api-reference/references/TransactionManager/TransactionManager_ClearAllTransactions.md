# TransactionManager.ClearAllTransactions Method

Parent Object: [TransactionManager](../TransactionManager/TransactionManager.md)

## Description

Method that clears all the transactions in the committed and undone stacks. After this method is called a user may no longer Undo/Redo until another transaction is committed. This method fails if an identified transaction is in progress.

## Syntax

TransactionManager.**ClearAllTransactions**()

## Version

Introduced in version 9
