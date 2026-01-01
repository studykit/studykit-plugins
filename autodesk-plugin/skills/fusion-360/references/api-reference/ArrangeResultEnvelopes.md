# ArrangeResultEnvelopes Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelopes.h>

## Description

Provides access to the results of an arrangement. For 3D arrangements, this will always contain a single result. For plane or profile envelopes this can contain multiple envelope results.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeResultEnvelopes_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ArrangeResultEnvelopes_item.htm) | Returns the specified Arrange envelope result using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ArrangeResultEnvelopes_count.htm) | Returns the number of Arrange envelope results for this Arrange feature. |
| [isValid](ArrangeResultEnvelopes_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeResultEnvelopes_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ArrangeFeature.resultEnvelopes](ArrangeFeature_resultEnvelopes.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |