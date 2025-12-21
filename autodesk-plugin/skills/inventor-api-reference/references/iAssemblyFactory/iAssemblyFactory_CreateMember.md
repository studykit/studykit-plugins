# iAssemblyFactory.CreateMember Method

Parent Object: [iAssemblyFactory](../iAssemblyFactory/iAssemblyFactory.md)

## Description

Method that creates an iAssembly member using the parameter values in a row. The created iAssemblyMember is returned. If the member already exists, the member is updated and the iAssemblyMember object is returned.

## Syntax

iAssemblyFactory.**CreateMember**( [***Row***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Row | Variant | Optional input Variant that specifies the row number within an iAssembly table. The row index is specified either by a Long (row index), a String (MemberName), or an iAssemblyTableRow object. If the argument is not specified, the default row of the factory will be used to create the iAssembly member. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |