# FaceDefinitions.Add Method

Parent Object: [FaceDefinitions](../FaceDefinitions/FaceDefinitions.md)

## Description

Method that creates a new FaceDefinition within the associated SurfaceBodyDefinition.

## Syntax

FaceDefinitions.**Add**( ***SurfaceGeometry*** As Object, ***IsParamReversed*** As Boolean ) As [FaceDefinition](../FaceDefinition/FaceDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SurfaceGeometry | Object | Input transient geometry object that defines the surface geometry of the face. Valid objects for input are BSplineSurface, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Plane, Sphere, and Torus. |
| IsParamReversed | Boolean | Input Boolean that indicates if the normal of this face is reversed with respect to the geometry. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |