# Document.Close Method

Parent Object: [Document](../Document/Document.md)

## Description

Closes this document.

## Syntax

Document.**Close**( [***SkipSave***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SkipSave | Boolean | Optional input Boolean that specifies whether to skip the save. If SkipSave is set to True, it indicates that the changes to the document should not be saved and that the document should be closed silently. If SkipSave is set to False, it indicates that the normal save process should be followed (including prompting a dialog to the user). In addition, if Application.SilentOperation is set to True, the default choice on the dialog should be accepted. The Close method will fail if the combination of SkipSave = False and SilentOperation = True is used for a previously unsaved document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |

## Version

Introduced in version 4
