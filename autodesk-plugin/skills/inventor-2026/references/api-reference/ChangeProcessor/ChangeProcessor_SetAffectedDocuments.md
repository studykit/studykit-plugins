# ChangeProcessor.SetAffectedDocuments Method

Parent Object: [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md)

## Description

Sets the FullDocumentNames, and optionally the change types, of the documents that will be affected by this change.

## Remarks

This method is particularly helpful for PDM applications that listen to the OnFileDirty event. This event will supply, in its context, all the documents for which the OnFileDirty event will follow. So the PDM system can ignore the subsequent OnFileDirty events and put up a single check-out dialog that shows all files that need to be checked out.

## Syntax

ChangeProcessor.**SetAffectedDocuments**( ***FullDocumentNames***() As String, [***ReasonsForChange***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentNames | String | Input array of strings that specifies the full document names of all the documents that will be changed as a part of this change process. |
| ReasonsForChange | Variant | Optional input array of CommandTypesEnum (bit-encoded values) that specifies the type of changes being made to the documents. If the size of this array is not the same as the size of the FullDocumentNames array, an error occurs. |

## Version

Introduced in version 2008
