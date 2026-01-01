# SketchDimensionList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensionList.h>

## Description

A list of sketch dimensions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchDimensionList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchDimensionList_item.htm) | Function that returns the specified sketch dimension using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchDimensionList_count.htm) | Returns the number of sketch dimensions in the sketch. |
| [isValid](SketchDimensionList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchDimensionList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchArc.sketchDimensions](SketchArc_sketchDimensions.htm), [SketchCircle.sketchDimensions](SketchCircle_sketchDimensions.htm), [SketchConicCurve.sketchDimensions](SketchConicCurve_sketchDimensions.htm), [SketchControlPointSpline.sketchDimensions](SketchControlPointSpline_sketchDimensions.htm), [SketchCurve.sketchDimensions](SketchCurve_sketchDimensions.htm), [SketchEllipse.sketchDimensions](SketchEllipse_sketchDimensions.htm), [SketchEllipticalArc.sketchDimensions](SketchEllipticalArc_sketchDimensions.htm), [SketchEntity.sketchDimensions](SketchEntity_sketchDimensions.htm), [SketchFittedSpline.sketchDimensions](SketchFittedSpline_sketchDimensions.htm), [SketchFixedSpline.sketchDimensions](SketchFixedSpline_sketchDimensions.htm), [SketchLine.sketchDimensions](SketchLine_sketchDimensions.htm), [SketchPoint.sketchDimensions](SketchPoint_sketchDimensions.htm), [SketchText.sketchDimensions](SketchText_sketchDimensions.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |