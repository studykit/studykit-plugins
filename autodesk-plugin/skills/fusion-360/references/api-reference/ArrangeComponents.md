# ArrangeComponents Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponents.h>

## Description

The collection of ArrangeComponent objects associated with an arrangement. This provides access to existing ArrangeComponent objects and supports adding new components to the the arrangement. An ArrangeComponent object defines an occurrence along with additional arrangement information. This object is used for both the creation of a new Arrange feature and querying and modifying an existing Arrange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ArrangeComponents_add.htm) | Adds a new ArrangeComponent object to the collection. |
| [classType](ArrangeComponents_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ArrangeComponents_item.htm) | Returns an ArrangeComponent object using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ArrangeComponents_count.htm) | Returns the number of ArrangeComponent objects in the collection. |
| [isValid](ArrangeComponents_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ArrangeComponents_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ArrangeFeature.arrangeComponents](ArrangeFeature_arrangeComponents.htm), [ArrangeFeatureInput.arrangeComponents](ArrangeFeatureInput_arrangeComponents.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |