# Sheet.AddTitleBlock Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that adds the specified title block definition to the sheet. Since a sheet can only have one title block at a time, calling this method will remove the existing title block.

## Syntax

Sheet.**AddTitleBlock**( ***TitleBlockDefinition*** As Variant, [***TitleBlockLocation***] As Variant, [***PromptStrings***] As Variant ) As [TitleBlock](../TitleBlock/TitleBlock.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TitleBlockDefinition | Variant | Input Variant that specifies which TitleBlockDefinition to use. The input for the argument can be either a TitleBlockDefinition object or string containing the name of an existing TitleBlockDefinition object. |
| TitleBlockLocation | Variant | Optional input value from the TitleBlockLocationEnum enum that defines which corner of the sheet the title block is positioned in. If not supplied, it defaults to the position defined by the sheet. |
| PromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the title block definition. If prompted strings exist in the title block definition you must supply input strings through this argument or this method will fail. The prompt strings and their order are obtained by querying the TextBox objects in the TitleBlockDefinition. The order they're returned by the TextBoxes collection is the same order the input strings need to be supplied in the PromptStrings array.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |