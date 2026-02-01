# Arc3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Transient 3D arc. A transient arc is not displayed or saved in a document. Transient 3D arcs are used as a wrapper to work with raw 3D arc information. They are created statically using one of the create methods of the Arc3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Arc3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Arc3D_copy.htm) | Creates and returns an independent copy of this Arc3D object. |
| [createByCenter](Arc3D_createByCenter.htm) | Creates a transient 3D arc object by specifying a center point and radius. |
| [createByThreePoints](Arc3D_createByThreePoints.htm) | Creates a transient 3D arc by specifying 3 points. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 3D arc information. |
| [getData](Arc3D_getData.htm) | Gets all of the data defining the arc. |
| [set](Arc3D_set.htm) | Sets all of the data defining the arc. |
| [setAxes](Arc3D_setAxes.htm) | Sets the normal and reference vectors of the arc. |
| [transformBy](Arc3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [asNurbsCurve](Arc3D_asNurbsCurve.htm) | Returns a NURBS curve that is geometrically identical to the arc. |
| [center](Arc3D_center.htm) | Gets and sets the center position of the arc. |
| [curveType](Arc3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [endAngle](Arc3D_endAngle.htm) | Gets and sets the end angle of the arc in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |
| [endPoint](Arc3D_endPoint.htm) | Gets the end point of the arc. |
| [evaluator](Arc3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](Arc3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [normal](Arc3D_normal.htm) | Gets the normal of the arc. |
| [objectType](Arc3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [radius](Arc3D_radius.htm) | Gets and sets the radius of the arc. |
| [referenceVector](Arc3D_referenceVector.htm) | Gets the reference vector of the arc. |
| [startAngle](Arc3D_startAngle.htm) | Gets and sets the start angle of the arc in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |
| [startPoint](Arc3D_startPoint.htm) | Gets the start point of the arc. |

## Accessed From

[Arc3D.copy](Arc3D_copy.htm), [Arc3D.createByCenter](Arc3D_createByCenter.htm), [Arc3D.createByThreePoints](Arc3D_createByThreePoints.htm), [SketchArc.geometry](SketchArc_geometry.htm), [SketchArc.worldGeometry](SketchArc_worldGeometry.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Circle and Arc Data from Edge API Sample](GetCircleAndArcDataFromEdge_Sample.htm) | Display the arc and circle geometric information from a selected circular edge. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |