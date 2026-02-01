# HolePositionDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HolePositionDefinition.h>

## Description

The base class for the classes that define how a hole can be positioned.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](HolePositionDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](HolePositionDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](HolePositionDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[HoleFeature.holePositionDefinition](HoleFeature_holePositionDefinition.htm)

## Derived Classes

[AtCenterHolePositionDefinition](AtCenterHolePositionDefinition.htm), [OnEdgeHolePositionDefinition](OnEdgeHolePositionDefinition.htm), [PlaneAndOffsetsHolePositionDefinition](PlaneAndOffsetsHolePositionDefinition.htm), [PointHolePositionDefinition](PointHolePositionDefinition.htm), [SketchPointHolePositionDefinition](SketchPointHolePositionDefinition.htm), [SketchPointsHolePositionDefinition](SketchPointsHolePositionDefinition.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |