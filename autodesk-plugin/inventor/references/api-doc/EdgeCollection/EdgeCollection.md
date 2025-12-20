# EdgeCollection Object

Derived from: [ObjectCollection](../ObjectCollection/ObjectCollection.md) Object

## Description

The EdgeCollection object provides access to all of the and EdgeCollection objects in a collection and provides methods to add Edge and EdgeCollection objects to the collection.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../EdgeCollection/EdgeCollection_Add.md) | Adds an object to the generic collection. |
| [Clear](../EdgeCollection/EdgeCollection_Clear.md) | Removes all objects from the generic collection. |
| [Remove](../EdgeCollection/EdgeCollection_Remove.md) | Method that removes the specified object from the generic collection. |
| [RemoveByObject](../EdgeCollection/EdgeCollection_RemoveByObject.md) | Method that removes the specified object from the generic object collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [CollectionType](../EdgeCollection/EdgeCollection_CollectionType.md) | Property that returns how the edge collection was constructed. Valid returns are kAllConcave, kAllConvex, kTangentiallyConnected, and kUndefined. This property is set when the EdgeCollection object is originally created. When the ConcaveEdges property of the SurfaceBody object is used, it is set to kAllConcave. When the ConvexEdges property of the SurfaceBody object is used, it is set to kAllConvex. When the TangentiallyConnectedEdges property of the Edge object is used, it is set to kTangentiallyConnected. When it is created using the CreateEdgeCollection method of the TransientObjects it is set to kUndefined. If an EdgeCollection has a collection type other than kUndefined and the contents are changed by adding or removing items from the collection, the CollectionType will be reset to kUndefined. |
| [Count](../EdgeCollection/EdgeCollection_Count.md) | Property that returns the number of items in this collection. |
| [Item](../EdgeCollection/EdgeCollection_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../EdgeCollection/EdgeCollection_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendDefinition.Edges](../BendDefinition/BendDefinition_Edges.md), [ChamferDefinition.ChamferedEdges](../ChamferDefinition/ChamferDefinition_ChamferedEdges.md), [ContourFlangeDefinition.BendEdges](../ContourFlangeDefinition/ContourFlangeDefinition_BendEdges.md), [CornerChamferDefinition.CornerEdges](../CornerChamferDefinition/CornerChamferDefinition_CornerEdges.md), [CornerDefinition.Edges](../CornerDefinition/CornerDefinition_Edges.md), [CornerRoundEdgeSet.Edges](../CornerRoundEdgeSet/CornerRoundEdgeSet_Edges.md), [CornerRoundFeatures.GetEdgesFromFeature](../CornerRoundFeatures/CornerRoundFeatures_GetEdgesFromFeature.md), [CosmeticWeldDefinition.Edges](../CosmeticWeldDefinition/CosmeticWeldDefinition_Edges.md), [DerivedAssemblyDefinition.GetHolePatchingOptions](../DerivedAssemblyDefinition/DerivedAssemblyDefinition_GetHolePatchingOptions.md), [Edge.TangentiallyConnectedEdges](../Edge/Edge_TangentiallyConnectedEdges.md), [EdgeProxy.TangentiallyConnectedEdges](../EdgeProxy/EdgeProxy_TangentiallyConnectedEdges.md), [FaceDraftDefinition.FixedEdges](../FaceDraftDefinition/FaceDraftDefinition_FixedEdges.md), [FilletConstantRadiusEdgeSet.Edges](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet_Edges.md), [FilletRadiusEdgeSet.Edges](../FilletRadiusEdgeSet/FilletRadiusEdgeSet_Edges.md), [FilletVariableRadiusEdgeSet.Edges](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_Edges.md), [FlangeEdgeSet.Edges](../FlangeEdgeSet/FlangeEdgeSet_Edges.md), [HemDefinition.Edges](../HemDefinition/HemDefinition_Edges.md), [PartialChamferEdge.Edge](../PartialChamferEdge/PartialChamferEdge_Edge.md), [SurfaceBody.ConcaveEdges](../SurfaceBody/SurfaceBody_ConcaveEdges.md), [SurfaceBody.ConvexEdges](../SurfaceBody/SurfaceBody_ConvexEdges.md), [SurfaceBodyProxy.ConcaveEdges](../SurfaceBodyProxy/SurfaceBodyProxy_ConcaveEdges.md), [SurfaceBodyProxy.ConvexEdges](../SurfaceBodyProxy/SurfaceBodyProxy_ConvexEdges.md), [TransientObjects.CreateEdgeCollection](../TransientObjects/TransientObjects_CreateEdgeCollection.md), [UnwrapDefinition.LinearResult](../UnwrapDefinition/UnwrapDefinition_LinearResult.md), [UnwrapDefinition.RigidResult](../UnwrapDefinition/UnwrapDefinition_RigidResult.md), [UnwrapDefinition.SeamEdges](../UnwrapDefinition/UnwrapDefinition_SeamEdges.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |