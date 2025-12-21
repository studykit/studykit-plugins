# ReferenceKeyManager.StringToKey Method

Parent Object: [ReferenceKeyManager](../ReferenceKeyManager/ReferenceKeyManager.md)

## Description

Converts a string to a reference key byte array.

## Syntax

ReferenceKeyManager.**StringToKey**( ***ReferenceKeyString*** As String, ***ReferenceKey***() As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceKeyString | String | The string to convert that represents a reference key. The string is a Base64 encoding of the original byte data representing the reference key. Typically it is created by calling the ReferenceKeyManager.KeyToString method. |
| ReferenceKey | Byte | The resultant reference key. |

## Version

Introduced in version 10
