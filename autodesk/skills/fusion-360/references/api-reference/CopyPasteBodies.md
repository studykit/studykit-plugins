# CopyPasteBodies Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBodies.h>

## Description

Collection that provides access to all of the existing copy-paste features in a design. These are created in the UI by copying and then pasting a B-Rep body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CopyPasteBodies_add.htm) | Copies the specified body into the component that owns this CopyPasteBodies collection. |
| [classType](CopyPasteBodies_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CopyPasteBodies_item.htm) | Function that returns the specified Copy/Paste Body feature using an index into the collection. |
| [itemByName](CopyPasteBodies_itemByName.htm) | Function that returns the specified Copy/Paste Body feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CopyPasteBodies_count.htm) | The number of Copy/Paste Body features in the collection. |
| [isValid](CopyPasteBodies_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CopyPasteBodies_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.copyPasteBodies](Features_copyPasteBodies.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copy Paste Bodies API Sample](CopyPasteBodiesSample_Sample.htm) | Demonstrates how to use Copy Paste Bodies related API. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |