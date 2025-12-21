# SketchedSymbol.GetResultText Method

Parent Object: [SketchedSymbol](../SketchedSymbol/SketchedSymbol.md)

## Description

Method that returns the text that is currently displayed for a specific text box. This is useful for text boxes that use input form other sources to define their content, i.e. properties and prompted text. The string displayed within this text box is returned.

## Syntax

SketchedSymbol.**GetResultText**( ***DefinitionText*** As [TextBox](../TextBox/TextBox.md) ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DefinitionText | [TextBox](../TextBox/TextBox.md) | Input TextBox object from the referenced TitleBlockDefinition object. This text box is used to specify which prompted text box to set the text for. |

## Version

Introduced in version 5.3
