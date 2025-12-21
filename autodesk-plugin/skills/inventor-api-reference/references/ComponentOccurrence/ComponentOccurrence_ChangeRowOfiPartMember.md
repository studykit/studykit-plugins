# ComponentOccurrence.ChangeRowOfiPartMember Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that changes the row in the iPartTable this iPartMember represents. This method can be used only if the iPartMember property is True.

## Syntax

ComponentOccurrence.**ChangeRowOfiPartMember**( ***NewRow*** As Variant, [***CustomInput***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NewRow | Variant | Specifies the new row from the factory. The row index is specified either by a Long (row index), a String (MemberName of a member or DocumentName of a member), or an iPartTableRow object. |
| CustomInput | Variant | Optional input array of Strings that specifies the input to use for the custom input. If the factory is a custom factory and this is not supplied the default values for custom values are used. The custom input strings are supplied in a column order. If the factory is not a custom factory this argument is ignored. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |