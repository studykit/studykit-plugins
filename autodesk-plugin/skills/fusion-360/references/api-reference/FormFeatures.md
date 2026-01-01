# FormFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeatures.h>

## Description

Collection that provides access to all of the existing Form features in a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](FormFeatures_add.htm) | Creates a new empty form feature in the parent component. |
| [classType](FormFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](FormFeatures_item.htm) | Function that returns the specified Form feature using an index into the collection. |
| [itemByName](FormFeatures_itemByName.htm) | Function that returns the specified form feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](FormFeatures_count.htm) | The number of Form features in the collection. |
| [isValid](FormFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FormFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.formFeatures](Features_formFeatures.htm)

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |