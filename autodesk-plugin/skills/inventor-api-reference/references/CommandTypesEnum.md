# CommandTypesEnum Enumerator

## Description

Constants that stand for the different types of commands.

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| kEditMaskCmdType | 57 | Commands that cause the document to become 'dirty'. Includes ShapeEdit, FilePropertyEdit, NonShapeEdit and UpdateWithReferences commands. |
| kFileOperationsCmdType | 4 | Commands that manage file operations - e.g. File Save. |
| kFilePropertyEditCmdType | 8 | Commands that edit File Properties (a.k.a Document Properties). |
| kModelStateSmudgeCmdType | 512 | Commands that cause model state switch, but does not dirty the document. |
| kModelStateUpdatesCmdType | 256 | Commands that cause model state updates (e.g. generate model state member document). |
| kNonShapeEditCmdType | 32 | Commands that edit data (other than File Properties) that is not directly related to the geometry of the model (e.g. color, style). |
| kQueryOnlyCmdType | 2 | Commands that purely query data. These do not 'dirty' the document. |
| kReferencesChangeCmdType | 64 | Commands that cause this document to change which files it references. |
| kSchemaChangeCmdType | 128 | Commands that change the format of the data, but do not change it otherwise (e.g. from the format of one Inventor release to another). |
| kShapeEditCmdType | 1 | Commands that can affect the geometry of the model. |
| kUpdateWithReferencesCmdType | 16 | Commands that cause this document to recalculate its contents with respect to changes that may have occurred in files it is referencing. |
| kViewRepSmudgeCmdType | 1024 | Commands that view representation switch, but does not dirty the document. |

## Version

Introduced in version 6
