# iPartMember.ChangeRow Method

Parent Object: [iPartMember](../iPartMember/iPartMember.md)

## Description

Method that changes the row in the iPartTable that this custom iPartMember represents. This method is only valid for custom members. This can be determined using the CustomMember property.

## Syntax

iPartMember.**ChangeRow**( ***NewRow*** As Variant, [***CustomInput***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NewRow | Variant | Input Variant that specifies the new row. The row index is specified either by a Long (row index), a String (part identifier, i.e. ''[Height=1.000 in][Length=2.000 in][Radius=0.250 in]''), or an iPartTableRow object. If a RowIndex is not specified, default row will be used to create the iPart member. |
| CustomInput | Variant | Optional input safearray of Strings that specifies the input to use for the custom input. If the factory is a custom factory and this is not supplied the default values for custom values are used. The custom input strings are supplied in a column order. If the factory is not a custom factory this argument is ignored. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |