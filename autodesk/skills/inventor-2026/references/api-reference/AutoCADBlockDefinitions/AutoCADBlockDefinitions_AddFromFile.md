# AutoCADBlockDefinitions.AddFromFile Method

Parent Object: [AutoCADBlockDefinitions](../AutoCADBlockDefinitions/AutoCADBlockDefinitions.md)

## Description

Method that imports AutoCAD block definitions from an AutoCAD or an Inventor DWG file.

## Syntax

AutoCADBlockDefinitions.**AddFromFile**( ***DWGFullFileName*** As String, [***DefinitionNames***] As Variant, [***ReplaceExisting***] As Boolean ) As [AutoCADBlockDefinitionsEnumerator](../AutoCADBlockDefinitionsEnumerator/AutoCADBlockDefinitionsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DWGFullFileName | String | Input String that specifies the full file name of the AutoCAD or Inventor DWG file from which to import the definitions. |
| DefinitionNames | Variant | Optional input array of strings that specifies the names of the definitions to import from the source file. If not specified, all AutoCAD block definitions are imported. |
| ReplaceExisting | Boolean | Optional input Boolean that specifies whether to replace or create a new definition with a different name if a definition of the same name exists in the target document. If not specified, the argument defaults to False indicating that a new definition will be created.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block definitions import](../../sample-programs/AutoCADBlockDefinitions_AddFromFile_Sample.md) | This sample demonstrates importing AutoCAD block definitions from an external dwg file. |

## Version

Introduced in version 2011
