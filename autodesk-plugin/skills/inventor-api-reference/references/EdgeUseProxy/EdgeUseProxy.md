# EdgeUseProxy Object

Derived from: [EdgeUse](../EdgeUse/EdgeUse.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../EdgeUseProxy/EdgeUseProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeUseProxy/EdgeUseProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContainingOccurrence](../EdgeUseProxy/EdgeUseProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CurveType](../EdgeUseProxy/EdgeUseProxy_CurveType.md) | Gets the type of the underlying curve geometry that this EdgeUse is defined by. |
| [Edge](../EdgeUseProxy/EdgeUseProxy_Edge.md) | Gets the that this EdgeUse references. |
| [EdgeLoop](../EdgeUseProxy/EdgeUseProxy_EdgeLoop.md) | Gets the that contains this EdgeUse. |
| [Evaluator](../EdgeUseProxy/EdgeUseProxy_Evaluator.md) | Gets the Curve2dEvaluator for this edge use. |
| [Geometry](../EdgeUseProxy/EdgeUseProxy_Geometry.md) | Property that returns the underlying geometry of the edge use. |
| [GeometryForm](../EdgeUseProxy/EdgeUseProxy_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [IsOpposedToEdge](../EdgeUseProxy/EdgeUseProxy_IsOpposedToEdge.md) | Gets whether this EdgeUse is opposed to or aligned with the orientation of the referenced Edge. |
| [IsParamReversed](../EdgeUseProxy/EdgeUseProxy_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Curve property is aligned or opposed to the topological sense of this EdgeUse. |
| [NativeObject](../EdgeUseProxy/EdgeUseProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Next](../EdgeUseProxy/EdgeUseProxy_Next.md) | Gets the next in the connected list of EdgeUses in the EdgeLoop. |
| [Parent](../EdgeUseProxy/EdgeUseProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Partner](../EdgeUseProxy/EdgeUseProxy_Partner.md) | In a solid, Face objects are connected to other Face objects by virtue of sharing at least one Edge. The shared Edge is the same object. objects, however ,are unique to a particular face. The Partner property returns the corresponding EdgeUse that belongs to the connected face. |
| [Previous](../EdgeUseProxy/EdgeUseProxy_Previous.md) | Gets the previous . |
| [TransientKey](../EdgeUseProxy/EdgeUseProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../EdgeUseProxy/EdgeUseProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wire](../EdgeUseProxy/EdgeUseProxy_Wire.md) | Get the Wire containing this EdgeUse. Returns Nothing if this EdgeUse does not belong to a Wire. |

## Version

Introduced in version 4
