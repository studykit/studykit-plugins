# ArrangeOccurrenceResults Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeOccurrenceResults.h>

## Description

A collection that contains the occurrences in an Arrange envelope.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeOccurrenceResults_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ArrangeOccurrenceResults_item.htm) | Returns the specified Arrange occurrence using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ArrangeOccurrenceResults_count.htm) | Returns the number of Arrange occurrences in the collection. |
| [isValid](ArrangeOccurrenceResults_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeOccurrenceResults_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Arrange3DResultEnvelope.occurrences](Arrange3DResultEnvelope_occurrences.htm), [ArrangePlaneResultEnvelope.occurrences](ArrangePlaneResultEnvelope_occurrences.htm), [ArrangeProfileOrFaceResultEnvelope.occurrences](ArrangeProfileOrFaceResultEnvelope_occurrences.htm), [ArrangeResultEnvelope.occurrences](ArrangeResultEnvelope_occurrences.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |