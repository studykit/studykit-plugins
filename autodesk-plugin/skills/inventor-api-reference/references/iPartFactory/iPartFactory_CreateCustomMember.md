# iPartFactory.CreateCustomMember Method

Parent Object: [iPartFactory](../iPartFactory/iPartFactory.md)

## Description

Method that creates an iPart member for a custom factory using the parameter values in a row. The created iPartMember is returned.

## Syntax

iPartFactory.**CreateCustomMember**( ***FullFileName*** As String, [***Row***] As Variant, [***CustomInput***] As Variant ) As [iPartMember](../iPartMember/iPartMember.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the full filename of the iPart member. |
| Row | Variant | Optional input Variant that specifies the row number within an iPart table. The row index is specified either by a Long (row index), a String (PartIdentifier), or an iPartTableRow object. If a RowIndex is not specified, default row will be used to create the iPart member. |
| CustomInput | Variant | Optional input safearray of Strings that specifies the input to use for the custom input. If the factory is a custom factory and this is not supplied the default values for custom values are used. The custom input strings are supplied in a column order. If the factory is not a custom factory this argument is ignored.   This is an optional argument whose default value is null. |

## Version

Introduced in version 6
