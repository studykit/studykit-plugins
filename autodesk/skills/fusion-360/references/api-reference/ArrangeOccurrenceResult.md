# ArrangeOccurrenceResult Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeOccurrenceResult.h>

## Description

The ArrangeOccurrence object represents a single occurrence within an Arrange envelope.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeOccurrenceResult_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [arrangeComponent](ArrangeOccurrenceResult_arrangeComponent.htm) | The ArrangeComponent from the Arrange definition that resulted in the create of this occurrence. |
| [isValid](ArrangeOccurrenceResult_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeOccurrenceResult_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurrence](ArrangeOccurrenceResult_occurrence.htm) | The Occurrence object in the Arrange envelope. |
| [parentEnvelope](ArrangeOccurrenceResult_parentEnvelope.htm) | The Arrange envelope this occurrence is within. |

## Accessed From

[ArrangeOccurrenceResults.item](ArrangeOccurrenceResults_item.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |