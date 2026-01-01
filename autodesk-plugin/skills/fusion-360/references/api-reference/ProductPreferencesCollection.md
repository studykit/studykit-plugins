# ProductPreferencesCollection Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferencesCollection.h>

## Description

A collection that provides access to product specific preference objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProductPreferencesCollection_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ProductPreferencesCollection_item.htm) | Function that returns the specified ProductPreferences object using an index into the collection. |
| [itemByName](ProductPreferencesCollection_itemByName.htm) | Returns the ProductPreference object with the specified name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ProductPreferencesCollection_count.htm) | Returns the number of ProductPreference objects. |
| [isValid](ProductPreferencesCollection_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ProductPreferencesCollection_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Preferences.productPreferences](Preferences_productPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |