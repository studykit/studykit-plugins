# MeasureResults Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureResults.h>

## Description

Provides measurement results from the various measurement methods available on the MeasureManager object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeasureResults_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MeasureResults_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MeasureResults_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [positionOne](MeasureResults_positionOne.htm) | For a distance measurement, this is the point on the first entity where the measurement was made from. For an angle measurement this is one of the three points defining the angle. |
| [positionThree](MeasureResults_positionThree.htm) | This point is only used for angle measurements and is one of the three points defining the angle. |
| [positionTwo](MeasureResults_positionTwo.htm) | For a distance measurement, this is the point on the second entity where the measurement was made to. For an angle measurement this is one of the three points defining the angle. |
| [value](MeasureResults_value.htm) | The measurement value. If the measurement is a distance this value will be in centimeters. If it's an angle then it will be in radians. |

## Accessed From

[MeasureManager.measureAngle](MeasureManager_measureAngle.htm), [MeasureManager.measureMinimumDistance](MeasureManager_measureMinimumDistance.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Measure Sample](MeasureSample_Sample.htm) | Measure related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |