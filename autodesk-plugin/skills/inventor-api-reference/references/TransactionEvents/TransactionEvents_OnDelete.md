# TransactionEvents.OnDelete Event

Parent Object: [TransactionEvents](../TransactionEvents/TransactionEvents.md)

## Description

The OnDelete event notifies the client when a transaction has been deleted from the transaction stack.

## Remarks

The transaction stack contains a list of all transactions that can be undone or redone. Transactions are deleted as the result of three things. First, the transaction stack has a fixed number of transactions it can hold, (which is defined in the registry). When the number of transactions goes over this limit, the transactions at the bottom of the stack are deleted. This means they can no longer be undone. The second reason a transaction is deleted is when a transaction is undone and then another transaction is committed. All transactions in the undone state are deleted and can't be redone. The third reason is as a result of a document being closed. Whenever a document is closed the entire transaction stack is cleared. All transactions in the stack will be deleted.

## Syntax

TransactionEvents.**OnDelete**( ***TransactionObject*** As [Transaction](../Transaction/Transaction.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransactionObject | [Transaction](../Transaction/Transaction.md) | The Transaction object just deleted. When the BeforeOrAfter argument is kAfter the actual Transaction has been deleted and the Transaction object provided is not functional except to have it's identify compared with a previously saved reference to a Transaction object. For example: Private m\_oSavedTransaction As Transaction Private Sub oTransActionEvents\_OnCommit( ByVal TransactionObject As Transaction, ...) If BeforeOrAfter = kAfter Then ' Somehow determine this is an interesting transaction. If Interesting(TransactionObject) Then ' Save a reference to the object. Set m\_oSavedTransaction = TransactionObject End If End If End Sub Private Sub oTransActionEvents\_OnDelete( ByVal TransactionObject As Transaction, ...) If BeforeOrAfter = kAfter Then ' Check to see if this is the interesting transaction being deleted. If TransactionObject is m\_oSavedTransaction Then ' The transaction was deleted. End If End If End Sub |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is sent only after the transaction is deleted. |

## Version

Introduced in version 4
