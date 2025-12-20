# MessageSection.AdoptMessages Method

Parent Object: [MessageSection](../MessageSection/MessageSection.md)

## Description

Method that adopts all messages within this section under the specified message and terminates the section.

## Syntax

MessageSection.**AdoptMessages**( ***Message*** As String, ***Error*** As Boolean, [***Reserved***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Message | String | Input String that specifies the error or warning message to be used as the parent of existing messages. |
| Error | Boolean | Input Boolean that specifies whether this is an error or a warning. True indicates error. |
| Reserved | Variant | Optional input Variant reserved for future use. Currently unused. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Display custom error messages](../../sample-programs/ErrorManager_AddMessage_Sample.md) | Demonstrates displaying custom error messages. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |