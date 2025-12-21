# PartsLists.Add Method

Parent Object: [PartsLists](../PartsLists/PartsLists.md)

## Description

Method that creates a new PartsList. The newly created PartsList is returned. Currently, this method will fail if the sheet from which this collection was obtained is not active.

## Syntax

PartsLists.**Add**( ***ViewOrModel*** As Object, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***Level***] As [PartsListLevelEnum](../PartsListLevelEnum.md), [***NumberingScheme***] As Variant, [***NumberOfSections***] As Long, [***WrapLeft***] As Boolean ) As [PartsList](../PartsList/PartsList.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewOrModel | Object | Input object that specifies the source for the parts list. This can either be a DrawingView object or a Document object. Valid document types include part files and assembly files. Use the Documents.Open method to open the file if not already open and obtain a Document object. Typically you'll want to set the OpenVisible argument of the Open method to False so the open is invisible to the user. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the parts list on the sheet. |
| Level | [PartsListLevelEnum](../PartsListLevelEnum.md) | Optional input enum that sets the type of numbering for the parts list. If supplied, this input is only used in the case where the ParentView references an assembly file. If this value was previously set on the parent drawing view as a result of creating a parts list or a balloon based on the view, this argument is ignored. Valid enums are: kFirstLevelComponents, that creates a parts list in which subassemblies are assigned nested numbering (for example, 1, 1.1, 1.1.1) and the nested number extends as many levels as needed for the assembly levels in the model and kPartsOnly, that creates a parts list that sequentially numbers all parts in the top level assembly, even if they are contained in subassemblies. |
| NumberingScheme | Variant | Optional input NameValueMap object that specifies the numbering scheme to use for the parts list. The NameValueMap can contain the following entries based on the input 'Level' argument: \* For kStructured: MinimumDigits As Long \* For kStructuredAllLevels: Delimiter As String \* For kPartsOnly: NumberingScheme As NumberingSchemeEnum and MinimumDigits As Long Valid values for NumberingSchemeEnum are kNumericNumbering, kLowercaseAlphaNumbering and kUppercaseAlphaNumbering. This input should be supplied only if the input argument Level is specified to be kPartsOnly. If this argument is not supplied for a 'parts only' parts list, a default value of kNumericNumbering is assumed.   This is an optional argument whose default value is null. |
| NumberOfSections | Long | Optional input long that specifies the number of sections desired in the parts list. If supplied, this input is only used in the case where the ParentView references an assembly file. The default value is 1.   This is an optional argument whose default value is 1. |
| WrapLeft | Boolean | Optional input Boolean that specifies whether to move the sections to the left or the right when the number of rows increase. If supplied, this input is only used in the case where the ParentView references an assembly file. The default value is true, indicating that sections will be moved to the left.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |