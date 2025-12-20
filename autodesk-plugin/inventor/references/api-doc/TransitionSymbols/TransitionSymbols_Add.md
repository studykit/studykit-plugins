# TransitionSymbols.Add Method

Parent Object: [TransitionSymbols](../TransitionSymbols/TransitionSymbols.md)

## Description

Creates a new transition symbol.

## Syntax

TransitionSymbols.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***TransitionSymbolDefinition*** As [TransitionSymbolDefinition](../TransitionSymbolDefinition/TransitionSymbolDefinition.md) ) As [TransitionSymbol](../TransitionSymbol/TransitionSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object containing a series of Point2d objects representing the leader originating at the transition symbol. If the ObjectCollection contains only one Point2d which is on empty space then no leader will be created, and the newly created transition symbol will have its AttachementType set to kNoAttachementType. If the ObjectCollection contains a series of Point2d objects, the last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to(the newly created transition symbol will have its AttachementType set to kGeometryAttachementType) or a Point2d which locates on the position within a drawing view(the newly created transition symbol will have its AttachementType set to kDrawingViewAttachementType). The ObjectCollection must contain at least one item, else the method will fail. This defines whether the symbol is attached to an empty space, a geometry or a DrawingView, and this will require different symbol indication options defined in the TransitionSymbolDefinition argument. |
| TransitionSymbolDefinition | [TransitionSymbolDefinition](../TransitionSymbolDefinition/TransitionSymbolDefinition.md) | Input TransitionSymbolDefinition object that defines the transition symbol to create. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |