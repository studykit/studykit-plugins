# TransactionEvents.OnCommit Event

Parent Object: [TransactionEvents](../TransactionEvents/TransactionEvents.md)

## Description

The OnCommit event notifies the client when a transaction has been committed.

## Remarks

A transaction is defined as an operation that the end-user can undo. When a transaction has been committed it means that the operation has been completed and is now on the transaction stack and can be undone. From Inventor 2009, this event no longer supports kEventCanceled.

## Syntax

TransactionEvents.**OnCommit**( ***TransactionObject*** As [Transaction](../Transaction/Transaction.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransactionObject | [Transaction](../Transaction/Transaction.md) | The Transaction object that is being committed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is sent before and after the transaction is committed. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 4
