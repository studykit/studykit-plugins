# Plane Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Transient plane. A transient plane is not displayed or saved in a document. Transient planes are used as a wrapper to work with raw plane information. A transient plane has no boundaries or size, but is infinite and is represented by a position, a normal, and an orientation in space. They are created statically using the create method of the Plane class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Plane_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Plane_copy.htm) | Creates and returns an independent copy of this Plane object. |
| [create](Plane_create.htm) | Creates a transient plane object by specifying an origin and a normal direction. |
| [createUsingDirections](Plane_createUsingDirections.htm) | Creates a transient plane object by specifying an origin along with U and V directions. |
| [intersectWithCurve](Plane_intersectWithCurve.htm) | Intersect this plane with a curve to get the intersection point(s). |
| [intersectWithLine](Plane_intersectWithLine.htm) | Creates a 3D point at the intersection of this plane and a line. |
| [intersectWithPlane](Plane_intersectWithPlane.htm) | Creates an infinite line at the intersection of this plane with another plane. |
| [intersectWithSurface](Plane_intersectWithSurface.htm) | Intersect this plane with a surface to get the intersection point(s). |
| [isCoPlanarTo](Plane_isCoPlanarTo.htm) | Checks if this plane is coplanar with another plane. |
| [isParallelToLine](Plane_isParallelToLine.htm) | Checks if this plane is parallel to a line. |
| [isParallelToPlane](Plane_isParallelToPlane.htm) | Checks if this plane is parallel to another plane. |
| [isPerpendicularToLine](Plane_isPerpendicularToLine.htm) | Checks if this plane is perpendicular to a line. |
| [isPerpendicularToPlane](Plane_isPerpendicularToPlane.htm) | Checks if this plane is perpendicular to another plane. |
| [setUVDirections](Plane_setUVDirections.htm) | Sets the U and V directions of the plane. |
| [transformBy](Plane_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [evaluator](Plane_evaluator.htm) | Returns the surface evaluator. |
| [isValid](Plane_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [normal](Plane_normal.htm) | Gets and sets the normal of the plane. |
| [objectType](Plane_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](Plane_origin.htm) | Gets and sets the origin point of the plane. |
| [surfaceType](Plane_surfaceType.htm) | Returns the surface type. |
| [uDirection](Plane_uDirection.htm) | Gets the U Direction of the plane. |
| [vDirection](Plane_vDirection.htm) | Gets the V Direction of the plane. |

## Accessed From

[Canvas.plane](Canvas_plane.htm), [CanvasInput.plane](CanvasInput_plane.htm), [ConstructionPlane.geometry](ConstructionPlane_geometry.htm), [ConstructionPlaneByPlaneDefinition.plane](ConstructionPlaneByPlaneDefinition_plane.htm), [OffsetStartDefinition.profilePlane](OffsetStartDefinition_profilePlane.htm), [Plane.copy](Plane_copy.htm), [Plane.create](Plane_create.htm), [Plane.createUsingDirections](Plane_createUsingDirections.htm), [Profile.plane](Profile_plane.htm), [ProfilePlaneStartDefinition.profilePlane](ProfilePlaneStartDefinition_profilePlane.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |