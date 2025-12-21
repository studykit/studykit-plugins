# PresentationDocument.PutInternalNameAndRevisionId Method

Parent Object: [PresentationDocument](../PresentationDocument/PresentationDocument.md)

## Description

Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs)

## Syntax

PresentationDocument.**PutInternalNameAndRevisionId**( ***InternalNameToken*** As String, ***RevisionIdToken*** As String, ***InternalName*** As String, ***RevisionId*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalNameToken | String | Input string value to specify the internal name token. |
| RevisionIdToken | String | Input string value to specify the revision token. |
| InternalName | String | Output string(GUID) value that indicates the internal name. |
| RevisionId | String | Output string(GUID) value that indicates the revision Id. |

## Version

Introduced in version 11
