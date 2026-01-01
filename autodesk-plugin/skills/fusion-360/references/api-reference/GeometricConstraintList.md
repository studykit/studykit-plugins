# GeometricConstraintList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraintList.h>

## Description

A list of geometric constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](GeometricConstraintList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](GeometricConstraintList_item.htm) | Function that returns the specified geometry constraint using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](GeometricConstraintList_count.htm) | Returns the number of constraints in the sketch. |
| [isValid](GeometricConstraintList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](GeometricConstraintList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchArc.geometricConstraints](SketchArc_geometricConstraints.htm), [SketchCircle.geometricConstraints](SketchCircle_geometricConstraints.htm), [SketchConicCurve.geometricConstraints](SketchConicCurve_geometricConstraints.htm), [SketchControlPointSpline.geometricConstraints](SketchControlPointSpline_geometricConstraints.htm), [SketchCurve.geometricConstraints](SketchCurve_geometricConstraints.htm), [SketchEllipse.geometricConstraints](SketchEllipse_geometricConstraints.htm), [SketchEllipticalArc.geometricConstraints](SketchEllipticalArc_geometricConstraints.htm), [SketchEntity.geometricConstraints](SketchEntity_geometricConstraints.htm), [SketchFittedSpline.geometricConstraints](SketchFittedSpline_geometricConstraints.htm), [SketchFixedSpline.geometricConstraints](SketchFixedSpline_geometricConstraints.htm), [SketchLine.geometricConstraints](SketchLine_geometricConstraints.htm), [SketchPoint.geometricConstraints](SketchPoint_geometricConstraints.htm), [SketchText.geometricConstraints](SketchText_geometricConstraints.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |