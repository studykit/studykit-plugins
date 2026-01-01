# OffsetFacesFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeatures.h>

## Description

Collection that provides access to all of the existing Offset Faces features in a design. Offset Face features are created in the UI using the "Press Pull" command.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OffsetFacesFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](OffsetFacesFeatures_item.htm) | Function that returns the specified Offset Face feature using an index into the collection. |
| [itemByName](OffsetFacesFeatures_itemByName.htm) | Function that returns the specified Offset Face feature using the name of the feature. Offset Face features are created in the UI using the "Press Pull" command. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](OffsetFacesFeatures_count.htm) | The number of Offset Face features in the collection. Offset Face features are created in the UI using the "Press Pull" command. |
| [isValid](OffsetFacesFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](OffsetFacesFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.offsetFacesFeatures](Features_offsetFacesFeatures.htm)

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |