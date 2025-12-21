# DrawingWeldingSymbols.Add Method

Parent Object: [DrawingWeldingSymbols](../DrawingWeldingSymbols/DrawingWeldingSymbols.md)

## Description

Method that creates a drawing welding symbol.

## Syntax

DrawingWeldingSymbols.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Definitions*** As [DrawingWeldingSymbolDefinitions](../DrawingWeldingSymbolDefinitions/DrawingWeldingSymbolDefinitions.md), [***WeldSymbolStyle***] As Variant ) As [DrawingWeldingSymbol](../DrawingWeldingSymbol/DrawingWeldingSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing a series of Point2d objects representing the leader originating at the symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| Definitions | [DrawingWeldingSymbolDefinitions](../DrawingWeldingSymbolDefinitions/DrawingWeldingSymbolDefinitions.md) | Input DrawingWeldingSymbolDefinitions object that defines the input for the DrawingWeldingSymbol. A DrawingWeldingSymbolDefinitions object can be created using the DrawingWeldingSymbols.CreateDefinitions method. It can also be obtained from an existing DrawingWeldingSymbol object. |
| WeldSymbolStyle | Variant | Optional input WeldSymbolStyle object to specify the weld symbol style for the object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drawing Welding Symbol Creation](../../sample-programs/DrawingWeldingSymbolCreation_Sample.md) | This sample is to demonstrate how to create a drawing welding symbol. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |