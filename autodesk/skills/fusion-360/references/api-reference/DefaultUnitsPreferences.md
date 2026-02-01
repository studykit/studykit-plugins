# DefaultUnitsPreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferences.h>

## Description

The base class for the default units preference. There is a derived class supported by each product where the specific preference values are exposed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DefaultUnitsPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](DefaultUnitsPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](DefaultUnitsPreferences_name.htm) | Returns the name of this DefaultUnitPreferences object. |
| [objectType](DefaultUnitsPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DefaultUnitsPreferencesCollection.item](DefaultUnitsPreferencesCollection_item.htm), [DefaultUnitsPreferencesCollection.itemByName](DefaultUnitsPreferencesCollection_itemByName.htm)

## Derived Classes

[FusionDefaultUnitsPreferences](FusionDefaultUnitsPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |