# InfiniteLine3D Object

Derived from: [Curve3D](Curve3D.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/InfiniteLine3D.h>

## Description

Transient 3D infinite line. An infinite line is defined by a position and direction in space and has no start or end points. They are created statically using the create method of the InfiniteLine3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](InfiniteLine3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](InfiniteLine3D_copy.htm) | Creates and returns a copy of this line object. |
| [create](InfiniteLine3D_create.htm) | Creates a transient 3D infinite line. |
| [getData](InfiniteLine3D_getData.htm) | Gets all of the data defining the infinite line. |
| [intersectWithCurve](InfiniteLine3D_intersectWithCurve.htm) | Intersect this line with a curve to get the intersection point(s). |
| [intersectWithSurface](InfiniteLine3D_intersectWithSurface.htm) | Intersect this line with a surface to get the intersection point(s). |
| [isColinearTo](InfiniteLine3D_isColinearTo.htm) | Compare this line with another to check for collinearity. |
| [set](InfiniteLine3D_set.htm) | Sets all of the data defining the infinite line. |
| [transformBy](InfiniteLine3D_transformBy.htm) | Transforms this curve in 3D space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [curveType](InfiniteLine3D_curveType.htm) | Returns the type of geometry this curve represents. |
| [direction](InfiniteLine3D_direction.htm) | Gets and sets the direction of the line. |
| [evaluator](InfiniteLine3D_evaluator.htm) | Returns an evaluator object that lets you perform additional evaluations on the curve. |
| [isValid](InfiniteLine3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](InfiniteLine3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [origin](InfiniteLine3D_origin.htm) | Gets and sets the origin point of the line. |

## Accessed From

[ConstructionAxis.geometry](ConstructionAxis_geometry.htm), [ConstructionAxisByLineDefinition.axis](ConstructionAxisByLineDefinition_axis.htm), [InfiniteLine3D.copy](InfiniteLine3D_copy.htm), [InfiniteLine3D.create](InfiniteLine3D_create.htm), [Line3D.asInfiniteLine](Line3D_asInfiniteLine.htm), [Plane.intersectWithPlane](Plane_intersectWithPlane.htm), [RotaryMachineAxis.rotationAxis](RotaryMachineAxis_rotationAxis.htm), [RotaryMachineAxisInput.rotationAxis](RotaryMachineAxisInput_rotationAxis.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |