# FusionDefaultUnitsPreferences Object

Derived from: [DefaultUnitsPreferences](DefaultUnitsPreferences.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDefaultUnitsPreferences.h>

## Description

Fusion Default Units for Design Preferences. The following code can be used to access this object.

```
unitPrefs = app.preferences.defaultUnitsPreferences.itemByName('Design')
```

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FusionDefaultUnitsPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [defaultUnitSystem](FusionDefaultUnitsPreferences_defaultUnitSystem.htm) | Gets and sets the default unit system when creating a new Fusion file. |
| [distanceDisplayUnits](FusionDefaultUnitsPreferences_distanceDisplayUnits.htm) | Gets and sets the default design units for length when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom. |
| [isValid](FusionDefaultUnitsPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [massDisplayUnits](FusionDefaultUnitsPreferences_massDisplayUnits.htm) | Gets and sets the default design units for mass when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom. |
| [name](FusionDefaultUnitsPreferences_name.htm) | Returns the name of this DefaultUnitPreferences object. |
| [objectType](FusionDefaultUnitsPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |