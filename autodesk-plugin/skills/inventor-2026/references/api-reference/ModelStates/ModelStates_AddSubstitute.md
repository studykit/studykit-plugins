# ModelStates.AddSubstitute Method

Parent Object: [ModelStates](../ModelStates/ModelStates.md)

## Description

Method that creates a new ModelState. The newly created ModelState is returned.

## Syntax

ModelStates.**AddSubstitute**( ***FullFileName*** As String, [***Name***] As Variant, [***SkipDocumentSave***] As Variant ) As [ModelState](../ModelState/ModelState.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full name of the file to create the substitute model state with. |
| Name | Variant | Optional input String that specifies the name of the new ModelState. If not specified a default name will be used. |
| SkipDocumentSave | Variant | Optional input Boolean that indicates whether to suppress the save dialogs that appear for dirty documents that are about to be closed as a result of this action. If set to True, any edits performed on the documents needing to be closed are lost. Also, any document never saved to disk and needing to be closed is lost. The default value is False indicating that the user will be prompted to save documents about to be closed.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 2022
