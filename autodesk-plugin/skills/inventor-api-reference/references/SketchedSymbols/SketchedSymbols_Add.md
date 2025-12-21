# SketchedSymbols.Add Method

Parent Object: [SketchedSymbols](../SketchedSymbols/SketchedSymbols.md)

## Description

Method that places a sketched symbol onto the sheet.

## Syntax

SketchedSymbols.**Add**( ***SketchedSymbolDefinition*** As Variant, ***Position*** As [Point2d](../Point2d/Point2d.md), [***Rotation***] As Double, [***Scale***] As Double, [***PromptStrings***] As Variant ) As [SketchedSymbol](../SketchedSymbol/SketchedSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchedSymbolDefinition | Variant | Input Variant that specifies which SketchedSymbolDefinition to use. The input for the argument can be either a SketchedSymbolDefinition object or string containing the name of an existing SketchedSymbolDefinition object. |
| Position | [Point2d](../Point2d/Point2d.md) | Input that specifies the location on the sheet to place the sketched symbol instance. |
| Rotation | Double | The rotation of the symbol, in radians. |
| Scale | Double | The scale of the symbol.   This is an optional argument whose default value is 1.0. |
| PromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the sketched symbol definition. If prompted strings exist in the sketched symbol definition you must supply input strings through this argument or this method will fail. The prompt strings and their order are obtained by querying the TextBox objects in the SketchedSymbolDefinition. The order they're returned by the TextBoxes collection is the same order the input strings need to be supplied in the PromptStrings array.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketched Symbol Definition Library Creation](../../sample-programs/SketchedSymbolDefinitionLibraries_Add_Sample.md) | This sample demonstrates how to create a sketched symbol definition and save it to the SketchedSymbolDefinitionLibrary, and then add the sketched symbol definition from the SketchedSymbolDefinitionLibrary to another drawing document. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |