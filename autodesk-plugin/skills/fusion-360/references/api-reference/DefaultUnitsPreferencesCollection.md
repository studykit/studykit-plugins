# DefaultUnitsPreferencesCollection Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferencesCollection.h>

## Description

A collection that provides access to product specific unit preference objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DefaultUnitsPreferencesCollection_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DefaultUnitsPreferencesCollection_item.htm) | Function that returns the specified DefaultUnitPreferences object using an index into the collection. |
| [itemByName](DefaultUnitsPreferencesCollection_itemByName.htm) | Returns the DefaultUnitsPreference object with the specified name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DefaultUnitsPreferencesCollection_count.htm) | Returns the number of DefaultUnitsPreference objects. |
| [isValid](DefaultUnitsPreferencesCollection_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DefaultUnitsPreferencesCollection_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Preferences.defaultUnitsPreferences](Preferences_defaultUnitsPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |