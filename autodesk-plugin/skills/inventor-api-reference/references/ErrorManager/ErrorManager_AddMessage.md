# ErrorManager.AddMessage Method

Parent Object: [ErrorManager](../ErrorManager/ErrorManager.md)

## Description

Method that adds a new message at the current level in the message tree.

## Syntax

ErrorManager.**AddMessage**( ***Message*** As String, ***Error*** As Boolean, [***Reserved***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Message | String | Input String that specifies the error or warning message. |
| Error | Boolean | Input Boolean that specifies whether this is an error or a warning. True indicates error. |
| Reserved | Variant | Optional input Variant reserved for future use. Currently unused. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display custom error messages](../../sample-programs/ErrorManager_AddMessage_Sample.md) | Demonstrates displaying custom error messages. |

## Version

Introduced in version 2010
