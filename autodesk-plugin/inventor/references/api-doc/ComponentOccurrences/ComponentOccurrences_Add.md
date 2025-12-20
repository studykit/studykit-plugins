# ComponentOccurrences.Add Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates a new for an existing part or subassembly. This method is the equivalent of the 'Place Component' command.

## Syntax

ComponentOccurrences.**Add**( ***FullDocumentName*** As String, ***Position*** As [Matrix](../Matrix/Matrix.md) ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input string that specifies the full document name of the part or the sub-assembly. If only the FullFileName is specified, the master document within the file is used. |
| Position | [Matrix](../Matrix/Matrix.md) | Input object that defines the location and orientation to position the occurrence. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [iMate Result Creation](../../sample-programs/iMateResult_Sample.md) | This sample demonstrates creating an iMate result using two existin iMate definitions. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |