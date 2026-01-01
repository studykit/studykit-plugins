# NurbsSurface Object

Derived from: [Surface](Surface.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Transient NURBS surface. A transient NURBS surface is not displayed or saved in a document. A transient NURBS surface is used as a wrapper to work with raw NURBS surface information. A transient NURBS surface is bounded by it's natural boundaries and does not support the definition of arbitrary boundaries. A NURBS surface is typically obtained from a BREPFace object, which does have boundary information. They are created statically using the create method of the NurbsSurface class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NurbsSurface_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](NurbsSurface_copy.htm) | Creates and returns an independent copy of this NurbsSurface object. |
| [create](NurbsSurface_create.htm) | Creates a transient NURBS surface object. |
| [getData](NurbsSurface_getData.htm) | Gets the data that defines the NURBS surface. |
| [set](NurbsSurface_set.htm) | Sets the data that defines the NURBS surface. |
| [transformBy](NurbsSurface_transformBy.htm) | Updates this surface by transforming it with a given input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [controlPointCountU](NurbsSurface_controlPointCountU.htm) | Gets the number of control points in the U direction. |
| [controlPointCountV](NurbsSurface_controlPointCountV.htm) | Gets the number of control points in the V direction. |
| [controlPoints](NurbsSurface_controlPoints.htm) | Gets an array of control points from the surface. |
| [degreeU](NurbsSurface_degreeU.htm) | Gets the degree in the U direction. |
| [degreeV](NurbsSurface_degreeV.htm) | Gets the degree in the V direction. |
| [evaluator](NurbsSurface_evaluator.htm) | Returns the surface evaluator. |
| [isValid](NurbsSurface_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [knotCountU](NurbsSurface_knotCountU.htm) | Gets the knot count in the U direction. |
| [knotCountV](NurbsSurface_knotCountV.htm) | Gets thekKnot count in the V direction. |
| [knotsU](NurbsSurface_knotsU.htm) | Get the knot vector from the U direction. |
| [knotsV](NurbsSurface_knotsV.htm) | Get the knot vector from the V direction |
| [objectType](NurbsSurface_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [propertiesU](NurbsSurface_propertiesU.htm) | Gets the properties (NurbsSurfaceProperties) of the surface in the U direction. |
| [propertiesV](NurbsSurface_propertiesV.htm) | Gets the properties (NurbsSurfaceProperties) of the surface in the V direction. |
| [surfaceType](NurbsSurface_surfaceType.htm) | Returns the surface type. |

## Accessed From

[NurbsSurface.copy](NurbsSurface_copy.htm), [NurbsSurface.create](NurbsSurface_create.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |