# ComponentOccurrences.AddiAssemblyMember Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates an occurrence of an iAssemblyMember in an assembly. The iAssemblyMember is specified by a factory and a row in the factory.

## Syntax

ComponentOccurrences.**AddiAssemblyMember**( ***FactoryDocumentName*** As String, ***Position*** As [Matrix](../Matrix/Matrix.md), [***Row***] As Variant, [***Options***] As Variant ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FactoryDocumentName | String | String that specifies the full document name of the iAssembly factory. |
| Position | [Matrix](../Matrix/Matrix.md) | Matrix that defines the position and orientation of the iAssembly member placement within the assembly. |
| Row | Variant | Optional input Variant that specifies the row for the member within the factory. The row index is specified either by a Long (row index), a String (MemberName of a member), or an iAssemblyTableRow object. If not specified, the default row within the factory is used. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for creating the occurrence. The valid options are:  Name Value Type  PrivateRepresentationFileName String  DesignViewRepresentation String  PositionalRepresentation String  UseiMate Boolean  PrivateRepresentationFileName As String If a PrivateRepresentationFileName (an idv file name) is specified, the DesignViewRepresentation name should be one of the private design views within that idv file else an error will occur. This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |