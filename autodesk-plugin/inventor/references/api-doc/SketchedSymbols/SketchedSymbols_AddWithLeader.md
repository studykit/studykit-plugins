# SketchedSymbols.AddWithLeader Method

Parent Object: [SketchedSymbols](../SketchedSymbols/SketchedSymbols.md)

## Description

Method that places a sketched symbol with a leader.

## Syntax

SketchedSymbols.**AddWithLeader**( ***SketchedSymbolDefinition*** As Variant, ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Rotation***] As Double, [***Scale***] As Double, [***PromptStrings***] As Variant, [***SymbolClipping***] As Boolean, [***Static***] As Boolean ) As [SketchedSymbol](../SketchedSymbol/SketchedSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchedSymbolDefinition | Variant | Input Variant that specifies which SketchedSymbolDefinition to use. The input for the argument can be either a SketchedSymbolDefinition object or string containing the name of an existing SketchedSymbolDefinition object. |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing a series of Point2d objects representing the leader originating at the symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| Rotation | Double | Optional input double that specifies a rotation angle for the symbol in radians. If not specified, a default value of 0 is used, indicating that no rotation is applied. |
| Scale | Double | Optional input double that specifies a scale for the symbol in radians. If not specified, a default value of 1 is used, indicating that no scaling is applied.   This is an optional argument whose default value is 1.0. |
| PromptStrings | Variant | Optional input array of Strings that specifies the input strings to use as input for prompted text fields that my be present in the sketched symbol definition. If prompted strings exist in the sketched symbol definition you must supply input strings through this argument or this method will fail. The prompt strings and their order are obtained by querying the TextBox objects in the SketchedSymbolDefinition. The order they’re returned by the TextBoxes collection is the same order the input strings need to be supplied in the PromptStrings array.   This is an optional argument whose default value is null. |
| SymbolClipping | Boolean | Optional input Boolean that indicates whether to trim the annotations applied to the symbol. If True, the annotations are trimmed. If not specified, a value of True is used.   This is an optional argument whose default value is True. |
| Static | Boolean | Optional input Boolean that indicates whether to show the scale and rotation grip points on the symbol. If True, the grip points are disabled. If not specified, a value of False is used.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |