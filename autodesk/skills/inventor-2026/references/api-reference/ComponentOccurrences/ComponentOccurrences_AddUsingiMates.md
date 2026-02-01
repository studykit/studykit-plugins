# ComponentOccurrences.AddUsingiMates Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that adds a new occurrence into the assembly. This method is the equivalent of using the Place Component command with the "Use iMate" check box checked. The method returns a failure if no matches are found.

## Remarks

The valid values for the Options parameter are:

| Name | Value Type | Valid Document Type |
| --- | --- | --- |
| PrivateRepresentationFileName | String | Assembly |
| DesignViewRepresentation | String | Assembly |
| DesignViewAssociative | Boolean | Assembly |
| PositionalRepresentation | String | Assembly |
| ModelState | String | Assembly |

## Syntax

ComponentOccurrences.**AddUsingiMates**( ***FullDocumentName*** As String, [***PlaceAllMatching***] As Boolean, [***Options***] As Variant ) As [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input string that specifies the full document name of the part or the sub-assembly. If only the FullFileName is specified, the master document within the file is used. |
| PlaceAllMatching | Boolean | Optional input Boolean that indicates whether to place multiple components corresponding to all iMate definition matches in the assembly. If specified to be True, multiple ComponentOccurrences could be returned. If specified to be False, a single ComponentOccurrence corresponding to the first match is returned. |
| Options | Variant | Input NameValueMap object that specifies additional options for creating the occurrence. (An empty NameValueMap object can be provided). See Remarks for valid options.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |

## Version

Introduced in version 6
