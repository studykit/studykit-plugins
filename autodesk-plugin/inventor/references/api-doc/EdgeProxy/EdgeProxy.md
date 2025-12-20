# EdgeProxy Object

Derived from: [Edge](../Edge/Edge.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateStrokes](../EdgeProxy/EdgeProxy_CalculateStrokes.md) | Method that calculates the set of strokes that approximate all of the edges of the SurfaceBody, Face or Edge from which the method was called. The Tolerance argument defines the accuracy of the strokes. The output from this method represents a series of line segments, not connected polylines. |
| [CalculateStrokesWithOptions](../EdgeProxy/EdgeProxy_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetClosestPointTo](../EdgeProxy/EdgeProxy_GetClosestPointTo.md) | Method that returns a point on the edge that is closest to the input point. A single point is returned even if multiple equidistant points are found. To get the u parameter of the returned point on the edge, use Edge.Evaluator.GetParamAtPoint method. |
| [GetExistingStrokes](../EdgeProxy/EdgeProxy_GetExistingStrokes.md) | Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetExistingStrokeTolerances](../EdgeProxy/EdgeProxy_GetExistingStrokeTolerances.md) | Method that gets the tolerances that were used to calculate the existing sets of display strokes. These can be used to determine if any existing strokes have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing strokes to retrieve when using the GetExistingStrokes method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. |
| [GetReferenceKey](../EdgeProxy/EdgeProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceEdge](../EdgeProxy/EdgeProxy_GetSourceEdge.md) | Method that gets the source edge that has been overridden by this edge. The method returns Nothing if this edge is not an override. An error is returned if this method is called on an edge in a part. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeProxy/EdgeProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EdgeProxy/EdgeProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../EdgeProxy/EdgeProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EdgeUses](../EdgeProxy/EdgeProxy_EdgeUses.md) | Gets the that reference this Edge. |
| [Evaluator](../EdgeProxy/EdgeProxy_Evaluator.md) | Gets the CurveEvaluator for this Edge. |
| [Faces](../EdgeProxy/EdgeProxy_Faces.md) | Property that returns the that this Edge is referenced from. |
| [Geometry](../EdgeProxy/EdgeProxy_Geometry.md) | Property that returns the underlying geometry of the edge (e.g. Arc2D, Circle, Cone etc.) |
| [GeometryForm](../EdgeProxy/EdgeProxy_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [GeometryType](../EdgeProxy/EdgeProxy_GeometryType.md) | Get the curve type of the curve that will be returned from the Geometry property. |
| [IsParamReversed](../EdgeProxy/EdgeProxy_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this Edge. |
| [IsTolerant](../EdgeProxy/EdgeProxy_IsTolerant.md) | Indicates if this Edge is using tolerant modeling to allow a non-exact model. |
| [NativeObject](../EdgeProxy/EdgeProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../EdgeProxy/EdgeProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PointOnEdge](../EdgeProxy/EdgeProxy_PointOnEdge.md) | Property that returns a characteristic somewhere in the middle of the Edge. |
| [StartVertex](../EdgeProxy/EdgeProxy_StartVertex.md) | Gets the Vertex referenced at the start of this Edge. |
| [StopVertex](../EdgeProxy/EdgeProxy_StopVertex.md) | Gets the Vertex referenced at the end of this Edge. |
| [TangentiallyConnectedEdges](../EdgeProxy/EdgeProxy_TangentiallyConnectedEdges.md) | Property that returns an that contains the input edge and all tangentially connected edges. The CollectionType of the output EdgeCollection is set to kTangentiallyConnected. |
| [Tolerance](../EdgeProxy/EdgeProxy_Tolerance.md) | Returns the tolerance being used for modeling calculations and this Edge. |
| [TransientKey](../EdgeProxy/EdgeProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../EdgeProxy/EdgeProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wire](../EdgeProxy/EdgeProxy_Wire.md) | Get the Wire containing this Edge. Returns Nothing if this Edge does not belong to a Wire. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |