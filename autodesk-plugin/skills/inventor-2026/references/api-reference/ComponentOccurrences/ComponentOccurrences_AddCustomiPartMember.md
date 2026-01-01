# ComponentOccurrences.AddCustomiPartMember Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates an of an iPartMember in this AssemblyComponentDefinition. The iPartMember is specified by a custom factory and a row in the factory.

## Syntax

ComponentOccurrences.**AddCustomiPartMember**( ***FactoryFileName*** As String, ***Position*** As [Matrix](../Matrix/Matrix.md), ***FullFileName*** As String, [***Row***] As Variant, [***CustomInput***] As Variant ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FactoryFileName | String | Input String that specifies the full filename of the iPart factory. |
| Position | [Matrix](../Matrix/Matrix.md) | Input object that defines the position and orientation of the iPart placement within the assembly. |
| FullFileName | String | Input String that defines the filename of the resulting member. If the filename is not specified the default filename for the row will be used. In the case of a custom factory the filename must be specified and is not optional. |
| Row | Variant | Optional input Variant that specifies the row for the member within the factory. The row index is specified either by a Long (row index), a String (part identifier, i.e. ''[Height=1.000 in][Length=2.000 in][Radius=0.250 in]''), or an iPartTableRow object. |
| CustomInput | Variant | Optional input array of Strings that specifies the input to use for the custom input. If the factory is a custom factory and this is not supplied the default values for custom values are used. The custom input strings are supplied in a column order. If the factory is not a custom factory this argument is ignored.   This is an optional argument whose default value is null. |

## Version

Introduced in version 6
