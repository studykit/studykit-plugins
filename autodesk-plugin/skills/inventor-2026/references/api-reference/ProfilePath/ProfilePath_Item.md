# ProfilePath.Item Property

Parent Object: [ProfilePath](../ProfilePath/ProfilePath.md)

## Description

Returns the specified ProfileEntity object from the collection. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply.

## Syntax

ProfilePath.**Item**( ***Index*** As Long ) As [ProfileEntity](../ProfileEntity/ProfileEntity.md)

## Property Value

This is a read only property whose value is a [ProfileEntity](../ProfileEntity/ProfileEntity.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the object to return. |

## Version

Introduced in version 5
