# Surface Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Surface.h>

## Description

Describes a two-dimensional topological, manifold in three-dimensional space. It is used as the underlying geometry for a BRepFace.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Surface_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [transformBy](Surface_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [evaluator](Surface_evaluator.htm) | Returns the surface evaluator. |
| [isValid](Surface_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Surface_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [surfaceType](Surface_surfaceType.htm) | Returns the surface type. |

## Accessed From

[BRepFace.geometry](BRepFace_geometry.htm), [BRepFaceDefinition.surfaceGeometry](BRepFaceDefinition_surfaceGeometry.htm)

## Derived Classes

[Cone](Cone.htm), [Cylinder](Cylinder.htm), [EllipticalCone](EllipticalCone.htm), [EllipticalCylinder](EllipticalCylinder.htm), [NurbsSurface](NurbsSurface.htm), [Plane](Plane.htm), [Sphere](Sphere.htm), [Torus](Torus.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |