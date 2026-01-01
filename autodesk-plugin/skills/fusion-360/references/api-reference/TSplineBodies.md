# TSplineBodies Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

A collection of TSpline bodies.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByTSMDescription](TSplineBodies_addByTSMDescription.htm) | Creates a new TSplineBody using the T-Spline description provided by the input string which contains TSM formatted text. |
| [addByTSMFile](TSplineBodies_addByTSMFile.htm) | Creates a new TSplineBody by reading in a TSM file from disk. |
| [classType](TSplineBodies_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](TSplineBodies_item.htm) | Function that returns the specified T-Spline body using an index into the collection. |
| [itemByName](TSplineBodies_itemByName.htm) | Returns a TSplineBody by specifying the name of the body as seen in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](TSplineBodies_count.htm) | The number of bodies in the collection. |
| [isValid](TSplineBodies_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TSplineBodies_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[FormFeature.tSplineBodies](FormFeature_tSplineBodies.htm)

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |