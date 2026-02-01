# Sheets.AddUsingSheetFormat Method

Parent Object: [Sheets](../Sheets/Sheets.md)

## Description

Method that creates a new Sheet based on the input format. The newly created Sheet is returned.

## Remarks

Supported values for the Options parameter:

| Name | Value Type | Valid document type |
| --- | --- | --- |
| WeldmentFeatureGroup | WeldmentFeatureGroupEnum | Weldment |
| SheetMetalFoldedModel | Boolean | Sheet Metal |
| DesignViewRepresentation | String | Assembly |
| DesignViewAssociative | Boolean | Assembly |
| PositionalRepresentation | String | Assembly |
| MemberName | String | Part, Assembly |

## Syntax

Sheets.**AddUsingSheetFormat**( ***SheetFormat*** As [SheetFormat](../SheetFormat/SheetFormat.md), [***Model***] As Variant, [***SheetName***] As String, [***AdditionalOptions***] As Variant, [***TitleBlockPromptStrings***] As Variant, [***BorderPromptStrings***] As Variant ) As [Sheet](../Sheet/Sheet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SheetFormat | [SheetFormat](../SheetFormat/SheetFormat.md) | Input Sheet object that specifies the sheet to be used as the template for creating the sheet format. |
| Model | Variant | Optional input that specifies the model to create drawings views of. This can either be the model Document object or a string that specifies the FullDocumentName of the model. This is a required input if the input SheetFormat defines at least one drawing view. |
| SheetName | String | Optional input String that defines the editable portion of the name that is displayed within the browser. If not specified, a default name is assigned to the sheet.   This is an optional argument whose default value is "". |
| AdditionalOptions | Variant | Optional input NameValueMap object that specifies additional or advanced options for drawing view creation. See Remarks for supported values.   This is an optional argument whose default value is null. |
| TitleBlockPromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the title block definition referenced by the sheet format. The prompt strings and their order are obtained by querying the TextBox objects in the TitleBlockDefinition. The order they’re returned by the TextBoxes collection is the same order the input strings need to be supplied in the TitleBlockPromptStrings array.   This is an optional argument whose default value is null. |
| BorderPromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the border definition. The prompt strings and their order are obtained by querying the TextBox objects in the BorderDefinition. The order they’re returned by the TextBoxes collection is the same order the input strings need to be supplied in the BorderPromptStrings array.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet with multiple views](../../sample-programs/SheetFormat_Sample.md) | This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views. |

## Version

Introduced in version 2009
