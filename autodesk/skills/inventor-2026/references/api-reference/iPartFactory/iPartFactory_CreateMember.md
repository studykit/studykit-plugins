# iPartFactory.CreateMember Method

Parent Object: [iPartFactory](../iPartFactory/iPartFactory.md)

## Description

Method that creates an iPart member using the parameter values in a row. The created iPartMember is returned.

## Syntax

iPartFactory.**CreateMember**( [***Row***] As Variant ) As [iPartMember](../iPartMember/iPartMember.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Row | Variant | Optional input Variant that specifies the row number within an iPart table. The row index is specified either by a Long (row index), a String (PartIdentifier), or an iPartTableRow object. If a RowIndex is not specified, the default row will be used to create the iPart member. |

## Version

Introduced in version 6
