# BRepCells Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCells.h>

## Description

Collection that provides access to all of the existing BRepCells defined by a BoundaryFillFeatureInput

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepCells_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepCells_item.htm) | Function that returns the specified BRepCell using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepCells_count.htm) | The number of BRepCells in the collection. |
| [isValid](BRepCells_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepCells_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BoundaryFillFeature.bRepCells](BoundaryFillFeature_bRepCells.htm), [BoundaryFillFeatureInput.bRepCells](BoundaryFillFeatureInput_bRepCells.htm), [TrimFeature.bRepCells](TrimFeature_bRepCells.htm), [TrimFeatureInput.bRepCells](TrimFeatureInput_bRepCells.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |