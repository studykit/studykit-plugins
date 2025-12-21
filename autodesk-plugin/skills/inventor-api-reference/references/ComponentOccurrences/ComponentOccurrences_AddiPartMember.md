# ComponentOccurrences.AddiPartMember Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates an of an iPartMember in this AssemblyComponentDefinition. The iPartMember is specified by a factory and a row in the factory.

## Syntax

ComponentOccurrences.**AddiPartMember**( ***FactoryFileName*** As String, ***Position*** As [Matrix](../Matrix/Matrix.md), [***Row***] As Variant ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FactoryFileName | String | Input String that specifies the full filename of the iPart factory. |
| Position | [Matrix](../Matrix/Matrix.md) | Input Matrix that defines the position and orientation of the iPart placement within the assembly. |
| Row | Variant | Optional input Variant that specifies the row for the member within the factory. The row index is specified either by a Long (row index), a String (part identifier, i.e. ''[Height=1.000 in][Length=2.000 in][Radius=0.250 in]''), or an iPartTableRow object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |

## Version

Introduced in version 6
