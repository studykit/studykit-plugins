# ProductPreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferences.h>

## Description

The base class for the general product preferences. There is a derived class for each product where the specific preference values are exposed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProductPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ProductPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ProductPreferences_name.htm) | Returns the name of this ProductPreferences object. |
| [objectType](ProductPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ProductPreferencesCollection.item](ProductPreferencesCollection_item.htm), [ProductPreferencesCollection.itemByName](ProductPreferencesCollection_itemByName.htm)

## Derived Classes

[FusionProductPreferences](FusionProductPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |