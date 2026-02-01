# MeasureTools.GetMinimumDistance Method

Parent Object: [MeasureTools](../MeasureTools/MeasureTools.md)

## Description

Method that returns the minimum distance between the two input entities and also returns the closest points associated with both entities (not necessarily on the entity).

## Remarks

The two input entities must belong to the same document, unless they are transient objects. A value of 0 is returned if an intersection is found. The following are the valid entities for minimum distance measure based on the document type:

| Document | Valid entities type |
| --- | --- |
| All (and with no documents open) | Transient objects ( Point, Line, Plane, Cylinder, BSplineSurface, etc.) |
| Part | Face, Edge, Vertex, work features, 2d and 3d sketch entities |
| Assembly | FaceProxy, EdgeProxy, VertexProxy, work features and their proxies, 2d and 3d sketch entities and their proxies, ComponentOccurrences and their proxies |
| Drawing | DrawingViewCurve, GeometryIntent, 2d sketch entities |

## Syntax

MeasureTools.**GetMinimumDistance**( ***EntityOne*** As Object, ***EntityTwo*** As Object, [***EntityOneInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***EntityTwoInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***Context***] As Variant ) As Double

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Object that specifies the first entity. |
| EntityTwo | Object | Object that specifies the second entity. |
| EntityOneInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Optional input InferredTypeEnum that specifies how the geometry of entity one is to be interpreted. Depending on the geometry of the entity one, different options are possible.  * If entity one is a cylinder this can be either kNoInference (cylindrical surface) or kInferredLine (axis). * If entity one is a sphere this can be either kNoInference (spherical surface) or kInferredPoint (center). * If entity one is a cone this can be either kNoInference (conical surface) or kInferredLine (axis). * If entity one is a torus this can be either kInferredLine (axis) or kInferredPoint (center). * If entity one is a circular or elliptical curve this can be either kNoInference (the curve) or kInferredPoint (center). * For all other inputs, only kNoInference is valid. |
| EntityTwoInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Optional input InferredTypeEnum that specifies how the geometry of entity two is to be interpreted. Depending on the geometry of the entity two, different options are possible.  * If entity two is a cylinder this can be either kNoInference (cylindrical surface) or kInferredLine (axis). * If entity two is a sphere this can be either kNoInference (spherical surface) or kInferredPoint (center). * If entity two is a cone this can be either kNoInference (conical surface) or kInferredLine (axis). * If entity two is a torus this can be either kInferredLine (axis) or kInferredPoint (center). * If entity two is a circular or elliptical curve this can be either kNoInference (the curve) or kInferredPoint (center). * For all other inputs, only kNoInference is valid.     This is an optional argument whose default value is 24833. |
| Context | Variant | Optional output NameValueMap object that returns additional information regarding the measurement. Following are the possible return values (descriptions are below the table):  | Name | Value Type | | --- | --- | | ClosestPointOne | Point object that returns a transient point closest to entity one in the minimum distance measure. This point may or may not lie on entity one (but will lie on the plane or axis of entity one). If entity one is a position input (Point, Vertex, WorkPoint, etc.), the position of the input entity is returned. | | ClosestPointTwo | Point object that returns a transient point closest to entity two in the minimum distance measure. This point may or may not lie on entity two (but will lie on the plane or axis of entity two). If entity two is a position input (Point, Vertex, WorkPoint, etc.), the position of the input entity is returned. | | ClosestEntityOne | Object type that returns the entity on which the returned ClosestPointOne lies. This is applicable only in the case where the input EntityOne is a ComponentOccurrence (or itG's proxy). | | ClosestEntityTwo | Object type that returns the entity on which the returned ClosestPointTwo lies. This is applicable only in the case where the input EntityTwo is a ComponentOccurrence (or itG's proxy). | | IntersectionFound | Boolean that indicates whether an intersection was found between entities one and two. If True, the method returns a value of 0. |     This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |

## Version

Introduced in version 11
