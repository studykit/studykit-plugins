# EdgeCollection.CollectionType Property

Parent Object: [EdgeCollection](../EdgeCollection/EdgeCollection.md)

## Description

Property that returns how the edge collection was constructed. Valid returns are kAllConcave, kAllConvex, kTangentiallyConnected, and kUndefined. This property is set when the EdgeCollection object is originally created. When the ConcaveEdges property of the SurfaceBody object is used, it is set to kAllConcave. When the ConvexEdges property of the SurfaceBody object is used, it is set to kAllConvex. When the TangentiallyConnectedEdges property of the Edge object is used, it is set to kTangentiallyConnected. When it is created using the CreateEdgeCollection method of the TransientObjects it is set to kUndefined. If an EdgeCollection has a collection type other than kUndefined and the contents are changed by adding or removing items from the collection, the CollectionType will be reset to kUndefined.

## Syntax

EdgeCollection.**CollectionType**() As [EdgeCollectionEnum](../EdgeCollectionEnum.md)

## Property Value

This is a read only property whose value is an [EdgeCollectionEnum](../EdgeCollectionEnum.md).

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |