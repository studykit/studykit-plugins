# UserParameters.Item Property

Parent Object: [UserParameters](../UserParameters/UserParameters.md)

## Description

Returns the specified UserParameter object from the collection. This is the default property of the UserParameters collection object.

## Syntax

UserParameters.**Item**( ***Index*** As Variant ) As [UserParameter](../UserParameter/UserParameter.md)

## Property Value

This is a read only property whose value is a [UserParameter](../UserParameter/UserParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the UserParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |