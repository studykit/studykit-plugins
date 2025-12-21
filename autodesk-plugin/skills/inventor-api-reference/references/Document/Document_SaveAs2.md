# Document.SaveAs2 Method

Parent Object: [Document](../Document/Document.md)

## Description

Saves this document into a file of the specified name.

## Syntax

Document.**SaveAs2**( ***FullFileName*** As String, ***SaveCopyAs*** As Boolean, [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full filename of the file to save the document into. |
| SaveCopyAs | Boolean | Input Boolean that indicates whether the file to be saved is new or is a copy of a previously existing file. |
| Options | Variant | Optional input NameValueMap to specify additional options when save the document. Valid options include: Name = SaveDependents. Value = Boolean that specifies whether or not to save dependent documents that have been dirtied. Defaults to True indicating that the dependents will be saved. If the DependentsToSave argument is not specified, all dirty dependents are saved. If the argument is specified as False, only this document will be saved. The argument is ignored if the document doesn't have any dependents needing save. Name = DocumentsToSave. Value = ObjectCollection that contains the Document objects to save. Use the Document.AllReferencedDocuments property to iterate over all dependent documents and find the ones that need to be saved (i.e. Dirty property returns True). If the SaveDependents argument is True and this argument is not specified, all dirty documents are saved. The argument is ignored if the document doesn't have any dependents needing save. |

## Version

Introduced in version 2024
