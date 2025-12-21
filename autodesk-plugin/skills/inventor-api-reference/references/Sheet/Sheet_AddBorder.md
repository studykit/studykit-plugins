# Sheet.AddBorder Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that adds the specified border definition to the sheet. This method will fail in the case where a border instance already exists on the sheet. In this case, use the Delete method of the Border object to remove the existing one first.

## Syntax

Sheet.**AddBorder**( ***BorderDefinition*** As Variant, [***PromptStrings***] As Variant ) As [Border](../Border/Border.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BorderDefinition | Variant | Input Variant that specifies which BorderDefinition to use. The input for the argument can be either a BorderDefinition object or string containing the name of an existing BorderDefinition object. |
| PromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the border definition. If prompted strings exist in the border definition you must supply input strings through this argument or this method will fail. The prompt strings and their order are obtained by querying the TextBox objects in the BorderDefinition. The order they're returned by the TextBoxes collection is the same order the input strings need to be supplied in the PromptStrings array. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |

## Version

Introduced in version 5.3
