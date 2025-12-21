# Edge Object

## Description

The Edge object. See the Boundary Representation article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateStrokes](../Edge/Edge_CalculateStrokes.md) | Method that calculates the set of strokes that approximate all of the edges of the SurfaceBody, Face or Edge from which the method was called. The Tolerance argument defines the accuracy of the strokes. The output from this method represents a series of line segments, not connected polylines. |
| [CalculateStrokesWithOptions](../Edge/Edge_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetClosestPointTo](../Edge/Edge_GetClosestPointTo.md) | Method that returns a point on the edge that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u parameter of the returned point on the edge, use Edge.Evaluator.GetParamAtPoint method. |
| [GetExistingStrokes](../Edge/Edge_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../Edge/Edge_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetReferenceKey](../Edge/Edge_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceEdge](../Edge/Edge_GetSourceEdge.md) | Method that gets the source edge that has been overridden by this edge. The method returns Nothing if this edge is not an override. An error is returned if this method is called on an edge in a part. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Edge/Edge_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Edge/Edge_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [EdgeUses](../Edge/Edge_EdgeUses.md) | Gets the that reference this Edge. |
| [Evaluator](../Edge/Edge_Evaluator.md) | Gets the CurveEvaluator for this Edge. |
| [Faces](../Edge/Edge_Faces.md) | Property that returns the that this Edge is referenced from. |
| [Geometry](../Edge/Edge_Geometry.md) | Property that returns the underlying geometry of the edge (e.g. Arc2D, Circle, Cone etc.) |
| [GeometryForm](../Edge/Edge_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [GeometryType](../Edge/Edge_GeometryType.md) | Get the curve type of the curve that will be returned from the Geometry property. |
| [IsParamReversed](../Edge/Edge_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this Edge. |
| [IsTolerant](../Edge/Edge_IsTolerant.md) | Indicates if this Edge is using tolerant modeling to allow a non-exact model. |
| [Parent](../Edge/Edge_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PointOnEdge](../Edge/Edge_PointOnEdge.md) | Property that returns a characteristic somewhere in the middle of the Edge. |
| [StartVertex](../Edge/Edge_StartVertex.md) | Gets the Vertex referenced at the start of this Edge. |
| [StopVertex](../Edge/Edge_StopVertex.md) | Gets the Vertex referenced at the end of this Edge. |
| [TangentiallyConnectedEdges](../Edge/Edge_TangentiallyConnectedEdges.md) | Property that returns an that contains the input edge and all tangentially connected edges. The CollectionType of the output EdgeCollection is set to kTangentiallyConnected. |
| [Tolerance](../Edge/Edge_Tolerance.md) | Returns the tolerance being used for modeling calculations and this Edge. |
| [TransientKey](../Edge/Edge_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../Edge/Edge_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wire](../Edge/Edge_Wire.md) | Get the Wire containing this Edge. Returns Nothing if this Edge does not belong to a Wire. |

## Accessed From

[AnalyticEdgeWorkAxisDef.Edge](../AnalyticEdgeWorkAxisDef/AnalyticEdgeWorkAxisDef_Edge.md), [Edge.GetSourceEdge](../Edge/Edge_GetSourceEdge.md), [EdgeProxy.GetSourceEdge](../EdgeProxy/EdgeProxy_GetSourceEdge.md), [EdgeProxy.NativeObject](../EdgeProxy/EdgeProxy_NativeObject.md), [Edges.Item](../Edges/Edges_Item.md), [EdgeUse.Edge](../EdgeUse/EdgeUse_Edge.md), [EdgeUseProxy.Edge](../EdgeUseProxy/EdgeUseProxy_Edge.md), [FilletIntermediateRadius.Edge](../FilletIntermediateRadius/FilletIntermediateRadius_Edge.md), [FilletSetback.Edge](../FilletSetback/FilletSetback_Edge.md), [FlatBendResult.Edge](../FlatBendResult/FlatBendResult_Edge.md), [MeshEdge.Edge](../MeshEdge/MeshEdge_Edge.md), [MeshEdgeProxy.Edge](../MeshEdgeProxy/MeshEdgeProxy_Edge.md), [MidPointWorkPointDef.Edge](../MidPointWorkPointDef/MidPointWorkPointDef_Edge.md), [NonLinearEdgeWorkPointDef.Edge](../NonLinearEdgeWorkPointDef/NonLinearEdgeWorkPointDef_Edge.md), [PublicationMeshEdge.Edge](PublicationMeshEdge_Edge.md), [RuledSurfaceEdgeFacePair.GetData](../RuledSurfaceEdgeFacePair/RuledSurfaceEdgeFacePair_GetData.md), [SurfaceGraphicsEdge.Edge](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Edge.md)

## Derived Classes

[EdgeProxy](../EdgeProxy/EdgeProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 4
