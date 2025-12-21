# ComponentOccurrence.ChangeRowOfiAssemblyMember Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that changes the row in the iAssemblyFactory this occurrence references. This method can be used only if the IsiAssemblyMember property returns True.

## Syntax

ComponentOccurrence.**ChangeRowOfiAssemblyMember**( ***NewRow*** As Variant, [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NewRow | Variant | Specifies the new row from the factory. The row index is specified either by a Long (row index), a String (MemberName of a member or DocumentName of a member), or an iAssemblyTableRow object. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for modifying the occurrence. This argument is currently ignored. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |