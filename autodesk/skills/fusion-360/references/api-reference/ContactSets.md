# ContactSets Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

Provides access to the existing contact sets in a design and supports creating new contact sets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ContactSets_add.htm) | Creates a new contact set for the provided occurrences and/or bodies. |
| [classType](ContactSets_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ContactSets_item.htm) | Returns the specified contact set using an index into the collection. |
| [itemByName](ContactSets_itemByName.htm) | Returns the specified contact set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ContactSets_count.htm) | Returns the number of contacts sets in the design. |
| [isValid](ContactSets_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ContactSets_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.contactSets](Design_contactSets.htm), [FlatPatternProduct.contactSets](FlatPatternProduct_contactSets.htm), [WorkingModel.contactSets](WorkingModel_contactSets.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |