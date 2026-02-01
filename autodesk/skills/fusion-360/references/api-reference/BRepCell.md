# BRepCell Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

Object that represents an existing BRepCell.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepCell_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [cellBody](BRepCell_cellBody.htm) | Returns a BRepBody that represents this cell. This is a transient B-Rep body. |
| [isSelected](BRepCell_isSelected.htm) | Gets and sets whether the cell is selected. For a Trim feature a selected cell is removed, whereas for a boundary fill feature, a selected cell is kept and used in the feature operation. |
| [isValid](BRepCell_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepCell_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sourceTools](BRepCell_sourceTools.htm) | Returns the tools that we're using in the definition of this cell. |

## Accessed From

[BRepCells.item](BRepCells_item.htm)

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