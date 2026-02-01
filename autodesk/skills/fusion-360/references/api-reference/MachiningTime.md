# MachiningTime Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/MachiningTime.h>

## Description

Object returned when using the getMachiningTime method from the CAM class. Use the properties on this object to get the machining time results.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachiningTime_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [feedDistance](MachiningTime_feedDistance.htm) | Gets the feed distance in centimeters. |
| [isValid](MachiningTime_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [machiningTime](MachiningTime_machiningTime.htm) | Gets the machining time in seconds. |
| [objectType](MachiningTime_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [rapidDistance](MachiningTime_rapidDistance.htm) | Gets the calculated rapid distance in centimeters. |
| [toolChangeCount](MachiningTime_toolChangeCount.htm) | Gets the number of tool changes. |
| [totalFeedTime](MachiningTime_totalFeedTime.htm) | Get the total feed time in seconds. |
| [totalRapidTime](MachiningTime_totalRapidTime.htm) | Gets the total rapid feed time in seconds. |
| [totalToolChangeTime](MachiningTime_totalToolChangeTime.htm) | Gets the total tool change time in seconds. |

## Accessed From

[CAM.getMachiningTime](CAM_getMachiningTime.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |