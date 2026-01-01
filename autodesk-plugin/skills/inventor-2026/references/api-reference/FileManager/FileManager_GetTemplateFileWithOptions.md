# FileManager.GetTemplateFileWithOptions Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Method that gets a template file that can be used to create a new document.

## Syntax

FileManager.**GetTemplateFileWithOptions**( ***DocType*** As [DocumentTypeEnum](../DocumentTypeEnum.md), [***SystemOfMeasure***] As Variant, [***DraftingStandard***] As Variant, [***DocumentSubType***] As Variant, [***MoreOptions***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocType | [DocumentTypeEnum](../DocumentTypeEnum.md) | Input constant that specifies the type of to create. |
| SystemOfMeasure | Variant | Optional input SystemOfMeasureEnum that specifies the system of measure to use in the drawing being created. |
| DraftingStandard | Variant | Optional input DraftingStandardEnum that specifies the drafting standard to use in the drawing being created.   This is an optional argument whose default value is null. |
| DocumentSubType | Variant | Optional input constant (GUID) that specifies the subtype of the document to be created (sheet metal or weldment).   This is an optional argument whose default value is null. |
| MoreOptions | Variant | Optional NameValueMap that species more options. Valid options are:   Name = “TemplatePathType”. Value = String value that indicates where the template file is retrieved from. The “Application” indicates that the template path that is defined by Application is used. The “Project” indicates that the template path that is defined by active Inventor Project is used. The “Global” indicates the template path that is from installation folder. If not specified the templates path defined in the active Inventor Project will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025
